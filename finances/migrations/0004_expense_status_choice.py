# Generated by Django 5.1.6 on 2025-02-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0003_expense_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='status_choice',
            field=models.CharField(choices=[('Pendente', 'Pendente'), ('Atrasado', 'Atrasado'), ('Pago', 'Pago')], default='Pendente', max_length=20),
        ),
    ]
