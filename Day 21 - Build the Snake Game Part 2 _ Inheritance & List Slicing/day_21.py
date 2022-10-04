# Defining Animal Class

class Animal:
    #Initializer
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, Exhale.")


# Defining Fish Class

class Fish(Animal):

    #Initializer
    def __init__(self):
        
        super().__init__()  # That's how Fish class can hold everything that Animal class holds. super().__init__ refers to super class

    def breathe(self):
        super().breathe()  # Everything that breath method from uper class do
        print("Doing this underwater.")  # Extra functionality of Fish class

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.breathe()
print(nemo.num_eyes)
