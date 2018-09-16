from flask import Flask
from phue import Bridge
import random
import socket
import requests

app = Flask(__name__)
bridge = Bridge('192.168.86.110')
bridge.connect()
#print(bridge.get_api())

@app.route('/')
def index():
    return 'Hello world'

@app.route('/counter-lights-off', methods=['GET','POST'])
def turn_coutner_ligths_off():
    print('Turning the counter lights off')
    led_setting={"red":0, "green":0, "blue":0}
    r = requests.post("http://192.168.86.130", json=dict(led_setting))
    return 'Turned the counter lights off'

@app.route('/counter-lights-on', methods=['GET','POST'])
def turn_counter_lights_on():
    print('Turning the counter lights on')
    led_setting={"red":255, "green":180, "blue":40}
    r = requests.post("http://192.168.86.130", json=dict(led_setting))
    return 'Turned the counter lights on'

@app.route('/test', methods=['POST'])
def test():
    lights = bridge.get_light_objects()
    for light in lights:
        light.brightness = 254
        light.xy = [random.random(),random.random()]
    return 'Testing testing'

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0', port=int('80'))
