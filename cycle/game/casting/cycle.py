import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Cycle(Actor):
    """
    A long limbless reptile.
    
    The responsibility of Snake is to move itself.
    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self,position):
        super().__init__()
        self._segments = []
        self._position = position
        self._prepare_body()


    def get_segments(self):
        """Creating the segments """
        return self._segments

    def move_next(self):
        """move all segments"""
        for segment in self._segments:
            segment.move_next()
        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        """Creating the Heads"""
        return self._segments[0]

    def grow_tail(self, number_of_segments):
        """Growing the tail of the cycle"""
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(self._color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        """To turn the cycles's head"""
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        """Preparing th body of the snakes"""
        x = self._position.get_x()
        y = self._position.get_y()

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x, y+ i * constants.CELL_SIZE)
            velocity = Point(0,-1 * constants.CELL_SIZE)
            text = "@" if i == 0 else "#"
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(self._color)
            self._segments.append(segment)
    
    def set_color(self, color):
        """Setting the color of the snakes"""
        self._color = color
        for segment in self._segments:
            segment.set_color(color)
    