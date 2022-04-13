from django.contrib import admin

from launio.club.models import *


@admin.register(Gymnast)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('first_name', 'last_name', 'birthdate')
    list_filter = ('first_name', 'birthdate')
    ordering = ('id',)
    list_display = ('first_name', 'last_name', 'birthdate', 'team')


@admin.register(Team)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_filter = ('name',)
    ordering = ('name',)
    list_display = ('name', 'description')


@admin.register(Competition)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('competition_club_organisation', 'competition_name', 'competition_place', 'competition_date')
    list_filter = ('competition_name', 'competition_date')
    ordering = ('competition_date',)
    list_display = ('competition_club_organisation', 'competition_name', 'competition_place', 'competition_date')


@admin.register(NotesTeam)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('nota_competition', 'competition', 'team', 'competition_place_on_board')
    list_filter = ('nota_competition', 'competition')
    ordering = ('competition',)
    list_display = ('competition', 'team', 'nota_competition', 'competition_place_on_board')


@admin.register(NotesIndividual)
class GymnastAdminConfig(admin.ModelAdmin):
    search_fields = ('nota_competition', 'competition', 'gymnast', 'competition_place_on_board')
    list_filter = ('nota_competition', 'competition')
    ordering = ('competition',)
    list_display = ('competition', 'gymnast', 'nota_competition', 'competition_place_on_board')

