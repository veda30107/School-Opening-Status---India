#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
import plotly.express as px


# In[3]:


with open(r'/home/veda/Videos/Custom map/test/Data/Indian States and Union Territories.geojson') as f:
    data1 = json.load(f)


# In[4]:


data1["features"][0]["properties"]


# In[5]:


state_id_map={}
for feature in data1['features']:
    feature['id']=feature['properties']['st_code']
    state_id_map[feature['properties']['ST_NM']]= feature['id']


# In[6]:


df = pd.read_csv('/home/veda/Videos/Custom map/test/Nov/EE policy tracker - SO_LPS.csv')
df['State_Code']=df['State Name'].apply(lambda x: state_id_map[x])


# In[7]:


df.head()


# In[8]:


import plotly.io as pio
pio.renderers.default = 'firefox'


# In[9]:


color_discrete_map = {'Fully shut': 'rgb(255, 49, 49)', 'Fully open': 'rgb(80,200,120)', 'Partially open': 'rgb(255,191,0)', 'Not Available':'rgb(168,168,168)'}


# In[10]:


fig = px.choropleth_mapbox(df, locations='State_Code', geojson=data1,color='Status',
                          hover_name='State Name',hover_data=['Status last changed on','Additional Info'],
                          mapbox_style="carto-positron", center = {'lat': 25, 'lon':79},
                          opacity=1, color_discrete_map=color_discrete_map, zoom=3,height=650,
                          animation_frame="Month")

fig.update_layout(hovermode='x unified', legend=dict(title= None), hoverlabel=dict(bgcolor='rgba(255,255,255,0.75)',
                                                                                  font=dict(color='black')))

fig.update_geos(fitbounds="locations",visible=False)

fig.show()


# In[11]:


fig.write_html("/home/veda/Videos/Custom map/test/Nov/new/map.html",include_plotlyjs="cdn")


# In[ ]:




