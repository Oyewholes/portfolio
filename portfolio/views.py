from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from .forms import ContactForm
from .models import ContactMessage
from django.urls import reverse_lazy
# Create your views here.

class Homepage(TemplateView):
  template_name = 'portfolio/index.html'
  
class ContactView(FormView):
  form_class = ContactForm
  success_url= reverse_lazy('home')
  
  def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        ContactMessage.objects.create(name=name, email=email, message=message)
        return super().form_valid(form)