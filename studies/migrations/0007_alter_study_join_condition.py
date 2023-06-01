# Generated by Django 3.2.18 on 2023-05-31 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studies', '0006_auto_20230531_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='join_condition',
            field=models.PositiveSmallIntegerField(choices=[(1, '승인 필요'), (2, '바로 가입')], default=1),
        ),
    ]