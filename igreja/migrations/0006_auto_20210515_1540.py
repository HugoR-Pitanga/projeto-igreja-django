# Generated by Django 2.2.22 on 2021-05-15 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('igreja', '0005_auto_20210515_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movimentofinanceiro',
            name='origem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='igreja.OrigemMovimentoFinanceiro'),
        ),
    ]
