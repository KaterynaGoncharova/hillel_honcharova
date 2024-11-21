class Rhombus:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                raise ValueError ("The length of the side of the diamond must be greater than 0")
            super().__setattr__(name, value)

        elif name == "angle_a":
            if not (0 < value < 180):
                raise ValueError ("The angle should be between 0 and 180 degrees")
            super().__setattr__(name, value)
            super().__setattr__("angle_b" , 180 - value)

        elif name == "angle_b":
            raise ValueError("You need to specify angle a, angle b is adjacent")

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Rhombus with side {self.side_a}, and angles a = {self.angle_a}, b = {self.angle_b}"

try:
    rhombus = Rhombus(5, 90)
    print(rhombus)

except ValueError as e:
    print(e)







