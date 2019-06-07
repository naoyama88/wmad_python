class Bottle:

    _amount_in_bedroom = 0

    def __init__(self, ml, color, label_color, bottle_color, is_open):
        Bottle._amount_in_bedroom += 1
        self._ml = ml
        self._color = color
        self._label_color = label_color
        self._bottle_color = bottle_color
        self._is_open = is_open

    def get_ml(self):
        return self._ml

    def get_color(self):
        return self._color

    def get_label_color(self):
        return self._label_color

    def get_bottle_color(self):
        return self._bottle_color

    def get_open(self):
        return self._is_open

    def set_ml(self, ml):
        self._ml = ml

    def set_color(self, color):
        self._color = color

    def set_label_color(self, label_color):
        self._label_color = label_color

    def set_bottle_color(self, bottle_color):
        self._bottle_color = bottle_color

    def set_open(self, is_open):
        self._is_open = is_open

    def open(self):
        self.set_open(True)

    def drink(self, ml):
        self._ml = self._ml - ml


class Fan:

    _amount_in_bedroom = 0

    def __init__(self, blades_number, color, height, angle, is_power_on):
        Fan._amount_in_bedroom += 1
        self._blades_number = blades_number
        self._color = color
        self._height = height
        self._angle = angle
        self._is_power_on = is_power_on

    def get_blades_number(self):
        return self._blades_number

    def get_color(self):
        return self._color

    def get_height(self):
        return self._height

    def get_angle(self):
        return self._angle

    def get_is_power_on(self):
        return self._is_power_on

    def set_blades_number(self, blades_number):
        self._blades_number = blades_number

    def set_color(self, color):
        self._color = color

    def set_height(self, height):
        self._height = height

    def set_angle(self, angle):
        self._angle = angle

    def set_is_power_on(self, is_power_on):
        self._is_power_on = is_power_on

    def power_on(self):
        self.set_is_power_on(True)

    def power_off(self):
        self.set_is_power_on(False)


class Bed:

    _amount_in_bedroom = 0

    def __init__(self):
        Bed._amount_in_bedroom += 1
        self._width = 100
        self._vertical = 180
        self._height = 50
        self._sheets_color = 'white'
        self._is_dirty = False

    def get_width(self):
        return self._width

    def get_vertical(self):
        return self._vertical

    def get_height(self):
        return self._height

    def get_sheets_color(self):
        return self._sheets_color

    def get_is_dirty(self):
        return self._is_dirty

    def set_width(self, width):
        self._width = width

    def set_vertical(self, vertical):
        self._vertical = vertical

    def set_height(self, height):
        self._height = height

    def set_sheets_color(self, sheets_color):
        self._sheets_color = sheets_color

    def set_is_dirty(self, is_dirty):
        self._is_dirty = is_dirty

    def change_sheets(self):
        self.set_is_dirty(False)

    def change_sheets_color(self, color):
        self.set_sheets_color(color)


class Tv:

    _amount_in_bedroom = 0

    def __init__(self):
        Tv._amount_in_bedroom += 1
        self._inch = 32
        self._color = 'black'
        self._brand = 'LG'
        self._channel = 1
        self._is_power_on = False

    def get_inch(self):
        return self._inch

    def get_color(self):
        return self._color

    def get_brand(self):
        return self._brand

    def get_channel(self):
        return self._channel

    def get_is_power_on(self):
        return self._is_power_on

    def set_inch(self, inch):
        self._inch = inch

    def set_color(self, color):
        self._color = color

    def set_brand(self, brand):
        self._brand = brand

    def set_channel(self, channel):
        self._channel = channel

    def set_is_power_on(self, is_power_on):
        self._is_power_on = is_power_on

    def next_channel(self):
        self.set_channel(self.get_channel() + 1)

    def paint_color(self, color):
        self._color = color


class Charger:

    _amount_in_bedroom = 0

    def __init__(self):
        Charger._amount_in_bedroom += 1
        self._length = 200
        self._color = 'black'
        self._connector = 'type-c'
        self._is_charging = False
        self._is_broken = False

    def get_length(self):
        return self._length

    def get_color(self):
        return self._color

    def get_connector(self):
        return self._connector

    def get_is_charging(self):
        return self._is_charging

    def get_is_broken(self):
        return self._is_broken

    def set_length(self, length):
        self._length = length

    def set_color(self, color):
        self._color = color

    def set_connector(self, connector):
        self._connector = connector

    def set_is_charging(self, is_charging):
        self._is_charging = is_charging

    def set_is_broken(self, is_broken):
        self._is_broken = is_broken

    def connect(self, connector):
        if self.get_connector() != connector:
            print("it's not fit for this connector")
        else:
            self.set_is_charging(True)

    def check(self):
        if self.get_is_broken():
            print('This charger is broken')
        else:
            print('This charger is not broken')

