# Generated by Django 2.2.4 on 2019-08-11 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='short_url',
            field=models.URLField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='title',
            field=models.CharField(default='No title', max_length=200),
        ),
        migrations.AlterField(
            model_name='site',
            name='visitors',
            field=models.IntegerField(default=0),
        ),
    ]
