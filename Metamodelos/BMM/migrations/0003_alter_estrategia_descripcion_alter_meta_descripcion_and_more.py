# Generated by Django 4.2.1 on 2023-06-02 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BMM', '0002_alter_estrategia_descripcion_alter_meta_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estrategia',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='meta',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='mision',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='objetivo',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='tactica',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
        migrations.AlterField(
            model_name='vision',
            name='descripcion',
            field=models.TextField(max_length=1400),
        ),
    ]
