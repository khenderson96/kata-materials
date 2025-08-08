import sys

class Submarine:
    def __init__(self, exercise: int):
        self.x = 0
        self.y = 0
        self.exercise = exercise
        if self.exercise == 1:
            self.forward = self.forward1
            self.up = self.up1
            self.down = self.down1
        elif self.exercise == 2:
            self.forward = self.forward2
            self.up = self.up2
            self.down = self.down2
            self.aim = 0
        else:
            print("Invalid exercise number. Must be 1 or 2.")
            sys.exit(1)

    def __repr__(self) -> str:
        if self.exercise == 1:
            return f"(x:{self.x}, y:{self.y})"
        elif self.exercise == 2:
            return f"(x:{self.x}, y:{self.y}, a:{self.aim})"

    def forward1(self, value: int):
        self.x += value

    def up1(self, value: int):
        self.y -= value

    def down1(self, value: int):
        self.y += value

    def forward2(self, value: int):
        self.x += value
        self.y += (self.aim * value)

    def up2(self, value: int):
        self.aim -= value

    def down2(self, value: int):
        self.aim += value

class SubmarineParent:
    def __init__(self):
        self.x = 0
        self.y = 0

    def forward(self, value: int):
        pass

    def up(self, value: int):
        pass

    def down(self, value: int):
        pass

class SubmarineEx1(SubmarineParent):
    def __init__(self):
        super().__init__()

    def forward(self, value: int):
        self.x += value

    def up(self, value: int):
        self.y -= value

    def down(self, value: int):
        self.y += value

    def __repr__(self) -> str:
        return f"(x:{self.x}, y:{self.y})"

class SubmarineEx2(SubmarineParent):
    def __init__(self):
        super().__init__()
        self.aim = 0

    def forward(self, value: int):
        self.x += value
        self.y += (self.aim * value)

    def up(self, value: int):
        self.aim -= value

    def down(self, value: int):
        self.aim += value


    def __repr__(self) -> str:
        return f"(x:{self.x}, y:{self.y}, a:{self.aim})"

if __name__ == "__main__":

    sub1 = Submarine(1)
    sub1.forward(5)
    sub1.down(3)
    sub1.up(3)
    print(sub1)

    sub2 = Submarine(2)
    sub2.forward(5)
    sub2.down(3)
    sub2.up(3)
    print(sub2)

    sub1_ex1 = SubmarineEx1()
    sub2.forward(5)
    sub2.down(3)
    sub2.up(3)
    print(sub1_ex1)

    sub2_ex2 = SubmarineEx2()
    sub2_ex2.forward(5)
    sub2_ex2.down(3)
    sub2_ex2.up(3)
    print(sub2_ex2)