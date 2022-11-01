from django import forms
from . models import Feedback
from . models import Farmers#
from . models import Feedback_reply
#from . models import Department



class feedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback

        fields ="__all__"
        

class FarmersForm(forms.ModelForm):

    class Meta:
        model= Farmers

        fields ="__all__"

class Feedback_replyForm(forms.ModelForm):
    class Meta:
        model = Feedback_reply

        fields="__all__"
        

#class DepartmentForm(forms.ModelForm):

  #class Meta:
        #model= Department

        #fields="__all__"