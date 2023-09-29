"""
In general, a sequence pattern matches the subject if:
1. The subject is a sequence and;
2. The subject and the pattern have the same number of items and;
3. Each corresponding item matches, including nested items.

NOTE: for sequence pattern the () and [] are the same thing.
"""
from amqp import InvalidCommand

metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]


def main():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [str(name), str(), _, (float(lat), lon) as coord] if lon <= 0:
                print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
                print(coord)  # you can bind any part of a pattern with a variable using the as keyword

"""
    the pattern [name, _, _, (lat, lon)] matches a sequence with four items,
    and the last item must be a two-item sequence.
    
    the second item checks the 2nd must be a str
    
    the str(name) and float(lat) indicate that the name must be str and the lat must be float.
    
    The optional guard clause starting with if is evaluated only if the pattern matches,
    and can reference variables bound in the pattern
"""

# -------------------------------------------------------------------------------------------------
def handle_command(self, message):
    match message:
        case ['BEEPER', frequency, times]:
            self.beep(times, frequency)
        case ['NECK', angle]:
            self.rotate_neck(angle)
        case ['LED', ident, intensity]:
            self.leds[ident].set_brightness(ident, intensity)
        case ['LED', ident, red, green, blue]:
            self.leds[ident].set_color(ident, red, green, blue)
        case _:
            raise InvalidCommand(message)

"""
The expression after the match keyword is the subject. The subject is the data that
Python will try to match to the patterns in each case clause.

This pattern matches any subject that is a sequence with three items. The first
item must be the string 'BEEPER'. The second and third item can be anything,
and they will be bound to the variables frequency and times, in that order.

This matches any subject with two items, the first being 'NECK'.

This will match a subject with three items starting with 'LED'. If the number of
items does not match, Python proceeds to the next case.

Another sequence pattern starting with 'LED', now with five items—including
the 'LED' constant.

This is the default case. It will match any subject that did not match a previous
pattern. The _ variable is special
"""
