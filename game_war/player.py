class Player():
    def __init__(self, name):
        self.name = name
        self.all_card = []

    def remove_one(self):
        return self.all_card.pop(0)
    
    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # win war
            self.all_card.extend(new_cards)
        else:
            self.all_card.append(new_cards)
    
    def __str__(self):
        return f"Player {self.name} has {len(self.all_card)} cards"
