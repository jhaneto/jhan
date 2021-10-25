import pandas as pd
import plotly.express as px
import numpy as n
import datetime as datatime
from geopy.geocoders import Nominatim

pd.options.display.float_format = '{:.2f}'.format
#Solicitações do CEO

df = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")

def converterData( data ):
    data['date']  = pd.to_datetime(data['date'])
    return None

def show_dtypes( data ):
    print( data.dtypes )
    return None

def show_dimensions( data ):
    print( 'Number of rows: {}'.format( df.shape[0] ))
    print( 'Number of columns: {}'.format( df.shape[1] ))
    return None

def createColumnsAddress( data ):
    #Create empty rows
        data['road'] = 'NA'
        data['house_number'] = 'NA'
        data['city'] = 'NA'
        data['county'] = 'NA'
        data['state'] = 'NA'
        return data
'''
def collect_geodata( data):
    #Inicialize API

    geolocator = Nominatim(user_agent = 'geolocal')
    data = data.head(1000)
   
    for i in range(len(data)):
           # print('Loop : {} / {}'.format(i, len(df)))
            #Make query
            query =str(data.loc[i,'lat'] ) + ',' + str(data.loc[i,'long'])
            #print(query)
            response = geolocator.reverse(query)
            #query =str(response.raw['lat']) + ',' + str(response.raw['lon'])
            #print(query)
            if 'road' in response.raw['address']:
               data.loc[i,'road'] = response.raw['address']['road']
            
            if 'house_number' in response.raw['address']:   
               data.loc[i,'house_number'] = response.raw['address']['house_number']
               
            if 'city' in response.raw['address']:      
               data.loc[i,'city'] = response.raw['address']['city']
              
            if 'county' in response.raw['address']:
               data.loc[i,'county'] = response.raw['address']['county']
            
            if 'state' in response.raw['address']:   
               data.loc[i,'state'] = response.raw['address']['state']
            
            return data
'''   

def collect_geodataWhile( data, num):
    #Inicialize API
    i = 1
    geolocator = Nominatim(user_agent = 'geolocal')
    data = data.head(num)
         
    while i < num:         
           # print('Loop : {} / {}'.format(i, len(df)))
            #Make query
            query =str(data.loc[i,'lat'] ) + ',' + str(data.loc[i,'long'])
            #print(query)
            response = geolocator.reverse(query)
            #query =str(response.raw['lat']) + ',' + str(response.raw['lon'])
            #print(query)
          
            if 'road' in response.raw['address']:
                       data.loc[i,'road'] = response.raw['address']['road']
                    
            if 'house_number' in response.raw['address']:   
                       data.loc[i,'house_number'] = response.raw['address']['house_number']
                       
            if 'city' in response.raw['address']:      
                       data.loc[i,'city'] = response.raw['address']['city']
                      
            if 'county' in response.raw['address']:
                       data.loc[i,'county'] = response.raw['address']['county']
                    
            if 'state' in response.raw['address']:   
                       data.loc[i,'state'] = response.raw['address']['state']
                       i+=1    
    return data

s = df[df['road'] == 'NA']             
        
def classifierDormitory( data ):
        data['dormitory_types'] = None
        data.loc[df.bedrooms == 1, 'dormitory_types'] = 'studio'
        data.loc[df.bedrooms == 2, 'dormitory_types'] = 'apartment'
        data.loc[df.bedrooms > 2, 'dormitory_types'] = 'house'
        data['dormitory_types'].value_counts()
        return data
    

def nivel( data):
            #a = df[(df['bedrooms'] == 4) & (df['floors'] == 3)]
            #Laço FOR 
            for i in range(len(data)):
                if ( data.loc[i, 'price'] > 0) & (data.loc[i, 'price'] < 321950):
                    data.loc[i, 'nivel'] = 'nivel_0'
                elif ( data.loc[i, 'price'] >= 321950) & (data.loc[i, 'price'] < 450000):
                    data.loc[i, 'nivel'] = 'nivel_1'
                elif ( data.loc[i, 'price'] >= 450000) & (data.loc[i, 'price'] < 645000):
                    data.loc[i, 'nivel'] = 'nivel_2'
                else:    
                    data.loc[i, 'nivel'] = 'nivel_3'
            return data

      
def level( data ):
    
        data['level'] = data['level'] = 0
        
        #data['level']  = data['level'].astype(int)
        for i in range(len(data)):
            if ( data.loc[i, 'price'] > 0) & (data.loc[i, 'price'] < 321950):
                data.loc[i, 'level'] = 0
            elif ( data.loc[i, 'price'] >= 321950) & (data.loc[i, 'price'] < 450000):
               data.loc[i, 'level'] = 1
            elif ( data.loc[i, 'price'] >= 450000) & (data.loc[i, 'price'] < 645000):
                data.loc[i, 'level'] = 2
            else:    
                data.loc[i, 'level'] = 3
                
        return data

def condition( data ): 
    
        data['condition_type'] = None
        data.loc[data.condition <= 2, 'condition_type'] = 'bad'
        data.loc[(data.condition == 3) | (data.condition == 4), 'condition_type'] = 'regular'
        data.loc[data.condition == 5, 'condition_type'] = 'good'
     
        return data

def showGrafico( data ):  
                #houses = data[['id', 'lat','long', 'price']].copy()                                    
                fig = px.scatter_mapbox(data,
                                        lat=data["lat"],
                                        lon=data["long"],
                                        color=data["level"],
                                        size=data["price"],
                                        color_continuous_scale = px.colors.cyclical.IceFire,
                                        size_max=15,
                                        zoom=10)
                
                fig.update_layout(mapbox_style='open-street-map')
                fig.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
                
                return fig.show()    
            
s = df[['id', 'lat','long', 'price', 'level']]
converterData( df )
show_dtypes( df )
show_dimensions( df )
createColumnsAddress( df )
#collect_geodata( df)
nivel( df )
level( df )
classifierDormitory( df )
condition( df ) 
collect_geodataWhile( df, 1000)
showGrafico(s)

#houses['level']  = houses['level'].astype(int)       

#df1 = pd.read_csv("C:\\Users\\win10\\Desktop\\python_excel\\kc_house_data.csv")
#houses = df1[['id', 'lat','long', 'price']].copy()



            
converterData(df)
df.info()
df['condition_type'].value_counts()