# Generated by Django 2.2.4 on 2019-09-04 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('no_of_researchers', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('ini_pitch', models.TextField()),
                ('researcher_id', models.IntegerField()),
            ],
        ),
    ]