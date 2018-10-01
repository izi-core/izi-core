# Generated by Django 2.1.1 on 2018-10-01 04:05

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('offer', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='This will be shown in the checkout and basket once the voucher is entered', max_length=128, verbose_name='Name')),
                ('code', models.CharField(db_index=True, help_text='Case insensitive / No spaces allowed', max_length=128, unique=True, verbose_name='Code')),
                ('usage', models.CharField(choices=[('Single use', 'Can be used once by one customer'), ('Multi-use', 'Can be used multiple times by multiple customers'), ('Once per customer', 'Can only be used once per customer')], default='Multi-use', max_length=128, verbose_name='Usage')),
                ('start_datetime', models.DateTimeField(verbose_name='Start datetime')),
                ('end_datetime', models.DateTimeField(verbose_name='End datetime')),
                ('num_basket_additions', models.PositiveIntegerField(default=0, verbose_name='Times added to basket')),
                ('num_orders', models.PositiveIntegerField(default=0, verbose_name='Times on orders')),
                ('total_discount', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Total discount')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('offers', models.ManyToManyField(limit_choices_to={'offer_type': 'Voucher'}, related_name='vouchers', to='offer.ConditionalOffer', verbose_name='Offers')),
            ],
            options={
                'verbose_name': 'Voucher',
                'verbose_name_plural': 'Vouchers',
                'get_latest_by': 'date_created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoucherApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order', verbose_name='Order')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
                ('voucher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='voucher.Voucher', verbose_name='Voucher')),
            ],
            options={
                'verbose_name': 'Voucher Application',
                'verbose_name_plural': 'Voucher Applications',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VoucherSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('count', models.PositiveIntegerField(verbose_name='Number of vouchers')),
                ('code_length', models.IntegerField(default=12, verbose_name='Length of Code')),
                ('description', models.TextField(verbose_name='Description')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('start_datetime', models.DateTimeField(verbose_name='Start datetime')),
                ('end_datetime', models.DateTimeField(verbose_name='End datetime')),
                ('offer', models.OneToOneField(blank=True, limit_choices_to={'offer_type': 'Voucher'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voucher_set', to='offer.ConditionalOffer', verbose_name='Offer')),
            ],
            options={
                'verbose_name': 'VoucherSet',
                'verbose_name_plural': 'VoucherSets',
                'get_latest_by': 'date_created',
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='voucher',
            name='voucher_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vouchers', to='voucher.VoucherSet'),
        ),
    ]
