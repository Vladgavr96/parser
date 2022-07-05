# Generated by Django 4.0.6 on 2022-07-05 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=512)),
                ('articul', models.IntegerField()),
                ('item_id', models.IntegerField()),
                ('full_price', models.IntegerField()),
                ('sale_price', models.IntegerField()),
                ('status', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Диван',
                'verbose_name_plural': 'Диваны',
            },
        ),
    ]