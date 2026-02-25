from django.db import migrations
from django.contrib.auth import get_user_model


def create_superuser(apps, schema_editor):
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            "admin",
            "admin@gmail.com",
            "Admin@123"
        )


class Migration(migrations.Migration):

    dependencies = [
        ('busbookings', '0001_initial'),  # change if needed
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]