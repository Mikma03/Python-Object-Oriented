# More on the Constructor/Initializer
class Car:
    # Class Attributes/Variables
    no_of_tires = 4
    # Class Constructor/Initializer (Method with a special name)
    def __init__(self, make, model, year, color, moon_roof=False):
        # Object Attributes/Variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False
    #  Methods
    def start_the_engine(self):
        self.engine_running = True
    def stop_the_engine(self):
        self.engine_running = False

def main():
    print("Hello from the main() method!")
if __name__ == '__main__':
    main()
