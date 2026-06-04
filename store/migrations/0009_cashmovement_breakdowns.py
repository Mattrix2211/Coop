from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('store', '0008_cashsession_current_counts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashmovement',
            name='tendered_breakdown',
            field=models.JSONField(blank=True, null=True, verbose_name='Ventilation espèces données'),
        ),
        migrations.AddField(
            model_name='cashmovement',
            name='change_breakdown',
            field=models.JSONField(blank=True, null=True, verbose_name='Ventilation rendu'),
        ),
        migrations.AddField(
            model_name='cashmovement',
            name='change_amount',
            field=models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2, verbose_name='Montant rendu'),
        ),
    ]
