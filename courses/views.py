from django.shortcuts import render

# Create your views here.
# views.py

from .models import Course
from .forms import InterestForm

# View for the form where users select their interests
def select_interests(request):
    if request.method == 'POST':
        form = InterestForm(request.POST)  # Bind form data from POST request
        if form.is_valid():
            # Get the selected interests from the form
            selected_interests = form.cleaned_data['interests']
            # Redirect to the recommend courses page, passing the selected interests
            return recommend_courses(request, selected_interests)
    else:
        form = InterestForm()  # Create an empty form on GET request
    return render(request, 'courses/select_interests.html', {'form': form})

# View to recommend courses based on user interests
def recommend_courses(request, selected_interests):
    # Fetch courses related to the selected interests (simplified logic)
    recommended_courses = Course.objects.filter(interest__in = selected_interests)
    return render(request, 'courses/recommend_courses.html', {'courses': recommended_courses})

