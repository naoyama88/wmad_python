from problem00 import *


def main():
    bottle = Bottle(500, 'transparent', 'white', 'green', False)
    print('ml', bottle.get_ml())
    print('color', bottle.get_color())
    print('bottle color', bottle.get_bottle_color())
    print('bottle label color', bottle.get_label_color())
    print('is opened?', bottle.get_open())
    print('open bottle')
    bottle.open()
    print('is opened?', bottle.get_open())
    print('drink 200ml')
    bottle.drink(200)
    print('ml', bottle.get_ml())

    print()

    fan = Fan(3, 'black', 120, 90, False)
    print('how many blades', fan.get_blades_number())
    print('color', fan.get_color())
    print('height', fan.get_height())
    print('angle', fan.get_angle())
    print('power on?', fan.get_is_power_on())
    print('power on')
    fan.power_on()
    print('power on?', fan.get_is_power_on())
    print('power off')
    fan.power_off()
    print('power on?', fan.get_is_power_on())

    print()

    bed = Bed()
    print('width', bed.get_width())
    print('height', bed.get_height())
    print('vertical', bed.get_vertical())
    print('sheets color', bed.get_sheets_color())
    print('is sheets dirty?', bed.get_is_dirty())
    print('change sheets color')
    bed.change_sheets_color('black')
    print('sheets color', bed.get_sheets_color())
    print('make sheets dirty')
    bed.set_is_dirty(True)
    print('is sheets dirty?', bed.get_is_dirty())
    print('change sheets')
    bed.change_sheets()
    print('is sheets dirty?', bed.get_is_dirty())

    print()

    tv = Tv()
    print('inch', tv.get_inch())
    print('color', tv.get_color())
    print('channel', tv.get_channel())
    print('brand', tv.get_brand())
    print('is power on?', tv.get_is_power_on())
    print('next channel')
    tv.next_channel()
    print('channel', tv.get_channel())
    print('paint tv color')
    tv.paint_color('red')
    print('color', tv.get_color())

    print()

    charger = Charger()
    print('color', charger.get_color())
    print('length', charger.get_length())
    print('is it broken?', charger.get_is_broken())
    print('what type of connector', charger.get_connector())
    print('is it charging?', charger.get_is_charging())
    print('connect with type-c')
    charger.connect('type-c')
    print('is it charging?', charger.get_is_charging())
    print('connect with lightning')
    charger.connect('lightning')
    print('is it charging?', charger.get_is_charging())
    print('let\'s check')
    charger.check()
    print('make it broken')
    charger.set_is_broken(True)
    print('let\'s check')
    charger.check()


main()
