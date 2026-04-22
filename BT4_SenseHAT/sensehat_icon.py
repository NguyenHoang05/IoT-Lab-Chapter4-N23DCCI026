from sense_emu import SenseHat
import time
sense = SenseHat()
#dinh nghia mau
y = [255, 255, 0] #vang
b = [0, 0, 0] #den
r = [255, 0, 0] #do
#mat cuoi 8x8
icon = [
b,b,y,y,y,y,b,b,
b,y,b,b,b,b,y,b,
y,b,r,b,b,r,b,y,
y,b,b,b,b,b,b,y,
y,b,b,b,b,b,b,y,
y,b,b,b,b,b,b,y,
b,y,b,b,b,b,y,b,
b,b,y,y,y,y,b,b,
]
sense.set_pixels(icon)
time.sleep(5)
sense.clear()
print('Bieu tuong da hien thi.')
