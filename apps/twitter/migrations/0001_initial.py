# Generated by Django 2.0 on 2018-01-14 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('removed', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Twit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('published', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('removed', models.BooleanField(default=False)),
                ('header', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('mid_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=20)),
                ('nick_name', models.CharField(max_length=30)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='twit',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.User'),
        ),
        migrations.AddField(
            model_name='tag',
            name='twit',
            field=models.ManyToManyField(to='twitter.Twit'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.Comment'),
        ),
        migrations.AddField(
            model_name='comment',
            name='twit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='twitter.Twit'),
        ),
    ]
