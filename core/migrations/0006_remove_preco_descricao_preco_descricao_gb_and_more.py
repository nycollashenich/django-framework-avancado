# Generated by Django 5.0.6 on 2024-07-02 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_preco_alter_recurso_icone_alter_servico_icone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preco',
            name='descricao',
        ),
        migrations.AddField(
            model_name='preco',
            name='descricao_gb',
            field=models.CharField(default='default description', max_length=100, verbose_name='Descrição gb'),
        ),
        migrations.AddField(
            model_name='preco',
            name='descricao_suporte',
            field=models.CharField(default='default description', max_length=100, verbose_name='Descrição sup'),
        ),
        migrations.AddField(
            model_name='preco',
            name='descricao_updates',
            field=models.CharField(default='default description', max_length=100, verbose_name='Descrição up'),
        ),
        migrations.AddField(
            model_name='preco',
            name='descricao_users',
            field=models.CharField(default='default description', max_length=100, verbose_name='Descrição users'),
        ),
        migrations.AddField(
            model_name='preco',
            name='tipo_plano',
            field=models.CharField(default='default description', max_length=100, verbose_name='Plano'),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-laptop-phone', 'Computador'), ('lni-leaf', 'Folha'), ('lni-layers', 'Camadas')], max_length=16, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni-rocket', 'Foguete'), ('lni-users', 'Usuário'), ('lni-layers', 'Design'), ('lni-stats-up', 'Gráfico'), ('lni-mobile', 'Mobile')], max_length=12, verbose_name='Icone'),
        ),
    ]
