#Weather Forecast Application - Python

#Necessary Modules
import requests
import bs4 as bs
import datetime
import sys

#Dictionary to store the Weather Details. Date as Keys and details as the value stored as a list.
weather_details = {}

#Current Date
curr_date = datetime.datetime.now().strftime("%d-%b-%Y")
date_1 = datetime.datetime.strptime(curr_date, "%d-%b-%Y")

#Using a browser Agent
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"}
area = input('Enter a Indian Location: ').strip().lower()

#Getting the webpage of the URL
url = 'https://www.timeanddate.com/weather/india/' + area + '/ext'
response = requests.get(url, headers = headers)
html = response.text

#Extracting the necessary information
soup = bs.BeautifulSoup(html, 'lxml')
temp = soup.find('tbody')

#Looping and extracting the Information about weather.
for i in range(3):
    end_date = date_1 + datetime.timedelta(days=i)
    try:
        temperature = temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(2)").text
        weather_details[end_date.strftime("%d-%b-%Y")] = [temperature]
        weather_details[end_date.strftime("%d-%b-%Y")].append(temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(3)").text)
        weather_details[end_date.strftime("%d-%b-%Y")].append(temp.select_one("tr:nth-of-type(" + str(i+1) + ")").select_one("td:nth-of-type(4)").text)
    except AttributeError:
        print('Invalid Location. Please Enter a popular location.')
        sys.exit(8)


print('Weather Forecast for {}'.format(area.title()))
print('-'*35)
for i in weather_details:
    print(i, *weather_details[i])





