from box import box

class grid:

    def __init__(self, number_of_rows: int):
        self.__n = number_of_rows
        self.the_grid = self.og_grid()
    
    @property
    def size(self):
        return (self.__n, self.__n)
    
    def og_grid(self):
        return [[box(0) for _ in range(self.size[0])] for __ in range(self.size[1])]
    
    def __iter__(self):
        pass
