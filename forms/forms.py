from django import forms

class ProposalForm1(forms.Form):
	possible_types = ['Testing','Development','Production']
    type = ChoiceField(choices=possible_types, label="Project Type")

class ProposalForm2(forms.Form):
    start_date = DateField(label="Project Start Date")
    end_date = DateField(label="Project End Date")
    ongoing_projects = CharField(max_length=1000, label="On going related projects")
    past_projects = CharField(max_length=1000, label="Past related projects")
	possible_editing_styles = ['Plain text','latex']
    editing_styles = ChoiceField(choices=possible_editing_styles, label="Choose your editing style")