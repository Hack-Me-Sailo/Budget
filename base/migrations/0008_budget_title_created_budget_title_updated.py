# Generated by Django 5.0.4 on 2024-08-24 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_item_created_item_updated_alter_budget_title_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='budget_title',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='budget_title',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
