# Generated by Django 4.2.6 on 2023-10-16 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RingPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.BinaryField()),
                ('color', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listOfRingPosition', models.ManyToManyField(to='threedgame.ringposition')),
            ],
        ),
        migrations.CreateModel(
            name='CubeData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.CharField(max_length=100)),
                ('numberOfMoves', models.IntegerField()),
                ('status', models.BooleanField()),
                ('listOfMoves', models.ManyToManyField(to='threedgame.move')),
            ],
        ),
    ]
