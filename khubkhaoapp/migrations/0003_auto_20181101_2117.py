# Generated by Django 2.1.2 on 2018-11-01 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('khubkhaoapp', '0002_auto_20181101_1313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='veggie',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='items',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='non_veg',
        ),
        migrations.RemoveField(
            model_name='veggie',
            name='item_name',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Ingredient',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='Veggie',
        ),
    ]
