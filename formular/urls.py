from django.conf.urls import patterns
from django.conf.urls import url

from .forms import ProposalForm1, ProposalForm2, ProposalForm3, ProposalForm4, ProposalForm5, ProposalForm6
from .views import ProposalWizard

urlpatterns = [
	url(r'^$', ProposalWizard.as_view([ProposalForm1, ProposalForm2, ProposalForm3, ProposalForm4, ProposalForm5, ProposalForm6])),
]