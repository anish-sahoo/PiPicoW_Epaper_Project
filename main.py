from picopaper import EPD_2in13
import machine, time
import network
import ntptime

print("Hello world")

epd = EPD_2in13()
epd.Clear(0xff)
led = machine.Pin("LED", machine.Pin.OUT)
led.on()
rtc = machine.RTC()
a=0

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect("Pixel_6893", "12345678") #replace with your WiFi ssid and password

max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    time.sleep(1)

# Handle connection error
if wlan.status() == 3:
    s = 3
    while s > 0:
        s -= 1
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)
    ntptime.settime()
    timezone_hour = -6
    timezone_sec = timezone_hour * 3600
    sec = ntptime.time()
    sec = int(sec + timezone_sec)
    (year, month, day, hours, minutes, seconds, weekday, yearday) = time.localtime(sec)
    print ("CST Time: ")
    print((year, month, day, hours, minutes, seconds))
    rtc.datetime((year, month, day, 0, hours, minutes, seconds, 0))

while 1==1:
    a += 1
    led.off()
    epd.Clear(0xff)
    epd.fill(0xff)
    epd.text("Current Time:", 0, 2, 0x00)
    print('Started calculating time')
    
    time_tuple = rtc.datetime() #time.localtime()
    time_hrs = time_tuple[4]
    time_mins = time_tuple[5]
    
    time_m = str(time_mins)
    time_h = str(time_hrs)
    
    if time_mins<10:
        time_m = "0" + time_m
    if time_hrs<10:
        time_h = "0" + time_h
    
    final_formatted_time = time_h + ":" + time_m
    print(final_formatted_time)
    epd.text(final_formatted_time, 0, 20, 0x00)
    epd.text("Text should refresh", 0, 100, 0x00)
    epd.text("In 3 mins", 0, 120, 0x00)
    epd.text("refresh count:", 0, 160, 0x00)
    epd.text(str(a), 0, 180, 0x00)
    epd.display(epd.buffer)
    led.on()
    epd.delay_ms(180000)

