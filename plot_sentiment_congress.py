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
m.drawcoastlines()
m.drawcountries()
m.drawstates()
#m.drawcities()
m.fillcontinents(color='#d0def4',lake_color='#FFFFFF')
m.drawmapboundary()
#m.bluemarble()

lon,lat = 72.4367386, 22.9232559
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=58.13)

lon,lat= 72.7037246, 22.9232559
x,y=m(lon,lat)
m.plot(x,y,'r.',markersize=9.3,alpha=0.7)

lon,lat = 72.70,22.9232559
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=32.55,alpha=0.7)
#----------------------------------------------------------
lon,lat=72.430081, 22.797559
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=25)

lon,lat=72.843275, 22.797559
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=25,alpha=0.7)

lon,lat=72.843275, 23.164295
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=50.00,alpha=0.7)
#----------------------------------------------------------

lon,lat=73.048892, 22.088382
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=16.66,alpha=0.7)

lon,lat=73.312138, 22.088382
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=33.33,alpha=0.7)

lon,lat=73.312138, 22.465446
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=50,alpha=0.7)

#---------------------------------------------------------

lon,lat=72.269606, 21.679278
x,y = m(lon,lat)
m.plot(x,y,'go',markersize=14.28,alpha=0.7)

lon,lat=772.283148, 21.679278
x,y = m(lon,lat)
m.plot(x,y,'r.',markersize=28.57,alpha=0.7)

lon,lat=72.283148, 21.693567
x,y = m(lon,lat)
m.plot(x,y,'bo',markersize=57.14,alpha=0.7)

plt.title('Gujrat Tweet Sentiment for Congress')
plt.show()
