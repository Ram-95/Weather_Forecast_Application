#Weather Forecast Application - Python

#Necessary Modules
from prettytable import PrettyTable
import requests
import bs4 as bs
import datetime
import sys
import Balloon_tip as Bt

#Dictionary to store the Weather Details. Date as Keys and details as the value stored as a list.
weather_details = {}

#Current Date
curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
date_1 = datetime.datetime.strptime(curr_date, "%d-%b-%Y")

#Using a browser Agent
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
area = input('Enter an Indian Location: ').strip().lower()
time_period = int(input('Enter the No. of Days [1-14]: '))
time_period = 3 if time_period <= 0 or time_period > 14 else time_period

#Getting the webpage of the URL
url = 'https://www.timeanddate.com/weather/india/' + area + '/ext'
response = requests.get(url, headers = headers)
html = response.text

#Extracting the necessary information
soup = bs.BeautifulSoup(html, 'lxml')
temp = soup.find('tbody')

#Looping and extracting the Information about weather.
for i in range(time_period):
    end_date = date_1 + datetime.timedelta(days=i)
    try:
        temperature = temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(2)").text
        weather_details[end_date.strftime("%d-%b-%Y")] = [temperature]
        weather_details[end_date.strftime("%d-%b-%Y")].append(temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(3)").text)
        weather_details[end_date.strftime("%d-%b-%Y")].append(temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(4)").text)
    except AttributeError:
        print('Weather Forecast NOT AVAILABLE for this Location. Please Enter a popular location.')
        sys.exit(8)

#Putting the data into a PrettyTable table
print('\n{}-Day Weather Forecast for {}:'.format(time_period, area.title()))
table = PrettyTable(['Date', 'Max/Min Temp.', 'Weather Conditions', 'Feels Like'])
for i in weather_details:
    table.add_row([i, *weather_details[i]])


print(table)

#This Part of code is used to show a desktop notification. It only shows the current day weather for the choosen location.
'''
Bt.balloon_tip('Weather Update - ' + area.title(),'Min/Max Temp: {}\nWeather: {}\nFeels Like: {}'
               .format(weather_details[curr_date][0], weather_details[curr_date][1],weather_details[curr_date][2]))

'''
