# Generated by Django 4.2.7 on 2023-11-16 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoApp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=44)),
                ('content', models.TextField()),
                ('ended', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
