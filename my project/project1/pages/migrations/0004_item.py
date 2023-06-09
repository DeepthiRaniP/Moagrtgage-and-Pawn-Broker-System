# Generated by Django 2.2.13 on 2023-05-07 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20230507_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.CharField(choices=[('House', 'House'), ('Gold', 'Gold'), ('Electronics', 'Electronics'), ('musical instruments', 'musical instruments'), ('smart phones', 'smart phones')], max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('interest_rate', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'Item_table',
            },
        ),
    ]
