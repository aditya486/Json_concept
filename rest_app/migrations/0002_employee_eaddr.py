# Generated by Django 2.1.7 on 2019-03-26 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='eaddr',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
