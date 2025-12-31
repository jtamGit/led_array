strip = neopixel.create(DigitalPin.P9, 24, NeoPixelMode.RGB)
strip.show_color(neopixel.colors(NeoPixelColors.BLACK))
basic.pause(1000)
strip.show_rainbow(1, 360)
basic.pause(1000)

def on_forever():
    strip.rotate(1)
    strip.show()
basic.forever(on_forever)


