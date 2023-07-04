from django import forms
from .models import ContactMessage
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget, RegionalPhoneNumberWidget, PhonePrefixSelect







class BlogSearchForm(forms.Form):
    search_query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder':"Search ..."}))
    


class ContactUsForm(forms.ModelForm):
    
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'phone_number', 'email', 'subject', 'message']        
        
        widgets = {                      
            'name': forms.TextInput(attrs={'placeholder': 'Name', 'aria-label':'Name',  }),  
            'phone_number' : PhoneNumberPrefixWidget(initial='GB', attrs={'placeholder': 'Enter phone number', 'aria-label':'phone_number'}, country_attrs={'class':'bg-transparent'}) ,
            'email': forms.EmailInput(attrs={'placeholder': 'email',  'aria-label':'email' , }),                
            'subject': forms.TextInput(attrs={'placeholder': 'Subject',  'aria-label':'subject',  }),            
            'message': forms.Textarea(attrs={'rows':'5','placeholder': 'Message', 'aria-label':'message', }), 
        }
        
        PhoneNumberPrefixWidget(attrs={'placeholder': 'Enter phone number'})