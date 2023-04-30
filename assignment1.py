"""
Replace the contents of this module docstring with your own details
Name:Hu Xiao
Date started:23/04/2023
GitHub URL:https://github.com/Hx010416/Assignment1
"""
import csv
import random


def main():
    print("Travel Tracker 1.0 - by HuXiao")
    places = load_places_from_file('places.csv')
    while True:
        display_menu()
        choice = get_valid_choice()
        if choice == 'Q':
            print("Goodbye!")
            save_places_to_file('places.csv', places)
            break
        elif choice == 'L':
            display_places(places)
        elif choice == 'R':
            recommend_place(places)
        elif choice == 'A':
            add_place(places)
        elif choice == 'M':
            mark_visited(places)


def load_places_from_file(filename):
    places = []
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            place = {'name': row[0], 'country': row[1], 'priority': int(row[2]), 'visited': False}
            places.append(place)
    return places


def save_places_to_file(filename, places):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            writer.writerow([place['name'], place['country'], place['priority']])


def display_menu():
    print("\nMenu:")
    print("[L] List places")
    print("[R] Recommend a place to visit")
    print("[A] Add a place")
    print("[M] Mark a place as visited")
    print("[Q] Quit")


def get_valid_choice():
    choice = input("Enter your choice: ")
    while choice.upper() not in ['Q', 'L', 'R', 'A', 'M']:
        print("Invalid choice.")
        choice = input("Enter your choice: ")
    return choice.upper()


def display_places(places):
    longest_name_length = max(len(place['name']) for place in places)
    longest_country_length = max(len(place['country']) for place in places)
    print(f"\n{'Name':<{longest_name_length}} {'Country':<{longest_country_length}} {'Priority'} {'Visited'}")
    for place in places:
        visited_mark = '' if not place['visited'] else 'X'
        unvisited_mark = '*' if not place['visited'] else ''
        print(f"{place['name']:<{longest_name_length}} {place['country']:<{longest_country_length}} {place['priority']} {unvisited_mark}{visited_mark}")
    num_unvisited_places = len([place for place in places if not place['visited']])
    if num_unvisited_places == 0:
        print("No unvisited places.")


def recommend_place(places):
    unvisited_places = [place for place in places if not place['visited']]
    if unvisited_places:
        random_place = random.choice(unvisited_places)
        print(f"\nYou should visit {random_place['name']}, {random_place['country']}.")
    else:
        print("No places left to visit!")


def add_place(places):
    name = input("Enter the place name: ")
    while not name:
        print("Name cannot be blank.")
        name = input("Enter the place name: ")
    country = input("Enter the country name: ")
    while not country:
        print("Country cannot be blank.")
        country = input("Enter the country name: ")
    priority = input("Enter the priority (1-5): ")
    while not priority.isdigit() or int(priority) not in range(1, 6):
        print("Priority must be a number between 1and 5.")
    place = {'name': name, 'country': country, 'priority': int(priority), 'visited': False}
    places.append(place)
    print(f"{place['name']}, {place['country']} (priority {place['priority']}) added to Travel Tracker.")

def mark_visited(places):
    unvisited_places = [place for place in places if not place['visited']]
    if unvisited_places:
        display_places(places)
    choice = input("Enter the number of a place to mark as visited: ")
    while not choice.isdigit() or int(choice) not in range(1, len(places) + 1):
        print("Invalid choice. Please enter a number between 1 and", len(places))
        choice = input("Enter the number of a place to mark as visited: ")
        place_to_mark = places[int(choice) - 1]
        place_to_mark['visited'] = True
        print(f"{place_to_mark['name']}, {place_to_mark['country']} marked as visited.")
    else:
        print("No unvisited places.")

def save_places_to_file(filename, places):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for place in places:
            visited_status = 'v' if place['visited'] else 'n'
            writer.writerow([place['name'], place['country'], place['priority'], visited_status])


if __name__ == '__main__':
    main()

