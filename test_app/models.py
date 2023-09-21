from django.contrib import admin
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)

    def create_user(self, username, first_name, last_name, email, password):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.save()

    def delete_user(self):
        self.delete()


class Note(models.Model):
    owned = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True)
    description = models.TextField(blank=True)
    title = models.CharField(max_length=100, blank=True, null=True)

    def create_note(self, owned, text, description, title):
        self.title = title
        self.owned = owned
        self.description = description
        self.text = text
        self.save()

    def delete_note(self):
        self.delete()

    def change_text(self, new_text):
        self.text = new_text
        self.save()

    def change_description(self, new_description):
        self.description = new_description
        self.save()

    def change_title(self, new_title):
        self.title = new_title
        self.save()

    def change_note(self, new_text, new_description, new_title):
        self.text = new_text
        self.description = new_description
        self.title = new_title
        self.save()
