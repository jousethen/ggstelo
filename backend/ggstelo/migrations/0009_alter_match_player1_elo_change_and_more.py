# Generated by Django 4.1.6 on 2023-02-28 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ggstelo', '0008_alter_match_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='player1_elo_change',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='match',
            name='player2_elo_change',
            field=models.IntegerField(default=0),
        ),
    ]
