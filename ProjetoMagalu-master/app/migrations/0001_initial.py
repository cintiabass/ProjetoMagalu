# Generated by Django 3.2.7 on 2021-09-24 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('razao', models.CharField(max_length=150)),
                ('cnpj', models.CharField(max_length=150)),
                ('telefone', models.CharField(max_length=150)),
                ('segmento', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nomep', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('preco', models.CharField(max_length=100)),
                ('qtdade', models.IntegerField()),
                ('fornecedor', models.CharField(max_length=100)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.empresa')),
            ],
        ),
    ]
