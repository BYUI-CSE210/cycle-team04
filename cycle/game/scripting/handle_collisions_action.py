import constants
from game.casting.actor import Actor                                       
from game.scripting.action import Action
from game.shared.point import Point
from game.casting.score1 import Score1
from game.casting.score2 import Score2


class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.

    The responsibility of HandleCollisionsAction is to handle the situation when a snake collides with its segments and the segments of the other snake, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False


    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if a snake collides with its segments or the segments of the other snake.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        score1 = cast.get_first_actor("score1")
        score2 = cast.get_first_actor("score2")
        all_cycles = cast.get_actors("cycles")
        cycle1 = cast.get_actors("cycles")[0]
        cycle2 = cast.get_actors("cycles")[1]
        segments_1 = []
        segments_2 = []
        heads = []
        for cycle in all_cycles:
            heads.append(cycle.get_segments()[0])
            segments_1 += cycle1.get_segments()[1:]
            segments_2 += cycle2.get_segments()[1:]
       
        for segment1 in segments_1:
            for head in heads:
                if head.get_position().equals(segment1.get_position()):
                    self._is_game_over = True
                    score2.add_points(1)
               
                    

        for segment2 in segments_2:
            for head in heads:
                if head.get_position().equals(segment2.get_position()):
                    self._is_game_over = True
                    score1.add_points(1)
               
                    
                    
                    
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snakes white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            for cycle in cast.get_actors("cycles"):
                cycle.set_color(constants.WHITE)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

      