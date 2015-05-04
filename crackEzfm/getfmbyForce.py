import urllib2
import random
import time
def send_request(url):
	try:
	    res = urllib2.urlopen(urllib2.Request(url))
	    code = res.getcode()
	    res.close()
	    return code
	except Exception,e:
	    return 404

def getTime():
	
	startTime = "2015-04-11 10:00:00"
	endTime = "2015-04-11 16:59:00"
	sTime =time.mktime(time.strptime(startTime,'%Y-%m-%d %H:%M:%S'))
	eTime =time.mktime(time.strptime(endTime,'%Y-%m-%d %H:%M:%S'))
	eDelta =int( eTime - sTime)
	iTimeList = []
	for i in range(int(sTime),int(eTime)):
		iTimeList.append( time.strftime('%H%M%S',time.localtime(i)))
	return iTimeList

def getRange():
	minRange = 10000
	maxRange = 90000 
	iRangeList = []
	for i in range(1,maxRange):
		iRangeList.append(minRange+i)
	return iRangeList



	
def check_link(iDate):
	f = open("cRes.txt","a")
	preUrl = "http://123.56.91.34/Uploads/media/"
	iTime = getTime()
	iRange = getRange() 
	for t in iTime:
		for r in iRange:
			crackUrl = preUrl + iDate + "/" + iDate + str(t) + "_" + str(r) +".mp3"
         		res = send_request(crackUrl)
                       	if res ==200:
                        	print >>f,crackUrl
 

			




if __name__ == '__main__':
	start = time.clock()
	print start
	check_link("20150325")
	end = time.clock()
	print end
	print ("We cost :%.03f seconds " % (end-start))

