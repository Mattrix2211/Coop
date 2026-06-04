from django.db import migrations, models


def init_current_counts(apps, schema_editor):
    CashSession = apps.get_model('store', 'CashSession')
    for session in CashSession.objects.all():
        if not session.current_counts:
            # Copier ouverture sinon structure minimale
            opening = session.opening_counts or {}
            if opening:
                session.current_counts = opening.copy()
            else:
                session.current_counts = {'cash': {}, 'cheques': 0}
            session.save(update_fields=['current_counts'])


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_cashsession_alter_stockmovement_id_cashmovement'),
    ]

    operations = [
        migrations.AddField(
            model_name='cashsession',
            name='current_counts',
            field=models.JSONField(blank=True, null=True, default=dict, verbose_name='Comptage courant'),
        ),
        migrations.RunPython(init_current_counts, migrations.RunPython.noop),
    ]
