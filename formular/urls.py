"""
URL file for the app "Formular"
"""
from django.conf.urls import patterns
from django.conf.urls import url
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required

from .forms import ProposalForm1, ProposalForm2, ProposalForm3, ProposalForm4, ProposalForm5, ProposalForm6, ProposalForm7, ProposalForm8
from .views import ProposalWizard

# Defines the different possible paths.
urlpatterns = [
	url(r'^$', login_required(
					ProposalWizard.as_view([ProposalForm1, ProposalForm2, ProposalForm3, ProposalForm4, ProposalForm5, ProposalForm6, ProposalForm7, ProposalForm8], instance_dict=""),
					login_url='/login/hbp'
			   )),
    url(r'^config.json$', 'formular.views.config', name='config'),
]