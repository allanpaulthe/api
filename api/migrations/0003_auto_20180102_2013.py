# Generated by Django 2.0 on 2018-01-02 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_marks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marks',
            name='marks',
            field=models.CharField(max_length=200),
        ),
    ]
