# Generated by Django 4.2.7 on 2023-11-26 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_berita_kategoriid_berita_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berita',
            name='kategoriID',
            field=models.IntegerField(null=True),
        ),
    ]