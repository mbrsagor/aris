# Generated by Django 2.0.6 on 2018-06-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aris_app', '0005_auto_20180614_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.IntegerField(),
        ),
    ]
