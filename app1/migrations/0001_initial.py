# Generated by Django 3.1.7 on 2021-06-10 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Audio_store',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record', models.FileField(upload_to='documents/')),
            ],
            options={
                'db_table': 'Audio_store',
            },
        ),
    ]
