# Generated by Django 4.1.2 on 2023-06-02 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ontologico', '0005_remove_meta_objetivo_remove_meta_tactica_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='curso',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ontologico.curso'),
            preserve_default=False,
        ),
    ]
