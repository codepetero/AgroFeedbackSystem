from django.shortcuts import render
from . forms import feedbackForm
from . forms import FarmersForm
from . models import Farmers
from . models import Feedback
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Sacco
from . models import Feedback_reply
from . forms import Feedback_replyForm
@login_required
def index(request):
    feedbacks = Feedback.objects.filter(owner=request.user.id)
    context={'feedbacks':feedbacks}
    return render(request,'agroFeedback/index.html', context)

@login_required
def create_feedback(request):
    form = feedbackForm(request.POST or None)
    context = {'form': form}
    

    if request.method=="POST":

        
        feedback_message= request.POST.get('feedback_message')
        feedback_reply= request.POST.get('feedback_reply')
        sacco_name=request.POST.get('sacco_name')
        



        feedback=Feedback()

        
        feedback.feedback_message= feedback_message
        feedback.feedback_reply = feedback_reply
        feedback.sacco_name=sacco_name
        
        feedback.owner = request.user
       
        

        feedback.save()

        messages.add_message(request, messages.SUCCESS, "feedback created successfully ")

        return HttpResponseRedirect(reverse('history', kwargs={'id':feedback.pk}))

    return render(request, 'agroFeedback/create_feedback.html',context)


@login_required
def feedback_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
    context={'history':history}
    return render(request, 'agroFeedback/feedback_history.html', context)

@login_required
def delete_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
    context={'history':history}

    if request.method=='POST':
        if history.owner== request.user:
             history.delete()
             return HttpResponseRedirect(reverse('home'))
        return render(request, 'agroFeedback/delete_history.html', context)

    return render(request, 'agroFeedback/delete_history.html', context)

@login_required
def edit_history(request,id):
    history = get_object_or_404(Feedback, pk=id)
   
    form=feedbackForm(instance=history)
    context={'history':history, 'form':form}

    if request.method=="POST":
        form = feedbackForm(request.POST)
        
        feedback_message= request.POST.get('feedback_message')
        feedback_reply= request.POST.get('feedback_reply')
        sacco_name=request.POST.get('sacco_name')
        
        


        feedback=Feedback()


        feedback.feedback_message=feedback_message
        feedback.feedback_reply = feedback_reply
        feedback.sacco_name=sacco_name
        

        
        feedback.save()
        
        messages.add_message(request, messages.SUCCESS, "agroFeedback updated successfully "
        )

        return HttpResponseRedirect(reverse('history', kwargs={'id':feedback.pk}))


    return render(request, 'agroFeedback/edit_history.html',context)


    

    




def student_profile(request):
    return render(request, 'agroFeedback/student_profile.html')


def handle_error(request,exception):
    return render(request, 'error_page.html')


def handle_server_error(request):
    return render(request, 'server_error_page.html')
@login_required
def updateProfile(request):
    feedback=Feedback()
    form =FarmersForm(request.POST)
    context = {'form': form}

    if request.method=="POST":

        farmer_id = request.POST.get('farmer_id')
        gender= request.POST.get('gender')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        reg_No=request.POST.get('reg_No')
        profile_pic= request.POST.get('profile_pic')
        location=request.POST.get('location')
        address=request.POST.get('address')


        profile=Farmers()

        profile.farmer_id= farmer_id
        profile.gender= gender
        profile.first_name=first_name
        profile.last_name=last_name
        profile.reg_No=reg_No
        profile.profile_pic = profile_pic
        profile.location=location
        profile.address=address
        
        profile.save()

        messages.add_message(request, messages.SUCCESS, "profile updated successfully "
        )
        return HttpResponseRedirect(reverse('create_feedback', args=None))

    return render(request, 'agroFeedback/update_profile.html',context)

def search(request):
    if request.method=="POST":
        searcher=request.POST['searcher']
        feedback=Feedback.objects.filter(id__icontains=searcher)
    else:
        feedback=Feedback.objects.all()
    context={'feedback':feedback}
    return render(request,'agroFeedback/search.html', context)

#def create_feedback(request, id):
    
   # form = feedbackForm()
    #feedback=Feedback()

   # if request.method == 'POST':
       # form = feedbackForm(request.POST)
       
        #if form.is_valid():
           # form.save()
       # messages.add_message(request, messages.SUCCESS, "feedback updated successfully ")

       # return HttpResponseRedirect(reverse('history', kwargs={'id':feedback.pk}))

    #context = {'form': form}   
    
    #return render(request, 'agroFeedback/create_feedback.html',context)  
def feedback_reply(request):
    form = Feedback_replyForm()
    feedback=Feedback_reply()
    context = {'form': form}
    if request.method == 'POST':
        form = Feedback_replyForm(request.POST)
       
        if form.is_valid():
            form.save()

        
    return render(request, 'agroFeedback/feedback_reply.html',context)  
def contact_us(request):
    return render(request, 'agroFeedback/contact_us.html')


