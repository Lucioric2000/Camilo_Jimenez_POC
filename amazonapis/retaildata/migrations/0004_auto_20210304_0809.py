# Generated by Django 3.1.7 on 2021-03-04 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retaildata', '0003_auto_20210304_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coderedemption',
            name='account_where_to_redeem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='retaildata.retaileraccount'),
        ),
    ]
