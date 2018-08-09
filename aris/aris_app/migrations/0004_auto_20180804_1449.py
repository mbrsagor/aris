# Generated by Django 2.0.7 on 2018-08-04 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aris_app', '0003_memberinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hand_type', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='memberinfo',
            name='name',
        ),
        migrations.DeleteModel(
            name='MemberInfo',
        ),
    ]
