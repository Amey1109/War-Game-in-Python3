from random import shuffle

suites = 'H D S C'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:
    def __init__(self):
        self.deck = [(suite, rank) for suite in suites for rank in ranks]
        shuffle(self.deck)

    def dealCards(self):
        return(self.deck[26:],self.deck[:26])


class Hand:
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Deck Contains {} cards".format(len(self.cards))

    def add(self,addCard):
        self.cards.extend(addCard)

    def remove(self):
        return self.cards.pop()


class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def playCard(self):
        card = self.hand.remove()
        print(self.name," has laid => ",card)
        return card

    def getWarCard(self):
        warCards=[]
        if len(self.hand.cards) < 3:
            return warCards
        else:
            for card in range(3):
                warCards.append(self.hand.cards.pop())
            return warCards

    def checkCards(self):
        if len(self.hand.cards) != 0:
            return True
        else:
            return False


D = Deck()
firstHalf,secondHalf = D.dealCards()

computer = Player("Computer",Hand(firstHalf))
player = Player("Amey",Hand(secondHalf))

totalRounds = 0
totalWar = 0


while (player.checkCards() and computer.checkCards())==True:
    totalRounds+=1

    print("\n")

    tableCards = []
    computerCard = computer.playCard()
    playerCard = player.playCard()


    if computerCard[1]==playerCard[1]:
        totalWar+=1
        print("**Its a War conditon!!**")
        tableCards.extend(player.getWarCard())
        tableCards.extend(computer.getWarCard())

        computerCard = computer.playCard()
        playerCard = player.playCard()


        tableCards.append(computerCard)
        tableCards.append(playerCard)

        if ranks.index(computerCard[1]) < ranks.index(playerCard[1]):
            print(player.name," has Won, adding card to the hand\n")
            player.hand.add(tableCards)
        else:
            print(computer.name," has Won, adding card to the hand\n")
            computer.hand.add(tableCards)

    else:
        if ranks.index(computerCard[1]) < ranks.index(playerCard[1]):
            print(player.name," has Won, adding card to the hand\n")
            player.hand.add(tableCards)
        else:
            print(computer.name," has Won, adding card to the hand\n")
            computer.hand.add(tableCards)


print("Total Rounds occured in game: ",totalRounds)
print("War occurred in game:",totalWar)


if len(computer.hand.cards) < len(player.hand.cards):
    print(player.name," has Won the Game!")
else:
    print(computer.name," has Won the Game!")



        

