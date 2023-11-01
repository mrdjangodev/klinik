from django.db import models

# from local
# from hr_management.doctor_models import Doctor
# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)
    building = models.CharField(max_length=150, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True, default="Room 5-45A")

    def __str__(self) -> str:
        return self.name

    def get_all_stuffs(self):
        return self.roomstuff_set.select_related('room')


class RoomStuff(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

class Bed(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    number_of_beds = models.PositiveBigIntegerField(default=1)
    price_for_one_day = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    STATUS_CHOICES = (
        (0, "Available"),
        (1, "Occupied"),
    )
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    class Meta:
        ordering = ['status']
    def __str__(self):
        return f"{self.room.name} | {self.status}"




