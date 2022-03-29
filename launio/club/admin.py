from django.contrib import admin

# Register your models here.
from launio.club import models
from launio.club.models import *

admin.site.register(Gymnast)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(NotesTeam)
admin.site.register(NotesIndividual)
# @admin.register(models.Gymnast)
# class GymnastAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(models.Team)
# class TeamAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(models.Competition)
# class CompetitionAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(models.NotesTeam)
# class NotesTeamAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(models.NotesIndividual)
# class NotesIndividualAdmin(admin.ModelAdmin):
#     pass

