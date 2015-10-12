from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView

class ProposalWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
