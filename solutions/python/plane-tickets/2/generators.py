"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """

    pass
    for seat in range(number):
        letters=["A","B","C","D"]
        yield letters[seat%4]
        

def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    pass
    total_rows = (number+3)//4
    count=0
    for row in range(total_rows):
        for seat in generate_seat_letters(4):
            count+=1
            if count<=number:
                if row<12:
                    actual_row = row+1
                else:
                    actual_row = row+2
                yield f"{actual_row}{seat}"
                
    
def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """

    pass
    seat_assigned = {}
    gen = generate_seats(len(passengers))
    for passenger,seat in zip(passengers,gen):
        seat_assigned[passenger]=seat
    return seat_assigned
        


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    pass
    no_of_zero = 0
    ticket_number = ""
    for seat in seat_numbers:
        no_of_zero = 12-(len(seat)+len(flight_id))
        ticket_number = f"{seat}{flight_id}{"0" * no_of_zero}"
        yield ticket_number
