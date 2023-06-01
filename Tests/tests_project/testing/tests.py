from django.test import Client, TestCase
from .models import Flight, Airport

# Django testing
class FlightTestCase(TestCase):

    # Create some entries for tests
    def setUp(self) -> None:

        # create airports
        a1 = Airport.objects.create(code="AAA", city="City A")
        a2 = Airport.objects.create(code="BBB", city="City B")

        # create Flight
        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)

    # We know, what origin field have 3 times a1
    def test_departures_count(self):
        """This test checks the departures is 3 time"""
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.origin.count(), 3)

    def test_arrivals_count(self):
        """This test checks the arrivals is 1 time"""
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.destination.count(), 1)

    def test_valid_flight(self):
        """This test checks the functionality of the model function"""
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight(self):
        """This test checks the functionality of the model function (Error: origin=destination)"""
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_duration(self):
        """This test checks the functionality of the model function (Error: duration<0)"""
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())


# Client testing
class ClientTestCase(TestCase):

    def test_index(self):
        """This function test the workability of index page"""

        client = Client()
        response = client.get("/flights")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["flights"].count(), 3)
