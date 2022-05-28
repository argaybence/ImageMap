# ImageMapTkinter
This library allows people to imagemap there pictures, while using Tkinter.


USAGE:
Only works if the image you are mapping, is setted as the background to the window, moreover the screen width, and height need to be equivalent to the image width, and height.
Since this library doesn't work with the natural Tkinter coordinates, I would suggest you to use show_coordinates() method, which will print the coordinates in the console. Those coordinates needs to be provided as the shape coordinate's.

Example calling the show_coordinates() method: show_coordinates((WIDTH, HEIGHT), x, y)

If you have all the peaks coordinates, then you have to place it in list like this: [(x1,y1),(x2,y2),(xn,yn)].
This list will provide the coordinates for the coords parameter.

First of all you need to create an object of ImageMapping class.
Example creating an object for a triangle: ImageMapping(geometry, event.x, event.y, tri_coordinates, triangle_click).triangle()

First parameter is the window Height, and Width. Next parameter is the peaks coordinate of the shape. Event.x, and event.y stands for the coordinate where the user clicked. The last one is the method, which gets invited whenever they clicked on the area of the shape. Then after you filled everything, you need to call a method which represents your shape.

Circle mapping is an exception from the others, because when you provide the coordinates, you only have to provide one.
You need to give a coordinate which is on the edge of the circle, and when you invite the circle(radius) method, you need to add the radius of the circle.
(May I will make a radius calculator in the close future to make usage more easy)

If you have any questions, my Discord: abence#0716, Email: argaybence.161@gmail.com.


I may made grammar mistakes sorry for that. :)
