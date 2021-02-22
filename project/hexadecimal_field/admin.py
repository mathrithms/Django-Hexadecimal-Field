from django.contrib import admin


from hexadecimal_field.models import hexadecimal

@admin.register(hexadecimal)
class hexaAdmin(admin.ModelAdmin):
    pass