from django.conf.urls import patterns
from django.conf.urls import url

from .forms import ProposalForm1, ProposalForm2
from .views import ProposalWizard

urlpatterns = [
	url(r'^$', ProposalWizard.as_view([ProposalForm1, ProposalForm2])),
]