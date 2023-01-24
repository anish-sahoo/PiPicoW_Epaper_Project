from picopaper_landscape import EPD_2in13_V3_Landscape
import machine, time
import network
import ntptime
import random

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
    epd.text("     Last Refresh - " + time_h + ':' + time_m, 0, 10, 0x00)

    
    quoteLineOne = ["The best way to get started is ",  "Nothing that's worth anything", "Everybody has talent, it's just", "You never fail until", "Nothing is impossible. The word"]
    quoteLineTwo = ["to quit talking and begin doing.", "is easy",                       "a matter of moving around until", "you stop trying.",     "itself says 'I'm possible!'"]
    quoteLineThr = [" ",                                " ",                             "you've discovered what it is.",   " ",                    " "]
    quoteAuthor = [ "- Walt Disney",                    "- Barack Obama",                "- George Lucas",                  "- Albert Einstein",    "- Audrey Hepburn"]
    #Have a great day!

    #Spanish:    
    vocabEspanol = ["la manzana", "hola", "el nombre", "la fecha", "el agua"]
    #English:
    vocabEnglish = ["the apple", "hello", "the name", "the date", "the water"]

    #FUN FACT
    #Did you know?
    techFactLineOne = ["Phones are computers.", "The first computer was basically", "The largest bridge in the world", "The Ancient Egyptians created ", "The most common computer science"]
    techFactLineTwo = [" ", "a giant calculator.", "is in China.", "canals to move limestone for ", "languages are JavaScript,"]
    techFactLineThr = [" ", "calculator.", " ", "the Great Pyramids.", "HTML/CSS, Python, and Java."]
    
    #Read this great book:
    book = ["The Very Hungry Caterpillar", "Where the Wild Things Are", "Chicka Chicka Boom Boom", "Goodnight Moon", "The Giving Tree"]
    bookAuthor = ["By Eric Carle", "By Maurice Sendak", "By Bill Martin, Jr.", "By Margaret Wise Brown", "By Shel Silverstein"]

    ##################################################################################################################################################
    #if statements - COPY TO COMPLETE CODE

    if(time_hrs==7):
        epd.text("         GOOD MORNING!         ", 0, 60, 0x00)
    elif(time_hrs==8):
        #QUOTE
        #Generate random int
        dispValue = random.randint(0, len(quoteLineOne)-1)

        #display quote
        epd.text(quoteLineOne[dispValue], 0, 50, 0x00)
        epd.text(quoteLineTwo[dispValue], 0, 60, 0x00)
        epd.text(quoteLineThr[dispValue], 0, 70, 0x00)
        epd.text(quoteAuthor[dispValue], 20, 80, 0x00)
        #epd.text("Have a great day!", 0, 20, 0x00)

        #Remove items from array after being displayed
        quoteLineOne.pop(dispValue)
        quoteLineTwo.pop(dispValue)
        quoteLineThr.pop(dispValue)
        quoteAuthor.pop(dispValue)
    elif(time_hrs==9):
        epd.text("      TIME FOR BREAKFAST!      ", 0, 62, 0x00)
    elif(time_hrs==11):
        #SPANISH
        #Generate random int
        dispValue = random.randint(0, len(vocabEspanol)-1)

        #display spanish & english
        epd.text("Let's learn a new Spanish word!", 0, 40, 0x00)
        epd.text("     Spanish: "+vocabEspanol[dispValue], 0, 60, 0x00)
        epd.text("     English: "+vocabEnglish[dispValue], 0, 70, 0x00)

        #Remove items from array after being displayed
        vocabEspanol.pop(dispValue)
        vocabEnglish.pop(dispValue)
    elif(time_hrs==12):
        epd.text("        TIME FOR LUNCH!        ", 0, 64, 0x00)
    elif(time_hrs==13):
        epd.text("         TAKE A BREAK!         ", 0, 64, 0x00) 
    elif(time_hrs==16):
        #TECH/ENGINEERING FACT
        #Generate random int
        dispValue = random.randint(0, len(techFactLineOne)-1)

        #display fact
        epd.text("    FUN FACT! Did you know?    ", 0, 30, 0x00)
        epd.text(techFactLineOne[dispValue], 0, 50, 0x00)
        epd.text(techFactLineTwo[dispValue], 0, 60, 0x00)
        epd.text(techFactLineThr[dispValue], 0, 70, 0x00)

        #Remove items from array after being displayed
        techFactLineOne.pop(dispValue)
        techFactLineTwo.pop(dispValue)
        techFactLineThr.pop(dispValue)
    elif(time_hrs==18):
        epd.text("        TIME FOR DINNER!       ", 0, 64, 0x00)
    elif(time_hrs==20):
        #READ
        #Generate random int
        dispValue = random.randint(0, len(book)-1)

        #display book
        epd.text("Read this great book:", 0, 40, 0x00)
        epd.text(book[dispValue], 0, 60, 0x00)
        epd.text("- "+bookAuthor[dispValue], 0, 72, 0x00)

        #Remove items from array after being displayed
        book.pop(dispValue)
        bookAuthor.pop(dispValue)
    elif(time_hrs==21):
        epd.text("         TIME FOR BED!         ", 0, 30, 0x00)
        epd.text("Let the stars light the way to", 0, 50, 0x00)
        epd.text("where your dreams can be found", 0, 60, 0x00)
        epd.text("awaiting your arrival.", 0, 70, 0x00)
        epd.text("   - Anthony T. Hincks", 0, 84, 0x00)
    
        
    if (time_hrs>4 and time_hrs<17):
        epd.text("       Have a great day!       ", 0, 120, 0x00)
    elif(time_hrs>17 and time_hrs<21):
        epd.text("         Good Evening!         ", 0, 120, 0x00)
    else:
        epd.text("          Good Night!          ", 0, 120, 0x00)
    
    epd.display(epd.buffer)
    led.on()
    
    total_seconds = 60*time_mins + time_secs
    print('waiting '+str((3600-total_seconds))+' seconds')
    epd.delay_ms((60-time_mins)*60000)