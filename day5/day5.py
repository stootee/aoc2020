class Plane:
    rows = range(128)
    cols = range(8)

    def __init__(self):
        self.seat_layout = self.seat_map()

    def calculate_seat_id(self, seat_row, seat_column):
        return seat_row * 8 + seat_column

    def seat_map(self):
        seat_layout = []
        for row in self.rows:
            row_seats = []
            for col in self.cols:
                row_seats.append('.')
            seat_layout.append(row_seats)

        return seat_layout

    def seat_view(self):
        print('     0 1 2 3 4 5 6 7')
        for row_number, x in enumerate(self.seat_layout):
            print(f"{('000'+str(row_number))[-3:]}: ", end='')
            for y in x:
                print(f"{y} ", end='')
            print()


class Seat(Plane):
    def __init__(self, bpass):
        super().__init__()
        self.bpass = bpass
        self.seat_row, self.seat_col = self.find_seat(bpass)
        self.id = self.calculate_seat_id(self.seat_row, self.seat_col)

    def find_seat(self, bpass):
        row_start = min(self.rows)
        row_end = max(self.rows)
        col_start = min(self.cols)
        col_end = max(self.cols)
        for bit in bpass:
            if bit == 'F':
                row_end = ((row_end - row_start) // 2) + row_start
            elif bit == 'B':
                row_start = ((row_end - row_start) // 2) + 1 + row_start
            elif bit == 'L':
                col_end = ((col_end - col_start) // 2) + col_start
            elif bit == 'R':
                col_start = ((col_end - col_start) // 2) + 1 + col_start
            else:
                'unknown bit'
                raise

        return row_start, col_start


with open('day5.txt', 'r') as fl:
    inp = fl.read().splitlines()

plane = Plane()

seat_id_check = 0
for boarding_pass in inp:
    seat = Seat(boarding_pass)

    if seat.id > seat_id_check:
        seat_id_check = seat.id

    plane.seat_layout[seat.seat_row][seat.seat_col] = '*'

print(seat_id_check)
plane.seat_view()

print(plane.calculate_seat_id(76, 7))
