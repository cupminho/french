# Generated by Django 3.2 on 2021-05-05 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('corpus', '0003_auto_20210505_2245'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tagging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('pos', models.CharField(max_length=20)),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='corpus.sentence')),
            ],
        ),
    ]