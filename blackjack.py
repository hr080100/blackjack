"""
This is a program that plays a Black Jack game with atmost 1 user.
"""

import random

class Account: 
    """
    This is a class defined for the account of the player to keep note of the
    current amount.
    """

    def __init__(self, owner, value):
        """
        This function is the constructor and initializes the players name and
        the opening balance.
        """

        self.owner = owner
        self.value = value


    def balance(self, bet):
        """
        This function keeps account for the balance remaining with the player.
        If the player wins it adds the winning amount to the initial balance.
        If the player loses it reduces the initial balance by the lost amount.
        """

        self.value = self.value + bet
    

    def display_balance (self):
        return self.value


    def __str__(self):
        """
        This function is definition for the str function.
        """

        return str(self.value)


class DeckofCards:
    """
    This is a class that forms a set of 52 standard playing cards and
    then deals them as the game procedes.
    """
    def __init__(self, computer): 
        self.computer = computer


    def cards(self):
        """
        This function makes a list of all cards and stores it in a list called cards_52.
        """

        self.computer = "Computer"
        suite = ["♠", "♣", "♦", "♥"]
        rank = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cards_52 = []
        for i in suite:
            for j in rank:
                cards_52.append(j + i)
        return cards_52


def random_cards(cards_52):
    """
    This function chooses a random card from the cards generated
    in the cards_52 list and returns it.
    After choosing the random card it deleted it from the sequence
    cards_52 so that it is not choosen again.
    """

    random.shuffle(cards_52)
    random_card = random.choice(cards_52)
    cards_52 = cards_52.remove(random_card)
    return random_card


def cards_value(randomcard):
    """
    This function return the mathematical value of the drawn card.
    """

    card_value = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
                  "6": 6, "7": 7, "8": 8, "9": 9, "1": 10, "J": 10,
                  "Q": 10, "K": 10}
    return card_value[randomcard[0]]


def blackjack():
    """
    This function plays the blackjack game.
    """

    # Creating an instance of the DeckofCards class.
    deckofcards = DeckofCards("computer")

    # Initializing betting value which is to be altered by asking from the user
    # for their desired betting value.
    betting = account.display_balance() + 1

    # The below while loop ensures that the betting value is within the
    # playing balance.
    while (betting > account.display_balance()):
        print(owner_name.title(), "how much would you like to bet with ?")
        betting = float(input("$ "))
        if betting > account.display_balance():
            print("\nPlease enter a value within your playing balance of $", account)
        elif betting <= 0:
            betting = account.display_balance() + 1
            print("\nPlease enter a value more than 0 and within your playing balance of $",
                account)
    print("")
    print("")

    # Changing the value of user balance.
    account.balance(-1 * betting)

    # Starting the game
    print("Come on", owner_name.title(), "let's get started !!!")
    print("")

    # Making a shuffled deck of 52 standard cards.
    cards_deck = deckofcards.cards()

    # Dealing the first four cards - two of the user and two for the computer.
    user_dealt_cards = []
    for deal in range(0, 2):
        user_dealt_cards.append(random_cards(cards_deck))
    computer_dealt_cards = []
    for deal in range(0, 2):
        computer_dealt_cards.append(random_cards(cards_deck))

    # Initializing the user's and computer's current card value sum to zero.
    current_user_sum = 0
    current_computer_sum = 0

    # Printing the first deal of the user and the current user card value sum.
    print(owner_name.title(), "your first deal is: \n    ", user_dealt_cards[0],
    "    ", user_dealt_cards[1])
    for deal_sum in range(0, len(user_dealt_cards)):
        current_user_sum += cards_value(user_dealt_cards[deal_sum])
    if current_user_sum > 21:
        current_user_sum -= 10
    print("Your current card value sum is:" ,current_user_sum, "\n")

    # Printing the first deal of the computer and the current computer card value sum.
    print("First deal of computer is: \n    ", computer_dealt_cards[0], "     **")
    current_computer_sum += cards_value(computer_dealt_cards[0])
    print("Computer's current card value sum is :", current_computer_sum)
    print("")

    # The current card value sum can never be more than 21 in the first two deals.
    # Checking if the user current sum is equal to 21.
    # If it is then the stopping the game and tell them that they have won.
    if current_user_sum == 21:
        print(owner_name.title(), "you have won !!!")
        print("Total sum that you win is :-\nYour Initial bet : $", betting,
        "\nYour winning amount : $", (1.5 * betting))
        account.balance(betting + 1.5 * betting)
        print("Renewed Balance = $", account)
        print("\n")

    # If the user current sum is not equal to 21.
    # Asking the user for their next move.
    # If the user inputs "h" then card are dealt to the user until the press a "s".
    else:
        # Creating a boolean which will be needed to alter the value of an ace from 11 to 1
        # if the current_user_sum or current_computer_sum exceeds 21.
        user_ace_counter = True
        computer_ace_counter = True

        # Creating a boolean that keeps the while loop running for inputs values of the user
        # for hit or stay.
        counter_boolean = True

        # Creating the string that stores the input from the user for their next move.
        next_move = ""

        # Starting the input while loop.
        while (counter_boolean):

            # Asking the user for the input of their next move.
            print(owner_name.title(), "what will be your next move :\n1) Hit(h)\n   or\n2) Stay(s)?")

            # Converting the input to lower so not to duplicate check statements in if-else statement.
            next_move = input("\n(h/s) ? ").lower()
            print("")

            # Checking if input is "h" for hit.
            if next_move == "h":

                # Dealing a new card to user and printing all of their dealt cards.
                user_dealt_cards.append(random_cards(cards_deck))
                print(owner_name.title(), "your deal is: ")
                for deal in range (0, len(user_dealt_cards)):
                    print("    ", user_dealt_cards[deal], end="    ")

                # Adding the current_user_sum of the new card.
                current_user_sum += cards_value(user_dealt_cards[deal])

                # Checking if the dealt cards contain an ace and is the value exceeding 21
                # and it it is exceeding 21 the reducing it by 10 to count the value of ace as 1.
                # making the ace counter false here so that any ace should not be counted twice.
                if current_user_sum > 21 and user_ace_counter:
                    for count in range (0, len(user_dealt_cards)):
                        if user_dealt_cards[count][0] == "A":
                            current_user_sum -= 10
                            user_ace_counter = False
                            break

                # Printing the new current_user_sum
                print("\nYour current card value sum is:" ,current_user_sum, "\n")

                # Printing the computer dealt cards.
                print("First deal of computer is: \n    ", computer_dealt_cards[0], "     **")
                print("Computer's current card value sum is :", current_computer_sum)
                print("")

                # Checking if the sum is greater than 21 it it is the telling that user busted.
                if current_user_sum > 21:
                    print(owner_name.title(), "you are busted !!!")
                    counter_boolean = False

            # Checking if the input is "s" for stay.
            elif next_move == "s":

                # Printing the final user_dealt_cards and current_user_sum.
                print(owner_name.title(), "your deal is: ")
                for deal in range (0, len(user_dealt_cards)):
                    print("    ", user_dealt_cards[deal], end="    ")
                print("\nYour current card value sum is:" ,current_user_sum)
                print("")

                # Printing the second dealt card of the computer for the first time and
                # the new current_computer_sum.
                print("Computer's deal is: \n    ", computer_dealt_cards[0], "    ", computer_dealt_cards[1])
                current_computer_sum += cards_value(computer_dealt_cards[1])
                if current_computer_sum > 21:
                    current_computer_sum -= 10
                print("Computer's current card value sum is :", current_computer_sum)
                print("")

                # Checking the various conditions for winning and losing of the user.
                # First case when both sum are 21.
                # If this happens the user loses.
                if current_user_sum == 21 and current_computer_sum == 21:
                    print("Computer's deal is: \n    ", computer_dealt_cards[0], "    ", computer_dealt_cards[1])
                    print("Computer's current card value sum is :", current_computer_sum)
                    print("")
                    print(owner_name.title(), "you lose. Sorry !!!")
                    counter_boolean = False

                # Second case when current_user_sum is 21 and current_computer_sum is less than 21.
                # If this happens the user wins.
                elif current_user_sum == 21 and current_computer_sum < 21:
                    print("Computer's deal is: \n    ", computer_dealt_cards[0], "    ", computer_dealt_cards[1])
                    print("Computer's current card value sum is :", current_computer_sum)
                    print("")
                    print(owner_name.title(), "you have won !!!")
                    print("Total sum that you win is :-\nYour Initial bet : $", betting,
                    "\nYour winning amount : $", betting)
                    account.balance(2 * betting)
                    print("Renewed Balance = $", account)
                    print("\n")
                    counter_boolean = False

                # Third case when current_user_sum is less than 21 and current_computer_sum is less
                # than equal to 16.
                # If this happens check for three sub cases.
                elif current_user_sum < 21 and current_computer_sum <= 16:

                    # Deal another card to the computer and then print it and new
                    # current_computer_sum.
                    computer_dealt_cards.append(random_cards(cards_deck))
                    current_computer_sum += cards_value(computer_dealt_cards[2])
                    if current_computer_sum > 21 and computer_ace_counter:
                        for count in range (0, len(user_dealt_cards)):
                            if user_dealt_cards[count][0] == "A":
                                current_user_sum -= 10
                                computer_ace_counter = False
                                break
                    print("Computer's deal is: ")
                    for deal in range (0, len(computer_dealt_cards)):
                        print("    ", computer_dealt_cards[deal], end="    ")
                    print("\nComputer's current card value sum is :", current_computer_sum)
                    print("")

                    # Checking if current_computer_sum is less than current_user_sum.
                    # If this happens the user wins.
                    if current_computer_sum < current_user_sum:
                        print(owner_name.title(), "you have won !!!")
                        print("Total sum that you win is :-\nYour Initial bet : $", betting,
                        "\nYour winning amount : $", betting)
                        account.balance(2 * betting)
                        print("Renewed Balance = $", account)
                        print("\n")
                        counter_boolean = False

                    # Checking if current_user_sum is less than current_computer_sum
                    # and current_computer_sum is less than 21.
                    # If this happens then user loses.
                    elif current_user_sum < current_computer_sum and current_computer_sum < 21:
                        print(owner_name.title(), "you lose. Sorry !!!")
                        counter_boolean = False

                    # Checking if current_user_sum is less than current_computer_sum
                    # and current_computer_sum is less than 21.
                    # If this happens then user wins.
                    elif current_user_sum < current_computer_sum and current_computer_sum > 21:
                        print("Computer has been busted !!!\n")
                        print(owner_name.title(), "you have won !!!")
                        print("Total sum that you win is :-\nYour Initial bet : $", betting,
                        "\nYour winning amount : $", betting)
                        account.balance(2 * betting)
                        print("Renewed Balance = $", account)
                        print("\n")
                        counter_boolean = False

                # Fourth case when current_user_sum is less than 21 and current_computer_sum is
                # more than 16.
                # If this happens check for two sub cases.
                elif current_user_sum < 21 and current_computer_sum > 16:

                    # Checking if current_computer_sum is less than current_user_sum.
                    # If this happens the user wins.
                    if current_computer_sum < current_user_sum:
                        print(owner_name.title(), "you have won !!!")
                        print("Total sum that you win is :-\nYour Initial bet : $", betting,
                        "\nYour winning amount : $", betting)
                        account.balance(2 * betting)
                        print("Renewed Balance = $", account)
                        print("\n")
                        counter_boolean = False

                    # Checking if current_computer_sum is more than current_user_sum.
                    # If this happens the user loses.
                    elif current_user_sum < current_computer_sum:
                        print(owner_name.title(), "you lose. Sorry !!!")
                        counter_boolean = False

            # If the input was neither "h" nor "s" the counter_boolean is not changed to false
            # and the while loop continues.
            else:
                print("Please input a valid key (h/s)")

    # Making another boolean value to run a while loop that asks user if they want to continue
    # playing or quit.
    count_boolean = True

    # Creating a string that stores the user value for yes or no.
    play_again = ""

    # Starting the while loop
    while (count_boolean):

        # Asking the user if they want to continue playing or not.
        print("Do you want to play again (y/n) ?")
        play_again = input("(y/n) ?").lower()
        print("")

        # If the input is "y" then checking two subcases.
        if play_again == "y":

            # Checking if account balance is greater thanzero or not.
            # If not then calling the blackjack function again.
            if account.display_balance() > 0:
                blackjack()

            # If it is zero then telling the user to start again with more sum.
            else:
                print(owner_name.title(), "your playing balance is zero")
                print("Please start again with more balance")
                count_boolean = False

        # If the input is "n" then exiting the game.
        elif play_again == "n":
            count_boolean = False
            print("Sorry to see you go", owner_name.title(), ".\nGood Bye.")

        # If the input is neither "y" nor "n" then the count -boolean is not set
        # false and the while loop continues to run.
        else:
            print("Please input a valid key (y/n)")


# Greeting the user.
print("Welcome to Black Jack !!!\n")

# Asking the user for their name and initial balance.
owner_name = input("What is your name ?\n")
print("")
print(owner_name.title(), "how much money would you like to start with ?")
initial_value = float(input("$ "))
print("")

# Creating an instance of the Account class.
account = Account(owner_name, initial_value)

# Calling the blackjack function that runs the game.
blackjack()