# Generated by Django 4.1.6 on 2023-03-01 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ggstelo', '0012_alter_player_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='player',
            options={'ordering': ('elo',)},
        ),
    ]
