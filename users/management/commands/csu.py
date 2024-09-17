from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='admin1@admin.ru',
            first_name='admin',
            last_name='admin',
            username='admin',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('admin')
        user.save()
