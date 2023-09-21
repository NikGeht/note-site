from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from test_app.models import Note, User


# Create your views here.
def reg_user(request):
    if request.method == "GET":
        return render(request, 'req_page.html')
    else:
        data = request.POST
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password1, password2 = data.get('password1'), data.get('password2')

        if not username or not first_name or not last_name or not email:
            return HttpResponse("<h3>Check your inputs</h3>")
        elif password1 is None or password2 is None:
            return HttpResponse("<h3>Enter password</h3>")
        elif password1 != password2:
            return HttpResponse("<h3>Passwords not equal</h3>")
        else:
            new_user = User()
            new_user.create_user(username, first_name, last_name, email, password1)
            return HttpResponse("<h3>Successfully register new user</h3>")


def login_user(request):
    if request.method == 'GET':
        user = request.user
        print(user)
        if request.user.is_authenticated:
            return render(request, 'base.html')
        else:

            return render(request, 'login_page.html')
    else:
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        try:
            user = User.objects.get(username=username)
            if user is None:
                return render(request, 'login_page.html')
            elif not password == user.password:
                return render(request, 'login_page.html')
            login(request, user)
            return render(request, 'base.html')
        except KeyError:
            return render(request, 'login_page.html')


def add_note(request):
    if request.method == 'GET':
        return render(request, 'add_note.html')
    else:
        data = request.POST
        text = data['text']
        title = data['title']
        description = data['description']
        user = request.user
        if user is not AnonymousUser:
            user_note = Note().create_note(user, text=text, title=title, description=description)
            return render(request, 'base.html', {'user': user})
        else:
            return render(request, 'login_page.html')




def notes(request):
    if request.method == 'GET':
        if request.user is not AnonymousUser:
            content = Note.objects.filter(owned=request.user)
            if content.count() == 0:
                return HttpResponse("<h3>NO NOTES</h3>"
                                    "<a href='/add_note'>ADD NOTE</a>")
            print(content)
            context = {'notes': content,
                       'user': request.user}
        else:
            return render(request, 'login_page.html')
        return render(request, 'notes.html', context)


def logout_user(request):
    logout(request)
    user = request.user
    return render(request, "base.html", {'user': user})


def base(request):
    if request.method == 'GET':
        user = request.user
        return render(request, 'header.html', {'user': user})


def profile(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'profile.html')
    else:
        return render(request, 'base.html')


def note(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        context = {'note': note}
        return render(request, 'note.html', context=context)

def update_note(request, pk):
    if request.method == 'POST':
        data = request.POST
        text = data['text']
        title = data['title']
        description = data['description']
        note = Note.objects.get(id=pk)
        note.update_note(text=text, title=title, description=description)
        return redirect('notes')


def edit_note(request, pk):
    if request.method == 'GET':
        note = Note.objects.get(id=pk)
        context = {'note': note}
        return render(request, 'edit_note.html', context=context)
    elif request.method == 'POST':
        data = request.POST
        print(data)
        title = data['title']
        description = data['description']
        text = data['text']
        note = Note.objects.get(id=pk)
        note.change_note(new_title=title, new_description=description, new_text=text)
        note.save()
        return redirect('notes')


def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete_note()
    return redirect('notes')