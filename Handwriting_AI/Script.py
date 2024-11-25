from PyQt5 import QtWidgets, QtGui, QtCore
import requests


class WeatherDashboard(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Window Configuration
        self.setWindowTitle("Weather Dashboard")
        self.setGeometry(100, 100, 400, 300)
        self.setStyleSheet("background-color: #2c2c2c; color: white; font-family: Arial;")
        
        # Layouts
        main_layout = QtWidgets.QVBoxLayout()
        
        # Search Bar
        search_layout = QtWidgets.QHBoxLayout()
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.setPlaceholderText("Search for your city...")
        self.search_bar.setStyleSheet("""
            padding: 8px; 
            font-size: 14px; 
            border: 1px solid #444; 
            border-radius: 5px;
            background-color: #3c3c3c; color: white;
        """)
        self.search_button = QtWidgets.QPushButton("Search")
        self.search_button.setStyleSheet("""
            padding: 8px 15px; 
            font-size: 14px; 
            background-color: #5c9bf5; 
            color: white; 
            border-radius: 5px;
        """)
        self.search_button.clicked.connect(self.fetch_weather)
        search_layout.addWidget(self.search_bar)
        search_layout.addWidget(self.search_button)

        # Weather Display
        self.city_label = QtWidgets.QLabel("City: -")
        self.city_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        self.date_label = QtWidgets.QLabel("Date: -")
        self.date_label.setStyleSheet("font-size: 14px; color: #aaaaaa;")

        self.weather_icon_placeholder = QtWidgets.QLabel()
        self.weather_icon_placeholder.setPixmap(QtGui.QPixmap("placeholder_icon.png").scaled(64, 64))  # Marker for icon replacement
        self.weather_icon_placeholder.setAlignment(QtCore.Qt.AlignCenter)

        self.temperature_label = QtWidgets.QLabel("Temperature: - °C")
        self.temperature_label.setStyleSheet("font-size: 32px; font-weight: bold;")

        self.description_label = QtWidgets.QLabel("Condition: -")
        self.description_label.setStyleSheet("font-size: 14px; color: #aaaaaa;")

        self.extra_details_label = QtWidgets.QLabel("Min: - °C | Max: - °C")
        self.extra_details_label.setStyleSheet("font-size: 14px; color: #aaaaaa;")

        # Add widgets to main layout
        main_layout.addLayout(search_layout)
        main_layout.addWidget(self.city_label, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.date_label, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.weather_icon_placeholder, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.temperature_label, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.description_label, alignment=QtCore.Qt.AlignCenter)
        main_layout.addWidget(self.extra_details_label, alignment=QtCore.Qt.AlignCenter)

        self.setLayout(main_layout)

    def fetch_weather(self):
        city = self.search_bar.text()
        if not city:
            QtWidgets.QMessageBox.warning(self, "Error", "Please enter a city name.")
            return

        # Replace with your OpenWeatherMap API key
        api_key = "023848bf787f0ebcdaebdcbe5efe97fb"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200:
                raise ValueError(data.get("message", "Failed to fetch weather data."))

            # Update UI with weather data
            self.city_label.setText(f"{data['name']}, {data['sys']['country']}")
            self.date_label.setText(QtCore.QDate.currentDate().toString("yyyy-MM-dd"))
            self.temperature_label.setText(f"{data['main']['temp']} °C")
            self.description_label.setText(data['weather'][0]['description'].capitalize())
            self.extra_details_label.setText(
                f"Min: {data['main']['temp_min']} °C | Max: {data['main']['temp_max']} °C"
            )

            # Update weather icon (placeholder for now)
            icon_code = data['weather'][0]['icon']
            icon_url = f"http://openweathermap.org/img/wn/{icon_code}@2x.png"
            icon_data = requests.get(icon_url).content
            pixmap = QtGui.QPixmap()
            pixmap.loadFromData(icon_data)
            self.weather_icon_placeholder.setPixmap(pixmap.scaled(64, 64))

        except Exception as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))


# Run the Application
app = QtWidgets.QApplication([])
window = WeatherDashboard()
window.show()
app.exec_()
