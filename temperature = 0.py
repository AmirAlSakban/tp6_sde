temperature = 0
luminozitate = 0
umiditate = 0

def on_button_pressed_a():
    global temperature
    temperature = input.temperature()
    basic.show_number(temperature)
    while input.temperature() <= 10:
        basic.show_string("mutati planta la caldura")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global luminozitate
    luminozitate = input.light_level()
    basic.show_number(luminozitate)
    while luminozitate <= 120:
        basic.show_string("mutati planta la lumina")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_pressed():
    while True:
        if umiditate < 60:
            basic.show_string("planta este in curs de udare")
        break
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_forever():
    pass
basic.forever(on_forever)

def on_every_interval():
    global umiditate
    umiditate = randint(0, 100)
    while True:
        if umiditate < 60:
            basic.show_string("uda planta")
        break
loops.every_interval(120000, on_every_interval)
