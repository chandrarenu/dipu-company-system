from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    salary = models.IntegerField()

    def __str__(self):
        return self.name

class Attendance(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.staff.name} - {self.status}"

    class Meta:
        unique_together = ('staff', 'date')