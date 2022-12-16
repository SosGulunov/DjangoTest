from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    DoesNotExist = models.Manager


class Company(models.Model):
    name = models.CharField(max_length=30)


class Course(models.Model):
    name = models.CharField(max_length=30)


class Student(models.Model):
    name = models.CharField(max_length=30)
    course = models.ManyToManyField(Course)


class Product(models.Model):
    company = models.ForeignKey(Company,on_delete= models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()
