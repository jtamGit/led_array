let strip = neopixel.create(DigitalPin.P9, 24, NeoPixelMode.RGB)
strip.showColor(neopixel.colors(NeoPixelColors.Black))
basic.pause(1000)
strip.showRainbow(1, 360)
basic.pause(1000)
basic.forever(function () {
    strip.rotate(1)
    strip.show()
})
