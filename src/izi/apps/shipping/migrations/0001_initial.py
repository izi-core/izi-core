# Generated by Django 2.1.1 on 2018-10-01 04:05

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import izi.models.fields.autoslugfield


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderAndItemCharges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', izi.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('price_per_order', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per order')),
                ('price_per_item', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=12, verbose_name='Price per item')),
                ('free_shipping_threshold', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='Free Shipping')),
                ('countries', models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries')),
            ],
            options={
                'verbose_name': 'Order and Item Charge',
                'verbose_name_plural': 'Order and Item Charges',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeightBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_limit', models.DecimalField(decimal_places=3, help_text='Enter upper limit of this weight band in kg. The lower limit will be determined by the other weight bands.', max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Upper Limit')),
                ('charge', models.DecimalField(decimal_places=2, max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Charge')),
            ],
            options={
                'verbose_name': 'Weight Band',
                'verbose_name_plural': 'Weight Bands',
                'ordering': ['method', 'upper_limit'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WeightBased',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', izi.models.fields.autoslugfield.AutoSlugField(blank=True, editable=False, max_length=128, populate_from='name', unique=True, verbose_name='Slug')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('default_weight', models.DecimalField(decimal_places=3, default=Decimal('0.000'), help_text='Default product weight in kg when no weight attribute is defined', max_digits=12, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))], verbose_name='Default Weight')),
                ('countries', models.ManyToManyField(blank=True, to='address.Country', verbose_name='Countries')),
            ],
            options={
                'verbose_name': 'Weight-based Shipping Method',
                'verbose_name_plural': 'Weight-based Shipping Methods',
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='weightband',
            name='method',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bands', to='shipping.WeightBased', verbose_name='Method'),
        ),
    ]
