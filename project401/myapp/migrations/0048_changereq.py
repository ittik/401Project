# Generated by Django 2.0.6 on 2019-03-13 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0047_auto_20190313_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='changeReq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amountChange', models.IntegerField(default=0)),
                ('timestamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.timeStamp')),
            ],
        ),
    ]