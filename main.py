import inquirer
import json
import os
import pickle
from PIL import Image
import random
import time
import urllib.request


class Deck:

    def __init__(self, deck_name):
        self._deck_name = deck_name
        self._deck_list = []
        self._deck_size = 0
        self._deck_exists = False

    def add_card(self, card):

        # Adds Card object to Deck List and sorts alphabetically
        self._deck_list.append(card)
        self._deck_list.sort(key=lambda x: x.get_card_name())
        self._deck_size = self._deck_size + 1

    def remove_card(self, card):
        self._deck_list.remove(card)
        self._deck_size = self._deck_size - 1

    def get_deck_name(self):
        return self._deck_name

    def get_deck_list(self):
        return self._deck_list

    def get_deck_size(self):
        return self._deck_size

    def get_deck_exists(self):
        return self._deck_exists

    def set_deck_name(self, deck_name):
        self._deck_name = deck_name
        return

    def create_deck(self, deck_name):
        self._deck_name = deck_name
        self._deck_exists = True

    def delete_deck(self, deck_index):

        # Deletes Deck and refreshes SAVE SLOT name
        self._deck_name = f'SAVE SLOT {deck_index + 1}'
        self._deck_list = []
        self._deck_size = 0
        self._deck_exists = False


class Card:

    def __init__(self, set_code, set_name, card_name, card_code, card_lore, game_text, image_url):
        self._set_code = set_code
        self._set_name = set_name
        self._card_name = card_name
        self._card_code = card_code
        self._card_lore = card_lore
        self._game_text = game_text
        self._image_url = image_url

    def get_set_code(self):
        return self._set_code

    def get_set_name(self):
        return self._set_name

    def get_card_name(self):
        return self._card_name

    def get_card_code(self):
        return self._card_code

    def get_card_lore(self):
        return self._card_lore

    def get_game_text(self):
        return self._game_text

    def get_image_url(self):
        return self._image_url


class Tutorial:

    def __init__(self):

        # Tutorial text generated through static function calls
        # To add steps, add new static function to List and adjust length parameter
        self._tutorial_db = [self.tutorial_step_one(), self.tutorial_step_two(),
                             self.tutorial_step_three(), self.tutorial_step_four(),
                             self.tutorial_step_five(), self.tutorial_step_six(),
                             self.tutorial_step_seven(), self.tutorial_step_eight(),
                             self.tutorial_step_nine(), self.tutorial_step_ten()]
        self._tutorial_length = 10

    @staticmethod
    def tutorial_step_one():
        return "Welcome to the Star Wars CCG: Card Explorer and Deck Builder Application!\n" \
               "Use this tutorial to discover and learn about the features included in this application.\n\n" \
               "Features include:\n\n" \
               "- The 'Card Explorer' to browse for individual Cards\n" \
               "- The 'Search By Card Name' feature to search for a specific Card\n" \
               "- The 'Search Random Card' feature to be shown a random Card\n" \
               "- The 'Card Information Panel' to be shown information about a specific Card\n" \
               "- The 'Deck Builder' to create/rename/delete Decks from your collection\n" \
               "- The 'Exit and Save' feature to save currently created Decks\n\n" \
               "Continue the Tutorial if you wish to learn more about these individual features!"

    @staticmethod
    def tutorial_step_two():
        return "Feature: Card Explorer\n\n" \
               "Use the 'Card Explorer' to browse for individual Cards organized by their Set.\n\n" \
               "- Select 'Card Explorer' from the Main Menu\n" \
               "- Select 'Explore By Set'\n" \
               "- Select a Set by name\n" \
               "- Select a Card by name\n\n" \
               "From this 'Card Information Panel' you can learn about the Card.\n" \
               "Additional details will be covered in a future step in this Tutorial."

    @staticmethod
    def tutorial_step_three():
        return "Feature: Search by Card Name\n\n" \
               "Use the 'Search by Card Name' feature to search for an individual Card by name.\n\n" \
               "- Select 'Search by Card Name' from the Main Menu\n" \
               "- Enter the Card name (case insensitive)\n" \
               "- If the Card has been located, you will be taken to the Card Information Panel\n" \
               "- If the Card could NOT be located, the Card search will refresh\n\n" \
               "- To Return to the Main Menu, type 'Return' (case insensitive)"

    @staticmethod
    def tutorial_step_four():
        return "Feature: Search Random Card\n\n" \
               "Use the 'Search Random Card' feature to be shown a random Card from the database.\n\n" \
               "- Select 'Search Random Card' from the Main Menu\n" \
               "- Select 'Yes - Show me a card'\n" \
               "- You will be taken to the Card Information Panel of a random Card"

    @staticmethod
    def tutorial_step_five():
        return "Feature: Card Information Panel\n\n" \
               "Use the 'Card Information Panel' to learn more about an individual card.\n\n" \
               "- Select 'View Card Image' to see an image of the Card\n" \
               "- Select 'Add Card to Deck' to add the Card to a saved Deck\n" \
               "- Deck building will be covered if a future step of this Tutorial\n" \
               "- If no saved Decks exist, you will not be able to add the Card to a Deck"

    @staticmethod
    def tutorial_step_six():
        return "Feature: View Deck Lists\n\n" \
               "Use the 'View Deck Lists' feature to create and save a Deck.\n\n" \
               "- Select 'View Deck Lists' from the Main Menu\n" \
               "- There are THREE save slots for Decks\n" \
               "- Select an unused SAVE SLOT to create a new Deck\n" \
               "- Select a saved Deck to view that Deck"

    @staticmethod
    def tutorial_step_seven():
        return "Feature: Create Deck\n\n" \
               "- Selecting an unused save slot will prompt you to enter a new Deck name\n" \
               "- Once entered, this will create a new Deck with that name\n" \
               "- You will then be returned to 'View Deck Lists'"

    @staticmethod
    def tutorial_step_eight():
        return "Feature: View Deck\n\n" \
               "- Selecting a saved Deck will allow you to View/Rename/Delete that Deck\n" \
               "- Viewing a Deck shows the Cards in that Deck\n" \
               "- Renaming a Deck changes that Deck's saved name\n" \
               "- Deleting a Deck deletes that Deck and all Cards saved in it"

    @staticmethod
    def tutorial_step_nine():
        return "Feature: View Deck List\n\n" \
               "- Viewing a Deck List will show all the Cards saved in that Deck\n" \
               "- You can View/Duplicate/Delete these Cards by selecting them"

    @staticmethod
    def tutorial_step_ten():
        return "IMPORTANT: When done with the application, please select 'Save and Exit to Windows.'\n\n" \
               "This will save your created Decks for future launches of the application."

    def get_tutorial_at_index(self, tutorial_index):
        return self._tutorial_db[tutorial_index]

    def get_tutorial_length(self):
        return self._tutorial_length


class Application:

    def __init__(self):
        self._api = "https://swccgdb.com/api/public/cards/"
        self._set_db = {}
        self._card_db = {}
        self._deck_db = [Deck('SAVE SLOT 1'), Deck('SAVE SLOT 2'), Deck('SAVE SLOT 3')]
        self._deck_db_size = 0
        self._application_tutorial = Tutorial()

    @staticmethod
    def clear_terminal():
        os.system('cls' if os.name == 'nt' else 'clear')

    # Application launch pad
    def launch_application(self):
        self.display_header()
        self.load_deck_database_from_memory()
        self.write_to_listener_file()
        self.display_main_menu()

    @staticmethod
    def display_header():
        print("\nStar Wars CCG: Card Explorer and Deck Builder Application\n")

    # Loads saved Decks from pkl file in memory
    def load_deck_database_from_memory(self):
        print('LOADING... PLEASE WAIT...\n')
        if os.path.isfile('deck_db.pkl'):
            with open('deck_db.pkl', 'rb') as inp:
                self._deck_db = pickle.load(inp)
        if os.path.isfile('deck_db_size.pkl'):
            with open('deck_db_size.pkl', 'rb') as inp:
                self._deck_db_size = pickle.load(inp)

    # Writes to file that microservice listens on
    # Listens for JSON data in return
    def write_to_listener_file(self):
        file = open('fetch.txt', 'w')
        file.write(f"run\n{self._api}")
        file.close()
        time.sleep(15)
        file = open('fetch.txt', 'r')
        json_data = json.load(file)
        self.load_cards_into_database(json_data)
        file = open('fetch.txt', 'w')
        file.close()

    # Loads Cards into database from JSON data
    def load_cards_into_database(self, json_data):
        for x in json_data:
            new_card = Card(x['set_code'], x['set_name'], x['name'], x['code'], x['lore'],
                            x['gametext'], x['image_url'])
            self._card_db[x['name'].lower()] = new_card
            if x['set_name'] in self._set_db:
                self._set_db[x['set_name']].append(new_card)
            else:
                self._set_db[x['set_name']] = [new_card]

    # Main Menu (central hub) of application, selections branch from here
    def display_main_menu(self):
        self.clear_terminal()
        self.display_header()
        menu = [
            inquirer.List('options',
                          message="Please select an option",
                          choices=['Card Explorer', 'Search By Card Name', 'Search Random Card', 'View Deck Lists',
                                   'Application Information & Updates', 'Display Tutorial',
                                   'Save & Exit to Windows'], ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Card Explorer':
            self.display_card_explorer()
        elif selection['options'] == 'Search By Card Name':
            self.display_card_search()
        elif selection['options'] == 'Search Random Card':
            self.display_random_card()
        elif selection['options'] == 'View Deck Lists':
            self.display_saved_deck_lists()
        elif selection['options'] == 'Application Information & Updates':
            self.display_application_information()
        elif selection['options'] == 'Display Tutorial':
            self.display_tutorial(0)
        elif selection['options'] == 'Save & Exit to Windows':
            self.display_exit_application()

    # 'Explore by Set' only current feature, total Card list not feasible in terminal
    def display_card_explorer(self):
        self.clear_terminal()
        print('\nStar Wars CCG: Card Explorer\n')
        menu = [
            inquirer.List('options',
                          message="Please select an option",
                          choices=['Explore By Set', 'Return to Main Menu'],
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Explore By Set':
            self.display_sets()
        elif selection['options'] == 'Return to Main Menu':
            self.display_main_menu()

    # Displays names of all Sets
    def display_sets(self):
        self.clear_terminal()
        set_menu = list(self._set_db)
        set_menu.append('Return to Explorer')
        print('\nStar Wars CCG: Sets\n')
        menu = [
            inquirer.List('options',
                          message="Please select a set",
                          choices=set_menu,
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Return to Explorer':
            self.display_card_explorer()
        else:
            self.explore_sets(selection['options'])

    # Displays all Cards in selected Set
    def explore_sets(self, set_name):
        self.clear_terminal()
        print(f'\nStar Wars CCG: {set_name}\n')
        card_list = []
        for card in self._set_db[set_name]:
            card_list.append(card.get_card_name())
        card_list.append('Return to Sets')
        menu = [
            inquirer.List('options',
                          message="Please select a card",
                          choices=card_list,
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Return to Sets':
            self.display_sets()
        else:
            for card in self._set_db[set_name]:
                if card.get_card_name() == selection['options']:
                    self.display_card_information(card)

    # Search Card by name
    def display_card_search(self):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Card Search\n')
        card_name = [
            inquirer.Text('card_name',
                          message="Please enter a card name or type 'Return' to return to the Main Menu"),
        ]
        answers = inquirer.prompt(card_name)
        if answers['card_name'].lower() == 'return':
            self.display_main_menu()
        if answers['card_name'].lower() in self._card_db:
            self.display_card_information(self._card_db[answers['card_name'].lower()])
        else:
            print('\nCard Not Found - Please Try Again')
        time.sleep(2)
        self.display_card_search()

    # Displays a randomly generated Card to the user
    def display_random_card(self):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Random Card Finder\n')
        menu = [
            inquirer.List('options',
                          message='Would you like to see a random card?',
                          choices=['Yes - Show me a card', 'No - Return to Main Menu'],
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Yes - Show me a card':
            random_integer = random.randint(0, 2327)
            dict_keys = list(self._card_db)
            self.display_card_information(self._card_db[dict_keys[random_integer]])
        elif selection['options'] == 'No - Return to Main Menu':
            self.display_main_menu()

    # Displays saved Decks or empty SAVE SLOTS
    def display_saved_deck_lists(self):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Deck Lists\n')
        option1 = self._deck_db[0].get_deck_name()
        option2 = self._deck_db[1].get_deck_name()
        option3 = self._deck_db[2].get_deck_name()
        menu = [
            inquirer.List('options',
                          message='Saved Deck Lists',
                          choices=[option1, option2, option3, 'Return to Main Menu'],
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'Return to Main Menu':
            self.display_main_menu()
        else:
            self.select_deck(selection['options'])

    # If empty SAVE SLOT, prompts to create a new Deck
    # If valid Deck, displays that Deck
    def select_deck(self, deck_id):
        self.clear_terminal()
        if deck_id == 'SAVE SLOT 1' or deck_id == 'SAVE SLOT 2' or deck_id == 'SLAVE SLOT 3':
            print(f'\nStar Wars CCG: Create Deck\n')
            menu = [
                inquirer.List('options',
                              message='Deck does not exist, would you like to create one?',
                              choices=['Yes - Create a new deck', 'No - Return to Main Menu'],
                              ),
            ]
            selection = inquirer.prompt(menu)
            if selection['options'] == 'Yes - Create a new deck':
                self.create_deck(deck_id)
            else:
                self.display_main_menu()
        else:
            self.modify_deck(deck_id)

    # Creates a new Deck in an empty SAVE SLOT
    def create_deck(self, deck_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Create Deck\n')
        deck_name = [
            inquirer.Text('deck_name',
                          message="Please enter a name for your Deck or type 'Return' to return to the Main Menu"),
        ]
        selection = inquirer.prompt(deck_name)
        if selection['deck_name'].lower() == 'return':
            self.display_main_menu()
        else:
            if deck_id == 'SAVE SLOT 1':
                self._deck_db[0].set_deck_name(selection['deck_name'])
                self._deck_db[0].create_deck(selection['deck_name'])
                self._deck_db_size = self._deck_db_size + 1
                self.display_saved_deck_lists()
            elif deck_id == 'SAVE SLOT 2':
                self._deck_db[1].set_deck_name(selection['deck_name'])
                self._deck_db[1].create_deck(selection['deck_name'])
                self._deck_db_size = self._deck_db_size + 1
                self.display_saved_deck_lists()
            else:
                self._deck_db[2].set_deck_name(selection['deck_name'])
                self._deck_db[2].create_deck(selection['deck_name'])
                self._deck_db_size = self._deck_db_size + 1
                self.display_saved_deck_lists()

    # Deck view hub, provides options to modify the saved Deck
    def modify_deck(self, deck_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Modify {deck_id}\n')
        menu = [
            inquirer.List('options',
                          message='How would you like to modify existing deck?',
                          choices=['View Deck', 'Rename Deck', 'Delete Deck',
                                   'Return to Deck Lists', 'Return to Main Menu'],
                          ),
        ]
        selection = inquirer.prompt(menu)
        if selection['options'] == 'View Deck':
            self.display_deck_list(deck_id)
        elif selection['options'] == 'Rename Deck':
            self.rename_deck(deck_id)
        elif selection['options'] == 'Delete Deck':
            self.delete_deck(deck_id)
        elif selection['options'] == 'Return to Deck Lists':
            self.display_saved_deck_lists()
        else:
            self.display_main_menu()

    # Rename a saved Deck
    def rename_deck(self, deck_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Rename {deck_id}?\n')
        deck_name = [
            inquirer.Text('deck_name',
                          message="Please enter a name for your deck or type 'Return' to return to Deck View"),
        ]
        selection = inquirer.prompt(deck_name)
        if selection['deck_name'].lower() == 'return':
            self.select_deck(deck_id)
        else:
            for deck in self._deck_db:
                if deck.get_deck_name() == deck_id:
                    deck.set_deck_name(selection['deck_name'])
                    break
            print(f'\n{deck_id} renamed successfully! Returning to Deck View...')
            time.sleep(2)
            self.select_deck(selection['deck_name'])

    # Deletes a saved Deck
    def delete_deck(self, deck_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Delete {deck_id}?\n')
        confirm_selection = [
            inquirer.List('options',
                          message=f'Are you sure you would like to delete {deck_id}?',
                          choices=['Yes - Delete this Deck', 'No - Return to Deck'],
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'Yes - Delete this Deck':
            for i in range(len(self._deck_db)):
                if self._deck_db[i].get_deck_name() == deck_id:
                    self._deck_db[i].delete_deck(i)
                    self._deck_db_size = self._deck_db_size - 1
                    break
            print(f'{deck_id} deleted successfully! Returning to Deck Lists...')
            time.sleep(2)
            self.display_saved_deck_lists()
        else:
            self.select_deck(deck_id)

    # Displays all the Cards in the selected Deck
    def display_deck_list(self, deck_id):
        self.clear_terminal()
        for deck in self._deck_db:
            if deck.get_deck_name() == deck_id:
                print(f'\nStar Wars CCG: {deck_id} Deck List\n')
                print(f'Total cards in deck: {deck.get_deck_size()}\n')
                menu_list = []
                for card in deck.get_deck_list():
                    menu_list.append(card.get_card_name())
                menu_list.append('Return to Deck Lists')
                menu_list.append('Return to Main Menu')
                menu = [
                    inquirer.List('options',
                                  message=f'Cards in {deck_id}:',
                                  choices=menu_list,
                                  ),
                ]
                selection = inquirer.prompt(menu)
                if selection['options'] == 'Return to Deck Lists':
                    self.display_saved_deck_lists()
                elif selection['options'] == 'Return to Main Menu':
                    self.display_main_menu()
                else:
                    for card in deck.get_deck_list():
                        if card.get_card_name() == selection['options']:
                            self.edit_card(deck_id, card)
                            break

    # Allows the user to View/Duplicate/Remove a Card from a saved Deck
    def edit_card(self, deck_id, card_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: {card_id.get_card_name()}?\n')
        confirm_selection = [
            inquirer.List('options',
                          message='Please select an action',
                          choices=['View Card', 'Duplicate Card', 'Remove Card',
                                   f'Return to {deck_id}', 'Return to Deck Lists', 'Return to Main Menu'],
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'View Card':
            self.display_card_information(card_id, deck_id)
        elif selection['options'] == 'Duplicate Card':
            self.duplicate_card(deck_id, card_id)
        elif selection['options'] == 'Remove Card':
            self.remove_card(deck_id, card_id)
        elif selection['options'] == f'Return to {deck_id}':
            self.display_deck_list(deck_id)
        elif selection['options'] == 'Return to Deck Lists':
            self.display_saved_deck_lists()
        elif selection['options'] == 'Return to Main Menu':
            self.display_main_menu()

    # Deletes a Card from a saved Deck
    def remove_card(self, deck_id, card_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Remove {card_id.get_card_name()} from {deck_id}?\n')
        confirm_selection = [
            inquirer.List('options',
                          message='Please select an action',
                          choices=[f'Yes - Remove {card_id.get_card_name()} from {deck_id}',
                                   f'No - Return to {deck_id}'],
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == f'Yes - Remove {card_id.get_card_name()} from {deck_id}':
            for deck in self._deck_db:
                if deck.get_deck_name() == deck_id:
                    deck.remove_card(card_id)
                    print(f'Card removed successfully! Returning to {deck_id}...')
                    time.sleep(2)
                    self.display_deck_list(deck_id)
        else:
            self.edit_card(deck_id, card_id)

    # Duplicates a Card in a saved Deck
    def duplicate_card(self, deck_id, card_id):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Duplicate {card_id.get_card_name()} in {deck_id}?\n')
        confirm_selection = [
            inquirer.List('options',
                          message='Please select an action',
                          choices=[f'Yes - Duplicate {card_id.get_card_name()} in {deck_id}',
                                   f'No - Return to {deck_id}'],
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == f'Yes - Duplicate {card_id.get_card_name()} in {deck_id}':
            for deck in self._deck_db:
                if deck.get_deck_name() == deck_id:
                    deck.add_card(card_id)
                    print(f'Card duplicated successfully! Returning to {deck_id}...')
                    time.sleep(2)
                    self.display_deck_list(deck_id)
        else:
            self.edit_card(deck_id, card_id)

    # Adds a Card to a saved Deck
    def add_card(self, card):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Add Card to which Deck?\n')
        menu_options = []
        for deck in self._deck_db:
            menu_options.append(deck.get_deck_name())
        menu_options.append('Return to Card Information Panel')
        confirm_selection = [
            inquirer.List('options',
                          message='Saved Deck Lists',
                          choices=menu_options,
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'Return to Card Information Panel':
            self.display_card_information(card)
        else:
            for deck in self._deck_db:
                if deck.get_deck_name() == selection['options'] and not deck.get_deck_exists():
                    print('Not a valid Deck! Returning to Card Information Panel...')
                    time.sleep(2)
                    self.display_card_information(card)
                if deck.get_deck_name() == selection['options']:
                    deck.add_card(card)
                    print('Success! Returning to Card Information Panel...')
                    time.sleep(2)
                    self.display_card_information(card, deck.get_deck_name())

    # Displays information about the Card and the option to add it to a saved Deck
    def display_card_information(self, card, deck_id=None):
        self.clear_terminal()
        print(f'\nStar Wars CCG: {card.get_card_name()} Card Information Panel\n\n')
        print(self.card_attributes(card))
        menu_options = ['View Card Image', 'Add Card to Deck', f'Return to {card.get_set_name()}',
                        'Return to Card Search', 'Return to Random Card', 'Return to Main Menu']
        if deck_id is not None:
            menu_options.insert(2, f'Return to {deck_id}')
        confirm_selection = [
            inquirer.List('options',
                          choices=menu_options,
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'View Card Image':
            self.display_card_image(card, deck_id)
        elif selection['options'] == 'Add Card to Deck':
            if self._deck_db_size == 0:
                print('You have no saved Decks! Returning to Card Information...')
                time.sleep(2)
                self.display_card_information(card)
            else:
                self.add_card(card)
        elif selection['options'] == f'Return to {deck_id}':
            self.display_deck_list(deck_id)
        elif selection['options'] == 'Return to Card Search':
            self.display_card_search()
        elif selection['options'] == f'Return to Random Card':
            self.display_random_card()
        elif selection['options'] == f'Return to {card.get_set_name()}':
            self.explore_sets(card.get_set_name())
        elif selection['options'] == 'Return to Main Menu':
            self.display_main_menu()

    # Modifiable data to be displayed about a Card when selected
    @staticmethod
    def card_attributes(card):
        return f'Card: {card.get_card_name()}\n\n' \
               f'Card Lore: {card.get_card_lore()}\n\n' \
               f'Game Text: {card.get_game_text()}\n\n'

    # Displays a Card image to the user
    def display_card_image(self, card, deck_id):
        urllib.request.urlretrieve(card.get_image_url(), 'card_image')
        image = Image.open('card_image')
        image.show()
        self.display_card_information(card, deck_id)

    # Displays general application information to the user including recent updates
    def display_application_information(self):
        self.clear_terminal()
        print(self.display_application_information_text())
        confirm_selection = [
            inquirer.List('options',
                          message="Would you like to return to the Main Menu?",
                          choices=['Yes - Return to the Main Menu', 'No - Remain Here'],
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'Yes - Return to the Main Menu':
            self.display_main_menu()
        else:
            self.display_application_information()

    # Informational text to be displayed to the user (modify this if you wish to change it)
    @staticmethod
    def display_application_information_text():
        return '\nStar Wars CCG: Card Search and Deck Builder Application - Information & Updates\n\n' \
               'This application can be used to explore the complete Star Wars CCG\n' \
               'card database and create and edit decks.\n\n' \
               'Current features include:\n' \
               '- Exploring for an individual card sorted by set\n' \
               '- Searching for an individual card by name\n' \
               '- Searching for a random card\n' \
               '- Saving a collection of decks\n' \
               '- Creating and adding a new deck to your collection\n' \
               '- Adding individual cards to a deck in your collection\n' \
               '- Editing decks in your collection\n' \
               '- Persisting decks across application instances\n\n' \
               'Version 0.1.1\n'

    # Tutorial process entry point
    def display_tutorial(self, tutorial_index):
        self.clear_terminal()
        print(f'\nStar Wars CCG: Card Search and Deck Builder Application - Tutorial Part {tutorial_index + 1}\n')
        print(f'{self._application_tutorial.get_tutorial_at_index(tutorial_index)}\n')
        menu_options = []
        if tutorial_index < self._application_tutorial.get_tutorial_length() - 1:
            menu_options.append('Yes - Continue the Tutorial')
        if tutorial_index != 0:
            menu_options.append('No - Return to Previous Step')
        menu_options.append('No - Return to Main Menu')
        confirm_selection = [
            inquirer.List('options',
                          message="Would you like to continue the tutorial?",
                          choices=menu_options,
                          ),
        ]
        selection = inquirer.prompt(confirm_selection)
        if selection['options'] == 'Yes - Continue the Tutorial':
            self.display_tutorial(tutorial_index + 1)
        elif selection['options'] == 'No - Return to Previous Step':
            if tutorial_index == 0:
                self.display_tutorial(0)
            else:
                self.display_tutorial(tutorial_index - 1)
        else:
            self.display_main_menu()

    # Saves created Decks into memory
    def display_exit_application(self):
        self.clear_terminal()
        print()
        confirm_selection = [
            inquirer.List('options',
                          message="Would you like to exit the application?",
                          choices=['Yes - Save and Exit the Application', 'No - Return to Main Menu'],
                          ),
        ]
        confirmation = inquirer.prompt(confirm_selection)
        if confirmation['options'] == 'Yes - Save and Exit the Application':
            with open('deck_db.pkl', 'wb') as outp:
                pickle.dump(self._deck_db, outp, pickle.HIGHEST_PROTOCOL)
            with open('deck_db_size.pkl', 'wb') as outp:
                pickle.dump(self._deck_db_size, outp, pickle.HIGHEST_PROTOCOL)
            quit()
        else:
            self.display_main_menu()


# Application entry point
if __name__ == '__main__':
    appInstance = Application()
    appInstance.launch_application()
