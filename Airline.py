class Passenger:
    def __init__(self, name, id_number,passportNumber,phoneNumber,email):
        self._name = name
        self._id_number = id_number
        self._passportNumber = passportNumber
        self._phoneNumber = phoneNumber
        self._email = email

    def get_name(self):
        return self._name

    def get_id_number(self):
        return self._id_number

    def get_email(self):
        return self._email

    def get_phone_number(self):
        return self._phoneNumber

    def get_passpotNumber(self):
        return self._passportNumber


    def set_name(self, name):
        self._name = name

    def set_id_number(self, id_number):
        self._id_number = id_number

    def set_email(self, email):
        self._email = email

    def set_phone_number(self, phoneNumber):
        self._phoneNumber = phoneNumber

    def set_passport_number(self, passportNumber):
        self._passportNumber = passportNumber

    def displayInfo(self):
       Passenger.displayInfo
       print(f"Name: {self._name}")
       print(f"Id Number: {self._id_number}")
       print(f"Email: {self._email}")
       print(f"Phone Number: {self._phoneNumber}")
       print(f"Passport Number: {self._passportNumber}")

class CheckIn:
    def __init__(self, passenger, flight_number, check_in_time, seat_preference, gate_number):
        self._passenger = passenger
        self._flight_number = flight_number
        self._check_in_time = check_in_time
        self._seat_preference = seat_preference
        self._gate_number = gate_number


    def perform_check_in(self, flight_service):
        # This would interact with the FlightService
        pass

    def get_flight_number(self):
        return self._flight_number

    def get_passenger(self):
        return self._passenger

    def get_check_in_time(self):
        return self._check_in_time

    def get_seat_preference(self):
        return self._seat_preference

    def get_gate_number(self):
        return self._gate_number

    def set_flight_number(self, flight_number):
        self._flight_number = flight_number

    def set_passenger(self, passenger):
        self._passenger = passenger

    def set_check_in_time(self, check_in_time):
        self._check_in_time = check_in_time

    def set_seat_preference(self, seat_preferenace):
        self._seat_preference = seat_preferenace

    def set_gate_number(self, gate_number):
        self._gate_number = gate_number

    def displayInfo(self):
        CheckIn.displayInfo
        print(f"Passenger: {self._passenger.get_name()}")
        print(f"Check in time: {self._check_in_time}")
        print(f"Seat prefrences: {self._seat_preference}")
        print(f"Gate Number: {self._gate_number}")
        print(f"Flight number: {self._flight_number}")




class BoardingPass:
    def __init__(self, flight_class, flight_from, flight_to, boarding_till, flight_time, ElectronicTicket):
        self._flight_class = flight_class
        self._flight_from = flight_from
        self._flight_to = flight_to
        self._boarding_till = boarding_till
        self._flight_time = flight_time
        self._ElectronicTicket = ElectronicTicket


    def get_flight_from(self):
        return self._flight_from

    def get_flight_class(self):
        return self._flight_class

    def get_flight_to(self):
        return self._flight_to

    def get_boarding_till(self):
        return self._boarding_till

    def get_flight_time(self):
        return self._flight_time

    def get_ElectronicTicket(self):
        return self._ElectronicTicket

    def set_flight_from(self, flight_from):
        self._flight_from = flight_from

    def set_flight_class(self, flight_class):
        self._flight_class = flight_class

    def set_flight_to(self, flight_to):
        self._flight_to = flight_to

    def set_boarding_till(self, boarding_till):
        self._boarding_till = boarding_till

    def set_flight_time(self, flight_time):
        self._flight_time = flight_time

    def set_ElectronicTicket(self, ElectronicTicket):
        self._ElectronicTicket = ElectronicTicket

    def displayInfo(self):

        BoardingPass.displayInfo
        print(f"Flight Class: {self._flight_class}")
        print(f"Flight from: {self._flight_from}")
        print(f"Flight to: {self._flight_to}")
        print(f"Boarding Till: {self._boarding_till}")
        print(f"Flight time: {self._flight_time}")
        print(f"Electronic Ticket: {self._ElectronicTicket}")


class FlightService:
    def __init__(self):
        self.boarding_passes = {}

    def generate_boarding_pass(self, check_in):
        pass

    def retrieve_boarding_pass(self, passenger):
        # Retrieves the boarding pass for the given passenger
        pass


# Simulation of the entire process
passenger = Passenger(name="JAMES SMITH", id_number="123456789",email="james@hotmail.com",phoneNumber="0567855433",passportNumber="NA132456788")
check_in = CheckIn(passenger= passenger, flight_number="NA4321",check_in_time="11:20", seat_preference= "09A",gate_number="03")
boarding_pass = BoardingPass(flight_class="first class", flight_from="Chicago",flight_to="New York",boarding_till="11:20",flight_time="11:40",ElectronicTicket="629")
flight_service = FlightService()
check_in.perform_check_in(flight_service)

passenger.displayInfo()
check_in.displayInfo()
boarding_pass.displayInfo()


