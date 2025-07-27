from gym_cooking.utils.core import *


class Recipe:
    def __init__(self, name, length, bonus):
        self.name = name
        self.length = length
        self.bonus = bonus
        self.contents = []

    def __str__(self):
        return self.name

    def add_ingredient(self, item):
        self.contents.append(item)

    def add_goal(self):
        self.contents = sorted(self.contents, key = lambda x: x.name)   # list of Food objects
        self.contents_names = [c.full_name for c in self.contents]   # list of strings
        self.full_name = '-'.join(sorted(self.contents_names))   # string
        self.full_plate_name = '-'.join(sorted(self.contents_names + ['Plate']))   # string
        self.final_task = Object(location=None, contents=self.contents + [Plate()])

class LettuceTomatoSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'LettuceTomatoSoup', 40, 15)
        self.add_ingredient(Tomato(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_goal()

class OnionTomatoSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionTomatoSoup', 40, 15)
        self.add_ingredient(Onion(state_index=4))
        self.add_ingredient(Tomato(state_index=4))
        self.add_goal()

class OnionLettuceSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionLettuceSoup', 40, 15)
        self.add_ingredient(Onion(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_goal()

class BellpepperLettuceSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperLettuceSoup', 40, 15)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_goal()

class BellpepperOnionSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperOnionSoup', 40, 15)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Onion(state_index=4))
        self.add_goal()

class BellpepperTomatoSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperTomatoSoup', 40, 15)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Tomato(state_index=4))
        self.add_goal()

class TLOSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Tomato(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_ingredient(Onion(state_index=4))
        self.add_goal()

class BOLSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_ingredient(Onion(state_index=4))
        self.add_goal()

class BOTSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Onion(state_index=4))
        self.add_ingredient(Tomato(state_index=4))
        self.add_goal()

class BLTSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_ingredient(Tomato(state_index=4))
        self.add_goal()

class LettuceTomatoGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'TomatoLettuceGrill', 40, 15)
        self.add_ingredient(Tomato(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_goal()

class OnionTomatoGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionTomatoGrill', 40, 15)
        self.add_ingredient(Onion(state_index=6))
        self.add_ingredient(Tomato(state_index=6))
        self.add_goal()

class OnionLettuceGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionLettuceGrill', 50, 15)
        self.add_ingredient(Onion(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_goal()


class BellpepperLettuceGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperLettuceGrill', 40, 15)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_goal()

class BellpepperOnionGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperOnionGrill', 40, 15)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Onion(state_index=6))
        self.add_goal()

class BellpepperTomatoGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'BellpepperTomatoGrill', 40, 15)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Tomato(state_index=6))
        self.add_goal()


class TLOGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullGrill', 50, 20)
        self.add_ingredient(Tomato(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_ingredient(Onion(state_index=6))
        self.add_goal()


class BOLGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_ingredient(Onion(state_index=6))
        self.add_goal()

class BOTGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Onion(state_index=6))
        self.add_ingredient(Tomato(state_index=6))
        self.add_goal()

class BLTGrill(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'FullSoup', 50, 20)
        self.add_ingredient(Bellpepper(state_index=6))
        self.add_ingredient(Lettuce(state_index=6))
        self.add_ingredient(Tomato(state_index=6))
        self.add_goal()



class TLSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'LettuceTomatoSoup', 50, 15)
        self.add_ingredient(Tomato(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_goal()

class OTSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionTomatoSoup', 50, 15)
        self.add_ingredient(Onion(state_index=4))
        self.add_ingredient(Tomato(state_index=4))
        self.add_goal()

class OLSoup(Recipe):
    def __init__(self):
        Recipe.__init__(self, 'OnionLettuceSoup', 50, 15)
        self.add_ingredient(Onion(state_index=4))
        self.add_ingredient(Lettuce(state_index=4))
        self.add_goal()