# views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse


def apply(request):
    if request.method == 'POST':
        # Retrieve data from the form
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        passport_number = request.POST.get('passport_number')
        nationality = request.POST.get('nationality')
        date_of_birth = request.POST.get('date_of_birth')
        purpose_of_visit = request.POST.get('purpose_of_visit')

        # Here, you can handle the data, e.g., save it to the database or send an email.

        # Redirect to a success page after handling the data
        return redirect('success')

    return render(request, 'apply.html')

def submit_passport(request):
    if request.method == 'POST':
        # Handle the form submission logic here
        # For example, save the data, validate input, etc.
        return HttpResponse("Passport application submitted successfully!")
    else:
        return HttpResponse("Invalid request.")
def submit_second_passport(request):
    if request.method == 'POST':
        # Handle form submission logic here
        return HttpResponse('Second passport application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')  # Or appropriate template
def submit_visa(request):
    if request.method == 'POST':
        # Handle the visa form submission
        # For example, save the form data or process the visa application
        return HttpResponse('Visa application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')  # Or the relevant template
def submit_extended_visa(request):
    if request.method == 'POST':
        # Process the extended visa form data here
        return HttpResponse('Extended visa application submitted successfully.')
    else:
        return render(request, 'userhomepage.html')  # Or render the appropriate template