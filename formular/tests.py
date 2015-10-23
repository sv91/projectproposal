from django.test import TestCase

from .views import ProposalWizard

class ProposalWizardTests(TestCase):
	
	def test_get_form_initial(self):
		
