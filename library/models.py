from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=15)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title}  {self.description}  {self.price}  {self.count}"


class Student(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15, null=True)
    username = models.CharField(max_length=20)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name}"


class Booking(models.Model):
    student = models.ManyToManyField(Student)
    book = models.ManyToManyField(Book)
    start_date = models.DateField()
    return_date = models.DateField(null=True)

    def __str__(self):
        return f"{self.student}  {self.book}"
