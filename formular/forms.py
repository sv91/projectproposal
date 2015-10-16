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
	ongoing_projects = forms.TextField(max_length=1000, label="On going related projects")
	past_projects = forms.TextField(max_length=1000, label="Past related projects")
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
	executive_summary = forms.TextField(max_length=1000, label="Executive Summary")
	impact_statement = forms.TextField(max_length=1000, label="Impact Statement")
	benefit_to_community = forms.TextField(max_length=1000, label="Benefit to Community")
	scientific_summary = forms.TextField(max_length=1000, label="Scientific Summary")
	technological_summary = forms.TextField(max_length=1000, label="Technological Summary")
	delivrables = forms.TextField(max_length=1000, label="Delivrables")
	references = forms.TextField(max_length=1000, label="References")
	
class ProposalForm5(forms.ModelForm):
	class Meta:
		model = Proposal5
		fields = '__all__'
	title = "Invite Team Members"
	role = forms.ChoiceField(choices=Proposal5.possible_roles, label="Role")
	involvement = forms.PositiveSmallIntegerField(label="Involvement", help_text="Number of person months")	
	
class ProposalForm6(forms.ModelForm):
	class Meta:
		model = Proposal6
		fields = '__all__'
	title = "Project team skill set evaluation"
	scientific_experience = forms.BooleanField(label="Scientific experience")
	scientific_publications = forms.TextField(max_length=1000, label="List of scientific publications", help_text="Add scientific publications in relation with the proposal")
	
	software_engineering_experience = forms.BooleanField(label="Software engineering experience")
	software_testing = forms.ChoiceField(choices=Proposal6.levels, label="Software testing", help_text="Unit, regression, integration testing")
	continuous_integretion = forms.ChoiceField(choices=Proposal6.levels, label="Continuous integration", help_text="Using jenkins, bamboo, ...")
	software_realease_packaging = forms.ChoiceField(choices=Proposal6.levels, label="Software release and packaging", help_text="RPM, Debian, ...")
	software_engineering_help = forms.BooleanField(label="Would you be interested in getting support in software engineering ?")
	
	software_programming_experience = forms.BooleanField(label="Software programming experience")
	interpreted_languages = forms.ChoiceField(choices=Proposal6.levels, label="Interpreted language", help_text="Such as Python or Ruby")
	imperative_programming_languades = forms.ChoiceField(choices=Proposal6.levels, label="Imperative Programming language", help_text="Such as C/C++/FORTRAN")
	software_programming_help = forms.BooleanField(label="Would you be interested in getting support in programming?")
	
	parallel_programming_experience = forms.BooleanField(label="Parallel programming experience")
	destributed_programming = forms.ChoiceField(choices=Proposal6.levels, label="Distributed Programming", help_text="MPI, ...")
	concurrent_programming = forms.ChoiceField(choices=Proposal6.levels, label="Concurrent Programming", help_text="OpenMP, Pthreads, ...")
	accelerator_programming = forms.ChoiceField(choices=Proposal6.levels, label="Accelerator Programming", help_text="Cuda, OpenACC, OpenMP, ...")
	distributed_programming_cloud = forms.ChoiceField(choices=Proposal6.levels, label="Distributed programming in the cloud", help_text="MapReduce, ...")
	parallel_programming_help = forms.BooleanField(label="Would you be interested in getting support in parallel programming ?")
	
	software_optimization_experience = forms.BooleanField(label="Software optimization experience")
	application_profiling = forms.ChoiceField(choices=Proposal6.levels, label="Application profiling using standard profiliers", help_text="Scalasca, TAU, VTune, Extrae, ...")
	code_optimization = forms.ChoiceField(choices=Proposal6.levels, label="Code optimization", help_text="Vectorization, ...")
	performance_modeling = forms.ChoiceField(choices=Proposal6.levels, label="Performance modeling", help_text="Algorithmic density, Roofline model, ...")
	software_optimization_help = forms.BooleanField(label="Would you be interested in getting support in software performance modeling and optimization ?")
	
class ProposalForm7(forms.ModelForm):
	class Meta:
		model = Proposal7
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.TextField(max_length=1000, label="On going related projects")
	past_projects = forms.TextField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm8(forms.ModelForm):
	class Meta:
		model = Proposal8
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.TextField(max_length=1000, label="On going related projects")
	past_projects = forms.TextField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm9(forms.ModelForm):
	class Meta:
		model = Proposal9
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.TextField(max_length=1000, label="On going related projects")
	past_projects = forms.TextField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")
	
class ProposalForm10(forms.ModelForm):
	class Meta:
		model = Proposal10
		fields = '__all__'
	start_date = forms.DateField(label="Project Start Date")
	end_date = forms.DateField(label="Project End Date")
	ongoing_projects = forms.TextField(max_length=1000, label="On going related projects")
	past_projects = forms.TextField(max_length=1000, label="Past related projects")
	editing_styles = forms.ChoiceField(choices=Proposal2.possible_editing_styles, label="Choose your editing style")