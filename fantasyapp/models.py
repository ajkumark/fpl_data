import os
import requests
import pymongo

from pymongo import MongoClient
from django.db import models

from djangotoolbox.fields import DictField


class Data(models.Model):
    fpl_data = DictField()

    def __unicode__(self):
    	return u'%s' % (self.fpl_data)

class Team(models.Model):
	name = models.CharField(max_length=50)

	def __unicode__(self):
		return u'%s' % (self.name)

class Fixture(models.Model):
	home = models.ForeignKey(Team, related_name='hometeam')
	away = models.ForeignKey(Team, related_name='awayteam')
	gameweek = models.ForeignKey('GameWeek')
	time = models.DateTimeField()
	winner = models.ForeignKey(Team, null=True, blank=True)
	result = models.CharField(max_length=10, null=True, blank=True)
	status = models.BooleanField(default=False)

	def __unicode__(self):
		return u'%s %s' % (self.home, self.away)

class GameWeek(models.Model):
	week = models.CharField(max_length=20)

	def __unicode__(self):
		return u'%s' % (self.week)

class CurrentGameWeek(models.Model):
	current = models.ForeignKey(GameWeek)

	def __unicode__(self):
		return u'%s' % (self.current)

class Players(models.Model):
	transfers_out = models.BigIntegerField(null=True, blank=True)
	yellow_cards = models.IntegerField(null=True, blank=True)
	code = models.IntegerField(null=True, blank=True)
	event_total = models.IntegerField(null=True, blank=True)
	goals_conceded = models.IntegerField(null=True, blank=True)
	photo = models.CharField(max_length=90, null=True, blank=True)
	saves = models.IntegerField(null=True, blank=True)
	ep_this = models.CharField(max_length=90, null=True, blank=True)
	value_form = models.CharField(max_length=90, null=True, blank=True)
	next_fixture = models.CharField(max_length=90, null=True, blank=True)
	team_id = models.IntegerField(null=True, blank=True)
	goals_scored = models.IntegerField(null=True, blank=True)
	loans_out = models.IntegerField(null=True, blank=True)
	web_name = models.CharField(max_length=90, null=True, blank=True)
	value_season = models.CharField(max_length=90, null=True, blank=True)
	team_code = models.IntegerField(null=True, blank=True)
	pl_id = models.IntegerField(null=True, blank=True)
	special = models.CharField(max_length=90, null=True, blank=True)
	first_name = models.CharField(max_length=90, null=True, blank=True)
	transfers_out_event = models.BigIntegerField(null=True, blank=True)
	chance_of_playing_next_round = models.IntegerField(null=True, blank=True)
	team_name = models.CharField(max_length=90, null=True, blank=True)
	cost_change_event_fall = models.IntegerField(null=True, blank=True)
	event_explain = models.CharField(max_length=90, null=True, blank=True)
	type_name = models.CharField(max_length=90, null=True, blank=True)
	bps = models.IntegerField(null=True, blank=True)
	cost_change_start_fall = models.IntegerField(null=True, blank=True)
	bonus = models.IntegerField(null=True, blank=True)
	total_points = models.IntegerField(null=True, blank=True)
	penalties_missed = models.IntegerField(null=True, blank=True)
	transfers_in = models.IntegerField(null=True, blank=True)
	status = models.CharField(max_length=90, null=True, blank=True)
	form = models.CharField(max_length=90, null=True, blank=True)
	own_goals = models.IntegerField(null=True, blank=True)
	loaned_in = models.IntegerField(null=True, blank=True)
	dreamteam_count = models.BooleanField()
	current_fixture = models.CharField(max_length=90, null=True, blank=True)
	now_cost = models.IntegerField(null=True, blank=True)
	clean_sheets = models.IntegerField(null=True, blank=True)
	assists = models.IntegerField(null=True, blank=True)
	selected_by_percent = models.CharField(max_length=90, null=True, blank=True)
	event_points = models.IntegerField(null=True, blank=True)
	loans_in = models.IntegerField(null=True, blank=True)
	news = models.CharField(max_length=90, null=True, blank=True)
	ea_index = models.IntegerField(null=True, blank=True)
	penalties_saved = models.IntegerField(null=True, blank=True)
	cost_change_start = models.IntegerField(null=True, blank=True)
	in_dreamteam = models.CharField(max_length=90, null=True, blank=True)
	points_per_game = models.CharField(max_length=90, null=True, blank=True)
	red_cards = models.IntegerField(null=True, blank=True)
	loaned_out = models.IntegerField(null=True, blank=True)
	transfers_in_event = models.IntegerField(null=True, blank=True)
	selected_by = models.CharField(max_length=90, null=True, blank=True)
	element_type = models.IntegerField(null=True, blank=True)
	ep_next = models.CharField(max_length=90, null=True, blank=True)
	team = models.IntegerField(null=True, blank=True)
	chance_of_playing_this_round = models.IntegerField(null=True, blank=True)
	minutes = models.IntegerField(null=True, blank=True)
	second_name = models.CharField(max_length=90, null=True, blank=True)
	cost_change_event = models.IntegerField(null=True, blank=True)

	def __unicode__(self):
		return u'%s' % (self.web_name)

def populate():
	data = Data.objects.all()
	players = Players.objects.all()
	players.delete()
	for x in data:
		a = Players()
		a.transfers_out = x.fpl_data['transfers_out']
		a.yellow_cards = x.fpl_data['yellow_cards']
		a.code = x.fpl_data['code']
		a.event_total = x.fpl_data['event_total']
		a.goals_conceded = x.fpl_data['goals_conceded']
		a.photo = 'http://cdn.ismfg.net/static/plfpl/img/shirts/photos/'+x.fpl_data['photo']
		a.saves = x.fpl_data['saves']
		a.ep_this = x.fpl_data['ep_this']
		a.value_form = x.fpl_data['value_form']
		a.next_fixture = x.fpl_data['next_fixture']
		a.team_id = x.fpl_data['team_id']
		a.goals_scored = x.fpl_data['goals_scored']
		a.loans_out = x.fpl_data['loans_out']
		a.web_name = x.fpl_data['web_name']
		a.value_season = x.fpl_data['value_season']
		a.team_code = x.fpl_data['team_code']
		a.pl_id = x.fpl_data['id']
		a.special = x.fpl_data['special']
		a.first_name = x.fpl_data['first_name']
		a.transfers_out_event = x.fpl_data['transfers_out_event']
		a.chance_of_playing_next_round = x.fpl_data['chance_of_playing_next_round']
		a.team_name = x.fpl_data['team_name']
		a.cost_change_event_fall = x.fpl_data['cost_change_event_fall']
		a.event_explain = str(x.fpl_data['event_explain'])
		a.type_name = x.fpl_data['type_name']
		a.bps = x.fpl_data['bps']
		a.cost_change_start_fall = x.fpl_data['cost_change_start_fall']
		a.bonus = x.fpl_data['bonus']
		a.total_points = x.fpl_data['total_points']
		a.penalties_missed = x.fpl_data['penalties_missed']
		a.transfers_in = x.fpl_data['transfers_in']
		a.status = x.fpl_data['status']
		a.form = x.fpl_data['form']
		a.own_goals = x.fpl_data['own_goals']
		a.loaned_in = x.fpl_data['loaned_in']
		a.dreamteam_count = x.fpl_data['dreamteam_count']
		a.current_fixture = x.fpl_data['current_fixture']
		a.now_cost = x.fpl_data['now_cost']
		a.clean_sheets = x.fpl_data['clean_sheets']
		a.assists = x.fpl_data['assists']
		a.selected_by_percent = x.fpl_data['selected_by_percent']
		a.event_points = x.fpl_data['event_points']
		a.loans_in = x.fpl_data['loans_in']
		a.news = x.fpl_data['news']
		a.ea_index = x.fpl_data['ea_index']
		a.penalties_saved = x.fpl_data['penalties_saved']
		a.cost_change_start = x.fpl_data['cost_change_start']
		a.in_dreamteam = x.fpl_data['in_dreamteam']
		a.points_per_game = x.fpl_data['points_per_game']
		a.red_cards = x.fpl_data['red_cards']
		a.loaned_out = x.fpl_data['loaned_out']
		a.transfers_in_event = x.fpl_data['transfers_in_event']
		a.selected_by = x.fpl_data['selected_by']
		a.element_type = x.fpl_data['element_type']
		a.ep_next = x.fpl_data['ep_next']
		a.team = x.fpl_data['team']
		a.chance_of_playing_this_round = x.fpl_data['chance_of_playing_this_round']
		a.minutes = x.fpl_data['minutes']
		a.second_name = x.fpl_data['second_name']
		a.cost_change_event = x.fpl_data['cost_change_event']
		a.save()

def populate_mongo():
	client = MongoClient()
	db = client.fpl
	db.drop_collection('fantasyapp_data')
	NO_OF_PLAYERS = 538

	for i in range(1,NO_OF_PLAYERS+1):
		url = os.path.join("http://fantasy.premierleague.com/web/api/elements/", str(i))
		r = requests.get(url)
		data = {}
		data['fpl_data'] = r.json()
		fantasyapp_data = db.fantasyapp_data
		insert = fantasyapp_data.insert(data)
		print insert, i

