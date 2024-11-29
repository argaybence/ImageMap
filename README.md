# ImageMap for Python GUI applications

ImageMap is a Python library that enables you to create interactive image maps using the Python GUI frameworks. It provides support for detecting clicks on various shapes (triangles, rectangles, and circles) overlayed on an image. In this documentation, we will use Tkinter for examples. However, you can apply this to any Python GUI framework, as it only requires the click event arguments and the window size, which are universal across GUI libraries.

## Features

- Easily map user clicks to specific shapes (triangles, rectangles, circles).
- Detect clicks within specific regions of an image.
- Supports Tkinter’s GUI framework for Python.
- Allows custom actions to be triggered when a shape is clicked.

## Requirements for the examples

- Python 3.6+
- `tkinter` (built-in with Python)
- `Pillow` (for handling images)

Install Pillow with:
```bash
pip install pillow
```
or

Install requirements.txt:
```bash
pip install -r requirements.txt
```

## Usage

### Prerequisites

The image you are mapping must:
- Be set as the background of the Tkinter window.
- Match the dimensions of the window (i.e., screen width and height should equal the image width and height).

### Defining Shapes

You can define shapes by their coordinates and associate them with specific actions:

1. **Triangles**:
   - Provide a list of 3 points (tuples) representing the vertices.
   - Example: `tri_coordinates = [(x1, y1), (x2, y2), (x3, y3)]`.

2. **Rectangles/Squares**:
   - Provide 4 corner points as a list of tuples.
   - Example: `rect_coordinates = [(x1, y1), (x2, y2), ..., (x4, y4)]`.

3. **Circles**:
   - Provide a single point (center) and a radius.
   - Example: `circle_coordinate = [(x, y)]`.

### Optional Helper Method
Use `show_coordinates()` to debug and print the coordinates clicked by the user. This helps in obtaining the required points for defining shapes.
Example with Tkinter:

```python
from ImageMap import ImageMap
from tkinter import Tk

WIDTH, HEIGHT = 1020, 510
geometry = (WIDTH, HEIGHT)
    
win = Tk()
win.geometry(f"{WIDTH}x{HEIGHT}")

im = ImageMap(geometry)

win.bind("<Button-1>", im.show_coordinates)

```

### Example Code

Here’s an example of how to use ImageMap with Tkinter with to set up an interactive image map:

```python
from tkinter import Tk, Label
from ImageMap import ImageMap
from PIL import ImageTk, Image

# Image and window dimensions
WIDTH, HEIGHT = 1020, 510

# Define shape coordinates
rect_coordinates = [(-448, 161), (-448, 25), (-197, 25), (-197, 161)]
tri_coordinates = [(170, 3), (402, 3), (287, 179)]
circle_coordinate = [(-35, 90)]

geometry = (WIDTH, HEIGHT)

# Initialize ImageMap
im = ImageMap(geometry)


# Define actions for shapes
@im.triangle(edges=tri_coordinates)
def tri_action(event):
   print('Clicked on a triangle.')


@im.rectangle(edges=rect_coordinates)
def rect_action(event):
   print('Clicked on a rectangle.')


@im.circle(edges=circle_coordinate, radius=116)
def circle_action(event):
   print('Clicked on a circle.')


# Combine actions (if needed)
def combined(event):
   rect_action(event)
   tri_action(event)
   circle_action(event)


# Main application setup
def main():
   win = Tk()
   win.geometry(f"{WIDTH}x{HEIGHT}")

   # Load and set the background image
   image = Image.open("Assets/shapes2.png")
   bg_image = ImageTk.PhotoImage(image)

   frame = Label(win, image=bg_image)
   frame.place(x=0, y=0)

   # Bind click event
   win.bind("<Button-1>", combined)

   win.mainloop()


if __name__ == '__main__':
   main()
```

## Explanation of the Code

1. **Defining Shape Coordinates**:
   Coordinates for shapes are defined as lists of tuples. For example, a triangle needs 3 points.

2. **Binding Actions**:
   Each shape is associated with a function using decorators like `@im.triangle`, `@im.rectangle`, or `@im.circle`.

3. **Combining Actions**:
   If multiple shapes overlap, you can define a `combined` function to handle multiple shape clicks. 
   (You can also use them separately, we just combined them for shorter explanation)
   However if you want to bind one type of event to one element multiple times, combining these functions like in the example can be a solution!

4. **Setting Up the GUI**:
   The background image is loaded using Pillow and placed in the Tkinter window. The `<Button-1>` event binds mouse clicks to your defined actions.

## Notes

1. For circles, you only need to provide a single edge coordinate(middle point), and then specify the radius in the `@im.circle(edges=..., radius=...)` method.

2. This library uses custom coordinate handling, so make sure the dimensions of the image and window match.

## Contact

If you have any questions or need assistance, feel free to reach out:

- Email: `argaybence.161@gmail.com`
