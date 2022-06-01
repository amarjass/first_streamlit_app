import pip
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My parent now healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
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

############################# Using try and except block
#New Section to display Fruityvice api response 
#first text box
#streamlit.header('Fruityvice Fruit  Advice!')
#try:
# fruit_choice = streamlit.text_input('What fruit would you like information about?')
#  if not fruit_choice:
#      streamlit.error("Please select a fruit to get information")
#  else:
#      fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#      #take the json version of the response  and normalized it.
#      fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
#      #output it to the screen as a table
#      streamlit.dataframe(fruityvice_normalized)
    
#except URLError as e:
#  streamlit.error()
  
  ############################# Using try and except block end
  
  ##Function block started
#create a repeatable code block
def get_fruitvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    #take the json version of the response  and normalized it.
    fruityvice_normalized=pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized
  
#New Section to display Fruityvice api response 
#first text box
streamlit.header('Fruityvice Fruit  Advice!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
  else:
      back_from_function = get_fruitvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      
    

      
      
        
# streamlit.write('The user entered ', fruit_choice)


#import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.text(fruityvice_response.json())  # just writes the data on the screen




#output it to the screen as a table
#streamlit.dataframe(fruityvice_normalized)


