# Generated by Django 4.2.6 on 2023-12-01 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_useradmin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useradmin',
            options={},
        ),
        migrations.AlterModelTable(
            name='comment',
            table='comments',
        ),
        migrations.AlterModelTable(
            name='game',
            table='games',
        ),
        migrations.AlterModelTable(
            name='review',
            table='reviews',
        ),
        migrations.AlterModelTable(
            name='useradmin',
            table='useradmin',
        ),
    ]