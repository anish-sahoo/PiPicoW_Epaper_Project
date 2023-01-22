#from picopaper import EPD_2in13
from picopaper_landscape import EPD_2in13_V3_Landscape
import machine, time
import network
import ntptime

print("Hello world")

epd = EPD_2in13_V3_Landscape()
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
    print('hotspot connected')
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
    
    #print('Started calculating time')
    
    time_tuple = rtc.datetime() #time.localtime()
    time_hrs = time_tuple[4]
    time_mins = time_tuple[5]
    time_secs = time_tuple[6]
    
    time_m = str(time_mins)
    time_h = str(time_hrs)
    
    if time_mins<10:
        time_m = "0" + time_m
    if time_hrs<10:
        time_h = "0" + time_h
    epd.text("Last Refresh - "+time_h+':'+time_m, 0, 10, 0x00)
    
    morning = "Good Morning!"
    quotes_line1 = ["Anything that can go wrong will","Don't judge a book by its"]
    quotes_line2 = ["go wrong. - Murphy's Law","cover. - Anonymus"]
    
    if (time_hrs>4 and time_hrs<24):
        epd.text("       Have a great day!       ", 0, 100, 0x00)
    
    
    if(time_hrs==7):
        epd.text("Good Morning", 0, 20, 0x00)
    elif(time_hrs==8):
        epd.text("quote", 0, 20, 0x00)
    elif(time_hrs==9):
        epd.text("breakfast", 0, 20, 0x00)
    elif(time_hrs==11):
        epd.text("spanish word", 0, 20, 0x00)
    elif(time_hrs==12):
        epd.text("lunch", 0, 20, 0x00)
    elif(time_hrs==13):
        epd.text("break", 0, 20, 0x00)
    elif(time_hrs==15):
        epd.text("it works", 0, 20, 0x00)    
    elif(time_hrs==16):
        #epd.text("tech/engineering", 0, 20, 0x00)
        epd.text(str(quotes_line1[0]), 0, 40, 0x00)
        epd.text(str(quotes_line2[0]), 0, 60, 0x00) 
    elif(time_hrs==18):
        epd.text("dinner", 0, 20, 0x00)
    elif(time_hrs==20):
        epd.text("read", 0, 20, 0x00)
    elif(time_hrs==21):
        epd.text("sleep", 0, 20, 0x00)
    
    epd.display(epd.buffer)
    led.on()
    

    total_seconds = 60*time_mins + seconds
    print('waiting '+str((3600-total_seconds))+' seconds')
    epd.delay_ms((60-minutes)*60000)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    '''time_m = str(time_mins)
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
    epd.display(epd.buffer)'''
    
    
    
