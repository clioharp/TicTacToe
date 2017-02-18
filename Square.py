class Square:
    x, y = 0, 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_input(cls, input_string):
        if not len(input_string) == 3:
            raise(ValueError('Input should be of form: x,y'))
        x_coord = input_string[0]
        y_coord = input_string[2]

        try:
            cls.x = int(x_coord)
            cls.y = int(y_coord)
        except ValueError:
            raise ValueError('Input should be of form: x,y')

        return cls
