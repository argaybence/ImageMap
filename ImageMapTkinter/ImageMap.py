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

    def triangle(self):
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
