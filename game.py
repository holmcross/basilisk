import random

class Deck:

    ## MEMBERS
    MASTER_DECK_STRING = None

    deck_list = None
    graveyard = None
    exile = None
    sideboard = None


    ## METHODS
    def __init__(self, card_list):
        super().__init__()

        self.MASTER_DECK_STRING = card_list
        self.deck_list = card_list.split()
        self.shuffle()


    def shuffle(self):
        print("Shuffling...")
        temp_list = self.deck_list
        new_deck = []
        for i in range(len(self.deck_list)):
            index = random.randint(0, len(temp_list)-1)
            new_deck.append( temp_list.pop(index) )
        self.deck_list = new_deck
        print(self.deck_list)
    
    def draw(self, draw_value):
        print("Drawing " + str(draw_value) + "...")

    def scry(self, scry_value):
        print("Scrying " + str(scry_value) + "...")
    
    def mill(self, mill_value):
        print("Milling " + str(mill_value) + "...")

    def tutor(self, tutor_list):
        print("Searching for " + tutor_list[0] + "...")

    def send_to_top(self, card_list):
        print("Returning card(s) to top of library...")

    def send_to_bottom(self, card_list):
        print("Returning card(s) to bottom of library...")

class Card:
    card_name: None
    owner: None
    controller: None
    cmc: None
    mana_cost: None
    alternate_cost: False
    color: None

    def __init__(self):
        print("Hello from the superclass")
        

class Creature(Card):

    def __init__(self):
        super().__init__(self)


            
        
class Player:
    hitpoints = None
    player_deck = None
    cards_in_play = None
    cards_in_hand = None
    

        
## MAIN PROGRAM

cards = "swamp forest mountain"
print(cards)

x = Deck(cards)
y = Card()