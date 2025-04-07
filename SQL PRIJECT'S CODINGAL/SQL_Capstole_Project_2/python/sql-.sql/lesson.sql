from google.colab import files 
updlouded = files.upload()

import numpy as np 
import pandas as pd 
import squlite3

database = 'database.squlite'

conn = squite3.connect(database)

tables = pd.read_sql("""select *
                     form squlite_master
                     where type='table'""", conn)
-- Get a list of tables and views in the current database
tables 

joined_city = pd.read_sql("""delect c.country_id, c.country_name, ci.city_namr
                              from country c
                              inner join city ci
                              on c.country_id""",conn)
joined_city 

joined_left = pd.read.player_id == season.man_of_the_series""",
conn)
joined_left


union = pd.read_sql("""select player_name
                       from player
                       UNION
                       select team""",conn)
union 