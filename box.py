from tttexceptions import TTTExceptions

class UnknownStateException(TTTExceptions):
    "Raised When the state of a box is not within the 3 known states"
    pass

class box:

    def __init__(self, state: int):
        """
        When state is 0, it is empty
        When state is 1, it is marked by an X
        When state is 2, it is marked by an O
        """
        self.state = state

    @property
    def state(self):
        return self.__state
    
    @state.setter
    def state(self, state: int):
        if state not in [0, 1, 2]:
            raise UnknownStateException
        else:
            self.__state = state