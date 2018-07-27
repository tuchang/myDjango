# Generated by Django 2.0.6 on 2018-07-09 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=20)),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='mood',
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
