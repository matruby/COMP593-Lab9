# COMP 593 Lab 9 

from tkinter import * 
from tkinter import ttk
from tkinter import messagebox
from pokeapi import fetch_poke_info

class PokeViewer:
    """Class to initialize tkinter"""
    def __init__(self, master):
        """
        Gui Initialization
        """
        self.root = master 
        self.root.configure(bg='#303f46')
        self.root.title('Poke_Viewer')
        self.root.iconbitmap("pokeball.ico")
        self.root.resizable(False, False)


    def searchFrame(self):
        """
        Create the search frame and place objects into the search frame
        """
        # Define the search frame and place it in root
        self.search_frame = Frame(self.root, bg='#263238')
        self.search_frame.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Define the search frame widgets 
        self.name_label = Label(self.search_frame, 
                                text='Pokemon Name:', 
                                font=('Open Sans', 12, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                )       
                               
        self.pokemon_name_entry = Entry(self.search_frame, 
                                        width=20, 
                                        justify='center',
                                        )
        
        self.search_button = Button(self.search_frame, 
                                    text='Get Info',
                                    font=('Open Sans', 9),
                                    bg='#263238',
                                    fg='white',
                                    padx=15,
                                    command=self.getPokemonInfo
                                    )

        # Place the widgets in the search frame
        self.name_label.grid(row=0, column=0, padx=(20, 5), pady=10)
        self.pokemon_name_entry.grid(row=0, column=1)
        self.search_button.grid(row=0, column=2, padx=(10, 20))


    def infoFrame(self):
        """
        Create the info frame and add widgets to the info frame
        """
        # Define the info frame and place it in root
        self.info_frame = Frame(self.root, bg='#263238')
        self.info_frame.grid(row=1, column=0, padx=(20, 10), pady=(10, 20), sticky=N)
        
        # Define the Label widgets 
        self.height_label = Label(self.info_frame,
                                text='Height: ', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
        
        self.height_value = Label(self.info_frame,
                                text='TBD', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
    
        self.weight_label = Label(self.info_frame,
                                text='Weight: ', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
        self.weight_value = Label(self.info_frame,
                                text='TBD', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
        
        self.type_label = Label(self.info_frame,
                                text='Height: ', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
        self.type_value = Label(self.info_frame,
                                text='Height: ', 
                                font=('Open Sans', 8, 'bold'), 
                                bg='#263238', 
                                fg='White',
                                 )
      
        # Place the widgets in the info frame 
        self.height_label.grid(row=0, column=0, padx=10, pady=5)
        self.weight_label.grid(row=1, column=0, padx=10, pady=5)
        self.type_label.grid(row=2, column=0, padx=10, pady=5)
        self.height_value.grid(row=0, column=1, padx=10, pady=5)
        self.weight_value.grid(row=1, column=1, padx=10, pady=5)
        self.type_value.grid(row=2, column=1, padx=10, pady=5)

    def statsFrame(self):
        """
        Create the stats frame and add widgets to the stats frame
        """
        # Define the stats frame and place it in root
        self.stats_frame = Frame(self.root, bg='#263238')
        self.stats_frame.grid(row=1, column=1, padx=(20, 10), pady=(10, 20))


        # Define the widgets for the stats frame 
        self.hp_label = Label(self.stats_frame,
                        text='HP: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                            )
        self.hp_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )
        
        self.attack_label = Label(self.stats_frame,
                        text='Attack: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                            )
        
        self.attack_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )
        
        self.defense_label = Label(self.stats_frame,
                        text='Defense: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                            )
        
        self.defense_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )
        
        self.special_attack_label = Label(self.stats_frame,
                        text='Special Attack: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                        )
        
        self.special_attack_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )
        
        self.special_defense_label = Label(self.stats_frame,
                        text='Special Defense: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                            )
        
        self.special_defense_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )
        

        self.speed_label = Label(self.stats_frame,
                        text='Speed: ', 
                        font=('Open Sans', 8, 'bold'), 
                        bg='#263238', 
                        fg='White',
                            )
        
        self.speed_bar = ttk.Progressbar(self.stats_frame,
                                    orient=HORIZONTAL,
                                    length=200,
                                    maximum=255,
                                      )

        # Place the labels in the stats frame 
        self.hp_label.grid(row=0, column=0)
        self.attack_label.grid(row=1, column=0)
        self.defense_label.grid(row=2, column=0)
        self.special_attack_label.grid(row=3, column=0)
        self.special_defense_label.grid(row=4, column=0)
        self.speed_label.grid(row=5, column=0)

        # Place the progress bars in the stats frame
        self.hp_bar.grid(row=0, column=1, padx=(0, 20), pady=(10, 5))
        self.attack_bar.grid(row=1, column=1, padx=(0, 20), pady=5)
        self.defense_bar.grid(row=2, column=1, padx=(0, 20), pady=5)
        self.special_attack_bar.grid(row=3, column=1, padx=(0, 20), pady=5)
        self.special_defense_bar.grid(row=4, column=1, padx=(0, 20), pady=5)
        self.speed_bar.grid(row=5, column=1, padx=(0, 20), pady=(5, 10))
    
    def getPokemonInfo(self):
        """
        Handles the pokemon information grabbing if the button is pressed
        """
        # Get the input from the Entry widget 
        user_input = self.pokemon_name_entry.get()

        # Check to make sure input was given 
        if user_input: 
            # Clear whitespace from input
            user_input = user_input.strip()
            # Try to request that pokemon 
            poke_info = fetch_poke_info(user_input)

            # Check if the search was a valid pokemon 
            if poke_info:
                # Add information in for the info_frame
                self.height_value['text'] = f"{(int(poke_info['height']) / 10)} m"
                self.weight_value['text'] = f"{(int(poke_info['weight']) / 10)} kg"
                
                # Pokemon types 
                types = [poke['type']['name'].title() for poke in poke_info['types']]
                
                # Add the type(s) to the type_value label 
                if len(types) == 1 :
                    self.type_value['text'] = types[0]
                else:
                    self.type_value['text'] = ', '.join(types)

                # Add information to the stats_frame 
                self.hp_bar['value'] = poke_info['stats'][0]['base_stat']
                self.attack_bar['value'] = poke_info['stats'][1]['base_stat']
                self.defense_bar['value'] = poke_info['stats'][2]['base_stat']
                self.special_attack_bar['value'] = poke_info['stats'][3]['base_stat']
                self.special_defense_bar['value'] = poke_info['stats'][4]['base_stat']
                self.speed_bar['value'] = poke_info['stats'][5]['base_stat']
            else:
                # Give a message box if the search failed 
                search_failed = f"Unable to get information on {user_input.title()} from the PokeAPI"
                messagebox.showinfo(title='Not Found!', message=search_failed, icon='error')
                    

if __name__ == '__main__':
  # Create the tk object 
  root = Tk()
  # Instantiate the PokeViewer class with tk object 
  gui = PokeViewer(root)

  # Create the frames with methods of the PokeViewer
  gui.searchFrame()
  gui.infoFrame()
  gui.statsFrame()
  
  # Look for events by looping 
  root.mainloop()

