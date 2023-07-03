from django import forms
from .models import Event

class EventCreationForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'time', 'location', 'description']


"""
Creating a forms.py file in Django serves multiple purposes and provides several benefits:

Separation of Concerns: Keeping form-related code separate from views and models helps maintain a clean and organized code structure. The forms.py file acts as a central place to define all the forms associated with your Django app.

Form Validation and Data Cleaning: Django forms provide built-in validation capabilities, allowing you to define rules and constraints for user input. By defining a form class, you can specify fields, their types, and validation rules. Django automatically handles form validation, ensuring that the submitted data meets the specified requirements. This helps prevent incorrect or malicious data from being saved to the database.

Reusable Forms: By defining forms in a separate file, you can easily reuse them across multiple views or even different apps within your project. This promotes code reusability and reduces duplication.

Convenience and Flexibility: Django forms provide various types of fields (e.g., CharField, DateField, BooleanField, etc.) and widgets (e.g., TextInput, CheckboxInput, Select, etc.), making it easier to handle different types of user input. The forms also offer built-in HTML rendering and error handling, saving you time and effort in creating and managing form elements manually in your templates.

Overall, using a forms.py file helps maintain a modular and structured codebase, ensures proper data validation, and simplifies form handling in your Django project.
"""