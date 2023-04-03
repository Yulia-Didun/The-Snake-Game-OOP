from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake_body()
        self.head = self.segments[0]

    def create_snake_body(self):
        """Creates the initial snake body with three segments at the start positions"""
        for position in START_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new segment to the snake at the given position"""
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("white")
        snake.setpos(x=position[0], y=position[1])
        self.segments.append(snake)

    def extend_snake(self):
        """Adds a new segment to the snake to make it longer"""
        next_segment_position = self.segments[-1].pos()
        self.add_segment(next_segment_position)

    def check_collision_with_wall(self):
        """Checks if the snake's head has collided with wall"""
        if self.head.xcor() > 290 or self.head.xcor() < -290:
            return True
        elif self.head.ycor() > 290 or self.head.ycor() < -290:
            return True
        return False

    def check_collision_with_tail(self):
        """Checks if the snake's head has collided with any of its segments"""
        for segment in self.segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def move(self):
        """Moves the snake forward by one segment length"""
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        """Changes the snake's heading to move up if it's not already moving down"""
        if self.head.heading() != 270:
            self.head.setheading(90)

    def move_down(self):
        """Changes the snake's heading to move down if it's not already moving up"""
        if self.head.heading() != 90:
            self.head.setheading(270)

    def move_left(self):
        """Changes the snake's heading to move left if it's not already moving right"""
        if self.head.heading() != 0:
            self.head.setheading(180)

    def move_right(self):
        """Changes the snake's heading to move right if it's not already moving left"""
        if self.head.heading() != 180:
            self.head.setheading(0)
