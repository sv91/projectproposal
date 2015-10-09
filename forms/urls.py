from django.conf.urls import patterns

from forms.forms import ProposalForm1, ProposalForm2
from forms.views import ProposalWizard

urlpatterns = patterns('',
    (r'^$', ContactWizard.as_view([ContactForm1, ContactForm2])),
)