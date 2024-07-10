# Generated by Django 5.0.7 on 2024-07-10 22:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerenciamento', '0006_alter_funcionario_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gerenciamento.funcionario'),
        ),
        migrations.AddField(
            model_name='pedidomaterial',
            name='funcionario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gerenciamento.funcionario'),
        ),
    ]
