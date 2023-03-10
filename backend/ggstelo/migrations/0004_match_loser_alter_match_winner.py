# Generated by Django 4.1.6 on 2023-02-10 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ggstelo', '0003_remove_match_players_alter_match_winner'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='loser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loser_match_set', to='ggstelo.player'),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='winner_match_set', to='ggstelo.player'),
        ),
    ]
