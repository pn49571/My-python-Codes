class Rocket():
    # Rocket simulates a rocket ship for a game,
    #  or a physics simulation.

    def __init__(self):
        # Each rocket has an (x,y) position.
        self.x = 0
        self.y = 0

    def move_up(self):
        # Increment the y-position of the rocket.
        self.y += 1

# Create a fleet of 5 rockets, and store them in a list.
my_rockets = []
for x in range(0,5):
    new_rocket = Rocket()
    my_rockets.append(new_rocket)

# Show that each rocket is a separate object.
for rocket in my_rockets:
    print(rocket)
