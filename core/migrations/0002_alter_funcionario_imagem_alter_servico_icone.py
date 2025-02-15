# Generated by Django 5.0.6 on 2024-06-28 19:18

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thum': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-rocket', 'Foguete'), ('lni-stats-up', 'Gráfico'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-users', 'Usuário'), ('lni-cog', 'Engrenagem')], max_length=12, verbose_name='Incone'),
        ),
    ]
