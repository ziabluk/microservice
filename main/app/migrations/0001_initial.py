# Generated by Django 5.1.3 on 2024-11-11 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('group', models.CharField(choices=[('SNICKERS', 'snickers'), ('SHIRTS', 'shirts'), ('TROUSERS', 'trousers')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Storage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('products', models.ManyToManyField(related_name='storage', to='app.product')),
            ],
        ),
    ]
