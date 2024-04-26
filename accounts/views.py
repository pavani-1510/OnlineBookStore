from django.shortcuts import render
from django.views.generic.base import RedirectView
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views.generic import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            email = form.cleaned_data.get('email')  # Get the email from the form
            Emailing(request, email)  # Call the Emailing view with the email
            return redirect('list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})


class BooksDetailView(DetailView):
    model = User
    template_name = 'dashboard.html'



class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the current user object to the template
        return context

class CustomLogoutView(LogoutView):
    @method_decorator(csrf_exempt)  # Exempt CSRF protection for POST requests
    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Handle logout for POST requests
            return self.post(request, *args, **kwargs)
        else:
            # Allow GET requests to be handled by parent class
            return super().dispatch(request, *args, **kwargs)


class AdminView(RedirectView):
    url = reverse_lazy('admin:index')



from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TwoStepVerificationForm
from django.core.mail import send_mail
from django.contrib import messages

def Emailing(request,email):
	subject = 'Account Creation Done Successfully'
	message = "Your email has been registered into our account. If this is not you please contact us."
	recipient = email
	send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
	return redirect('Payment')


from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import CCareForm
from .models import CustomerCareMessage


def CCare(request):
    if request.method == 'POST':
        form = CCareForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['message']
            username = request.user.username if request.user.is_authenticated else 'Anonymous User'

            # Save the message and username to the database
            CustomerCareMessage.objects.create(message=message, username=username)

            send_mail(
                subject='Customer Issue',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['pravalikar212@gmail.com'],
                fail_silently=False
            )
            # Optionally, you can add a success message here
            return redirect('/')  # Redirect to some page after sending the email
    else:
        form = CCareForm()
    return render(request, 'ccare_form.html', {'form': form})
