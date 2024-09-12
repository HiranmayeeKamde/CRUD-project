from django.shortcuts import render,redirect
from .forms import StudentRegistration
from .models import UserProfile
# Create your views here.
def add_show(request):
    # how to collected data
    if request.method == 'POST': # POST method
        fm = StudentRegistration(request.POST)
        # Check request POSt data is valid or not?
        if fm.is_valid(): # is _valid is in build function to validate the object   
            fm.save()    # Jo form k sath model attachted hai usme ye data ajayega
            # Input filed get empty after adding the data or ADD button is pressed
            fm = StudentRegistration()
            
    else : # When form is empty and no data is added or POST in the form
        fm = StudentRegistration() # Instatnce ----> GET method
    stud = UserProfile.objects.all()
    return render(request, 'enroll/addandshow.html',{'form': fm, 'stu':stud})


def delete_data(request,id):
    if request.method == 'POST':
        pi = UserProfile.objects.get(pk=id)
        pi.delete()
    return redirect('/enroll')



def update_data(request,id):
    # this will run when we update some thing otherwise else part will run 1st
    if request.method == 'POST':
        pi = UserProfile.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    # If did not change any thing 1st time it come to else part
    else:
        pi=UserProfile.objects.get(pk=id)
        fm=StudentRegistration(instance=pi)
    return render(request,'enroll/update.html',{'form':fm})
    