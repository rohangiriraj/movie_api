# Generated by Django 4.1.5 on 2023-01-26 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Collections',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('uuid', models.UUIDField(default=uuid.UUID('6c4bd16a-d50f-412c-b595-9eb66b57c900'), editable=False, primary_key=True, serialize=False)),
                ('movies', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]