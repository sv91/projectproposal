'''
File used to define specific widgets for the 'formular' app.
'''
from django.forms.widgets import DateInput

# Class used to set the type of an input to 'date'.
class DateTimeInput(DateInput):
    input_type = 'date'
