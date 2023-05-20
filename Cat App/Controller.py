from django.shortcuts import render
from django.http import HttpResponseRedirect


def my_view(request):
    if request.method == 'GET':
        return render(request, 'my_template.html')

    if request.method == 'POST':
        # Do something with the form data

        # Get the value of the selected option from the first drop down
        selected_option = request.POST['first_dropdown']

        # Get the options for the second drop down
        options = [
            ('option1', 'Option 1'),
            ('option2', 'Option 2'),
            ('option3', 'Option 3'),
        ]

        # Filter the options for the second drop down based on the selected option from the first drop down
        filtered_options = [
            option for option in options if option[0].startswith(selected_option)
        ]

        # Move the existing form to the left
        request.session['form_left'] = request.session.get('form_left', '') + request.POST.get('form_id', '')

        # Slide in the new form from the right
        request.session['form_right'] = request.session.get('form_right', '') + request.POST.get('form_id', '')

        return render(request, 'my_template.html', {
            'first_dropdown': selected_option,
            'second_dropdown': filtered_options,
        })


def my_template(request):
    form_left = request.session.get('form_left', '')
    form_right = request.session.get('form_right', '')

    if form_left:
        form_left = forms.Form(request.POST or None, data=request.session['form_left'])
    else:
        form_left = None

    if form_right:
        form_right = forms.Form(request.POST or None, data=request.session['form_right'])
    else:
        form_right = None

    return render(request, 'my_template.html', {
        'form_left': form_left,
        'form_right': form_right,
    })
