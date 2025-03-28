from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'This will update your system to TCG AGENCY version 1.4.'

    def handle(self, *args, **options):
        # Run migrations
        self.stdout.write('Update initiating...')
        self.stdout.write('Running migrations...')
        call_command("makemigrations", interactive=False)
        call_command("migrate", interactive=False)
        self.stdout.write(self.style.SUCCESS('Migrations completed.'))
        
        self.stdout.write('Updated successfully. You can use your system now.')

        
