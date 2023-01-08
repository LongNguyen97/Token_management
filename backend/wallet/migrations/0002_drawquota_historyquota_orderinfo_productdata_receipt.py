# Generated by Django 3.0.8 on 2023-01-07 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrawQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128)),
                ('identify', models.CharField(max_length=128)),
                ('game_id', models.CharField(max_length=128)),
                ('amount', models.IntegerField()),
                ('amount_used', models.IntegerField()),
            ],
            options={
                'db_table': 'draw_quota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HistoryQuota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=64)),
                ('product_id', models.CharField(max_length=64)),
                ('game_id', models.CharField(max_length=128)),
                ('amount', models.IntegerField()),
                ('time_add', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'history_quota',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=128)),
                ('device_number', models.CharField(max_length=64)),
                ('time', models.DateTimeField()),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'order_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identify', models.CharField(max_length=200)),
                ('real_price', models.CharField(max_length=12)),
                ('virtual_currency', models.CharField(max_length=64)),
                ('game_id', models.CharField(max_length=128)),
                ('game_name', models.CharField(max_length=128)),
                ('price_amount_micros', models.BigIntegerField()),
                ('price_currency_code', models.CharField(max_length=16)),
                ('skudetailstoken', models.TextField()),
                ('type', models.CharField(max_length=16)),
                ('description', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'product_data',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_id', models.CharField(max_length=64)),
                ('identify', models.CharField(max_length=64)),
                ('user_id', models.CharField(max_length=64)),
                ('assigned_user', models.CharField(max_length=128)),
                ('token', models.TextField()),
                ('signature', models.TextField()),
                ('order_id', models.CharField(max_length=64)),
                ('used', models.BooleanField()),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'receipt',
                'managed': False,
            },
        ),
    ]