import web
import serial

urls = (
  '/', 'hello',
  '/block/(\d+)', 'Device')

app = web.application(urls, globals())
ser = serial.Serial("/dev/ttyACM0", 9600) 

#http://0.0.0.0:8080/block?d=1&a=2
class hello:
    def GET(self):
        return 'Hello!'

class Device:
    def POST(self,id):
       	
	#d=str(web.input().d)
 	d=str(id)
	print d
	a=str(d)
        ser.write(a)
        return 1
        

if __name__ == "__main__":
    app.run()
