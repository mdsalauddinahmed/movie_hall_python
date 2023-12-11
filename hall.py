class Star_cinema:
    def __init__(self) -> None:
        self.shows = []
        self.hall_list = []
    def entry_hall(self, hall_id, seats):
        new_hall = Hall(hall_id, seats)
        self.hall_list.append(new_hall)

class Hall:

    def __init__(self, rows, cols, hall_no):
        self._seats = {}   
        self._show_list = []  
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        
        
    # Star_Cinema.entry_hall(self, hall_id, capacity)
    def display_menu(self):
        
        print("0. Show list of Halls: ")
        print("1. View All Shows Today")
        print("2. View Available Seats for a Show")
        print("3. Book Ticket")
      
        print("4. Exit")
    def _initialize_seats(self):
        for i in range(1, self._rows + 1):
            for j in range(1, self._cols + 1):
                self._seats[(i, j)] = 'Free'

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)
        self._allocate_seats(id)

    def _allocate_seats(self, id):
        seat_matrix = [['Free' for _ in range(self._cols)] for _ in range(self._rows)]
        self._seats[id] = seat_matrix
        
    def view_available_seats(self, show_id):
        for show in self.shows:
            if show['id'] == show_id:
                booked_seats = show['booked_seats']
                total_seats = show['total_seats']
                available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
                print(f"Available seats for Show ID {show_id}: {available_seats}")

    def book_ticket(self, show_id, seat_number):
        for show in self.shows:
            if show['id'] == show_id:
                booked_seats = show['booked_seats']
                total_seats = show['total_seats']
                if seat_number in booked_seats:
                    print("Seat already booked. Please choose another seat.")
                    return
                elif 1 <= seat_number <= total_seats:
                    booked_seats.append(seat_number)
                    print(f"Ticket booked successfully for Show ID {show_id}, Seat Number {seat_number}.")
                else:
                    print("Invalid seat number.")
                return
        print(f"Show ID {show_id} not found.")



    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-4): ")
            if choice =='0':
                self.entry_hall(1200,'Start_cineplex',50)
                self.entry_hall(1212,'Bonolota',60)
            elif choice == '1':
                self.view_all_shows_today()
            elif choice == '2':
                show_id = int(input("Enter Show ID: "))
                self.view_available_seats(show_id)
            elif choice == '3':
                show_id = int(input("Enter Show ID: "))
                seat_number = int(input("Enter Seat Number: "))
                self.book_ticket(show_id, seat_number)
            elif choice == '4':
                print("Exiting the program. Thank you")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
   
movie_booking = Hall(rows=10,cols=10,hall_no=123)
movie_booking.run()
