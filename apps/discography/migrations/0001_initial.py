# Generated by Django 2.0 on 2018-01-14 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('published', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateField()),
                ('broke_up', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BandRole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Performer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PerformerBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.BooleanField()),
                ('member_from', models.DateField()),
                ('member_to', models.DateField(blank=True, null=True)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discography.Band')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discography.Performer')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('written', models.DateField()),
                ('album', models.ManyToManyField(to='discography.Album')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discography.Genre')),
            ],
        ),
        migrations.CreateModel(
            name='TrackPerformer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('band_role', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='discography.BandRole')),
                ('performer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discography.Performer')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='discography.Track')),
            ],
        ),
        migrations.AddField(
            model_name='track',
            name='performer',
            field=models.ManyToManyField(through='discography.TrackPerformer', to='discography.Performer'),
        ),
        migrations.AddField(
            model_name='performer',
            name='band',
            field=models.ManyToManyField(through='discography.PerformerBand', to='discography.Band'),
        ),
    ]
