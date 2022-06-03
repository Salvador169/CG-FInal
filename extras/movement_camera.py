import math

from core_ext.object3d import Object3D


class MovementCamera(Object3D):
    """
    Add moving forwards and backwards, left and right, up and down (all local translations),
    as well as turning left and right, and looking up and down
    """
    def __init__(self, units_per_second=1, degrees_per_second=60):
        # Initialize base Object3D.
        # Controls movement and turn left/right.
        super().__init__()
        # Initialize attached Object3D; controls look up/down
        self._look_attachment = Object3D()
        self.children_list = [self._look_attachment]
        self._look_attachment.parent = self
        # Control rate of movement
        self._units_per_second = units_per_second
        self._degrees_per_second = degrees_per_second
        self.initial = self._look_attachment.local_matrix

        # Customizable key mappings.
        # Defaults: W, A, S, D, R, F (move), Q, E (turn), T, G (look)
        self.MAIN_PAGE = "z"
        self.INSTRUCTIONS = "2"
        self.WINNING = "3"
        self.GAMEOVER = "4"
        self.GAME = "5"
        self.isGame = False

    # Adding and removing objects applies to look attachment.
    # Override functions from the Object3D class.
    def add(self, child):
        self._look_attachment.add(child)
    def remove(self, child):
        self._look_attachment.remove(child)

    def Play(self):
        return self.isGame

    def setPlay(self, play):
        self.isGame = play

    def update(self, input_object, delta_time):
        if input_object.is_key_pressed(self.MAIN_PAGE):
            self.isGame = False
            self.set_position([10,0,80.75])
        if input_object.is_key_pressed(self.INSTRUCTIONS):
            self.isGame = False
            self.set_position([7.5,0,81])
        if input_object.is_key_pressed(self.GAMEOVER):
            self.isGame = False
            self.set_position([5,0,80.75])
        if input_object.is_key_pressed(self.WINNING):
            self.isGame = False
            self.set_position([2.5,0,80.75])
        if input_object.is_key_pressed(self.GAME):
            self.isGame = True
            self.set_position([0,0,0])