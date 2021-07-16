# Generated by Django 3.2.5 on 2021-07-07 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0003_auto_20210707_1901'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transacao',
            options={'verbose_name_plural': 'Transacoes'},
        ),
        migrations.RenameField(
            model_name='transacao',
            old_name='categoria',
            new_name='tipo_de_transacao',
        ),
        migrations.RemoveField(
            model_name='categoria',
            name='data_criacao',
        ),
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
