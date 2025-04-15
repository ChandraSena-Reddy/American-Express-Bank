from django .urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('acc_transfer/',views.acc_transfer,name='acc_transfer'),
    path('balance/',views.balance,name='balance'),
    path('deposit/',views.deposit,name='deposit'),
    path('new_acc/',views.new_acc,name='new_acc'),
    path('pin_gen/',views.pin_gen,name='pin_gen'),
    path('withdraw/',views.withdraw,name='withdraw'),  

]