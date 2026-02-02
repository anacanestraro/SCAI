from django.contrib import admin
from .models import Aluno


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ("matricula", "usuario", "status", "data_ingresso")
    search_fields = (
        "matricula",
        "usuario__username",
        "usuario__first_name",
        "usuario__last_name",
    )
    list_filter = ("status",)