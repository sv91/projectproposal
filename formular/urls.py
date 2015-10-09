from django.conf.urls import patterns

from formular.forms import ProposalForm1, ProposalForm2
from formular.views import ProposalWizard

urlpatterns = patterns('',
    (r'^$', ProposalWizard.as_view([ProposalForm1, ProposalForm2])),
)