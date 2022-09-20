from django.shortcuts import render,redirect
from django.db.models import*
from APP_TALLY .models import*


def Index(request):
    return render(request,'index.html')

def Statitics(request):
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    vt_total=Voucher.objects.count()
    # total=int(sgtotal+sitotal)
    context={'vt_total':vt_total,'sgtotal':sgtotal,'sitotal':sitotal}
    return render(request,"statistic.html",context)

# stkgrp ---------------

def Statistics_Stock_Groups(request):
    sgdata=stockgroupcreation.objects.all()
    # SGdata=stock_itemcreation.objects.all()
    sqtotal=stockgroupcreation.objects.count()
    # swtotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sqtotal':sqtotal}
    return render(request,'stockgroup.html',context)

def Statistics_Stock_Group_Creation_Page(request):
    sg_data=stockgroupcreation.objects.all()
    context={'sg_data':sg_data}
    return render(request,'stockgrpcreationpage.html',context)

def Statistics_Stock_Group_Creation(request):
    if request.method =='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under_name=request.POST['under_name']
        quantities=request.POST['quantities']

        data=stockgroupcreation(name=name,alias=alias,under=under_name,quantities=quantities)
        data.save()
        return redirect("Statistics_Stock_Groups")

def Statistics_Stock_Group_Edit_Page(request,pk):
    sg_data=stockgroupcreation.objects.all()
    sgedit=stockgroupcreation.objects.get(id=pk)
    context={'sgedit':sgedit,'sg_data':sg_data}
    return render(request,"editstockgroup.html",context)

def Statistics_Edit_Stock_Group(request,pk):
    if request.method =='POST':
        sgdata=stockgroupcreation.objects.get(id=pk)
        sgdata.name=request.POST['name']
        sgdata.alias=request.POST['alias']
        sgdata.under=request.POST['under_name']
        sgdata.quantities=request.POST['quantities']

        sgdata.save()
        return redirect('Statistics_Stock_Groups')
    return render(request,'editstockgroup.html')

def Statistics_Delete_Stock_Group(request,pk):
    stk=stockgroupcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Groups')

# syk item--------------------

def Statistics_Stock_Items(request):
    sgdata=stockgroupcreation.objects.all()
    sidata=stock_itemcreation.objects.all()
    sgtotal=stockgroupcreation.objects.count()
    sitotal=stock_itemcreation.objects.count()
    context={'sgdata':sgdata,'sgtotal':sgtotal,'sidata':sidata,'sitotal':sitotal}
    return render(request,'stockitem.html',context)

def Statistics_Stock_Item_Creation_Page(request):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    context={'si_data':si_data,"grp":grp,'u':u,'unt':unt}
    return render(request,'stockitemcreationpage.html',context)


def Statistics_Stock_Item_Creation(request):
    if request.method=='POST':
        nm=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        units=request.POST['units']
        gst_applicable=request.POST['gst_applicable']
        set_alter=request.POST['set_alter']
        typ_sply=request.POST['typ_sply']
        rate_of_duty=request.POST['rate_of_duty']
        
        crt=stock_itemcreation(name=nm,alias=alias,under=under,units=units,typ_sply=typ_sply,
        gst_applicable=gst_applicable,set_alter=set_alter,rate_of_duty=rate_of_duty)
        crt.save()
        
        return redirect('Statistics_Stock_Items')



def Statistics_Stock_Item_Edit_Page(request,pk):
    si_data=stock_itemcreation.objects.all()
    grp=stockgroupcreation.objects.all()
    unt=unit_compound.objects.all()
    u=unit_simple.objects.all()
    sidata=stock_itemcreation.objects.get(id=pk)
    context={'edit':sidata,"si_data":si_data,'grp':grp,'unt':unt,'u':u}
    return render(request,"editstockitem.html",context)

def Statistics_Edit_Stock_Item(request,pk):
    if request.method =='POST':
        sidata=stock_itemcreation.objects.get(id=pk)
        sidata.name=request.POST['name']
        sidata.alias=request.POST['alias']
        sidata.under=request.POST['under']
        sidata.units=request.POST['units']
        sidata.gst_applicable=request.POST['gst_applicable']
        sidata.set_alter=request.POST['set_alter']
        sidata.typ_sply=request.POST['typ_sply']
        sidata.rate_of_duty=request.POST['si_data']
        sidata.quantity=request.POST['quantity']
        sidata.rate=request.POST['rate']
        sidata.per=request.POST['per']
        sidata.value=request.POST['value']

        sidata.save()
        return redirect('Statistics_Stock_Items')
    return render(request,'editstockitem.html')

def Statistics_Delete_Stock_Item(request,pk):
    stk=stock_itemcreation.objects.get(id=pk)
    stk.delete()
    return redirect('Statistics_Stock_Items')

# vchr typ ---------------------

def Statistics_Voucher_Types(request):
    vt_data=Voucher.objects.all()
    vt_total=Voucher.objects.count()
    context={'vt_data':vt_data,'vt_total':vt_total}
    return render(request,'vouchertype.html',context)

def Statistics_Voucher_Type_Creation_Page(request):
    data=Voucher.objects.all()
    context={'data':data}
    return render(request,'vouchertypecreationpage.html',context)

def Statistics_Voucher_Type_Creation(request):
        if request.method=='POST':
            nm=request.POST['vname']
            als=request.POST['alias']
            vtp=request.POST['vouch_type']
            abbr=request.POST['Abbreviation']
            actp=request.POST['activate_Vtype']
            mvno=request.POST['method_Vno']
            prnt=request.POST['prevent']
            acn=request.POST['advance_con']
            use=request.POST['use_EDV']
            zero=request.POST['zero_val']
            mvd=request.POST['mVoptional_defualt']
            anar=request.POST['allow_nar']
            prvdl=request.POST['provide_L']
            jrnl=request.POST['manu_jrnl']
            track=request.POST['track_purchase']
            enbl=request.POST['enable_acc']
            prntva=request.POST['prnt_VA_save']
            prntfml=request.POST['prnt_frml']
            juri=request.POST['jurisdiction']
            tprint=request.POST['title_print']
            setaltr=request.POST['set_alter']
            posinv=request.POST['pos_invoice']
            msg1=request.POST['msg_1']
            msg2=request.POST['msg_2']
            dbank=request.POST['default_bank']
            nc=request.POST['name_class']

            vhr=Voucher(voucher_name=nm,
                        alias = als,
                        voucher_type = vtp,
                        abbreviation = abbr,
                        voucherActivate = actp,
                        voucherNumber = mvno,
                        preventDuplicate = prnt,
                        advance_con = acn,
                        voucherEffective = use,
                        transaction = zero,
                        make_optional = mvd,
                        voucherNarration = anar,
                        provideNarration = prvdl,
                        manu_jrnl = jrnl,
                        track_purchase = track,
                        enable_acc = enbl,
                        prnt_VA_save = prntva,
                        prnt_frml = prntfml,
                        jurisdiction = juri,
                        title_print = tprint,
                        set_alter = setaltr,
                        pos_invoice = posinv,
                        msg_1 = msg1,
                        msg_2 = msg2,
                        default_bank = dbank,
                        name_class = nc,)          
            vhr.save()
            return redirect('Statistics_Voucher_Types')

def Statistics_Voucher_Type_Edit_Page(request,pk):
    vt_edit=Voucher.objects.get(id=pk)
    edit=Voucher.objects.all()
    context={'vt_edit':vt_edit,'edit':edit}
    return render(request,'vouchertypeeditpage.html',context)

def Statistics_Edit_Voucher_Types(request,pk):
    if request.method =='POST':
        vchrdata=Voucher.objects.get(id=pk)
        vchrdata.voucher_name=request.POST['vname']
        vchrdata.alias=request.POST['alias']
        # vchrdata.voucher_type=request.POST['vouch_type']
        vchrdata.abbreviation=request.POST['Abbreviation']
        vchrdata.voucherActivate=request.POST['activate_Vtype']
        vchrdata.voucherNumber=request.POST['method_Vno']
        vchrdata.preventDuplicate=request.POST['prevent']
        vchrdata.advance_con=request.POST['advance_con']
        vchrdata.voucherEffective=request.POST['use_EDV']
        vchrdata.transaction=request.POST['zero_val']
        vchrdata.make_optional=request.POST['mVoptional_defualt']
        vchrdata.voucherNarration=request.POST['allow_nar']
        vchrdata.provideNarration=request.POST['provide_L']
        vchrdata.manu_jrnl=request.POST['manu_jrnl']
        vchrdata.track_purchase=request.POST['track_purchase']
        vchrdata.enable_acc=request.POST['enable_acc']
        vchrdata.prnt_VA_save=request.POST['prnt_VA_save']
        vchrdata.prnt_frml=request.POST['prnt_frml']
        vchrdata.jurisdiction=request.POST['jurisdiction']
        vchrdata.title_print=request.POST['title_print']
        vchrdata.set_alter=request.POST['set_alter']
        vchrdata.pos_invoice=request.POST['pos_invoice']
        vchrdata.msg_1=request.POST['msg_1']
        vchrdata.msg_2=request.POST['msg_2']
        vchrdata.default_bank=request.POST['default_bank']
        vchrdata.name_class=request.POST['name_class']

    vchrdata.save()
    return redirect('Statistics_Voucher_Types')

def Statistics_Delete_Voucher_Type(request,pk):
    vt=Voucher.objects.get(id=pk)
    vt.delete()
    return redirect('Statistics_Voucher_Types')