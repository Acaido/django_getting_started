# Generated by Django 2.0 on 2018-01-14 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0006_auto_20180114_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='twitter.Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='twit',
            name='updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mid_name',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
