from django.db import models

# Create your models here.

# Represents a course offered at the institution
class Course(models.Model):
    name = models.CharField(max_length = 200)  # Name of the course
    description = models.TextField()  # Brief description of the course

    def __str__(self):
        return self.name  # Returns the course name as the string representation

# Represents a user interest e.g Math
class Interest(models.Model):
    name = models.CharField(max_length =100)  # Name of the interest

    def __str__(self):
        return self.name  # Returns the interest name as the string representation
