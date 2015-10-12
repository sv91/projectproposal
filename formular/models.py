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