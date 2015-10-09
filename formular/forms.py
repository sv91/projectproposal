from django import forms

from .models import Proposal1, Proposal2

class ProposalForm1(forms.ModelForm):
    type = ChoiceField(choices=Proposal1.possible_types, label="Project Type")

class ProposalForm2(forms.ModelForm):
    start_date = forms.DateField(label="Project Start Date")
    end_date = forms.DateField(label="Project End Date")
    ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
    past_projects = forms.CharField(max_length=1000, label="Past related projects")
    editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")