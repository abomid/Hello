#Import important libraries

import gmplot
import pandas as pd
import numpy as np

#later change to company name
company_id= int(input('enter company id:'))

#fo = open("df_location.csv", "r")
data = pd.read_csv("df_location.csv")

# grab the row with matching name
# noinspection PyStatementEffect
comp= data.loc[data['id'] == company_id]

num_row = comp.shape[0]

gmap = gmplot.GoogleMapPlotter(0, 0, 2)
# plot heatmap
# gmap.heatmap(latitude[0:100], longitude[0:100])
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/"




#gmap.scatter(latitude[0:100], longitude[0:100], c='r', marker=True)
#Your Google_API_Key   AIzaSyCrzaLijjGj9mJDTzDYNPC5I2arqodYSME

gmap.apikey = "AIzaSyCZ7jEYGuiW7JrL2slJRSql53vUbwdRYt4"
    # save it to html
    # save it to html
gmap.draw(r"my_map2.html")

print(comp)