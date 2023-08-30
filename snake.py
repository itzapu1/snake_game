from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Creates snake functionality for snake game """

    def __init__(self):
        self.segments = []
        self.segment_color = "white"

        self.create_snake()
        self.head = self.segments[0]
        pass

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        pass

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(self.segment_color)
        new_segment.penup()
        new_segment.setposition(position)
        self.segments.append(new_segment)

    def extend(self):
        # add new segment to snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
        return

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
