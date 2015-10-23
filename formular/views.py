from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView

class ProposalWizard(SessionWizardView):
	
	def get_form_initial(self, step):
		initial = {}
		for step in self.get_form_list(): 
			initial [str(step)]= self.storage.get_step_data(step)
		return self.initial_dict.get(step, initial)
		
	
	def done(self, form_list, **kwargs):
		return render_to_response('done.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})
