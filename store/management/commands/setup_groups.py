from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, User


class Command(BaseCommand):
    help = "Crée les groupes Admin/Caissier et un superuser par défaut si aucun n'existe."

    def handle(self, *args, **options):
        for name in ('Admin', 'Caissier'):
            _, created = Group.objects.get_or_create(name=name)
            if created:
                self.stdout.write(f'  Groupe « {name} » créé.')
            else:
                self.stdout.write(f'  Groupe « {name} » déjà existant.')

        if not User.objects.filter(is_superuser=True).exists():
            User.objects.create_superuser('admin', '', 'admin123')
            self.stdout.write(self.style.WARNING(
                '  Superuser « admin » créé avec le mot de passe « admin123 ».'
                ' CHANGEZ-LE immédiatement en production !'
            ))
        else:
            self.stdout.write('  Un superuser existe déjà — aucun compte créé.')

        self.stdout.write(self.style.SUCCESS('setup_groups terminé.'))
