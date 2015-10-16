from django.db import models

class Proposal1(models.Model):
	possible_types = [['test','Testing'],['dev','Development'],['prod','Production']]
	project_type = models.CharField(max_length=4,choices=possible_types)
    
class Proposal2(models.Model):
	start_date = models.DateField()
	end_date = models.DateField()
	ongoing_projects = models.CharField(max_length=1000)
	past_projects = models.CharField(max_length=1000)
	possible_editing_styles = [['plain','Plain text'],['latex','Latex']]
	editing_styles = models.CharField(max_length=5,choices=possible_editing_styles)
	
class ProposalForm3(models.Model):
	pi = models.CharField(max_length=100)
	cpi = models.CharField(max_length=100)
	
class ProposalForm4(models.Model):
	possible_tasks = [['t111','T1.1.1'],['t112','T1.1.2']]
	hbp_task = models.CharField(max_length=20, choices=possible_tasks)
	project_title = models.CharField(max_length=300)
	project_tags = models.CharField(max_length=300)
	executive_summary = models.TextField(max_length=1000)
	impact_statement = models.TextField(max_length=1000)
	benefit_to_community = models.TextField(max_length=1000)
	scientific_summary = models.TextField(max_length=1000)
	technological_summary = models.TextField(max_length=1000)
	delivrables = models.TextField(max_length=1000)
	references = models.TextField(max_length=1000)
	
class ProposalForm5(models.Model):
	role = models.CharField(max_length=20, choices=Proposal5.possible_roles)
	involvement = models.PositiveSmallIntegerField()	
	
class ProposalForm6(models.Model):
	levels= [['beginner','Begginer'],['intermediate','Intermediate'],['advanced','Advanced']]

	scientific_experience = models.BooleanField()
	scientific_publications = models.TextField(max_length=1000)
	
	software_engineering_experience = models.BooleanField()
	software_testing = models.CharField(max_length=20, choices=levels)
	continuous_integretion = models.CharField(max_length=20, choices=levels)
	software_realease_packaging = models.CharField(max_length=20, choices=levels)
	software_engineering_help = models.BooleanField()
	
	software_programming_experience = models.BooleanField()
	interpreted_languages = models.CharField(max_length=20, choices=levels)
	imperative_programming_languades = models.CharField(max_length=20, choices=levels)
	software_programming_help = models.BooleanField()
	
	parallel_programming_experience = models.BooleanField()
	destributed_programming = models.CharField(max_length=20, choices=levels)
	concurrent_programming = models.CharField(max_length=20, choices=levels)
	accelerator_programming = models.CharField(max_length=20, choices=levels)
	distributed_programming_cloud = models.CharField(max_length=20, choices=levels)
	parallel_programming_help = models.BooleanField()
	
	software_optimization_experience = models.BooleanField()
	application_profiling = models.CharField(max_length=20, choices=levels)
	code_optimization = models.CharField(max_length=20, choices=levels)
	performance_modeling = models.CharField(max_length=20, choices=levels)
	software_optimization_help = models.BooleanField()
