
from item_operations import insert_item_to_dynamodb
from saveToDB import random_pokemon, check_if_pokemon_in_database

def main():


    while True:
        userValue = input("Would you like to draw a Pokemon? yes/ no?: ").lower()
        if userValue == 'yes':
            random_pokemon_name = random_pokemon()
            check_if_pokemon_in_database(random_pokemon_name)
            break
        elif userValue == 'no':
            print('Goodbye, exiting...')
            break
        
        else:
            print('Enter only yes or no')

main()

if __name__ == "__main__":
    main()