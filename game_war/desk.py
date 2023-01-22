from card import Card, suits, ranks
from random import shuffle

class Desk():
    
    '''
    Hệ thống game, khởi tạo những lá bài
    '''
    def __init__(self):
        self.all_cards = []
        '''
        Khởi tạo 52 là bài
        '''
        for suit in suits:
            for rank in ranks:
                # Create the Card Object
                created_card = Card(suit=suit,rank=rank)
                self.all_cards.append(created_card)

    '''
    Xóa trộn bài
    '''
    def shuffle(self):
        shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
