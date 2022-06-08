import random
from classes.ninja import Ninja
from classes.pirate import Pirate

print(random.randint(0, 1))

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
#michelangelo.use_item(jack_sparrow)
jack_sparrow.use_item(michelangelo)
jack_sparrow.attack(michelangelo)
jack_sparrow.show_stats()

