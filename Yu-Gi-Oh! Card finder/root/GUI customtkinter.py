import tkinter
import os
import os.path
from PIL import Image, ImageTk
import tkinter.messagebox
import customtkinter

#Set's the appearance of application including widgets
customtkinter.set_appearance_mode("System") # Set the backgroud of app to dark mode
customtkinter.set_default_color_theme("blue") #Set the themes of the widgets to blue

class ToplevelWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("1250x780")
        self.title("How to use")
        self.wm_iconbitmap('icon2.ico')

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

        self.title("Yu-Gi-Oh card finder")#Sets the title of the application
        self.geometry("800x800")#set the width and size of application in minmized mode
        self.wm_iconbitmap('icon2.ico')

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
        
        #Info for the user buttun
        self.howtoplaybutton_1 = customtkinter.CTkButton(self.navigation_frame, text="How to play", command=self.open_toplevel)
        self.howtoplaybutton_1.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.toplevel_window = None

        self.input_button_searchc = customtkinter.CTkButton(self.navigation_frame, text="Card Search", command=self.input_button_searchc_button_event)# creates a button
        self.input_button_searchc.grid(row=0, column=0, padx=10, pady=10)#places button within the grid
        
        self.input_button_addc = customtkinter.CTkButton(self.navigation_frame, text="Add a card", command=self.input_button_addc_button_event)# creates a button
        self.input_button_addc.grid(row=1, column=0, padx=10, pady=10)#places button within the grid

        
        self.flist_button_1 = customtkinter.CTkButton(self.navigation_frame,text="Forbidden List", command=self.flist_button_event)#creates a button
        self.flist_button_1.grid(row=2, column=0, padx=10, pady=(10,10))#places button within the grid
        
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
    
    def flist_button_event(self): #prints the text
        print("It works!!!!")
        self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
        self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox
        self.home_frame_large_image_label2 = customtkinter.CTkLabel(self.home_frame, text="", image=self.fl_image)#creates an instance of label widget which will display an image
        self.home_frame_large_image_label2.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid
        self.card_info_text.insert("0.0", "FORRBIDEN CARDS\n\n" + "Archnemeses Protos \n\n" 
        + "Blackwing - Gofu the Vague Shadow\n\n" 
        + "Blaster\n\n"
        +"Block Dragon\n\n"
        + "Dragon Ruler of Infernos Block Dragon\n\n" ) #Prints text in text box
    
    def input_button_searchc_button_event(self):
        search_card_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Card search")# Opens a mini window that allows vaules to be inputted
        search_card = search_card_dialog.get_input()#Assaigns input from user
        search_card = str(search_card)
        photo_search = (search_card.lower()+ ".png")
        print(search_card)
        Cd = ("7")

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)),"C:\\Users\jedib\Documents\School\Computer Science\Coursework\OneDrive_1_04-02-2023\Image files")#Assiagns path to image folder to the variable
        self.searchered_card_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, photo_search)), size=(400, 540))#Assiagns the size of the Image, path and image to the variable
        
        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.searchered_card_image)#creates an instance of label widget which will display an image
        self.home_frame_large_image_label.grid(row=1, column=1, padx=20, pady=10)#Places it within a specfic place image label grid

        #print("The card searched for", dialog.get_input())#prints inputed dialog
        self.card_info_text.delete("0.0" , "end")#clears the text in card_info_text textbox
        self.related_card_info_text.delete("0.0" , "end")#clears the text in related_card_info_text textbox
        self.card_info_text.insert("0.0", "Blue-Eyes White Dragon\n\n" + "Attribute: Light\n\n"#Prints text i////n text box 
        + "Card level: " + Cd + " \n\n"
        + "ATK: 3000\n\n" 
        + "DEF: 2500\n\n"
        + "Dragon / Normal\n\n"
        + "Card Text: This legendary dragon is a powerful engine of destruction. Virtually invincible, very few have faced this awesome creature and lived to tell the tale.\n\n" ) 
        self.related_card_info_text.insert("0.0", "REALATED CARDS:\n\n" + "Beacon of White\n\n"
        + "Bingo Machine, Go!!!\n\n" 
        + "Blue-Eyes Abyss Dragon\n\n"
        + "Blue-Eyes Alternative Ultimate Dragon\n\n"
        + "Blue-Eyes Alternative White Dragon\n\n")
        
        #self.card_info_text.configure(state="disabled")
        #self.related_card_info_text.configure(state="disabled")
        
    
    def input_button_addc_button_event(self):
        card_name_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        card_name = card_name_dialog.get_input()
        card_name = str(card_name)
        print("The card added", card_name)#prints inputed dialog
        
        #card_level_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #card_level = card_name_dialog.get_input()
        #card_level = str(card_level)
        
        #card_attribute_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #card_attribute = card_name_dialog.get_input()
        #card_attribute = str(card_attribute)

        #card_att_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #card_att = card_name_dialog.get_input()
        #card_att = str(card_att)
        
        #card_def_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #card_def = card_name_dialog.get_input()
        #card_def = str(card_def)
        
        #fltext_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #fltext = card_name_dialog.get_input()
        #fltext = str(fltext)
        
        #card_type_dialog = customtkinter.CTkInputDialog(text="Please enter name of Yu-Gi-Oh! Card:", title="Add a card")# Opens a mini window that allows vaules to be inputted
        #card_type = card_name_dialog.get_input()
        #card_type = str(card_type)
        
        


if __name__ == "__main__":
    app = App()
    app.mainloop()


