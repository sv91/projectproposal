from django.db import models

class Proposal1(models.Model):
	possible_types = [['test','Testing'],['dev','Development'],['prod','Production']]
    
class Proposal2(models.Model):
	possible_editing_styles = [['plain','Plain text'],['latex','Latex']]
	editing_styles = models.CharField(max_length=5,choices=possible_editing_styles)