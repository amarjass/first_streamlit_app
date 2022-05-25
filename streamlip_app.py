import streamlit
streamlit.title("My parent now healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
import pandas
my_fruit_list=pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
#streamlit.dataframe(my_fruit_list)



# lets put a pick list here so they can pick the fruits they want to include
#streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_selected= streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the page 
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

#New Section to display Fruityvice api response
streamlit.header('Fruityvice Fruit  Advice!')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


#take the json version of the response  and normalized it.
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)


