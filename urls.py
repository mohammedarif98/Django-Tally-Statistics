from APP_TALLY import views
from django.urls import path

urlpatterns=[
    path('',views.Index,name='Index'),
    path('Statitics',views.Statitics,name="Statitics"),

    path('Statistics_Stock_Groups',views.Statistics_Stock_Groups,name="Statistics_Stock_Groups"),
    path('Statistics_Stock_Group_Creation_Page',views.Statistics_Stock_Group_Creation_Page,name="Statistics_Stock_Group_Creation_Page"),
    path('Statistics_Stock_Group_Creation',views.Statistics_Stock_Group_Creation,name='Statistics_Stock_Group_Creation'),
    path('Statistics_Stock_Group_Edit_Page/<int:pk>',views.Statistics_Stock_Group_Edit_Page,name='Statistics_Stock_Group_Edit_Page'),
    path('Statistics_Edit_Stock_Group/<int:pk>',views.Statistics_Edit_Stock_Group,name='Statistics_Edit_Stock_Group'),
    path('Statistics_Delete_Stock_Group/<int:pk>',views.Statistics_Delete_Stock_Group,name='Statistics_Delete_Stock_Group'),

    path('Statistics_Stock_Items',views.Statistics_Stock_Items,name="Statistics_Stock_Items"),
    path('Statistics_Stock_Item_Creation_Page',views.Statistics_Stock_Item_Creation_Page,name="Statistics_Stock_Item_Creation_Page"),
    path('Statistics_Stock_Item_Creation',views.Statistics_Stock_Item_Creation,name='Statistics_Stock_Item_Creation'),
    path('Statistics_Stock_Item_Edit_Page/<int:pk>',views.Statistics_Stock_Item_Edit_Page,name='Statistics_Stock_Item_Edit_Page'),
    path('Statistics_Edit_Stock_Item/<int:pk>',views.Statistics_Edit_Stock_Item,name='Statistics_Edit_Stock_Item'),
    path('Statistics_Delete_Stock_Item/<int:pk>',views.Statistics_Delete_Stock_Item,name='Statistics_Delete_Stock_Item'),

    path('Statistics_Voucher_Types',views.Statistics_Voucher_Types,name="Statistics_Voucher_Types"),
    path('Statistics_Voucher_Type_Creation_Page',views.Statistics_Voucher_Type_Creation_Page,name='Statistics_Voucher_Type_Creation_Page'),
    path('Statistics_Voucher_Type_Creation',views.Statistics_Voucher_Type_Creation,name='Statistics_Voucher_Type_Creation'),
    path('Statistics_Voucher_Type_Edit_Page/<int:pk>',views.Statistics_Voucher_Type_Edit_Page,name='Statistics_Voucher_Type_Edit_Page'),
    path('Statistics_Edit_Voucher_Types/<int:pk>',views.Statistics_Edit_Voucher_Types,name='Statistics_Edit_Voucher_Types'),
    path('Statistics_Delete_Voucher_Type/<int:pk>',views.Statistics_Delete_Voucher_Type,name='Statistics_Delete_Voucher_Type'),

]