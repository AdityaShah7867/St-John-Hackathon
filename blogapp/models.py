from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from autoslug import AutoSlugField# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self, email, name, password = None):
        if not email:
            raise ValueError('User must provide a email')
        
        user = self.model(
            email = email,
            name = name
        )


        user.set_password(password)
        user.save(using = self._db)

        return user


    def modNotes(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_mod = True
        user.is_nUser = True
        user.is_staff = False
        user.save(using = self._db)

        return user

    def create_superuser(self, email, name, password = None):
        user = self.create_user(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.is_nUser = False
        user.is_mod = False

        user.save(using = self._db)

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    email = models.CharField(max_length = 50,unique=True)
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    is_mod = models.BooleanField(default=False)
    is_nUser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    coins_scored = models.IntegerField(default=100,null=True,blank=True)
    rank = models.IntegerField(default=0)

    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return f"{self.name} ({self.coins_scored})"

class Subject(models.Model):

    name = models.CharField(max_length=50)
    teacher = models.CharField(max_length=50)
    teacherurl = models.CharField(max_length=300,null=True,blank=True)
    img = models.ImageField(upload_to='subImage/',null=True,blank=True)
    def __str__(self):
        return self.name

class Module(models.Model):

    name = models.CharField(max_length=50)
    sub = models.ForeignKey(Subject,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



