from django.core.management.base import BaseCommand, CommandError
from fantasyapp.models import Data, Players, populate, populate_mongo

class Command(BaseCommand):

	def handle(self, *args, **options):
		populate()
		self.stdout.write('Success')