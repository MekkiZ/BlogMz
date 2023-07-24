from django.contrib import admin
from authenticate.models import UserCus
from profil.models import Profile


admin.site.register(UserCus)
admin.site.register(Profile)

