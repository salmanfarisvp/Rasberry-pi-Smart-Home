import RPi.GPIO as GPIO
import urllib2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5,GPIO.OUT)
true = 1
while(true):
                try:
                        response = urllib2.urlopen('http://salfarsmarthome.azurewebsites.net/buttonStatus.php')
                        status = response.read()
                except urllib2.HTTPError, e:
                                        print e.code

                except urllib2.URLError, e:
                                        print e.args

                print status
                if status=='ON':
                                GPIO.output(5,True)
                elif status=='OFF':
                                GPIO.output(5,False)
