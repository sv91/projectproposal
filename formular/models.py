from django.db import models
from django.utils import timezone
import tagulous.models

	
# Data model corresponding to the first page of the form.
class Proposal1(models.Model):
	possible_types = [['test','Testing'],['dev','Development'],['prod','Production']]
	possible_grants = [['hbp','Human Brain Project'],['bbp','Blue Brain Project'],['none','Other Grant']]
	project_type = models.CharField(max_length=4,choices=possible_types)
	grant = models.CharField(max_length=4,choices=possible_grants)
	other = models.CharField(max_length=200)
	
class PastProject(models.Model):
	project_title = models.CharField(max_length=200)
	funding_agency = models.CharField(max_length=200)
	starting_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField(max_length=1000)
	
# Data model corresponding to the third page of the form.
class Proposal3(models.Model):
	pi = models.CharField(max_length=100)
	cpi = models.CharField(max_length=100)
	
# Data model corresponding to the forth page of the form.
class Proposal4(models.Model):
	task = models.CharField(max_length=300)
	project_title = models.CharField(max_length=300)
	project_tags = tagulous.models.TagField()
	executive_summary = models.TextField(max_length=1000)
	impact_statement = models.TextField(max_length=1000)
	benefit_to_community = models.TextField(max_length=1000)
	scientific_summary = models.TextField(max_length=1000)
	technological_summary = models.TextField(max_length=1000)
	
class Member(models.Model):
	camipro = models.CharField(max_length=100)
	
class MembersPosition(models.Model):
	camipro = models.CharField(max_length=100)
	deli = models.CharField(max_length=100)
	role = models.CharField(max_length=20)
	pm = models.PositiveSmallIntegerField()
	
	
class Delivrable(models.Model):
	idN = models.PositiveSmallIntegerField()
	date = models.DateField()
	description = models.CharField(max_length=200)
	
class DelivrableComp(models.Model):
	idN = models.PositiveSmallIntegerField()
	cycles = models.PositiveIntegerField()
	storage = models.PositiveIntegerField()
	
	
class Publication(models.Model):
	name = models.CharField(max_length=300)
	link = models.CharField(max_length=200)
	
	
# Data model corresponding to the sixth page of the form.
class Proposal8(models.Model):
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
