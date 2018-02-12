from urllib.request import urlopen
from xml.etree.ElementTree import parse
import time

# Download the RSS feed and parse it
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'
WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

def parseXml(URL):
    rss = parse(urlopen(URL)).getroot()
    location = {}
    data = {}
    forecast = []

    elment = rss.find('results/channel/{'+'{0}'.format(WEATHER_NS)+'}location')
    location['city'] = elment.get('city')

    elment = rss.findall('results/channel/item/{'+'{0}'.format(WEATHER_NS)+'}forecast')
    for x in elment:
        data['date'] = time.strftime('%Y-%m-%d',time.strptime(x.get('date'),'%d %b %Y'))
        data['high'] = x.get('high')
        data['low'] = x.get('low')
        forecast.append(data)
    return {'city': location['city'],
            'forecast': forecast}

result = parseXml(URL)
assert result['city'] == 'Beijing'
print('ok')