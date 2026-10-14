import streamlit as st
import requests as req
from dotenv import load_dotenv
import os
API_KEY = os.getenv('WEATHER_API_KEY')
st.set_page_config(page_title='weather app', page_icon='🌦️')


st.title('weather app🌧️')
 
st.write('enter the city name and click to procced ')

city=st.text_input('enter city name')

if(st.button('fetch weather')):

    response  = req.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric')
    if(response.status_code == 200):
        st.success('weather data fetched succuessfully')
        data=(response.json())
        print(data)
        #extract weather information
        temperature  = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        weather_conditions =data['weather'][0]['description']
        name = data['name']
        country = data['sys']['country']

        st.subheader(f'{name},{country}')


        #create 2 columns
        col1, col2 = st.columns(2)
        col3, col4 =st.columns(2)
        col1.metric('temperature🌡️', f'{temperature} °C')
        col2.metric('Humidity💦',f'{humidity}%')
        col3.metric('Wind speed💨💨', f'{wind_speed}m/s')
        col4.metric('weather conditions🌤️', f'{weather_conditions}')
    else:
        st.error('city not found')