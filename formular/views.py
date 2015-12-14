from django.shortcuts import render_to_response
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponse, HttpResponseServerError
from django.conf import settings
import hbp_app_python_auth.settings as auth_settings
import json
import requests
from .forms import ProposalForm1, ProposalForm2, ProposalForm3, ProposalForm4, ProposalForm5, ProposalForm6, ProposalForm7, ProposalForm8

# List of templates for each step.
# Steps are simply represented by their number, starting from 0
TEMPLATES = {'0': "formular/pf1.html",
             '1': "formular/pf2.html",
             '2': "formular/pf3.html",
             '3': "formular/pf4.html",
             '4': "formular/pf5.html",
             '5': "formular/pf6.html",
             '6': "formular/pf7.html",
             '7': "formular/pf8.html"}

# Wizard Class managing the steps in the form
class ProposalWizard(SessionWizardView):
	
	# Method that select the templates to use for each step.
	# Uses the TEMPLATES array.
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]
	
	# Method used to verify that the user is logged in in the Collaboratory portal.
	# @method_decorator is used in order to let it argument function on a method inside a class.
	# @method_decorator(login_required(login_url='/login/hbp'))
	def dispatch(self, *args,**kwargs):
		return super(ProposalWizard,self).dispatch(*args,**kwargs)

	# Method to provide each step with the inputs from other steps
	def get_form_initial(self, step):
		initial = {}
		for step in self.get_form_list(): 
			initial [str(step)]= self.storage.get_step_data(step)
		return self.initial_dict.get(step, initial)
	
	# Method called after the last step in order to treat the inputs of the form.
	def done(self, form_list, **kwargs):
		return render_to_response('done.html', {
			'form_data': [form.cleaned_data for form in form_list],
		})
		
# Method managing the connection to the Collaboratory portal.
def config(request):
	'''Render the config file'''
	res = requests.get(settings.HBP_ENV_URL)
	if res.status_code != 200:
		return HttpResponseServerError('Unable to query %s' % settings.HBP_ENV_URL)
	
	config = res.json()

	# Use this app client ID
	config['auth']['clientId'] = auth_settings.SOCIAL_AUTH_HBP_KEY
		
	# Add user token informations
	if request.user.is_authenticated():
		request.user.social_auth.get().extra_data
		config['auth']['token'] = {
			'access_token': request.user.social_auth.get().extra_data['access_token'],
			'token_type': request.user.social_auth.get().extra_data['token_type'],
			'expires_in': request.session.get_expiry_age()
		}

	return HttpResponse(json.dumps(config), content_type='application/json')
	
	
