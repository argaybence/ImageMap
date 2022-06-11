from tkinter import *
from ImageMap import *
from PIL import ImageTk
from PIL import Image


WIDTH, HEIGHT = 1020, 510


# methods that will be invited when you click on the specific shape
def triangle_click():
    print("You have clicked on the triangle!")


def rectangle_click():
    print("You have clicked on the rectangle!")


def circle_click():
    print("You have clicked on the circle!")


# shapes method gets called on event <Button-1> click all the time
def shapes(event):

    geometry = (WIDTH, HEIGHT)

    rect_coordinates = [(-448, 161), (-448, 25), (-197, 25), (-197, 161)]

    tri_coordinates = [(170, 3), (402, 3), (287, 179)]
    tri2_coordinates = [(-351, -150), (-155, -146), (-282, -75)]
    tri3_coordinates = [(-54, -30), (-102, -82), (-9, -147)]

    circle_coordinate = [(-35, 90)]
    # First parameter is the window Height, and Width. Next parameter is the peaks coordinate of the shape.
    # event.x, and event.y stands for the coordinate where the user clicked. The last one is the method, which
    # gets invited whenever they clicked on the area of the shape.
    ImageMapping(geometry, event.x, event.y, rect_coordinates, rectangle_click).rectangle()

    ImageMapping(geometry, event.x, event.y, tri_coordinates, triangle_click).triangle()
    ImageMapping(geometry, event.x, event.y, tri2_coordinates, triangle_click).triangle()
    ImageMapping(geometry, event.x, event.y, tri3_coordinates, triangle_click).triangle()

    # A circle takes a coordinate which is on the circle edge and the other parameters stay the same
    # The circle method requires an extra parameter, and that is radius of the circle
    ImageMapping(geometry, event.x, event.y, circle_coordinate,  circle_click).circle(116)

    # Shows the real coordinates, which you have to provide, when you are using ImageMap
    # show_coordinates(geometry, event.x, event.y)


def main():
    win = Tk()
    win.geometry(f"{WIDTH}x{HEIGHT}")

    # Creating the background image
    image = Image.open("Setup/shapes3.png")
    bg_image = ImageTk.PhotoImage(image)

    # Place the image on the whole screen
    frame = Label(win, image=bg_image)
    frame.place(x=0, y=0)

    # Binding shapes method to get invited whenever the user clicked on the frame
    win.bind("<Button-1>", shapes)

    win.mainloop()


if __name__ == '__main__':
    main()
