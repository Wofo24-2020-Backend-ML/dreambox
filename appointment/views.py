from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import AppointmentSerializer
from .models import Appointment
from .permission import IsAdminorIsOwner, IsUser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

days = {
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday',
}


class NewAppointmentView(APIView):
    """
        this view is for Schedule an appointment by user and allows put/patch/delete only to admin
    """

    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated, IsAdminorIsOwner)
    queryset = Appointment.objects.all()


    def get(self, request, *args, **kwargs):
        appointments = Appointment.objects.filter(user=self.request.user)
        serializer = AppointmentSerializer(data=appointments, many=True)
        serializer.is_valid()
        return Response(serializer.data)



    def post(self, request, *args, **kwargs):
        serializer = AppointmentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        scheduled_check = serializer.validated_data['scheduled']
        scheduled_day = days[scheduled_check.weekday()]

        if scheduled_day != 'Saturday' and scheduled_day != 'Sunday' and CalculateTime(scheduled_check):

            serializer.save(user=self.request.user, status="Pending", payment_status=False, day=scheduled_day,
                            appointment_end=CalculateDateTime(scheduled_check))
            return Response({'info': 'Successfully Scheduled  Your Appointment'},
                            status=status.HTTP_201_CREATED)

        else:
            return Response({'Sorry': 'We are not Available on Sunday and Saturday and you can only book appointment '
                                      '9:00am - 5:00pm Monday - Friday', 'on': scheduled_day})


class MyAppointment(APIView):
    """
    Providing appointment details of the authenticated user.
    """
    serializer_class = AppointmentSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        myappointment = Appointment.objects.filter(user=self.request.user)
        serializer = AppointmentSerializer(data=myappointment, many=True)
        serializer.is_valid()
        return Response(serializer.data)


def CalculateTime(time):
    time = str(time)
    time = time.split(' ')[1]
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    if hour <= '16' and minute <= '59':
        return True
    else:
        return False


def CalculateDateTime(time):
    """Function for providing date and time in more readable form. """
    time = str(time)
    date = time.split(' ')[0]
    splitted_date = date.split('-')
    day = splitted_date[2]
    month = splitted_date[1]
    year = splitted_date[0]
    time = time.split(' ')[1]
    hour = time.split(':')[0]
    minute = time.split(':')[1]
    updated_hour = int(hour) + 1
    if updated_hour > 12:
        updated_hour = updated_hour - 12
        fulldate = day + " " + month + " " + year + " | " + str(updated_hour) + ":" + minute
        return fulldate
    else:
        fulldate = day + " - " + month + " - " + year + " | " + str(updated_hour) + ":" + minute
        return fulldate
