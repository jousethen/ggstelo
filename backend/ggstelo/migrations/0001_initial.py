# Generated by Django 4.1.7 on 2023-03-22 23:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField()),
                ('gamer_tag', models.CharField(max_length=50)),
                ('elo', models.PositiveIntegerField(default=1000)),
                ('highest_elo', models.PositiveIntegerField(default=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-elo',),
            },
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created_at',),
            },
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True)),
                ('player1_score', models.CharField(max_length=50)),
                ('player2_score', models.CharField(max_length=50)),
                ('player1_elo_change', models.IntegerField(default=0)),
                ('player2_elo_change', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('player1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player1_match_set', to='ggstelo.player')),
                ('player2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='player2_match_set', to='ggstelo.player')),
                ('tournament', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ggstelo.tournament')),
            ],
            options={
                'verbose_name_plural': 'matches',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userId', models.CharField(default=uuid.uuid4, editable=False, max_length=16, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Custom User',
            },
        ),
    ]
