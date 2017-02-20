from helper import greetings, welcome_place
from places import PLACES
from names import NAMES

greetings("hello")

for place in PLACES:
   welcome_place(place)

for name in NAMES:
   greetings(name)
