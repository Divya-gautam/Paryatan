# Generated by Django 3.2.3 on 2022-03-09 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qrscan', '0003_auto_20220309_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='city',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='count',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='date',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='monument',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='order_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='paid',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='razorpay_payment_id',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='total_cost',
        ),
    ]
