import logging
from typing import List, Tuple, Callable
from tkinter import Event

from logging import getLogger, INFO

from Equations import two_point_equation, circle_equation
from ImageMapExceptions import InvalidEdgeAmount


logger = getLogger(__name__)
logging.basicConfig(
    level=INFO,
    format='%(asctime)s | %(filename)s | %(levelname)s: %(message)s'
    )



class ImageMap:
    def __init__(self, geometry: Tuple[int, int]):
        self.geometry = geometry

    def triangle(self, edges: List[Tuple[int, int]]) -> Callable:

        if len(edges) != 3:
            raise InvalidEdgeAmount('The length of the edges must be 3, if you are using triangle.')

        def function_wrapper(func: Callable = None) -> Callable:
            def wrapped_func(event: Event) -> bool:
                x, y = self._coordinate_translater((event.x, event.y))
                lines = sorted(self._proper_lines(self._combine(edges, duplicate=False), len(edges)), key=lambda n: n[0])

                if len(lines) == 2:
                    x1 = {two_point_equation(lines[0][0], lines[0][1], y): [lines[0][0][1], lines[0][1][1]]}
                    x2 = {two_point_equation(lines[1][0], lines[1][1], y): [lines[1][0][1], lines[1][1][1]]}

                    y_values = list(x1.values())[0]

                    if self._between(y, y_values[0], y_values[1]):
                        left_x, right_x = list(x1.keys())[0], list(x2.keys())[0]
                        if self._between(x, left_x, right_x):
                            if func is None:
                                return True

                            func(event)
                            return True

                        return False

                else:
                    x1 = {two_point_equation(lines[0][0], lines[0][1], y): [lines[0][0][1], lines[0][1][1]]}
                    x2 = {two_point_equation(lines[1][0], lines[1][1], y): [lines[1][0][1], lines[1][1][1]]}
                    x3 = {two_point_equation(lines[2][0], lines[2][1], y): [lines[2][0][1], lines[2][1][1]]}

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

                        if self._between(y, y_values[0], y_values[1]):
                            left_x = list(x_values[index].keys())[0]
                            right_x = list(x_values[j].keys())[0]

                            if self._between(x, left_x, right_x):
                                if func is None:
                                    return True

                                func(event)
                                return True

                            return False


            return wrapped_func
        return function_wrapper

    def rectangle(self, edges: List[Tuple[int, int]]) -> Callable:

        if len(edges) != 4:
            raise InvalidEdgeAmount('The length of the edges must be 4, if you are using rectangle.')

        def function_wrapper(func: Callable = None) -> Callable:
            def wrapped_func(event: Event) -> bool:

                x, y = self._coordinate_translater((event.x, event.y))
                lines = sorted(self._proper_lines(self._combine(edges, duplicate=False), len(edges)), key=lambda n: n[0])

                min_y, max_y = self._value_set(lines)

                left_x, right_x = None, None

                if self._between(y, min_y, max_y):
                    left_x = two_point_equation(lines[0][0], lines[0][1], y)
                    right_x = two_point_equation(lines[1][0], lines[1][1], y)

                if left_x is not None:

                    if self._between(x, left_x, right_x):
                        if func is None:
                            return True

                        func(event)
                        return True

                    return False

            return wrapped_func
        return function_wrapper

    def circle(self, edges: List[Tuple[int, int]], radius: int) -> Callable:

        if len(edges) != 1:
            raise InvalidEdgeAmount('The length of the edges must be 1, if you are using circle.')

        def function_wrapper(func: Callable = None) -> Callable:
            def wrapped_func(event: Event) -> bool:
                mid_x, mid_y = edges[0]
                x, y = self._coordinate_translater((event.x, event.y))

                try:
                    left_x, right_x = circle_equation(mid_x, mid_y, y, radius)
                except TypeError:
                    return False

                if left_x is not None:
                    if left_x <= x <= right_x:
                        if func is None:
                            return True

                        func(event)
                        return True

                    return False

            return wrapped_func
        return function_wrapper

    def show_coordinates(self, event: Event) -> None:
        x, y = self._coordinate_translater((event.x, event.y))
        logger.info('Event position: (%s; %s)', x, y)


    def _coordinate_translater(self, coord: Tuple[int, int] | Tuple[float, float]) -> tuple:
        reduce_x = self.geometry[0] // 2
        reduce_y = self.geometry[1] // 2

        if coord[1] > reduce_y:
            return coord[0] - reduce_x, -(coord[1] - reduce_y)
        return coord[0] - reduce_x, abs(coord[1] - reduce_y)

    # TODO: Replace, or rewrite this function
    @staticmethod
    def _proper_lines(lines: list, angles: int) -> list:
        ls = []  # lines

        #  triangle
        if angles == 3:
            for i in range(len(lines)):
                if lines[i][0][1] != lines[i][1][1]:
                    temporary = [lines[i][1], lines[i][0]]

                    if temporary not in ls:
                        ls.append(lines[i])

            return ls

        # square
        for i in range(len(lines)):
            if lines[i][0][0] == lines[i][1][0]:
                temporary = [lines[i][1], lines[i][0]]

                if temporary not in ls:
                    ls.append(lines[i])
        return ls

    # TODO: Replace, or rewrite this function
    @staticmethod
    def _value_set(edges: List[List[Tuple[int, int]]]) -> tuple:
        y_axis = []

        for i in range(len(edges)):
            y_axis.append(edges[i][0][1])
            y_axis.append(edges[i][1][1])

        return min(y_axis), max(y_axis)

    # TODO: Replace, or rewrite this function
    @staticmethod
    def _combine(elements: list, duplicate: bool = True) -> list:
        out_list = []
        if duplicate:
            for i in range(len(elements)):
                for j in range(len(elements)):
                    out_list.append([elements[i], elements[j]])
            return out_list

        for i in range(len(elements)):
            for j in range(len(elements)):
                if elements[i] != elements[j]:
                    out_list.append([elements[i], elements[j]])
        return out_list

    @staticmethod
    def _between(x: int | float, x1: int | float, x2: int | float) -> bool:
        if x1 < x2:
            if x1 <= x <= x2:
                return True

        if x1 >= x >= x2:
            return True
        return False
