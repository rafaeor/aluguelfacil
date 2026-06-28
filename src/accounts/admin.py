from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'user_type', 'is_staff')
    list_filter = ('user_type', 'is_staff', 'is_superuser')
    fieldsets = UserAdmin.fieldsets + (
        ('Tipo de Usuário', {'fields': ('user_type',)}),
        ('Contato', {'fields': ('whatsapp',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Tipo de Usuário', {'fields': ('user_type',)}),
        ('Contato', {'fields': ('whatsapp',)}),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj is None:
            form.base_fields['user_type'].initial = 'proprietario'
        return form
