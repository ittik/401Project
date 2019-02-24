# Generated by Django 2.0.6 on 2019-02-22 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_auto_20190222_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='currentCard2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCard', models.CharField(max_length=100)),
                ('typeCard', models.CharField(max_length=50)),
                ('descCard', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=50)),
                ('currenttime', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='historyCard2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCard', models.CharField(max_length=100)),
                ('typeCard', models.CharField(max_length=50)),
                ('descCard', models.CharField(max_length=500)),
                ('compare', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('currenttime', models.CharField(max_length=50)),
            ],
        ),
    ]
