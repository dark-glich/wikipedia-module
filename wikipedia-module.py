import wikipedia
import emoji
running = True
#d = wikipedia.random("facts")
#print(f"{d} :\n")
#print(wikipedia.summary(d, sentences=2))


while running:
    try :
        key = input("""# type 'quit' to exit from this page   #\n# type 'about' to know about this page #
# type hindi to get results in hindi   #
\nwhat you are looking for ? \nSearch : \n""")

        if key == "quit":   
            print("-------------> sucessfully exited from wikipedia <-------------")
            running = False

        if key == "hindi":
            wikipedia.set_lang("hi")

        if key == "about":
            emoj = (emoji.emojize(":red_heart:",variant="emoji_type"))

            print("""this page is created to deliver you the most related information about your 
searches. It is directly connected to the wikipedia to get the latest and most relevant information for you.
Thank You {}
    ~ Mohd Bilal (creator)""".format(emoj))

            
        else:
            print(wikipedia.summary(key, sentences=5))
    except wikipedia.WikipediaException:

        print(f"Sorry we dont have any information about your input")
    

     