from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **kwargs):

        if not email:
            raise ValueError('Email address is required.')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password):

        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save()

        return user
