from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from accounts.forms import SignUpForm, UserChangingForm
from accounts.models import User
from tweets.models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile


class AccountUserAdmin(UserAdmin):
    add_form = SignUpForm
    form = UserChangingForm
    model = User
    list_display = ['username', 'email']
    inlines = [ProfileInline]
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        # ('Permissions', {'fields': ('username',)})
    )


admin.site.register(User, AccountUserAdmin)
admin.site.unregister(Group)

admin.site.site_header = 'Parakeet'
admin.site.index_title = 'Welcome to Parakeet'
