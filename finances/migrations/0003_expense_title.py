# Generated by Django 5.1.6 on 2025-02-11 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finances', '0002_alter_expense_userfk'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
