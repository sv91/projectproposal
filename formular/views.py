from django.shortcuts import render_to_response
from django.contrib.formtools.wizard.views import SessionWizardView

class ContactWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render_to_response('wizard_form.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
