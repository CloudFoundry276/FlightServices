from django.shortcuts import render
from flightApp import serializers
from flightApp.models import Flight, Passenger, Reservation
from flightApp.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets, status, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@api_view(['POST'])
def find_flights(request):
    flights = Flight.objects.filter(departure_city=request.data['departure_city'], arrival_city=request.data['arrival_city'], departure_date=request.data['departure_date'])
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def save_reservations(request):
    flight = Flight.objects.get(id=request.data['flight_id'])

    passenger = Passenger()
    passenger.first_name = request.data['first_name']
    passenger.last_name = request.data['last_name']
    passenger.middle_name = request.data['middle_name']
    passenger.email = request.data['email']
    passenger.phone = request.data['phone']
    passenger.save()

    reservation = Reservation()
    reservation.flight = flight
    reservation.passenger = passenger

    reservation.save()
    return Response(status=status.HTTP_201_CREATED)


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['departure_city', 'arrival_city', 'departure_date']
    permission_classes = [IsAuthenticated]


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
    permission_classes = [IsAuthenticated]


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsAuthenticated]
