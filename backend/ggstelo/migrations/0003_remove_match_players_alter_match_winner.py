# Generated by Django 4.1.6 on 2023-02-10 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ggstelo', '0002_alter_player_options_tournament_match'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='players',
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='loser_match_set', to='ggstelo.player'),
        ),
    ]
