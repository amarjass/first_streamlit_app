import pip
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
#first text box
streamlit.header('Fruityvice Fruit  Advice!')

fruit_choice = streamlit.text_input('What fruit would you like information about?', 'Kiwi')
streamlit.write('The user entered ', fruit_choice)


import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.text(fruityvice_response.json())  # just writes the data on the screen


#take the json version of the response  and normalized it.
fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())

#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)


#New Section to display Fruityvice api response 
#Second  text box
streamlit.header('Fruityvice Fruit   2 Advice!')

fruit_choice2 = streamlit.text_input('What fruit would you like information about?', 'apple')
streamlit.write('The user entered ', fruit_choice2)
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)



import snowflake.connector
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_rows = my_cur.fetchall()
#my_data_row = my_cur.fetchone()
#streamlit.text("the fruit load list contains")
streamlit.header("the fruit load list contains")
# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
#streamlit.dataframe(my_data_row)
streamlit.dataframe(my_data_rows)
