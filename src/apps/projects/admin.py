from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.projects.models import Project
from project.utils.xforms import gen_textinput_admin_form

# Register your models here.


@admin.register(Project)
class ProjectAdminModel(ModelAdmin):
    form = gen_textinput_admin_form(
        Project, (
            Project.name,
            Project.link,
            Project.linkName,
            Project.description,
            Project.gallery,
            Project.started_at,
            Project.finished_at,
            Project.sponsor,
            Project.sponsorLogo
        ),
    )
