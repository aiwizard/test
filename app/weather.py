'''
https://allhpy35.tistory.com/15
'''


import tkinter as tk
from tkinter import font
import requests


Height = 500
Width = 700

def test_function(entry):
    print('button clicked :',entry)


def get_weather(city):
    weather_key = '본인의 apikey'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q':city, 'units':'Metric'}
    response = requests.get(url, params = params)
    weather = response.json()
    label['text'] = format_response(weather)
    

def format_response(weather):
    try:
        name = weather['name']
        dec = weather['weather'][0]['description']
        temper= weather['main']['temp']

        final_str =  '도시: %s \n날씨: %s \n온도:(C)%s' %(name,dec,temper)
    except:
        final_str = 'Ther was a problem retrieving that information'


    return final_str

# http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={APIKEY}
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

    

root = tk.Tk()

canvas = tk.Canvas(root, height=Height, width =Width)
canvas.pack()

background_image = tk.PhotoImage(file='image_1529034574120_750.png')
background_label = tk.Label(root,image= background_image)

background_label.place(x= 0, y =0, relwidth=1, relheight=1)


frame = tk.Frame(root,bg='#80c1ff',bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1,anchor='n')

button = tk.Button(frame, text ='Search',font=40, command=lambda: get_weather(entry.get())) 
button.place(relx=0.7, relwidth=0.3, relheight=1)


entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)



lower_frame = tk.Frame(root, bg='#80c1ff',bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75,relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=("휴먼매직체",18) )
label.place( relwidth=1, relheight=1)


#print(tk.font.families())



root.mainloop()

