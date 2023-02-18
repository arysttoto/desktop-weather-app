import lxml
import requests
from bs4 import BeautifulSoup
from ui import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets


weather_token = '{{ encrypted }}'
code_to_condition = {
    'Clear': 'Clear \U00002600',
    'Clouds': 'Cloudy \U00002601',
    'Rain': 'Rainy \U00002614',
    'Drizzle': 'Rainy \U00002614',
    'Thunderstorm': 'Thunderstorm \U000026A1',
    'Snow': 'Snowy \U0001F32B',
    'Mist': 'Mist \U0001F32B'
}

class GetWeather(QtWidgets.QMainWindow):
    def __init__(self):
        super(GetWeather, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.detect_getting()
    def detect_getting(self):
        self.setWindowTitle('Weather Now')
        self.ui.pushButton.clicked.connect(self.start_getting)
    def start_getting(self):
        city = self.ui.comboBox.currentText()
        self.ui.label_5.setText(f'Weather in {city}')
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
        data = r.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        condition = data['weather'][0]['main']
        condition = code_to_condition[condition]
        visibility = int(data['visibility'])/1000
        self.ui.label_3.setText(f"It's {condition}\n"
                                f"The temperature is {temperature}°C\n"
                                f"Wind speed is {wind}m/s")
        self.ui.label_4.setText(f"Pressure is {pressure}\n"
                                f"Visibility is {visibility}km\n"
                                f"Humidity is {humidity}")
        


app = QtWidgets.QApplication([])
window = GetWeather()
window.show()
app.exec()

