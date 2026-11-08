"""EXERCISE: finish the Polygon class. Use import turtle (not selective imports)."""
import turtle


class Polygon:
    def __init__(self, x, y, sides, side_length, color, pen_size=3, angle=0):
        """Store the first vertex, number of sides, side length, color,
        line width, angle, and an internal turtle.Turtle object.
        Reject sides < 3, side_length <= 0, and pen_size <= 0.
        """
        if not isinstance(sides, int) or sides < 3:
            raise ValueError("sides must be an integer >= 3")
        if side_length <= 0:
            raise ValueError("side_length must be positive")
        if pen_size <= 0:
            raise ValueError("pen_size must be positive")

        self._x = x
        self._y = y
        self._sides = sides
        self._side_length = side_length
        self._color = color
        self._pen_size = pen_size
        self._angle = angle

        # Each Polygon owns its own Turtle (private by convention).
        self._pen = turtle.Turtle()
        self._pen.hideturtle()
        self._pen.speed(0)

    def draw(self):
        """Draw a regular polygon using left(360 / sides)."""
        self._pen.penup()
        self._pen.goto(self._x, self._y)
        self._pen.setheading(self._angle)
        self._pen.pencolor(self._color)
        self._pen.pensize(self._pen_size)
        self._pen.pendown()
        turn = 360 / self._sides  # derived value, not stored state
        for _ in range(self._sides):
            self._pen.forward(self._side_length)
            self._pen.left(turn)
        self._pen.penup()

    def move_to(self, x, y):
        """Update the starting vertex; clear only this polygon; redraw."""
        self._x = x
        self._y = y
        self._pen.clear()
        self.draw()