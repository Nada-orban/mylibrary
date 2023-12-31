# Generated by Django 4.2.3 on 2023-07-19 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250, null=True)),
                ('photo_book', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('photo_author', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_price_month', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('rental_period', models.IntegerField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(blank=True, choices=[('availble', 'availble'), ('rental', 'rental'), ('sold', 'sold')], max_length=50, null=True)),
                ('Category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='mylibrary_app.category')),
            ],
        ),
    ]
