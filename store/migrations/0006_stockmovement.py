from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_min_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change', models.IntegerField(verbose_name='Variation')),
                ('reason', models.CharField(choices=[('RESTOCK', 'Entrée (réassort)'), ('SALE', 'Sortie (vente)'), ('ADJUST', 'Ajustement'), ('OTHER', 'Autre')], default='OTHER', max_length=16, verbose_name='Motif')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Créé le')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movements', to='store.product', verbose_name='Produit')),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.sale', verbose_name='Vente liée')),
            ],
            options={
                'verbose_name': 'Mouvement de stock',
                'verbose_name_plural': 'Mouvements de stock',
                'ordering': ['-created_at'],
            },
        ),
    ]
