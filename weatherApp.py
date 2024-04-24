# import required modules 
from configparser import ConfigParser 
import requests 
from tkinter import *
from tkinter import messagebox 

# extract key from the 
# configuration file 
config_file = "config.ini"
config = ConfigParser() 
config.read(config_file) 
api_key = config['gfg']['api'] 
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'


# explicit function to get 
# weather details 
def getweather(city): 
	result = requests.get(url.format(city, api_key)) 
	
	if result: 
		json = result.json() 
		city = json['name'] 
		country = json['sys'] 
		temp_kelvin = json['main']['temp'] 
		temp_celsius = temp_kelvin-273.15
		weather1 = json['weather'][0]['main'] 
		final = [city, country, temp_kelvin, 
				temp_celsius, weather1] 
		return final 
	else: 
		print("NO Content Found") 


# explicit function to 
# search city 
def search(): 
	city = city_text.get() 
	weather = getweather(city) 
	print(weather)
	if weather: 
		city_label.config(text="City : " + str(weather[0]))
		country_label.config(text="Country : " + str(weather[1]['country']))
		atmospheric_condition.config(text="Atmospheric Condition : " + str(weather[4]))
		temperature_label.config(text=str(round(weather[3], 2)) + " Degree Celsius")
	else: 
		messagebox.showerror('Error', "Cannot find {}".format(city)) 


# Driver Code 
# create object 
app = Tk() 
# add title 
app.title("Weather App") 
# adjust window size 
app.geometry("300x300") 

# add labels, buttons and text 
city_text = StringVar() 
city_entry = Entry(app, textvariable=city_text) 
city_entry.pack() 
Search_btn = Button(app, text="Search Weather", 
					width=12, command=search) 
Search_btn.pack() 

city_label = Label(app, text="")
city_label.pack()
country_label = Label(app, text="")
country_label.pack()
atmospheric_condition  = Label(app, text="")
atmospheric_condition.pack()


temperature_label = Label(app, text="") 
temperature_label.pack() 

weather_l = Label(app, text="") 
weather_l.pack() 

app.mainloop() 
