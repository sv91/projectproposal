from django import forms
from django.forms import modelformset_factory

from .models import Proposal1, Proposal3, Proposal4, Proposal8, PastProject, Member, Delivrable, Publication, MembersPosition, DelivrableComp
from .widgets import DateTimeInput

# First page of the form containing only a drop-down menu.
class ProposalForm1(forms.ModelForm):
	class Meta:
		model = Proposal1
		fields = '__all__'
	title = "What type of project would you like to apply for?"
	project_type = forms.ChoiceField(choices=Proposal1.possible_types, label="Project Type")
	grant = forms.ChoiceField(choices=Proposal1.possible_grants, label="Grant")
	other = forms.CharField(max_length=200, label="Grant name", required=False)

# Second page with two data fields and two multi-fields.
class ProposalForm2(forms.Form):
	title = "Time line of the project and related projects"
	start_date = forms.DateField(label="Project Start Date", widget = DateTimeInput)
	end_date = forms.DateField(label="Project End Date", widget = DateTimeInput)
	past_projects = modelformset_factory(PastProject,extra=1, exclude=('proposal',))
	past = past_projects(queryset=PastProject.objects.order_by('project_title'))
	
# Third page with the Pi and Co-pi selection.	
class ProposalForm3(forms.ModelForm):
	class Meta:
		model = Proposal3
		fields = '__all__'
	title = "Project Management"
	pi = forms.CharField(max_length=100, label="Principal Investigator")
	cpi = forms.CharField(max_length=100, label="Co-Principal Investigator", required=False)

# Forth page with the description of the different aspects of the project.		
class ProposalForm4(forms.ModelForm):
	class Meta:
		model = Proposal4
		fields = '__all__'
	title = "Project Description Overview"
	task = forms.CharField(max_length=300,required = False)
	project_title = forms.CharField(max_length=300, label="Project Title")
	project_tags = forms.CharField(max_length=300, label="Project Key Words")
	executive_summary = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), max_length=1000, label="Executive Summary")
	impact_statement = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), max_length=1000, label="Impact Statement")
	benefit_to_community = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), max_length=1000, label="Benefit to Community")
	scientific_summary = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), max_length=1000, label="Scientific Summary")
	technological_summary = forms.CharField(widget=forms.Textarea(attrs={'rows':5, 'cols':100}), max_length=1000, label="Technological Summary")

	publications = modelformset_factory(Publication,extra=1, exclude=('proposal',))
	publi = publications(queryset=Publication.objects.order_by('name'))
	
	
# Fifth page with the selection of the team members	
class ProposalForm5(forms.Form):
	title = "Invite Team Members"
	member = modelformset_factory(Member,extra=1, exclude=('proposal',))
	members = member(queryset=Member.objects.order_by('camipro'))
	
# Sixth page with the selection of the team members	
class ProposalForm6(forms.Form):
	title = "Define the Delivrables"
	mem = modelformset_factory(MembersPosition,extra=1, exclude=('proposal',))
	members = mem(queryset=MembersPosition.objects.order_by('camipro'))

class ProposalForm7(forms.Form):
	title = "Computing Ressources"
	delivrablesComp = modelformset_factory(DelivrableComp,extra=1, exclude=('proposal',))
	deli = delivrablesComp(queryset=DelivrableComp.objects.order_by('idN'))
			
# Eighth page with skill assessment	
class ProposalForm8(forms.ModelForm):
	class Meta:
		model = Proposal8
		fields = '__all__'
	title = "Project team skill set evaluation"
	scientific_experience = forms.BooleanField(label="Scientific experience", required=False)
	scientific_publications = forms.CharField(widget=forms.Textarea, max_length=1000, label="List of scientific publications", help_text="Add scientific publications in relation with the proposal")
	
	software_engineering_experience = forms.BooleanField(label="Software engineering experience", required=False)
	software_testing = forms.ChoiceField(choices=Proposal8.levels, label="Software testing", help_text="Unit, regression, integration testing")
	continuous_integretion = forms.ChoiceField(choices=Proposal8.levels, label="Continuous integration", help_text="Using jenkins, bamboo, ...")
	software_realease_packaging = forms.ChoiceField(choices=Proposal8.levels, label="Software release and packaging", help_text="RPM, Debian, ...")
	software_engineering_help = forms.BooleanField(label="Would you be interested in getting support in software engineering ?", required=False)
	
	software_programming_experience = forms.BooleanField(label="Software programming experience", required=False)
	interpreted_languages = forms.ChoiceField(choices=Proposal8.levels, label="Interpreted language", help_text="Such as Python or Ruby")
	imperative_programming_languades = forms.ChoiceField(choices=Proposal8.levels, label="Imperative Programming language", help_text="Such as C/C++/FORTRAN")
	software_programming_help = forms.BooleanField(label="Would you be interested in getting support in programming?", required=False)
	
	parallel_programming_experience = forms.BooleanField(label="Parallel programming experience", required=False)
	destributed_programming = forms.ChoiceField(choices=Proposal8.levels, label="Distributed Programming", help_text="MPI, ...")
	concurrent_programming = forms.ChoiceField(choices=Proposal8.levels, label="Concurrent Programming", help_text="OpenMP, Pthreads, ...")
	accelerator_programming = forms.ChoiceField(choices=Proposal8.levels, label="Accelerator Programming", help_text="Cuda, OpenACC, OpenMP, ...")
	distributed_programming_cloud = forms.ChoiceField(choices=Proposal8.levels, label="Distributed programming in the cloud", help_text="MapReduce, ...")
	parallel_programming_help = forms.BooleanField(label="Would you be interested in getting support in parallel programming ?", required=False)
	
	software_optimization_experience = forms.BooleanField(label="Software optimization experience", required=False)
	application_profiling = forms.ChoiceField(choices=Proposal8.levels, label="Application profiling using standard profiliers", help_text="Scalasca, TAU, VTune, Extrae, ...")
	code_optimization = forms.ChoiceField(choices=Proposal8.levels, label="Code optimization", help_text="Vectorization, ...")
	performance_modeling = forms.ChoiceField(choices=Proposal8.levels, label="Performance modeling", help_text="Algorithmic density, Roofline model, ...")
	software_optimization_help = forms.BooleanField(label="Would you be interested in getting support in software performance modeling and optimization ?", required=False)
