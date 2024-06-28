import tkinter
import os
import os.path
from PIL import Image, ImageTk
import tkinter.messagebox
import customtkinter
import mysql.connector



connection = mysql.connector.connect(host='sql8.freesqldatabase.com',
                                     user='sql8681610',
                                    password='bjTUhQneyh',
                                    database="sql8681610"
                                    )#Connect to the database

mycursor = connection.cursor()


Q3 = "INSERT INTO Cards (Cardname, Cardtype, relatedid, forbiddenlistid) VALUES (%s, %s, %s, %s)"#Query for inserting vaules into Cardname and Cardtype columns

Q4 = "INSERT INTO Cardsdetails(carddetailsID, cardlevel, cardattributte, cardattack, carddefence, flavourtext) VALUES (%s, %s, %s, %s, %s, %s)"#Query for inserting vaules into columns of card detail table

Q12 = "INSERT INTO Spelltrap (SpelltrapID, speedspell, stflavourtext) VALUES (%s,%s, %s)"#Query for inserting vaules into columns of spelltrap table




#Set's the appearance of application including widgets
customtkinter.set_appearance_mode("System") # Set the backgroud of app to dark mode
customtkinter.set_default_color_theme("blue") #Set the themes of the widgets to blue

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1250x780")
        self.title("How to use")

        self.help_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.help_frame.grid(row=0, column=1, sticky="ne")
        self.help_frame.grid_columnconfigure(0, weight=1)

        #self.help_info_text  = customtkinter.CTkTextbox(self.help_frame,width=950,height=780) #creates the text box to that exact width and size
        #self.help_info_text .grid(row=0, column=1, padx=20, pady=20)
        script_dir = os.path.dirname(__file__) 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "Image files")#Assiagns path to image folder to the variable
        self.help_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "help2.png")), size=(1200,720))

        self.help_frame_large_image_label2 = customtkinter.CTkLabel(self.help_frame, text="", image=self.help_image)#creates an instance of label widget which will display an image
        self.help_frame_large_image_label2.grid(row=0, column=1, padx=20, pady=10)#Places it within a specfic place image label grid



        

#Creates a class witch inherits from customtkinter.CTk
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Yu-Gi-Oh Card Finder")#Sets the title of the application
        self.geometry("800x800")#set the width and size of application in minmized mode

        # Code underneath sets the grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        script_dir = os.path.dirname(__file__) 
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "Image files")#Assiagns path to image folder to the variable
        self.card_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Blue-Eyes White Dragon.png")), size=(400, 540))#Assiagns the size of the Image, path and image to the variable
        self.fl_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Pot_of_greed.png")), size=(400, 540))
        

        #creates frames for navigation widgets
        self.navigation_frame = customtkinter.CTkFrame(self,corner_radius=0)#Initialised a new object storing the refence in the navigation frame, also corner_radius decided how rounded the frame is
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        #Creates frames for home widgets
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=1, sticky="ne")
        self.home_frame.grid_columnconfigure(0, weight=1)

        #Creates frames for textbox which will hold certain info on cards
        self.related_card_info_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.related_card_info_frame.grid(row=0, column=1, padx=20, pady=20, sticky="esw")
        self.related_card_info_frame.grid_rowconfigure(0, weight=1)

        #Creates an instance of objects
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.card_image)#creates an instance of label widget which will display an image
        self.home_frame_large_image_label.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid

        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w")#Creates a laberl named Appearance for menu option
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))#Posistions it on the grid,therefore when the app expand or minmize it will srink or grow to accordance
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System","Light", "Dark"],command=self.change_appearance_mode_event)#Creates a menu optition for system apperance within navigation frame
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(10, 10), sticky="s")#places menu in an specfic area within the grid, therefore when the app expand or minmize it will srink or grow to accordance
        
        self.input_button_searchc = customtkinter.CTkButton(self.navigation_frame, text="Card Search", command=self.input_button_searchc_button_event)# creates a button
        self.input_button_searchc.grid(row=0, column=0, padx=10, pady=10)#places button within the grid
        
        self.input_button_addc = customtkinter.CTkButton(self.navigation_frame, text="Add a card", command=self.input_button_addc_button_event)# creates a button
        self.input_button_addc.grid(row=1, column=0, padx=10, pady=10)#places button within the grid

        
        self.flist_button_1 = customtkinter.CTkButton(self.navigation_frame,text="Forbidden List", command=self.flist_button_event)#creates a button
        self.flist_button_1.grid(row=2, column=0, padx=10, pady=(10,10))#places button within the grid

        self.howtoplaybutton_1 = customtkinter.CTkButton(self.navigation_frame, text="How to play", command=self.open_toplevel)
        self.howtoplaybutton_1.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.toplevel_window = None
        
        self.card_info_text = customtkinter.CTkTextbox(self.home_frame,width=1250,height=540) #creates the text box to that exact width and size
        self.card_info_text.grid(row=1, column=2, padx=20, pady=20)
        

        self.related_card_info_text = customtkinter.CTkTextbox(self.related_card_info_frame,width=1680,height=400) #creates the text box to that exact width and size
        self.related_card_info_text.grid(row=1, column=0, padx=10, pady=10)
        
        
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ToplevelWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it   
    

    #function to be run when certain buttons are clicked
    def change_appearance_mode_event(self, new_appearance_mode):#Creates a function that takes inputds of the user request  appearance  of application
        customtkinter.set_appearance_mode(new_appearance_mode)#Changes appearance on apps use input from the menu opition 

        print("cool")
    
    def flist_button_event(self): #prints the text
        print("It works!!!!")
        self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
        self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox
        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.home_frame, text="", image=self.fl_image)#creates an instance of label widget which will display an image
        self.home_frame_large_image_label2.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid
        #self.card_info_text.insert("0.0", "FORRBIDEN CARDS\n\n") #Prints text in text box


        #code to convert a tuple into a string using a for loop
        def convertTuple(tup):
            # initialize an empty string
            conw = ''
            for item in tup:
                conw = conw + item
            return conw   



        Foribdden = ["F"]#Used to search for forbidden cards
        Lim1 = ["L1"]#Used to search for limited to 1 cards
        Lim2 = ["L2"]#Used to search for limted to 2 cards

        Q18 = "SELECT cardname FROM Cards WHERE forbiddenlistid = (%s)"#Select card names with the matching forbidden list id
        mycursor.execute(Q18, Foribdden)#Excutes the query for forbidden cards

        FCresults = []
        for y in mycursor:#loops through the cursour
            FCresults.append(y)
            print(y)#print out every thing retreievd 


        length = len(FCresults)#Get the length of items in the list
        z = 0
        while z != length:#Keeps going till it's done every item in the list
            tuple = (FCresults[z])#Convet each retrieved item and converts it
            conw = convertTuple(tuple)# converts tuple into a string
            self.related_card_info_text.insert("0.0", conw +" = F \n\n")#displays out converted string
            z = z + 1


        mycursor.execute(Q18, Lim1)#Excutes the query for limted 1 cards

        FCresults = []
        for y in mycursor:#loops through the cursour
            FCresults.append(y)
            print(y)#print out every thing retreievd 


        length = len(FCresults)#Get the length of items in the list
        z = 0
        while z != length:#Keeps going till it's done every item in the list
            tuple = (FCresults[z])#Convet each retrieved item and converts it
            conw = convertTuple(tuple)# converts tuple into a string
            self.related_card_info_text.insert("0.0", conw +" = L1 \n\n")#displays out converted string
            z = z + 1


        mycursor.execute(Q18, Lim2)#Excutes the query for limted 2 cards

        FCresults = []
        for y in mycursor:#loops through the cursour
            FCresults.append(y)
            print(y)#print out every thing retreievd 


        length = len(FCresults)#Get the length of items in the list
        z = 0
        while z != length:#Keeps going till it's done every item in the list
            tuple = (FCresults[z])#Convet each retrieved item and converts it
            conw = convertTuple(tuple)# converts tuple into a string
            self.related_card_info_text.insert("0.0", conw +"= L2 \n\n")#display out converted string
            z = z + 1

        self.card_info_text.insert("0.0", "FORRBIDEN CARDS\n\n"
                                        + "F = Forrbidden\n\n"
                                        + "L1 = Limit 1\n\n"
                                        + "L2 = Limit 2\n\n") #Prints text in text box

    def input_button_searchc_button_event(self):
        search_card_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Card search")# Opens a mini window that allows vaules to be inputted
        search_card = search_card_dialog.get_input()#Assaigns input from user
        print(search_card)
        #print("The card searched for", dialog.get_input())#prints inputed dialog

        photo_search = (search_card+ ".png")
        print(search_card)

        try:
            script_dir = os.path.dirname(__file__) 
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "Image files")#Assiagns path to image folder to the variable
            self.searchered_card_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, photo_search)), size=(400, 540))#Assiagns the size of the Image, path and image to the variable
            
            self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.searchered_card_image)#creates an instance of label widget which will display an image
            self.home_frame_large_image_label.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid


            name = [search_card]#places user input into an array

            Q15 = "SELECT Cardtype FROM Cards WHERE cardname = (%s)"#Select the card type column related to the name user inputted
            mycursor.execute(Q15, name)#Excutes the query using name as a parameter
            for x in mycursor:#loops through my cursor 
                Cardidentificationresult = list(x)#Places result from the table in a list form storeted in variable
                x = 0 #Set which Item in the list I want to retrieve
                Cardidentification = Cardidentificationresult[x]#Store item in the first slot in the list into a variable
                print(Cardidentification)#Print my request in a string form

                    
                if Cardidentification == "SPELL":
                        
                        Q13 = "SELECT* FROM Cards FULL JOIN Spelltrap ON cardID = SpelltrapID WHERE cardname = (%s)"#Search cards table for the card name and coloumns linked to it in the card details table
                        mycursor.execute(Q13, name)#excutesthe queries
                        for x in mycursor:#loops through the cursour
                            stcardsearched = list(x)#everything selected from the search placed into a list and stored in varaible stcardsearchered
                            print(x)#prints everythin selected

                            x = 0
                            stcardidgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardnamegui= stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardtypegui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stspellrelatedidtextgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardforbiddenlistgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardforgeingui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardspellspeedgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardflavourtextgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1

                            #code to convert a tuple  into a string using a for loop
                            def convertTuple(tup):
                                # initialize an empty string
                                conw = ''
                                for item in tup:
                                    conw = conw + item
                                return conw  
                            

                            self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
                            self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox
                            
                            if stcardforbiddenlistgui == "F":
                                self.card_info_text.insert("0.0", "Prohibited = F \n\n")#displays out converted string
                                   
                            
                            elif stcardforbiddenlistgui == "L1": 
                                self.card_info_text.insert("0.0", "Prohibited = L1 \n\n")#displays out converted string
                                    
                            
                            elif stcardforbiddenlistgui == "L2": 
                                self.card_info_text.insert("0.0", "Prohibited = L2 \n\n")#display out converted string
                            else:
                                print("No Prohibited")

                            self.card_info_text.insert("0.0", "Card name: " + stcardnamegui + " \n\n" +  "Card type: " + stcardtypegui + " \n\n"#Prints text in text box 
                            + "Card Icon: "+ stcardspellspeedgui + " \n\n"
                            + "Card text: " + stcardflavourtextgui + " \n\n" ) 

                            
                
                            result = [stspellrelatedidtextgui]#Places the related id in an array from which it can be searchered from
                            Q17 = "SELECT cardname FROM Cards WHERE relatedid = (%s)"#Select card names with the matching related id
                            
                            if stspellrelatedidtextgui == "NO98":
                                self.related_card_info_text.insert("0.0", "NO RELATED CARDS\n\n")
                            else:
                                mycursor.execute(Q17, result)#Excutes the query

                                Rcresults = []
                                for y in mycursor:#loops through the cursour
                                    Rcresults.append(y)
                                    print(y)#print out every thing retreievd 


                                length = len(Rcresults)#Get the length of items in the list
                                z = 0
                                while z != length:#Keeps going till it's done every item in the list
                                    tuple = (Rcresults[z])#Convet each retrieved item and converts it
                                    conw = convertTuple(tuple)# converts tuple into a string
                                    self.related_card_info_text.insert("0.0", conw +" \n\n")
                                    z = z + 1

                                self.related_card_info_text.insert("0.0", "RELATED CARDS:\n\n")


                elif Cardidentification == "TRAP":
                        
                        Q13 = "SELECT* FROM Cards FULL JOIN Spelltrap ON cardID = SpelltrapID WHERE cardname = (%s)"#Search cards table for the card name and coloumns linked to it in the card details table
                        mycursor.execute(Q13, name)#excutesthe queries

                        for x in mycursor:#loops through the cursour
                            stcardsearched = list(x)#everything selected from the search placed into a list and stored in varaible stcardsearchered
                            print(x)#prints everythin selected


                            x = 0
                            
                            stcardidgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardnamegui= stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardtypegui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stspellrelatedidtextgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardforbiddenlistgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardforgeingui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardspellspeedgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                            stcardflavourtextgui = stcardsearched[x]#stores vaules retrieved from database into variables
                            x = x + 1
                                
                            self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
                            self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox

                            if stcardforbiddenlistgui == "F":
                                self.card_info_text.insert("0.0", "Prohibited = F \n\n")#displays out converted string
                                   
                            
                            elif stcardforbiddenlistgui == "L1": 
                                self.card_info_text.insert("0.0", "Prohibited = L1 \n\n")#displays out converted string
                                    
                            
                            elif stcardforbiddenlistgui == "L2": 
                                self.card_info_text.insert("0.0", "Prohibited = L2 \n\n")#display out converted string
                            else:
                                print("Not Prohibited")

                            self.card_info_text.insert("0.0", "Card name: " + stcardnamegui + " \n\n" +  "Card type: " + stcardtypegui + " \n\n"#Prints text i////n text box 
                            + "Card Icon: "+ stcardspellspeedgui + " \n\n"
                            + "Card text: " + stcardflavourtextgui + " \n\n" ) 


                            #code to convert a tuple  into a string using a for loop
                            def convertTuple(tup):
                                # initialize an empty string
                                conw = ''
                                for item in tup:
                                    conw = conw + item
                                return conw    

                            result = [stspellrelatedidtextgui]#Places the related id in an array from which it can be searchered from
                            Q17 = "SELECT cardname FROM Cards WHERE relatedid = (%s)"#Select card names with the matching related id
                            
                            if stspellrelatedidtextgui == "NO98":
                                self.related_card_info_text.insert("0.0", "NO RELATED CARDS\n\n")
                            else:
                                mycursor.execute(Q17, result)#Excutes the query

                                Rcresults = []
                                for y in mycursor:#loops through the cursour
                                    Rcresults.append(y)
                                    print(y)#print out every thing retreievd 


                                length = len(Rcresults)#Get the length of items in the list
                                z = 0
                                while z != length:#Keeps going till it's done every item in the list
                                    tuple = (Rcresults[z])#Convet each retrieved item and converts it
                                    conw = convertTuple(tuple)# converts tuple into a string
                                    self.related_card_info_text.insert("0.0", conw +" \n\n")
                                    z = z + 1

                                self.related_card_info_text.insert("0.0", "RELATED CARDS:\n\n")


                else:
                    Q10 = "SELECT* FROM Cards FULL JOIN Cardsdetails ON cardID = carddetailsID WHERE cardname = (%s)"#Search cards table for the card name and coloumns linked to it in the card details table
                    mycursor.execute(Q10, name)#excutesthe queries
                    for x in mycursor:#loops through the cursour
                        cardsearched = list(x)#everything selected from the search placed into a list and stored in varaible cardsearchered
                        print(x)#prints everythin selected

                        x = 0
                        cardidgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardnamegui= cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardtypegui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardrelatedidtextgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardforbiddenlistgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardforgeingui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardlevelgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardattributtegui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardattackgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        carddefencegui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1
                        cardflavourtextgui = cardsearched[x]#stores vaules retrieved from database into variables
                        x = x + 1

                        self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
                        self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox

                        if cardforbiddenlistgui == "F":
                                self.card_info_text.insert("0.0", "Prohibited = F \n\n")#displays out converted string
                                   
                            
                        elif cardforbiddenlistgui == "L1": 
                                self.card_info_text.insert("0.0", "Prohibited = L1 \n\n")#displays out converted string
                                    
                            
                        elif cardforbiddenlistgui == "L2": 
                                self.card_info_text.insert("0.0", "Prohibited = L2 \n\n")#display out converted string
                        else:
                                print("No Prohibited")

                        self.card_info_text.insert("0.0", "Card Name: " + cardnamegui + " \n\n" +  "Card Attributte: " + str(cardattributtegui) + " \n\n"#Prints text i////n text box 
                        + "Card Level: " + str(cardlevelgui) + " \n\n"
                        + "Card Attack: " + str(cardattackgui) + " \n\n"
                        + "Card Defence: " + str(carddefencegui) + " \n\n"
                        + "Card Type: "+ cardtypegui + " \n\n"
                        + "Card Text: " + cardflavourtextgui + " \n\n" ) 


                        #code to convert a tuple  into a string using a for loop
                        def convertTuple(tup):
                            # initialize an empty string
                            conw = ''
                            for item in tup:
                                conw = conw + item
                            return conw   

                        
            
                        result = [cardrelatedidtextgui]#Places the related id in an array from which it can be searchered from
                        Q17 = "SELECT cardname FROM Cards WHERE relatedid = (%s)"#Select card names with the matching related id
                        
                        if cardrelatedidtextgui == "NO98":
                            self.related_card_info_text.insert("0.0", "NO RELATED CARDS\n\n")
                        else:
                            mycursor.execute(Q17, result)#Excutes the query

                            Rcresults = []
                            for y in mycursor:#loops through the cursour
                                Rcresults.append(y)
                                print(y)#print out every thing retreievd 


                            length = len(Rcresults)#Get the length of items in the list
                            z = 0
                            while z != length:#Keeps going till it's done every item in the list
                                tuple = (Rcresults[z])#Convet each retrieved item and converts it
                                conw = convertTuple(tuple)# converts tuple into a string
                                self.related_card_info_text.insert("0.0", conw +" \n\n")
                                z = z + 1

                            self.related_card_info_text.insert("0.0", "RELATED CARDS:\n\n")
                
                    #self.card_info_text.configure(state="disabled")
                    #self.related_card_info_text.configure(state="disabled")
        except:
            self.card_info_text.delete("0.0" , "end")
            self.related_card_info_text.delete("0.0" , "end")
            self.card_info_text.insert("0.0", "CARD NOT FOUND. PLEASE CHECK HOW YOU SPELLED THE CARD NAME AND REMOVE WHITESPACES.\n\n")
            self.related_card_info_text.insert("0.0", "CARD NOT FOUND. PLEASE CHECK HOW YOU SPELLED THE CARD NAME AND REMOVE WHITESPACES.\n\n")
            script_dir = os.path.dirname(__file__) 
            image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),script_dir, "Image files")#Assiagns path to image folder to the variable
            self.no_card_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "NO CARD FOUND.jpeg")), size=(400, 540))#Assiagns the size of the Image, path and image to the variable
            
            self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.no_card_image)#creates an instance of label widget which will display an image
            self.home_frame_large_image_label.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid
    
    
    def input_button_addc_button_event(self):
        try:
            spell_trap_mon_dialog = customtkinter.CTkInputDialog(text="Please if your making a spell, trap or monster Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
            spell_trap_mon = spell_trap_mon_dialog .get_input()
            spell_trap_mon = str(spell_trap_mon)
            spell_trap_mon = spell_trap_mon.upper()

            self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
            self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox
            self.card_info_text.insert("0.0", "FOR FORRBIDEN CARDS ID ENTER ONE CODE BELOW:\n\n"
                                            + "F = Forrbidden\n\n"
                                            + "L1 = Limit 1\n\n"
                                            + "L2 = Limit 2\n\n"
                                            + "N = Not Forrbidden") #Prints text in text box

            if spell_trap_mon == "MONSTER":

                user_insert_data = []#Holds data inserted into cads table
                user_insert_data_details = []#Holds data inserted into cards details table
                

                card_name_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_name = card_name_dialog.get_input()
                card_name = str(card_name)
                user_insert_data.append(card_name)
                

                card_type_dialog = customtkinter.CTkInputDialog(text="Please enter card type of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_type = card_type_dialog.get_input()
                card_type = str(card_type)
                card_type = card_type.upper()
                user_insert_data.append(card_type)
                
                
                card_relatedid_dialog = customtkinter.CTkInputDialog(text="Please enter related id of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_relatedid = card_relatedid_dialog.get_input()
                card_relatedid = str(card_relatedid)
                user_insert_data.append(card_relatedid)
                

                card_forbiddenid_dialog = customtkinter.CTkInputDialog(text="Please enter forrbidden id of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_forbiddenid = card_forbiddenid_dialog.get_input()
                card_forbiddenid = str(card_forbiddenid)
                user_insert_data.append(card_forbiddenid)
                
                
                card_level_dialog = customtkinter.CTkInputDialog(text="Please enter level of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_level = card_level_dialog.get_input()
                card_level = int(card_level)
                user_insert_data_details.append(card_level)
                

                card_attribute_dialog = customtkinter.CTkInputDialog(text="Please enter card attribute of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_attribute = card_attribute_dialog.get_input()
                card_attribute = str(card_attribute)
                user_insert_data_details.append(card_attribute)
                

                card_att_dialog = customtkinter.CTkInputDialog(text="Please enter card attack Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_att = card_att_dialog.get_input()
                card_att = int(card_att)
                user_insert_data_details.append(card_att)
                
                
                
                card_def_dialog = customtkinter.CTkInputDialog(text="Please enter card deffence Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                card_def = card_def_dialog.get_input()
                card_def = int(card_def)
                user_insert_data_details.append(card_def)
                
                
                
                fltext_dialog = customtkinter.CTkInputDialog(text="Please enter flavour text of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                fltext = fltext_dialog.get_input()
                fltext = str(fltext)
                user_insert_data_details.append(fltext)
                
            
                #For monsters cards
                
                mycursor.execute(Q3, user_insert_data[0:5])
                last_id = mycursor.lastrowid
                mycursor.execute(Q4, [last_id,] + user_insert_data_details[0:6]) #loops through array of data and inserts them into columns from in both table linked correctly by primary and foregin key.
                

                
                self.related_card_info_text.insert("0.0", "MONSTER CARD ADDDED\n\n")
                connection.commit()

            else:
                user_insert_data = []#Holds data inserted into cads table
                user_insert_data_details = []#Holds data inserted into spelltrap details table
                

                sptcard_name_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptcard_name = sptcard_name_dialog.get_input()
                user_insert_data.append(sptcard_name)
                

                sptcard_type_dialog = customtkinter.CTkInputDialog(text="Please enter type of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptcard_type = sptcard_type_dialog.get_input()
                sptcard_type = sptcard_type.upper()
                user_insert_data.append(sptcard_type)
                

                sptcard_relatedid_dialog = customtkinter.CTkInputDialog(text="Please enter related ID of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptcard_relatedid = sptcard_relatedid_dialog.get_input()
                user_insert_data.append(sptcard_relatedid)
                

                sptcard_forbiddenid_dialog = customtkinter.CTkInputDialog(text="Please enter forbidden ID of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptcard_forbiddenid = sptcard_forbiddenid_dialog.get_input()
                user_insert_data.append(sptcard_forbiddenid)
                
                

                sptcard_speedspell_dialog = customtkinter.CTkInputDialog(text="Please enter spell speed of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptcard_speedspell = sptcard_speedspell_dialog.get_input()
                user_insert_data_details.append(sptcard_speedspell)
                

                sptfltext_dialog = customtkinter.CTkInputDialog(text="Please enter flavour text of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
                sptfltext = sptfltext_dialog.get_input()
                user_insert_data_details.append(sptfltext)
                

                #For spell cards
                mycursor.execute(Q3, user_insert_data[0:5])
                last_id = mycursor.lastrowid
                mycursor.execute(Q12, [last_id,] + user_insert_data_details[0:3]) #loops through array of data and inserts them into columns from in both table linked correctly by primary and foregin key.
                

                        
                self.related_card_info_text.insert("0.0", "SPELL OR TRAP CARD ADDDED\n\n")
                connection.commit()
        except:
            self.related_card_info_text.insert("0.0", "CARD NOT ADDED. PLEASE CHECH DETAILS ENTERED\n\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()


