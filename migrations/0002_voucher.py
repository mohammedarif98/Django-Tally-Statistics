# Generated by Django 4.0.5 on 2022-09-18 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP_TALLY', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Voucher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_name', models.CharField(max_length=255, null=True)),
                ('alias', models.CharField(max_length=255, null=True)),
                ('voucher_type', models.CharField(max_length=255, null=True)),
                ('abbreviation', models.CharField(max_length=255, null=True)),
                ('voucherActivate', models.CharField(max_length=20, null=True)),
                ('voucherNumber', models.CharField(max_length=200, null=True)),
                ('preventDuplicate', models.CharField(max_length=20, null=True)),
                ('advance_con', models.CharField(max_length=20, null=True)),
                ('voucherEffective', models.CharField(max_length=20, null=True)),
                ('transaction', models.CharField(max_length=20, null=True)),
                ('make_optional', models.CharField(max_length=20, null=True)),
                ('voucherNarration', models.CharField(max_length=20, null=True)),
                ('provideNarration', models.CharField(max_length=20, null=True)),
                ('manu_jrnl', models.CharField(max_length=20, null=True)),
                ('track_purchase', models.CharField(max_length=20, null=True)),
                ('enable_acc', models.CharField(max_length=20, null=True)),
                ('prnt_VA_save', models.CharField(max_length=20, null=True)),
                ('prnt_frml', models.CharField(max_length=20, null=True)),
                ('jurisdiction', models.CharField(max_length=20, null=True)),
                ('title_print', models.CharField(max_length=20, null=True)),
                ('set_alter', models.CharField(max_length=20, null=True)),
                ('pos_invoice', models.CharField(max_length=20, null=True)),
                ('msg_1', models.CharField(max_length=255, null=True)),
                ('msg_2', models.CharField(max_length=255, null=True)),
                ('default_bank', models.CharField(max_length=255, null=True)),
                ('name_class', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
