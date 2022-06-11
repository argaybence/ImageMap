from Setup.Lines import proper_lines
from Setup.Equations import two_point_equation, circle_equation
from Setup.Combination import combine
from Setup.ValueSet import value_set
from Setup.RealCoordinates import coordinate_translater


class ImageMapping:
    def __init__(self, geometry: tuple, x: int, y: int, coords=None, command=None):
        self.geometry = geometry  # The window height, and width
        self.coords = coords  # Shape coordinates which are required
        self.x = x  # event.x (x coordinate)
        self.y = y  # event.y (y coordinate)
        self.command = command  # the method which gets executed whenever the user clicks on the shape

        # Since tkinter coordinate system starts from the top left corner (0;0), I made my own coordinate system using
        # the geometry, so now the middle of the frame has the coordinate (0;0)
        self.x, self.y = coordinate_translater(self.geometry, (self.x, self.y))

    @staticmethod
    def between(x, x1, x2):
        if x1 < x2:  # -20 < -150
            if x1 <= x <= x2:
                return True

        if x1 >= x >= x2:
            return True
        return False

    def triangle(self):
        # Combine creates all variation of coordinate pairs (without duplications)
        # Proper_lines goes through these coordinate pairs, and select the correct ones (the lines on each side - which
        # is moving on the y-axis)
        # Sorting it to avoid wrong calculation (avoid the exchange of the right_x, and left_x)
        lines = sorted(proper_lines(combine(self.coords, duplicate=False), len(self.coords)), key=lambda x: x[0])

        if len(lines) == 2:
            x1 = {two_point_equation(lines[0][0], lines[0][1], self.y): [lines[0][0][1], lines[0][1][1]]}
            x2 = {two_point_equation(lines[1][0], lines[1][1], self.y): [lines[1][0][1], lines[1][1][1]]}

            y_values = list(x1.values())[0]

            if y_values[0] <= self.y <= y_values[1]:
                left_x, right_x = list(x1.keys())[0], list(x2.keys())[0]
                if left_x <= self.x <= right_x:
                    self.command()
        else:
            x1 = {two_point_equation(lines[0][0], lines[0][1], self.y): [lines[0][0][1], lines[0][1][1]]}
            x2 = {two_point_equation(lines[1][0], lines[1][1], self.y): [lines[1][0][1], lines[1][1][1]]}
            x3 = {two_point_equation(lines[2][0], lines[2][1], self.y): [lines[2][0][1], lines[2][1][1]]}

            x_values = [x1, x2, x3]

            distances = [list(x1.values())[0], list(x2.values())[0], list(x3.values())[0]]
            largest = 0
            index = 0

            for i in range(3):
                if abs(distances[i][0] - distances[i][1]) > largest:
                    largest = abs(distances[i][0] - distances[i][1])
                    index = i

            for j in range(3):
                if j == index:
                    continue
                y_values = x_values[j][list(x_values[j].keys())[0]]

                if self.between(self.y, y_values[0], y_values[1]):
                    left_x = list(x_values[index].keys())[0]
                    right_x = list(x_values[j].keys())[0]

                    if self.between(self.x, left_x, right_x):

                        self.command()

    def rectangle(self):
        # Combine creates all variation of coordinate pairs (without duplications)
        # Proper_lines goes through these coordinate pairs, and select the correct ones (the lines on each side - which
        # is moving on the y-axis)
        # Sorting it to avoid wrong calculation (avoid the exchange of the right_x, and left_x)
        lines = sorted(proper_lines(combine(self.coords, duplicate=False), len(self.coords)), key=lambda x: x[0])

        # The lowest and the highest y coordinate on the line
        min_y, max_y = value_set(lines)

        left_x, right_x = None, None

        if min_y <= self.y <= max_y:
            left_x = two_point_equation(lines[0][0], lines[0][1], self.y)
            right_x = two_point_equation(lines[1][0], lines[1][1], self.y)

        if left_x is not None:

            if left_x <= self.x <= right_x:
                self.command()

    def circle(self, radius: int):
        x, y = self.coords[0]

        try:
            left_x, right_x = circle_equation(x, y, self.y, radius)
        except TypeError:
            return None

        if left_x is not None:
            if left_x <= self.x <= right_x:
                self.command()


def show_coordinates(geometry, x, y):
    x, y = coordinate_translater(geometry, (x, y))
    print(f"({x} ; {y})")
