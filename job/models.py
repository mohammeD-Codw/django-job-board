from django.db import models
JobType=(
('Full Time','Full Time'),
('Part Time','Part Time'),

)
# Create your models here.
class job(models.Model):
    title=models.CharField(max_length=100)
    JobType=models.CharField(choices=JobType,max_length=10)
    description=models.TextField(max_length=1000)
    publish_at=models.DateTimeField(auto_now=True)
    Vacancy=models.IntegerField(default=1)
    Salary=models.IntegerField(default=0)
    experince=models.IntegerField(default=1)
    category=models.ForeignKey("Category", verbose_name=("Categoy"), on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
    

class Category(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name


    
