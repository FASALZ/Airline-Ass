class Passenger:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


class CheckIn:
    def __init__(self, passenger, flight_number):
        self.passenger = passenger
        self.flight_number = flight_number

    def perform_check_in(self, flight_service):
        # This would interact with the FlightService
        flight_service.generate_boarding_pass(self)


class BoardingPass:
    def __init__(self, passenger, flight_number, seat_number, boarding_time, gate_number):
        self.passenger = passenger
        self.flight_number = flight_number
        self.seat_number = seat_number
        self.boarding_time = boarding_time
        self.gate_number = gate_number

    def display_info(self):
        # Formats and prints the boarding pass information
        print(f"Passenger: {self.passenger.get_name()}")
        print(f"Flight Number: {self.flight_number}")
        print(f"Seat Number: {self.seat_number}")
        print(f"Boarding Time: {self.boarding_time}")
        print(f"Gate Number: {self.gate_number}")


class FlightService:
    def __init__(self):
        self.boarding_passes = {}

    def generate_boarding_pass(self, check_in):
        # Assuming we create a BoardingPass object here and add it to the dictionary
        boarding_pass = BoardingPass(
            passenger=check_in.passenger,
            flight_number=check_in.flight_number,
            seat_number="09A",
            boarding_time="11:20",
            gate_number="03"
        )
        self.boarding_passes[check_in.passenger.get_name()] = boarding_pass

    def retrieve_boarding_pass(self, passenger):
        # Retrieves the boarding pass for the given passenger
        return self.boarding_passes.get(passenger.get_name(), None)


# Simulation of the entire process
passenger = Passenger(name="JAMES SMITH", id_number="123456789")
check_in = CheckIn(passenger=passenger, flight_number="NA4321")
flight_service = FlightService()
check_in.perform_check_in(flight_service)

# Retrieve and display the boarding pass information
boarding_pass = flight_service.retrieve_boarding_pass(passenger)
if boarding_pass:
    boarding_pass.display_info()
else:
    print("Boarding pass not found.")
