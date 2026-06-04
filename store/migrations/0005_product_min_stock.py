from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='min_stock',
            field=models.IntegerField(default=5, help_text="Alerte si quantité ≤ seuil", validators=[django.core.validators.MinValueValidator(0)], verbose_name="Seuil d'alerte stock"),
        ),
    ]
