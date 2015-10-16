from django import forms

from .models import Proposal1, Proposal2

class ProposalForm1(forms.ModelForm):
	class Meta:
		model = Proposal1
		fields = '__all__'
	project_type = forms.ChoiceField(choices=Proposal1.possible_types, label="Project Type")

class ProposalForm2(forms.ModelForm):
	class Meta:
		model = Proposal2
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm3(forms.ModelForm):
	class Meta:
		model = Proposal3
		fields = '__all__'
	title = "Project Management"
	pi = forms.CharField(max_length=100, label="Principal Investigator")
	cpi = forms.CharField(max_length=100, label="Co-Principal Investigator")
	
class ProposalForm4(forms.ModelForm):
	class Meta:
		model = Proposal4
		fields = '__all__'
	title = "Project Description Overview"
	hbp_task = forms.ChoiceField(choices=Proposal4.possible_tasks, label="Choose the HBP task this allocation will support")
	project_title = forms.CharField(max_length=300, label="Project Title")
	project_tags = forms.CharField(max_length=300, label="Project Key Words")
	executive_summary = forms.CharField(max_length=1000, label="Executive Summary")
	impact_statement = forms.CharField(max_length=1000, label="Impact Statement")
	benefit_to_community = forms.CharField(max_length=1000, label="Benefit to Community")
	scientific_summary = forms.CharField(max_length=1000, label="Scientific Summary")
	technological_summary = forms.CharField(max_length=1000, label="Technological Summary")
	delivrables = forms.CharField(max_length=1000, label="Delivrables")
	references = forms.CharField(max_length=1000, label="References")
	
class ProposalForm5(forms.ModelForm):
	class Meta:
		model = Proposal5
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm6(forms.ModelForm):
	class Meta:
		model = Proposal6
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm7(forms.ModelForm):
	class Meta:
		model = Proposal7
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm8(forms.ModelForm):
	class Meta:
		model = Proposal8
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm9(forms.ModelForm):
	class Meta:
		model = Proposal9
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm10(forms.ModelForm):
	class Meta:
		model = Proposal10
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.CharField(max_length=1000, label="On going related projects")
	past_projects = forms.CharField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")