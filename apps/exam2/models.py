from __future__ import unicode_literals
import datetime

from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ]+$')

class UserManager(models.Manager):
    def register_validate(self, postData):
        fail = False
        errors = {}

        if len(postData['name']) < 3:

            errors['name']="Invalid  Name, minimim 3 characters"
            fail = True
            # makes sure the name field is only characters no digits
        elif not NAME_REGEX.match(postData['name']):
            errors['name'] = "Name field must be characters only"
   # ===========================================Email auth

        try:
            found_user_email = User.objects.get(email=postData['email'])
        except:
            found_user_email = False

        if len(postData['email']) < 1:
           errors['email'] = "Email is required!"
           fail = True

        elif not EMAIL_REGEX.match(postData['email']):
           errors['email'] = "Please enter a valid email!"
           fail = True
        elif found_user_email:
           errors['email'] = "This email is already registered!"
           fail= True

        #    =======================================User auth
        # ==================================================
        # print "we want to check if the username exists in the database from here"
        try:
            found_user_name = User.objects.get(username=postData['username'])
        except:
            found_user_name = False

        if len(postData['username']) < 3 :
            errors['username']= "Invalid Username, minimum 3 characters"
            fail = True
        elif found_user_name:
            errors['username']="this username is already in the system"
        # ===========================================

        if len(postData['password']) < 8:
            errors['password']="Minimum of 8 characters required for password"
            fail = True

        elif postData['conf_pwd'] != postData['password']:
            errors['conf_pwd']= "Password doesn't match"
            fail = True

        return errors

        # salt = bcrypt.gensalt()


# hash1 = bcrypt.hashpw('test'.encode(), bcrypt.gensalt())


# ===================username login
    def login_validate(self, postData):
        fail = False
        errors= {}

        # try:
        #     found_user_name = User.objects.get(username=postData['username'])
        # except:
        #     found_user_name = False
        #
        # if not found_user_name:
        #     errors['username']= "No user found with this Username address. Please register new user."
        #     fail = True
        # if fail:
        #     return errors
        # return errors

# ===========================================Email login

        try:
            found_user_email = User.objects.get(email=postData['email'])
        except:
            found_user_email = False

        if len(postData['email']) < 1:
            errors['email'] = "Email is required!"
            fail = True
        elif not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Please enter a valid email!"
            fail = True
        elif not found_user_email:
            errors['email'] = "This email is already registered!"
            fail= True

        return errors
# =========================

        # hash1 = bcrypt.hashpw('password'.encode(), bcrypt.gensalt())

            # fail = True


            # return {'result':'success', 'messages':errors, 'user':found_user}



class User(models.Model):
    name = models.CharField(max_length = 255 )
    username = models.CharField(max_length = 255 )
    email = models.CharField(max_length = 255)
    birthday = models.TextField(blank=True)
    password = models.CharField(max_length = 255 )
    desc = models.TextField(default="")
    salt = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

class Quote(models.Model):
    message= models.TextField();
    # quoted_by=models.CharField(max_length=255, blank=True)
    wished_by = models.ManyToManyField(User, related_name='wishing')
    quoted_by = models.ForeignKey(User, related_name='quotes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
