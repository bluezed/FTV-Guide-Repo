import urllib,urllib2,sys,re,xbmcplugin,xbmcgui,xbmcaddon,xbmc
#below you can add anything here just to keep your typing down to a minimum(shortcuts)

# i.e 
icon = 'http://a0.twimg.com/profile_images/1880386140/logo-square.jpg'
#now look at the first addDir where i have written icon then look at second listed item i have put the url for image directly makes no odds how you do it !!

ADDON = xbmcaddon.Addon(id='plugin.video.myfirstplugin')



 #      addDir('name','url','mode','iconimage','description') mode is where it tells the plugin where to go scroll to bottom to see where mode is
def CATEGORIES():
        addDir('this is first listed item in first directory','url',1,icon,'hello everyone this is the description')
        addDir('this is second listed item first directory','url',1,'http://a0.twimg.com/profile_images/1880386140/logo-square.jpg','hello everyone this is the description')
        setView('movies', 'default') 
       #setView is setting the automatic view.....first is what section "movies"......second is what you called it in the settings xml  
       
       
                      												  
def Beginners(url):#  cause mode is empty in this one it will go back to first directory
        addDir('this is first listed item in second directory','url','','http://a0.twimg.com/profile_images/1880386140/logo-square.jpg','hello everyone this is the description')
        addDir('this is second listed item in second directory','url','','http://a0.twimg.com/profile_images/1880386140/logo-square.jpg','hello everyone this is the description')
        setView('tvshows', 'anything') 
 

    
def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param

# this is the listing of the items        
def addDir(name,url,mode,iconimage,description):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&iconimage="+urllib.quote_plus(iconimage)+"&description="+urllib.quote_plus(description)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description} )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok
#same as above but this is addlink this is where you pass your playable content so you dont use addDir you use addLink "url" is always the playable content         
def addLink(name,url,iconimage,description):
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name, "Plot": description } )
        liz.setProperty("IsPlayable","true")
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=url,listitem=liz,isFolder=False)
        return ok 
 
        
#below tells plugin about the views                
def setView(content, viewType):
        # set content type so library shows more views and info
        if content:
                xbmcplugin.setContent(int(sys.argv[1]), content)
        if ADDON.getSetting('auto-view') == 'true':#<<<----see here if auto-view is enabled(true) 
                xbmc.executebuiltin("Container.SetViewMode(%s)" % ADDON.getSetting(viewType) )#<<<-----then get the view type
                      
               
params=get_params()
url=None
name=None
mode=None
iconimage=None
description=None


try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        iconimage=urllib.unquote_plus(params["iconimage"])
except:
        pass
try:        
        mode=int(params["mode"])
except:
        pass
try:        
        description=int(params["description"])
except:
        pass

print "Mode: "+str(mode)
print "URL: "+str(url)
print "Name: "+str(name)
print "IconImage: "+str(iconimage)
   
        
#these are the modes which tells the plugin where to go
if mode==None or url==None or len(url)<1:
        print ""
        CATEGORIES()
       
elif mode==1:
        print ""+url
        Beginners(url)
        

       
xbmcplugin.endOfDirectory(int(sys.argv[1]))
