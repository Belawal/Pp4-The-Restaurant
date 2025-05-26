from django.core.management.base import BaseCommand
from django.contrib.staticfiles.finders import get_finders

class Command(BaseCommand):
    help = 'Check static files finders'

    def handle(self, *args, **options):
        print("\n=== STATICFILES FINDERS ===")
        for finder in get_finders():
            print(f"\nFinder: {finder.__class__.__name__}")
            for path, _ in finder.list([]):
                print(f"Found: {path}")
