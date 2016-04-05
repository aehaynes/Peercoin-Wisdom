"""
models imports app, but app does not import models so we haven't created
any loops.
"""
import datetime
from flask_peewee.auth import BaseUser  # provides password helpers..
from peewee import *
from app import db

class User(db.Model, BaseUser):
    username = CharField()
    password = CharField()
    email = CharField()
    join_date = DateTimeField(default=datetime.datetime.now)
    active = BooleanField(default=True)
    admin = BooleanField(default=False)
    is_superuser = BooleanField()
    
    def __unicode__(self):
        return self.username
    
# create a modeladmin for it
    columns = ('username', 'email', 'is_superuser',)

    # Make sure the user's password is hashed, after it's been changed in
    # the admin interface. If we don't do this, the password will be saved
    # in clear text inside the database and login will be impossible.
    def save_model(self, instance, form, adding=False):
        orig_password = instance.password

        user = super(UserAdmin, self).save_model(instance, form, adding)

        if orig_password != form.password.data:
            user.set_password(form.password.data)
            user.save()

        return user
    
# subclass Auth so we can return our custom classes
class CustomAuth(Auth):
    def get_user_model(self):
        return User

    def get_model_admin(self):
        return UserAdmin

# instantiate the auth
auth = CustomAuth(app, db)

# subclass Admin to check for whether the user is a superuser
class CustomAdmin(Admin):
    def check_user_permission(self, user):
        return user.is_superuser

# instantiate the admin
admin = CustomAdmin(app, auth)

admin.register(User, UserAdmin)
admin.setup()
