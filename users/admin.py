from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom Fields",
            {
                "fields" : (
                    "avatar",
                    "gender",
                    "bio",
                    "superhost",
                    "currency",
                    "language",
                    "birthdate"                
                    )
            }
        ),
    )


    list_display =('username','first_name','last_name','gender','language','currency','superhost','is_superuser','is_staff',)
    list_filter =  UserAdmin.list_filter + ('superhost',)
