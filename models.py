from django.db import models

# Create your models here.

class stockgroupcreation(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under=models.CharField(max_length=100)
    quantities=models.CharField(max_length=100)

class stock_itemcreation(models.Model):
    name=models.CharField(max_length=100,null=True)
    alias=models.CharField(max_length=100,null=True)
    under=models.CharField(max_length=100,null=True)
    units=models.CharField(max_length=100,null=True)
    batches=models.CharField(max_length=10,null=True)
    trackdate=models.CharField(max_length=10,null=True)
    expirydate=models.CharField(max_length=10,null=True)
    gst_applicable=models.CharField(max_length=100,null=True)
    typ_sply=models.CharField(max_length=100)
    set_alter=models.CharField(max_length=100)
    rate_of_duty=models.IntegerField()
    quantity=models.CharField(max_length=100,null=True)
    rate=models.CharField(max_length=100,null=True)
    per=models.CharField(max_length=100,null=True)
    value=models.CharField(max_length=100,null=True)

class Voucher(models.Model):
    voucher_name = models.CharField(max_length=255,null=True)
    alias = models.CharField(max_length=255,null=True)
    voucher_type = models.CharField(max_length=255,null=True)
    abbreviation = models.CharField(max_length=255,null=True)
    voucherActivate = models.CharField(max_length=20,null=True)
    voucherNumber = models.CharField(max_length=200,null=True)
    preventDuplicate = models.CharField(max_length=20,null=True)
    advance_con = models.CharField(max_length=20,null=True)
    voucherEffective = models.CharField(max_length=20,null=True)
    transaction = models.CharField(max_length=20,null=True)
    make_optional = models.CharField(max_length=20,null=True)
    voucherNarration = models.CharField(max_length=20,null=True)
    provideNarration = models.CharField(max_length=20,null=True)
    manu_jrnl = models.CharField(max_length=20,null=True)
    track_purchase = models.CharField(max_length=20,null=True)
    enable_acc = models.CharField(max_length=20,null=True)
    prnt_VA_save = models.CharField(max_length=20,null=True)
    prnt_frml = models.CharField(max_length=20,null=True)
    jurisdiction = models.CharField(max_length=20,null=True)
    title_print = models.CharField(max_length=20,null=True)
    set_alter = models.CharField(max_length=20,null=True)
    pos_invoice = models.CharField(max_length=20,null=True)
    msg_1 = models.CharField(max_length=255,null=True)
    msg_2 = models.CharField(max_length=255,null=True)
    default_bank = models.CharField(max_length=255,null=True)
    name_class = models.CharField(max_length=255,null=True)


class unit_simple(models.Model):
    type=models.CharField(max_length=100)
    symbol=models.CharField(max_length=100)
    formal_name=models.CharField(max_length=100)
    uqc=models.CharField(max_length=100)
    decimal=models.IntegerField()
    
class unit_compound(models.Model):
    typ=models.CharField(max_length=100)
    f_unit=models.CharField(max_length=100,null=True)
    conversion=models.IntegerField()
    s_unit=models.CharField(max_length=100,null=True)