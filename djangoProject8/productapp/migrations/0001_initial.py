# Generated by Django 4.2.2 on 2023-06-06 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('pip', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=20)),
                ('pcost', models.DecimalField(decimal_places=2, max_digits=20)),
                ('pmfdt', models.DateField()),
                ('expdt', models.DateField()),
            ],
        ),
    ]
