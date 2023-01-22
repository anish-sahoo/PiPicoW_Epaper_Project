quoteLineOne = [1 : "The best way to get started is to", 2 : "Nothing that's worth anything",
                3 : "Everybody has talent, it's just a matter of", 4 : "You never fail", 5 : "Nothing is impossible."]
quoteLineTwo = [1 : "quit talking and begin doing.", 2 : "is easy", 3 : "moving around until you've discovered what it is.",
                4 : "until you stop trying.", 5 : "The word itself says 'I'm possible!'"]
quoteAuthor = [1 : "- Walt Disney", 2 : "- Barack Obama", 3 : "- George Lucas", 4 : "- Albert Einstein", 5 : "- Audrey Hepburn"]
#Have a great day!

#Spanish:    
vocabEspanol = [1 : "la manzana", 2 : "hola", 3 : "el nombre", 4 : "la fecha", 5 : "el agua"]
#English:
vocabEnglish = [1 : "the apple", 2 : "hello", 3 : "the name", 4 : "the date", 5 : "the water"]

#FUN FACT
#Did you know?
techFactLineOne = [1 : "Phones are computers.", 2 : "was basically a giant calculator.",
            3 : "The largest bridge in the", 4 : "The Ancient Egyptians created canals",
            5 : "The most common computer science languages are"]

techFactLineTwo = [1 : " ", 2 : "was basically a giant calculator.",
            3 : "world is in China.", 4 : "to move limestone for the Great Pyramids.",
            5 : "JavaScript, HTML/CSS. SQL, Python, and Java."]

#Read this great book:
book = [1 : "The Very Hungry Caterpillar", 2 : "Where the Wild Things Are",
        3 : "Chicka Chicka Boom Boom", 4 : "Goodnight Moon", 5 : "The Giving Tree"]
bookAuthor = [1 : "By Eric Carle", 2 : "By Maurice Sendak",
              3 : "By Bill Martin, Jr.", 4 : "By Margaret Wise Brown", 5 : "By Shel Silverstein"]

##################################################################################################################################################
#if statements - COPY TO COMPLETE CODE

if(time_hrs==7):
    epd.text("GOOD MORNING!", 0, 20, 0x00)
elif(time_hrs==8):
    #QUOTE
    #Generate random int
    dispValue = random.randint(1,quoteLineOne.len())

    #display quote
    epd.text(quoteLineOne.get(dispValue), 0, 20, 0x00)
    epd.text(quoteLineTwo.get(dispValue), 0, 20, 0x00)
    epd.text(quoteAuthor.get(dispValue), 0, 20, 0x00)
    epd.text("Have a great day!", 0, 20, 0x00)


    #Remove items from array after being displayed
    quoteLineOne.pop(dispValue)
    quoteLineTwo.pop(dispValue)
    quoteAuthor.pop(dispValue)
elif(time_hrs==9):
    epd.text("TIME FOR BREAKFAST!", 0, 20, 0x00)
elif(time_hrs==11):
    #SPANISH
    #Generate random int
    dispValue = random.randint(1,vocabEspanol.len())


    #display spanish & english
    epd.text("Time to learn a new word in Spanish!", 0, 20, 0x00)
    epd.text("Spanish:", 0, 20, 0x00)
    epd.text(vocabEspanol.get(dispValue), 0, 20, 0x00)
    epd.text("English:", 0, 20, 0x00)
    epd.text(vocabEnglish.get(dispValue), 0, 20, 0x00)


    #Remove items from array after being displayed
    vocabEspanol.pop(dispValue)
    vocabEnglish.pop(dispValue)
elif(time_hrs==12):
    epd.text("TIME FOR LUNCH!", 0, 20, 0x00)
elif(time_hrs==13):
    epd.text("TAKE A BREAK", 0, 20, 0x00) 
elif(time_hrs==16):
    #TECH/ENGINEERING FACT
    #Generate random int
    dispValue = random.randint(1,techFact.len())


    #display fact
    epd.text("FUN FACT", 0, 20, 0x00)
    epd.text("Did you know?", 0, 20, 0x00)
    epd.text(techFact.get(dispValue), 0, 20, 0x00)


    #Remove items from array after being displayed
    techFact.pop(dispValue)
elif(time_hrs==18):
    epd.text("TIME FOR DINNER!", 0, 20, 0x00)
elif(time_hrs==20):
    #READ
    #Generate random int
    dispValue = random.randint(1,book.len())

    #display book
    epd.text("Read this great book:", 0, 20, 0x00)
    epd.text(book.get(dispValue), 0, 20, 0x00)
    epd.text(bookAuthor.get(dispValue), 0, 20, 0x00)


    #Remove items from array after being displayed
    book.pop(dispValue)
    bookAuthor.pop(dispValue)
elif(time_hrs==21):
    epd.text("TIME FOR BED", 0, 20, 0x00)
    epd.text("GOOD NIGHT", 0, 20, 0x00)
    epd.text("Let the starts light the way", 0, 20, 0x00)
    epd.text("to where your dreams", 0, 20, 0x00)
    epd.text("can be found awaiting your arrival.", 0, 20, 0x00)
    epd.text("- Anthony T. Hincks", 0, 20, 0x00)
