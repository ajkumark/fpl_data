from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from fantasyapp.models import Data, Fixture, CurrentGameWeek

def home(request):
	fpl_data = Data.objects.all()
	fixtures = Fixture.objects.all()
	current_gameweek = CurrentGameWeek.objects.all() 
	return render_to_response('index.html', 
		context_instance=RequestContext(request, {'data':fpl_data,
			'current_gameweek':current_gameweek,
			'fixtures':fixtures
			}))
