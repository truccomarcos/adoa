# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-11 02:53
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('orden', models.CharField(max_length=140)),
                ('descripcion', models.CharField(max_length=500)),
                ('contenido', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContenidoPatron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden', models.IntegerField()),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoAsociacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='ElementoIdentificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('correcto', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ElementoOpcionMultiple',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('correcta', models.CharField(max_length=100)),
                ('incorrecta1', models.CharField(max_length=100)),
                ('incorrecta2', models.CharField(max_length=100)),
                ('incorrecta3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ElementoOrdenamiento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('orden', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ElementoVoF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=100)),
                ('verdad', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ObjetoAprendizaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Patron',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=300)),
                ('problemas', ckeditor.fields.RichTextField()),
                ('solucion', ckeditor.fields.RichTextField()),
            ],
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='patron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.Patron'),
        ),
        migrations.AddField(
            model_name='objetoaprendizaje',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='elementovof',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
        migrations.AddField(
            model_name='elementoordenamiento',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
        migrations.AddField(
            model_name='elementoopcionmultiple',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
        migrations.AddField(
            model_name='elementoidentificacion',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
        migrations.AddField(
            model_name='elementoasociacion',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
        migrations.AddField(
            model_name='contenidopatron',
            name='patron',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.Patron'),
        ),
        migrations.AddField(
            model_name='contenido',
            name='objetoAprendizaje',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adoa.ObjetoAprendizaje'),
        ),
    ]
