from urllib import request, parse
from xml.parsers.expat import ParserCreate
import re

def fetch_xml(url):
    with request.urlopen(url) as f:
        html=f.read()
        return handlerWeather(html)
result_Weather={}
class WeatherSaxHandler(object):
    def start_element(self,name,attrs):
        if name=='yweather:location':
            result_Weather['city']=attrs['city']
            result_Weather['country']=attrs['country']

        if name=='yweather:condition':
            self.today=int(re.split(r'[\s\,]+',attrs['date'])[1])

        if name=='yweather:forecast':
            if int(re.split(r'[\s\,]+',attrs['date'])[0])==self.today:
                Weather = {}
                Weather['text']=attrs['text']
                Weather['low'] = int(attrs['low'])
                Weather['high'] = int(attrs['high'])
                result_Weather['today']=Weather
            if int(re.split(r'[\s\,]+', attrs['date'])[0]) == self.today+1:
                Weather = {}
                Weather['text'] = attrs['text']
                Weather['low'] = int(attrs['low'])
                Weather['high'] = int(attrs['high'])
                result_Weather['tomorrow'] = Weather

    def end_element(self,name):
        pass
    def char_data(self,data):
        pass

def handlerWeather(xml):
    handler = WeatherSaxHandler()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml)
    #print(result_Weather)
    return result_Weather


print(fetch_xml('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22Beijing%2C%20ak%22)&format=xml&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys'))