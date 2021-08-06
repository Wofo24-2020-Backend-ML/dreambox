from django.db import models
from main.models import User



STATUS_CHOICE = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Cancelled', 'Cancelled'),
    ('Declined', 'Declined'),
    ('Completed', 'Completed')
)

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    scheduled= models.DateTimeField(blank=False, null=False)
    appointment_end = models.CharField(null=True, blank=True, max_length=50)
    created_date_time = models.DateTimeField(auto_now_add=True)
    day = models.CharField(null=True, blank=True, max_length=50)
    status = models.CharField(choices=STATUS_CHOICE, max_length=100,null=True, blank=True)
    payment_status = models.BooleanField(default=False)

    #def __str__(self):
       # return self.user.username +' '+"Appointment Scheduled on " + ' ' + self.day