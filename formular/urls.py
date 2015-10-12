from django.conf.urls import patterns


from formular.views import ProposalWizard
from formular.forms import ProposalForm1, ProposalForm2

urlpatterns = [
    url(r'^$', ProposalWizard.as_view([ProposalForm1, ProposalForm2])),
]