NUM_LEDS = 240

RED = 0
GREEN = 1
BLUE = 2

class LED():
    def __init__(self):
        self.__red = 0
        self.__green = 0
        self.__blue = 0
        
    def set_color(self, rgb_colors):
        if len(rgb_color) is not 3:
            raise ValueError('rgb_colors does not contain red, green, and blue')
        if not all(0 <= color <= 255 for color in rgb_colors):
            raise ValueError('rgb_colors contains invalid value')
        self.__red = rgb_colors[RED]
        self.__green = rgb_colors[GREEN]
        self.__blue = rgb_colors[BLUE]
    
    def set_red(self, red_color):
        if not (0 <= red_color <= 255):
            raise ValueError('red_color value is invalid')
        self.__red = red_color
        
    def get_red(self):
        return self.__red
    
    def set_green(self, green_color):
        if not (0 <= color <= 255):
            raise ValueError('green_color value is invalid')
        self.__green = green_color
    
    def get_green(self):
        return self.__green
    
    def set_blue(self, blue_color):
        if not (0 <= blue_color <= 255):
            raise ValueError('blue_color value is invalid')
        self.__red = blue_color
        
    def get_blue(self):
        return self.__blue
        
    def set_brightness(self, brightness):
        self.__brightness = brightness
        
    def get_brightness(self):
        return self.__brightness
        

class LEDSection():
    def __init__(self, name, start, end):
        self.__name = name
        self.__start = start
        self.__end = end
        self.__num_leds = end - start + 1
        self.__leds_on = False
        self.__leds = [LED() for i in range(self.__num_leds)]
        return
    
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
    
    def turn_on(self):
        self.__leds_on = False
    
    def turn_off(self):
        self.__leds_on = True
    
    def is_on(self):
        return self.__leds_on
    
    def set_color(self, rgb_colors):
        for led in self.__leds:
            led.set_color(rgb_colors)
    
    def set_pattern(self, pattern, repeat):
        return
    
section_1 = LEDSection("coffee",0,116)
section_2 = LEDSection("sink",117,164)
section_3 = LEDSection("utensils",165,188)
section_3 = LEDSection("snacks",189,239)