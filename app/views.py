from django.shortcuts import render , redirect
from .models import bank

# Create your views here.


def home(request):
    return render(request, 'home.html')

def new_acc(request):
    if request.method == "POST":
        name=request.POST.get("nname")
        gender=request.POST.get("ngender")
        phone=request.POST.get("nphone")
        aadhar=request.POST.get("naadhar")
        email=request.POST.get("nemail")
        address=request.POST.get("naddress")

        data=bank(name=name,gender=gender,phone=phone,aadhar=aadhar,email=email,address=address)
        data.save()
        
    return render(request, 'new_acc.html')

def acc_transfer(request):
    msg = ''
    if request.method == "POST":
        acc = request.POST.get("faccnum")
        acc2 = request.POST.get("taccnum")
        amount = request.POST.get("tamount")
        pin = request.POST.get("tpin")

        try:
            sender = bank.objects.get(acc=acc)
            receiver = bank.objects.get(acc=acc2)

            if sender.pin != int(pin):
                msg = "Incorrect PIN for sender account."
            elif sender.bal < int(amount):
                msg = "Insufficient balance in sender account."
            else:
                sender.bal -= int(amount)
                receiver.bal += int(amount)
                sender.save()
                receiver.save()
                msg = f"₹{amount} transferred successfully from {acc} to {acc2}."
        except bank.DoesNotExist:
            msg = "One or both account numbers are incorrect."

    return render(request, 'acc_transfer.html', {'msg': msg})



def balance(request):
    msg = ''
    if request.method == "POST":
        acc = request.POST.get("baccount")
        pin = request.POST.get("bpin")

        try:
            data = bank.objects.get(acc=acc)
            if data.pin != int(pin):
                msg = "Incorrect PIN."
            else:
                msg = f"Your current balance is ₹{data.bal}"
        except bank.DoesNotExist:
            msg = "Account not found."

    return render(request, 'balance.html', {'msg': msg})


def deposit(request):
    msg = ''
    if request.method == "POST":
        acc = request.POST.get("daccnum")
        pin = request.POST.get("dpin")
        amount = request.POST.get("damount")

        try:
            data = bank.objects.get(acc=acc)
            if data.pin != int(pin):
                msg = "Incorrect PIN."
            else:
                data.bal += int(amount)
                data.save()
                msg = f"₹{amount} deposited successfully. New balance: ₹{data.bal}"
        except bank.DoesNotExist:
            msg = "Account not found."

    return render(request, 'deposit.html', {'msg': msg})



def pin_gen(request):
    context = {}
    if request.method == "POST":
        acc = request.POST.get("paccount")
        pin = request.POST.get("ppin")
        pin2 = request.POST.get("cpin")

        if pin != pin2:
            context['error'] = "PIN and Confirm PIN do not match."
        else:
            try:
                data = bank.objects.get(acc=acc)
                data.pin = int(pin)
                data.save()
                context['success'] = "PIN successfully updated."
            except bank.DoesNotExist:
                context['error'] = "Account does not exist."

    return render(request, 'pin_gen.html', context)


def withdraw(request):
    msg = ''
    if request.method == "POST":
        acc = request.POST.get("waccount")
        pin = request.POST.get("wpin")
        amount = request.POST.get("wamount")

        try:
            data = bank.objects.get(acc=acc)
            if data.pin != int(pin):
                msg = "Incorrect PIN."
            elif data.bal < int(amount):
                msg = "Insufficient balance."
            else:
                data.bal -= int(amount)
                data.save()
                msg = f"₹{amount} withdrawn successfully. New balance: ₹{data.bal}"
        except bank.DoesNotExist:
            msg = "Account not found."

    return render(request, 'withdraw.html', {'msg': msg})


