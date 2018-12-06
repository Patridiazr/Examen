# Generated by Django 2.1.2 on 2018-12-06 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_tienda_aprobado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('total_A', models.IntegerField()),
                ('total_C', models.IntegerField()),
                ('costo_P', models.IntegerField()),
                ('costo_R', models.IntegerField()),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]