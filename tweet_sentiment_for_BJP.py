from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib import rcParams

# Plotting the overall sentiment
# Total positive % = 88.49
# Total neutral % = 215.27
# Total negative % = 96.17
# Total ~ 400

# Data for Congress
# Color scheme : 
# Yellow : Neutral sentiment
# Red : Negative sentiment
# Green : Positive sentiment

# westlimit=68.11; southlimit=6.46; eastlimit=97.4; northlimit=35.51
westlimit=68.2
southlimit=20.1
eastlimit=74.5
northlimit=24.7

rcParams['figure.figsize'] = (7,14)

m = Basemap(projection='merc',llcrnrlat=southlimit,urcrnrlat=northlimit,llcrnrlon=westlimit,urcrnrlon=eastlimit,resolution='h',area_thresh=500)
#m.drawcoastlines()
m.drawcountries()
m.drawstates()
m.drawcities()
m.fillcontinents(color='#d0def4',lake_color='#FFFFFF')
m.drawmapboundary()
#m.bluemarble()

lon,lat = 72.430081, 22.797559
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=57.14)

lon,lat= 72.843275, 22.797559
x,y=m(lon,lat)
m.plot(x,y,'r.',markersize=14,alpha=0.7)

lon,lat = 72.843275, 23.164295
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=28.57,alpha=0.7)
#----------------------------------------------------------
lon,lat=72.4367386, 22.9232559
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=4.12)

lon,lat=72.7037246, 22.9232559
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=63.91,alpha=0.7)

lon,lat=72.4367386, 23.1046616
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=31.95,alpha=0.7)
#----------------------------------------------------------

lon,lat=72.845067, 20.458952
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=43.75,alpha=0.7)

lon,lat=73.141436, 20.458952
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=0.0,alpha=0.7)

lon,lat=73.141436, 20.742669
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=56.25,alpha=0.7)

#---------------------------------------------------------

lon,lat=73.048892, 22.088382
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=33.33333,alpha=0.7)

lon,lat=73.312138, 22.088382
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=11.11111111111111,alpha=0.7)

lon,lat=73.312138, 22.465446
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=55.55555555555556,alpha=0.7)

#--------------------------------------------------------
lon,lat=73.156484, 22.348049
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=27.2727,alpha=0.7)

lon,lat=73.20095, 22.348049
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=0.0,alpha=0.7)

lon,lat=73.20095, 22.374853
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=72.72727272727273,alpha=0.7)

#-------------------------------------------------------------
lon,lat=72.269606, 21.679278
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=66.66666666666667,alpha=0.7)

lon,lat=72.283148, 21.679278
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=0.0,alpha=0.7)

lon,lat=72.283148, 21.693567
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=33.333333333333336,alpha=0.7)

#------------------------------------------------------------
lon,lat=72.529616, 23.088656
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=33.333333333333336,alpha=0.7)

lon,lat=72.814936, 23.088656
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=11.11111111111111,alpha=0.7)

lon,lat=72.814936, 23.341798
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=55.55555555555556,alpha=0.7)

#----------------------------------------------------------
lat,long=70.297645, 21.313876
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=43.75,alpha=0.7)

lat,long=70.6781615, 21.313876
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=0.0,alpha=0.7)

lat,long=70.6781615, 21.6746697
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=56.25,alpha=0.7)

#------------------------------------------------------------

plt.title('Gujrat Tweet Sentiment for BJP')
plt.show()
