import urllib2, urllib
mydata=[('one','1'),('two','2')]    #The first is the var name the second is the value
mydata=urllib.urlencode(mydata)
path='http://localhost/new.php'    #the url you want to POST to
req=urllib2.Request(path, mydata)
req.add_header("Content-type", "application/x-www-form-urlencoded")
page=urllib2.urlopen(req).read()
print page
