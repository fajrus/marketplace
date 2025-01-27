# Generated by Django 3.2 on 2024-03-25 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_customer_options_alter_customer_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransaksiPembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_transaksi', models.CharField(max_length=200, null=True)),
                ('nama_suplayer', models.CharField(max_length=200, null=True)),
                ('total_transaksi', models.BigIntegerField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Baru', 'Baru'), ('Lunas', 'Lunas')], default='Baru', max_length=200, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('tanggal_kulakan', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DetailTransaksiPembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.IntegerField(blank=True, null=True)),
                ('produk', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transaksi_pembelian_produk', to='core.produk')),
                ('transaksi_pembelian', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='detail_pembelians', to='core.transaksipembelian')),
            ],
        ),
    ]
