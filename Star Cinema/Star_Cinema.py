class Star_Cinema:
    __hall_list = []

    def entry_hall(self, hall):
        self.__hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, hall_no):
        super().__init__()
        self.__seats = {}
        self.__show_list = []
        self.__rows = 10
        self.__cols = 10
        self.__hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, movie_id, movie_name, time):
        show = (movie_id, movie_name, time)
        self.__show_list.append(show)
        self.__seats[movie_id] = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

    def book_seats(self, movie_id, row, col):
        if 1 <= row and row <= self.__rows and 1 <= col and col <= self.__cols:
            if self.__seats[movie_id][row - 1][col - 1] == 0:
                self.__seats[movie_id][row - 1][col - 1] = 1
                print(f"\nSeat No: Row: {row}, Col: {col} is Booked.\n")
                return True

            else:
                print(
                    f"\nSeat No: Row: {row}, Col: {col} is already Booked.\nTry Again\n"
                )
                return False

        else:
            print(f"\nSeat No: Row: {row}, Col: {col} is Invalid.\nTry Again\n")
            return False

    def view_show_list(self):
        for show in self.__show_list:
            print(f"ID: {show[0]}\t Name: {show[1]}\t Time: {show[2]}")

    def view_available_seats(self, movie_id):
        if movie_id not in self.__seats:
            print(f"{movie_id} is Invalid Try Again")
            return True

        else:
            for show in self.__show_list:
                if show[0] == movie_id:
                    print(f"\nID: {show[0]}\t Name: {show[1]}\t Time: {show[2]}:\n")
                    for row in self.__seats[movie_id]:
                        print(row)


cinema = Star_Cinema()

hall1 = Hall(1)
hall1.entry_show(101, "Inception", "25/10/2024 11:00 AM")
hall1.entry_show(102, "Megalopolis", "26/10/2024 08:00 AM")
hall1.entry_show(103, "Interstellar", "29/10/2024 07:00 PM")

hall2 = Hall(2)
hall2.entry_show(201, "The Martian", "25/10/2024 11:00 AM")
hall2.entry_show(202, "The Godfather", "29/10/2024 07:00 PM")

print(f"Welcome to The Star Cinema")
print(f"--------------------------\n")

while True:
    print(f"1. VIEW ALL SHOW\n2. VIEW AVAILABLE SEATS\n3. BOOK TICKET\n4. EXIT")
    option = int(input("ENTER OPTION: "))
    print(f"--------------------------\n")

    if option == 1:
        hall1.view_show_list()
        hall2.view_show_list()
        print(f"\n--------------------------\n")

    elif option == 2:
        movie_id = int(input("Enter Movie ID: "))

        if movie_id // 100 == 1:
            hall1.view_available_seats(movie_id)
        elif movie_id // 100 == 2:
            hall2.view_available_seats(movie_id)
        else:
            print(f"{movie_id} is Invalid\nTry Again")

        print(f"\n--------------------------\n")

    elif option == 3:
        run = True
        while run:
            movie_id = int(input("Enter Movie ID: "))

            if movie_id // 100 == 1:
                run = hall1.view_available_seats(movie_id)
            elif movie_id // 100 == 2:
                run = hall2.view_available_seats(movie_id)
            else:
                print(f"{movie_id} is Invalid\nTry Again")
            print("\n")

        tickets = int(input("Number of Tickets: "))

        i = 0
        while i < tickets:
            row = int(input("Seat Row: "))
            col = int(input("Seat Col: "))

            booked = True
            if movie_id // 100 == 1:
                booked = hall1.book_seats(movie_id, row, col)
            elif movie_id // 100 == 2:
                booked = hall2.book_seats(movie_id, row, col)

            if booked:
                i += 1

            print(f"Number of tickets left to purchase: {tickets-i}")

        print(f"\n--------------------------\n")

    elif option == 4:
        print(f"Have a good day!\nCome again, buddy!")
        print(f"\n--------------------------\n")
        break

    else:
        print(f"Invalid option")
        print(f"\n--------------------------\n")
