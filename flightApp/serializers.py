from rest_framework import serializers
from flightApp.models import Flight, Passenger, Reservation
import re


# custom validation way 3
def is_valid_flight_number(data):
    print("is_valid_flight_number")
    print(data)


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'
        validators = [is_valid_flight_number]
    
    # custom validation way 1
    def validate_flight_number(self, flight_number):
        print("validate_flight_number")
        if re.match("^[a-zA-Z0-9]*$", flight_number) == None:
            raise serializers.ValidationError("Invalid Flight Number! Flight Number should be Alpha Numeric.")
        return flight_number
    
    # custom validation way 2
    def validate(self, data):
        print("validate")
        print(data)
        return data


class PassengerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passenger
        fields = '__all__'


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
