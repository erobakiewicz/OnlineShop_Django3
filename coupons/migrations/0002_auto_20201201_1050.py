# Generated by Django 3.1.3 on 2020-12-01 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Coupons',
            new_name='Coupon',
        ),
        migrations.RenameField(
            model_name='coupon',
            old_name='vaild_from',
            new_name='valid_from',
        ),
    ]
