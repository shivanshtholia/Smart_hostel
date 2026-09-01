from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from hostel.models import Hostel_user,Admin
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import redirect, get_object_or_404
from django.core.mail import send_mail
from django.conf import settings



def home(request):
    return render(request,'hostel/dashboard.html')
def Roomsinfo(request):
    return render(request,'hostel/roomsinfo.html')

@csrf_exempt
def signup(request):
    if request.method=='POST':
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirm_password=request.POST.get("confirm_password")
        name=request.POST.get("name")
        print(email, password, confirm_password)
        
        if password!=confirm_password:
            messages.error(request,"password doesnot match")
            return render(request,'hostel/signup.htmnl')
        
        if Hostel_user.objects.filter(email=email).exists():
            messages.error(request,"User with this email already exists")
            return render(request,'hostel/signup.htmnl')
        hashed_password=make_password(password)
        Hostel_user.objects.create(email=email,password=hashed_password,name=name)
        send_custom_email(
            subject='Welcome to SmartHostel!',
            message=f"Hello {name},\n\nYour account has been successfully created.\n\nThanks for joining SmartHostel!",
            recipient_email=email,
            html_message=f"""
                <h2>Welcome {name}!</h2>
                <p>Your account has been successfully created.</p>
                <p>Thanks for joining <b>SmartHostel</b>!</p>
            """
        )
        messages.success(request, "Account created successfully! A confirmation email has been sent.")
        return  render(request,'hostel/signup.html')
    else:
        return render(request,'hostel/signup.html')
    
@csrf_exempt
def login(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        print(email,password)

        if not Hostel_user.objects.filter(email=email).exists():
            messages.success(request,"Invalid email id")
            return render(request,'hostel/signup.htmnl')
        res=Hostel_user.objects.get(email=email)
        password1=res.password
        if check_password(password, password1):
            return render(request,'hostel/dashboard.html',{"data":email})
        else:
            return messages.error(request,"invalid password...")
        
def logout(request):
    request.session.flush()
    return redirect('/')

@csrf_exempt
def booking(request):
    return render(request,"hostel/booking.html")
@csrf_exempt
def profile(request):
    return render(request,"hostel/profile.html")


@csrf_exempt
def admin_register(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        confirm_password=request.POST.get("confirm_password")
        

        if Admin.objects.filter(email=email).exists():
            messages.error(request,"email id already exists..")
            return render(request,'hostel/admin.html')
        
        if password != confirm_password:
            messages.error(request,"password doesnot match")
            return render(request,'hostel/admin.html')
        h_password=make_password(password)
       

        Admin.objects.create(first_name=first_name,last_name=last_name,email=email,password=h_password)
        messages.success(request,"account created successfully...")
        return  render(request,'hostel/admin.html')
   
@csrf_exempt
def admin(request):
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        if not Admin.objects.filter(email=email).exists():
            messages.error(request,"Invalid email id")
            return render(request,'hostel/admin.html')
        res=Admin.objects.get(email=email)
        password1=res.password
        name=res.first_name
        if check_password(password, password1):
            request.session['admin_id'] = res.id
            request.session['admin_name'] = res.first_name

            return redirect('admin_panel')  # recommended to use redirect not render
        else:
            messages.error(request, "Invalid password")
            return render(request, 'hostel/admin.html')

    else:
        return render(request, 'hostel/admin.html')
@csrf_exempt
def admin_panel_students(request):
     students=Hostel_user.objects.all()
     return render(request,'hostel/admin_panel_student.html',{'students':students})
@csrf_exempt
def admin_panel_staff(request):
    staff = Admin.objects.all()
    return render(request,'hostel/admin_panel_staff.html',{
        'staff': staff })
@csrf_exempt
def delete_student(request, id):
    student = get_object_or_404(Hostel_user, id=id)
    student.delete()
    return redirect('admin_panel_students')
@csrf_exempt
def admin_panel(request):
     if 'admin_id' not in request.session:
        return redirect('admin')
     return render(request,'hostel/admin_panel.html',{"name":request.session['admin_name']}) 
@csrf_exempt
def room_booking(request):
    return render(request,"hostel/booking.html")
def send_custom_email(subject, message, recipient_email, html_message=None):
    """
    Sends an email to a given recipient.
    
    Args:
        subject (str): Subject of the email.
        message (str): Plain text message.
        recipient_email (str): Receiver's email address.
        html_message (str, optional): HTML content for better formatting.
    """
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[recipient_email],
        fail_silently=False,
        html_message=html_message  # Optional HTML content
    )


@csrf_exempt
def notices(request):
    return render(request,"hostel/notices.html")

# changing the protype of the project to a hostel management system with admin and student login, room booking, and notice board functionalities. 

def about(request):
    return render(request,"hostel/about.html")

def contact(request):
    return render(request,"hostel/contact.html")
