from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelangelo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow)
michelangelo.use_item(jack_sparrow)
jack_sparrow.attack(michelangelo)
jack_sparrow.show_stats()

