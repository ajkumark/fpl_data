from django.contrib import admin
from fantasyapp.models import Data, Team, Fixture, GameWeek, CurrentGameWeek, Players

admin.site.register(Data)
admin.site.register(Team)
admin.site.register(Fixture)
admin.site.register(GameWeek)
admin.site.register(CurrentGameWeek)
admin.site.register(Players)