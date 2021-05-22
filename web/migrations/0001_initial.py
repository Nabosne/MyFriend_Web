# Generated by Django 3.2.3 on 2021-05-22 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beacon_espaco', models.BigIntegerField()),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('auxiliar', models.IntegerField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Beacon',
                'db_table': 'Beacon',
                'ordering': ('nome', 'beacon_espaco'),
            },
        ),
        migrations.CreateModel(
            name='BeaconAA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name_plural': 'Destinos',
                'db_table': 'Destino',
            },
        ),
        migrations.CreateModel(
            name='Espacos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destinos', models.ManyToManyField(null=True, to='web.Destino')),
                ('espaco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.beacon')),
            ],
            options={
                'verbose_name_plural': 'Espaços',
                'db_table': 'Espacos',
            },
        ),
        migrations.CreateModel(
            name='LocalApp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Tipos de Local',
                'db_table': 'TipoLocal',
            },
        ),
        migrations.CreateModel(
            name='Percurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sequencia', models.IntegerField()),
                ('instrucao', models.TextField()),
                ('proximo_destino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.beacon')),
            ],
            options={
                'verbose_name_plural': 'Percursos',
                'db_table': 'Percurso',
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beacon_local', models.BigIntegerField(unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=100)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=10)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('auxiliar', models.IntegerField(max_length=1)),
                ('tipo_local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.tipolocal')),
            ],
            options={
                'verbose_name_plural': 'Local',
                'db_table': 'Local',
                'ordering': ('nome', 'beacon_local'),
            },
        ),
        migrations.CreateModel(
            name='Locais',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('espacos', models.ManyToManyField(null=True, to='web.Espacos')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.local')),
            ],
            options={
                'verbose_name_plural': 'Locais My Friend',
                'db_table': 'Locais',
            },
        ),
        migrations.AddField(
            model_name='destino',
            name='caminho',
            field=models.ManyToManyField(to='web.Percurso'),
        ),
        migrations.AddField(
            model_name='destino',
            name='destino_final',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.beacon'),
        ),
    ]
