from django.shortcuts import render

import os
import random
from django.shortcuts import render, redirect,reverse
from django.urls import reverse
from efuelapp.models import *
from datetime import datetime,date,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django. contrib import messages
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import auth, User
from django.db.models import Q

from efuel.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

from django.http import JsonResponse
import json
from .utils import cookieCart, cartData, guestOrder
# from efuel.settings import EMAIL_HOST_USER
# from django.core.mail import send_mail


# Create your views here.

def login(request):
    if request.method == 'POST':
        email  = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email,password=password)
        if user is not None:
            request.session['SAdm_id'] = user.id
            return redirect( 'SuperAdmin_home')

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="owner").exists():
        
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['Own_id'] = member.id 
                mem=user_registration.objects.filter(id= member.id)
                return render(request,'Owner_home.html',{'mem':mem})

        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],status="user").exists():
                
                member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
                request.session['usr_id'] = member.id 
                mem1=user_registration.objects.filter(id= member.id)
                
                return render(request,'User_home.html',{'mem1':mem1})
        else:
            return render(request, 'login.html')
    return render(request,'login.html')




def Registration(request):
    if request.method == 'POST':
        acc = user_registration()
        acc.fullname = request.POST['name']
        acc.pincode = request.POST['pincode']
        acc.district = request.POST['district']
        acc.state = request.POST['state']
        acc.country = request.POST['country']
        acc.mobile = request.POST['mobile']
        acc.email = request.POST['email']
        acc.password = request.POST['password']
        acc.save()
    return render(request,'login.html')

def SuperAdmin_logout(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        request.session.flush()
        return redirect("/")
    else:
        return redirect('/')


def Forgot_password(request):
    if request.method == "POST":
        email_id = request.POST.get('email')
        access_user_data = user_registration.objects.filter(email=email_id).exists()
        if access_user_data:
            _user = user_registration.objects.filter(email=email_id)
            password = random.SystemRandom().randint(100000, 999999)
            print(password)
            _user.update(password = password)
            subject =' your authentication data updated'
            message = 'Password Reset Successfully\n\nYour login details are below\n\nUsername : ' + str(email_id) + '\n\nPassword : ' + str(password) + \
                '\n\nYou can login this details\n\nNote: This is a system generated email, do not reply to this email id'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email_id, ]
            send_mail(subject, message, email_from,
                      recipient_list, fail_silently=True)
            # _user.save()
            msg_success = "Password Reset successfully check your mail new password"
            return render(request, 'Forgot_password.html', {'msg_success': msg_success})
        else:
            msg_error = "This email does not exist  "
            return render(request, 'Forgot_password.html', {'msg_error': msg_error})
    return render(request,'Forgot_password.html')

######################## Owner Section ######################

def Owner_index(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_index.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_home(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_home.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_addcategory(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            c_name=request.POST['c_name']
            addcategory=category(category_name=c_name
                                 )
            addcategory.save()
            return render(request, 'Owner_addcategory.html')
        return render(request,'Owner_addcategory.html')
    else:
        return redirect('/')

def Owner_addbunk(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            current_id = request.session['Own_id'] 
            b_name = request.POST['bunkname']
            vtype =request.POST.get('vehicletype')
            contrs =request.POST.get('connector')
            email = request.POST['email']
            ph = request.POST['phone']
            address = request.POST['address']
            city = request.POST['city']
            state = request.POST['state']
            pincode = request.POST['pincode']
            country = request.POST['country']
            img=request.FILES.get('file')
            addbunk=bunk(owner_ide=current_id,
                         bunk_name=b_name,
                         vehicle_type=vtype,
                         connector=contrs,
                         email=email,
                         phone=ph,
                         address=address,
                         city=city,
                         state=state,
                         country=country,
                         pincode=pincode,
                         image=img)
            addbunk.save()
            return render(request, 'Owner_addbunk.html',{'mem':mem})
        return render(request,'Owner_addbunk.html')
    else:
        return redirect('/')

def Owner_view_booking(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        bookings=bunk_booked.objects.filter(bunkowner_ide=Own_id)
        return render(request,'Owner_view_booking.html',{'mem':mem,'bookings':bookings})
    else:
        return redirect('/')

def Owner_change_time(request,i_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        booking=bunk_booked.objects.get(id=i_id)
        return render(request,'Owner_change_time.html',{'mem':mem,'booking':booking})
    else:
        return redirect('/')

def change_time(request,booking_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            bookings = bunk_booked.objects.get(id=booking_id)
            bookings.date = request.POST.get('date')
            bookings.time = request.POST.get('time')
            bookings.save()
            subject = 'Time schedule changed'
            message = 'dear customer,\nSorry for the inconvienience,your bunk booked time has changed.'
            recipient = bookings.email
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('Owner_view_booking')
        return render(request, 'Owner_change_time.html')
    else:
        return redirect('/')

def Owner_contact(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            u_name=request.POST['name']
            email=request.POST['email']
            sub=request.POST['subject']
            mess=request.POST['message']
            addcontact=admin_contact(name=u_name,
                                     email=email,
                                     subject=sub,
                                     message=mess)
            addcontact.save()
            return render(request, 'Owner_contact.html')
        return render(request,'Owner_contact.html',{'mem':mem})
    else:
        return redirect('/')

def Owner_contact_view(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        contacts=owner_contact.objects.all()
        return render(request,'Owner_contact_view.html',{'mem':mem,'contacts':contacts})
    else:
        return redirect('/')


def Owner_addproduct(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        categorys=category.objects.all()
        return render(request,'Owner_addproduct.html',{'mem':mem,'categorys':categorys})
    else:
        return redirect('/')
    
def Owner_addpro(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            p_name = request.POST['p_name']
            sel1 = request.POST['sel']
            category1=category.objects.get(id=sel1)
            desc=request.POST['description']
            price=request.POST['price']
            img=request.FILES.get('file')
            addproduct=Product(product_name=p_name,
                               product_image=img,
                               price=price,
                               description=desc,
                               category=category1
                               )
            addproduct.save()
            return redirect('Owner_addproduct')
        return render(request, 'Owner_view_product.html')
    else:
        return redirect('/')

def Owner_view_product(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        products=Product.objects.all()
        return render(request,'Owner_view_product.html',{'mem':mem,'products':products})
    else:
        return redirect('/')

def Owner_product_edit(request,p_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        products=Product.objects.get(id=p_id)
        return render(request,'Owner_product_edit.html',{'mem':mem,'products':products})
    else:
        return redirect('/')

def edit_product_details(request,products_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        if request.method=='POST':
            products = Product.objects.get(id=products_id)
            products.product_name = request.POST.get('p_name')
            products.description = request.POST.get('description')
            products.price = request.POST.get('price')
            products.product_image = request.FILES.get('file')
            products.save()
            return redirect('Owner_view_product')
        return render(request, 'Owner_product_edit.html')
    else:
        return redirect('/')

def Owner_add_payment(request,i_id):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        pay=bunk_booked.objects.get(id=i_id)
        return render(request,'Owner_add_payment.html',{'mem':mem,'pay':pay})
    else:
        return redirect('/')

def add_payment(request,pay_user_ide):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        us_ide=pay_user_ide
        if request.method=='POST':
            date=request.POST['date']
            bname=request.POST['bankname']
            accnum=request.POST['accnumber']
            ifse=request.POST['ifsecode']
            amo=request.POST['amount']
            addpayment=payment(user_ide=us_ide,
                                 date=date,
                                 payment=amo,
                                 bank=bname,
                                 accountnumber=accnum,
                                 ifse=ifse,
                                 )
            addpayment.save()
            return redirect('Owner_view_booking')
        return render(request,'Owner_view_booking.html',{'mem':mem})
    else:
        return redirect('/')

def delete_product(request,p_id):
    products=Product.objects.get(id=p_id)
    products.delete()
    return redirect('Owner_view_product')

def Owner_logout(request):
    if 'Own_id' in request.session:
        request.session.flush()
        return redirect('/')
    else:
        return redirect('/')

def Owner_profile(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        return render(request,'Owner_profile.html',{'mem':mem})
    else:
        return redirect('/')


def Owner_edit_profile(request):
    if 'Own_id' in request.session:
        if request.session.has_key('Own_id'):
            Own_id = request.session['Own_id']
        else:
            return redirect('/')
        mem = user_registration.objects.filter(id=Own_id)
        pro = user_registration.objects.get(id=Own_id)
        if request.method=='POST':
            usrs = user_registration.objects.get(id=Own_id)
            usrs.fullname = request.POST.get('u_name')
            usrs.pincode = request.POST.get('pincode')
            usrs.district = request.POST.get('district')
            usrs.state = request.POST.get('state')
            usrs.country = request.POST.get('country')
            usrs.mobile = request.POST.get('mobile')
            usrs.email = request.POST.get('email')
            usrs.password = request.POST.get('password')
            usrs.save()
            return redirect('Owner_profile')
        return render(request,'Owner_edit_profile.html',{'mem':mem,'pro':pro})
    else:
        return redirect('/')

##################### Owner Section end #########################

##################### User Section Start ########################

def User_index(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_index.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_home(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_home.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_about(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_about.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_allbunk(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        bunks=bunk.objects.all()
        return render(request,'User_allbunk.html',{'mem1':mem1,'bunks':bunks})
    else:
        return redirect('/')

def book_bunk(request,book_owner_ide):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        bown_ide=book_owner_ide
        if request.method=='POST':
            nam=request.POST['u_name']
            em=request.POST['email']
            ph=request.POST['phone']
            u_vtype=request.POST['sel1']
            u_vconnector=request.POST['sel2']
            da=request.POST['date']
            ti=request.POST['time']
            addbunkbook=bunk_booked(user_ide=usr_id,
                                 bunkowner_ide=bown_ide,
                                 name=nam,
                                 email=em,
                                 phone=ph,
                                 uservehicle_type=u_vtype,
                                 userconnector=u_vconnector,
                                 date=da,
                                 time=ti
                                 )
            addbunkbook.save()
            return render(request, 'User_allbunk.html')
        return render(request, 'User_allbunk.html')
    else:
        return redirect('/')

def User_contact(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        if request.method=='POST':
            u_name=request.POST['name']
            email=request.POST['email']
            sub=request.POST['subject']
            mess=request.POST['message']
            addcontact=owner_contact(name=u_name,
                                     email=email,
                                     subject=sub,
                                     message=mess)
            addcontact.save()
            return render(request, 'User_contact.html')
        return render(request,'User_contact.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_shop(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        products=Product.objects.all()
        return render(request,'User_shop.html',{'mem1':mem1,'products':products})
    else:
        return redirect('/')

def User_addcart(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_addcart.html',{'mem1':mem1})
    else:
        return redirect('/')


def User_booking(request,i_id):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        book=bunk.objects.get(id=i_id)
        return render(request,'User_booking.html',{'mem1':mem1,'book':book,'v_list':book.vehicle_type.split(","),'c_list':book.connector.split(",")})
    else:
        return redirect('/')

def User_mybooking(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        mybooking=bunk_booked.objects.filter(user_ide=usr_id)
        return render(request,'User_mybooking.html',{'mem1':mem1,'mybooking':mybooking})
    else:
        return redirect('/')

def User_payment_history(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        payments=payment.objects.filter(user_ide=usr_id)
        return render(request,'User_payment_history.html',{'mem1':mem1,'payments':payments})
    else:
        return redirect('/')

def User_myorders(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        orders=ShippingAddress.objects.filter(user_ide=usr_id)
        return render(request,'User_myorders.html',{'mem1':mem1,'orders':orders})
    else:
        return redirect('/')

def add_userorder(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        if request.method=='POST':
            nam=request.POST['u_name']
            em=request.POST['email']
            itm=request.POST['items']
            pric=request.POST['price']
            addres=request.POST['address']
            ci=request.POST['city']
            stat=request.POST['state']
            code=request.POST['pincode']
            addshipping=ShippingAddress(user_ide=usr_id,
                                 name=nam,
                                 email=em,
                                 items=itm,
                                 price=pric,
                                 address=addres,
                                 city=ci,
                                 state=stat,
                                 zipcode=code
                                 )
            addshipping.save()
            return render(request, 'User_allbunk.html')
        return render(request, 'User_allbunk.html')
    else:
        return redirect('/')




def User_logout(request):
    if 'usr_id' in request.session:
        request.session.flush()
        return redirect('logouttwo')
    else:
        return redirect('/')

def logouttwo(request):
    response = redirect('login')
    response.delete_cookie('cart')
    return response

def cancel_booking(request,i_id):
    booking=bunk_booked.objects.get(id=i_id)
    booking.delete()
    return redirect('User_mybooking')

def cancel_order(request,i_id):
    booking=ShippingAddress.objects.get(id=i_id)
    booking.delete()
    return redirect('User_myorders')


def User_profile(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        return render(request,'User_profile.html',{'mem1':mem1})
    else:
        return redirect('/')

def User_edit_profile(request):
    if 'usr_id' in request.session:
        if request.session.has_key('usr_id'):
            usr_id = request.session['usr_id']
        else:
            return redirect('/')
        mem1 = user_registration.objects.filter(id=usr_id)
        pro = user_registration.objects.get(id=usr_id)
        if request.method=='POST':
            usrs = user_registration.objects.get(id=usr_id)
            usrs.fullname = request.POST.get('u_name')
            usrs.pincode = request.POST.get('pincode')
            usrs.district = request.POST.get('district')
            usrs.state = request.POST.get('state')
            usrs.country = request.POST.get('country')
            usrs.mobile = request.POST.get('mobile')
            usrs.email = request.POST.get('email')
            usrs.password = request.POST.get('password')
            usrs.save()
            return redirect('User_profile')
        return render(request,'User_edit_profile.html',{'mem1':mem1,'pro':pro})
    else:
        return redirect('/')
###################### User section end ########################

###################### Super Admin section start ###############

def SuperAdmin_index(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_index.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_home(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        return render(request,'SuperAdmin_home.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_bunkrequest(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        bunkreq=bunk.objects.all()
        return render(request,'SuperAdmin_bunkrequest.html',{'users':users,'bunkreq':bunkreq})
    else:
        return redirect('/')

def decline_bunk(request,i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        booking=bunk.objects.get(id=i_id)
        booking.delete()
        return redirect('SuperAdmin_bunkrequest')
        return render(request,'SuperAdmin_index.html',{'users':users})
    else:
        return redirect('/')

def SuperAdmin_bunkbookings(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        booking=bunk_booked.objects.all()
        return render(request,'SuperAdmin_bunkbookings.html',{'users':users,'booking':booking})
    else:
        return redirect('/')

def SuperAdmin_ownerview(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        usrs = user_registration.objects.all()
        return render(request,'SuperAdmin_ownerview.html',{'users':users,'usrs':usrs})
    else:
        return redirect('/')

def SuperAdmin_change_desig(request,i_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        usrs=user_registration.objects.get(id=i_id)
        return render(request,'SuperAdmin_change_desig.html',{'users':users,'usrs':usrs})
    else:
        return redirect('/')

def change_designation(request,usrs_id):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        if request.method=='POST':
            userdesig = user_registration.objects.get(id=usrs_id)
            userdesig.fullname = request.POST.get('name')
            userdesig.email = request.POST.get('email')
            userdesig.status = request.POST.get('sel')
            userdesig.save()
            subject = 'Time schedule changed'
            message = 'dear customer,\nyou are approved as an owner.'
            recipient = userdesig.email
            send_mail(subject,message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('SuperAdmin_ownerview')
        return render(request, 'SuperAdmin_ownerview.html')
    else:
        return redirect('/')

def SuperAdmin_view_contacts(request):
    if 'SAdm_id' in request.session:
        if request.session.has_key('SAdm_id'):
            SAdm_id = request.session['SAdm_id']
        else:
            return redirect('/')
        users = User.objects.filter(id=SAdm_id)
        contacts=admin_contact.objects.all()
        return render(request,'SuperAdmin_contact_view.html',{'users':users,'contacts':contacts})
    else:
        return redirect('/')

def delete_user(request,i_id):
    userss=user_registration.objects.get(id=i_id)
    userss.delete()
    return redirect('SuperAdmin_ownerview')



###################### Super Admin section end ###############

###################### Cart views start #######################


def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	products = Product.objects.all()
	context = {'products':products, 'cartItems':cartItems}
	return render(request, 'store.html', context)


def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

########################### cart views end ######################3