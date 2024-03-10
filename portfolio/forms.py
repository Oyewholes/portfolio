from django import forms
from .models import ContactMessage
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class ContactForm(forms.ModelForm):
    class Meta:
      model = ContactMessage
      fields =('name', 'email','message')
      
    def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      self.helper= FormHelper()
      self.helper.form_method= 'post'
      self.helper.add_input(Submit('submit','Submit', css_class='bg-green-500 hover:bg-green-700 text-black font-bold py-2 px-4 rounded'))