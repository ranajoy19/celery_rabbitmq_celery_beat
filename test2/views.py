from django.shortcuts import HttpResponse
from .form import ReviewForm
from django.views.generic import FormView

# Create your views here.

class ReviewEmailView(FormView):
    template_name = 'review.html'
    form_class = ReviewForm

    def form_valid(self, form):
        form.send_email()
        msg ='Thanks for the review!'
        return HttpResponse(msg)