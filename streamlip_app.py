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
except URLError as e:      
   streamlit.error() 

 ############### Function end
    
streamlit.header("the fruit load list contains")
    ################### snowflake-related function   
 def get_fruit_load_list():
     with my_cnx.cursor() as my_cur
          my_cur.execute("select * from fruit_load_list")
          return my_cur.fetchall()
 # add a button to load the fruits
 if streamlit.button('Get Fruit load list'):
    my_cur = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_list()
    streamlit.dataframe(my_data_rows)
    
 ###############Snowflake function end###########
    
    
    
    
    
        
# streamlit.write('The user entered ', fruit_choice)


#import requests
# fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + "Kiwi")

#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)

#streamlit.text(fruityvice_response.json())  # just writes the data on the screen




#output it to the screen as a table
#streamlit.dataframe(fruityvice_normalized)
#dont run anything post here while  we troublshoot
streamlit.stop()

# import snowflake.connector
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
# my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("SELECT * from fruit_load_list")
#my_data_rows = my_cur.fetchall()
#my_data_row = my_cur.fetchone()
##streamlit.text("the fruit load list contains")

streamlit.header("the fruit load list contains")

# streamlit.text("Hello from Snowflake:")
# streamlit.text(my_data_row)
#streamlit.dataframe(my_data_row)
#streamlit.dataframe(my_data_rows)



#New Section to display Fruityvice api response 
#Second  text box
streamlit.header('Fruityvice Fruit   2 Advice!')

fruit_choice2 = streamlit.text_input('What fruit would you like information about?', 'apple')
streamlit.write('The user entered ', fruit_choice2)
# import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice2)
streamlit.write('Thanks for adding ',fruit_choice2)

my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from streamlit')")

