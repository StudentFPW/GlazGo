import secrets

from django.contrib.auth.models import BaseUserManager

from referral_system.models import ReferralRelationship, ReferralCode


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, referral_token=None):
        if not referral_token:
            raise ValueError("Please use your token!")
        if not email:
            raise ValueError("Users must have an email address!")
        if not username:
            raise ValueError("Users must have an username!")
        ref_code = ReferralCode.objects.filter(token=referral_token)
        if not ref_code:
            raise ValueError("Your token is not valid!")

        # print(ref_code[0].user)

        usages_token = ReferralRelationship.objects.filter(refer_token=ref_code[0])
        if not usages_token:
            user = self.model(
                username=username,
                email=self.normalize_email(email),
                referral_token=referral_token,
            )
            user.set_password(password)
            user.save(using=self._db)
            ReferralRelationship(
                employer=ref_code[0].user, employee=user, refer_token=ref_code[0]
            ).save()
            for i in range(30):
                self.create_reftoken(user)
        else:
            raise ValueError("This token is used!")
        return user

    def create_superuser(self, username, email, password=None, referral_token=None):
        user = self.model(username=username, email=email, referral_token=referral_token)
        user.set_password(password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        for i in range(100):
            self.create_reftoken(user)
        return user

    def create_reftoken(self, user):
        token = secrets.token_urlsafe(40)
        ReferralCode(token=token, user=user).save()
