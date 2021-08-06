from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from .models import CSVData
from .serializers import CSVDataSerializer, FileUploadSerializer
import io
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from .permission import *
from rest_framework.permissions import IsAuthenticated
from main.models import User


class CSVDataView(APIView):
    serializer_class = FileUploadSerializer
    permission_classes = (IsAuthenticated, IsAdminorIsOwner)
    queryset = CSVData.objects.all()

    def get(self, request, *args, **kwargs):
        try:
            user_id= self.request.user.id
            user = User.objects.get(id=user_id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user:
            serializer = UserSignupSerializer(data={"phone_number":user.phone_number,"name":user.name})
            serializer.is_valid()
            return Response(serializer.data)
        raise ValidationError({'error':'Not a valid user'})

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        csv_file = serializer.validated_data['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        #next(io_string)
        try:
            df = pd.read_csv(io_string, delimiter=',', index_col=0)
            for i in range(0, len(df)):
                symbole = df.iloc[i][0]
                date = df.iloc[i][1]
                open = df.iloc[i][2]
                high = df.iloc[i][3]
                low = df.iloc[i][4]
                close = df.iloc[i][5]
                volume = df.iloc[i][6]
                adjclose = df.iloc[i][7]
                #CSVData.objects.save(symbole=symbole, date=date, open=open, high=high, low=low, close=close, volume=volume, adjclose=adjclose)
                CSVData.objects.create(user=self.request.user, symbole=symbole, date=date, open=open, high=high, low=low, close=close, volume=volume, adjclose=adjclose)
                return Response({'Sucessfully'}, status=status.HTTP_201_CREATED)

        except:
            return Response({'Oops Something went wrong'},status=status.HTTP_400_BAD_REQUEST)



