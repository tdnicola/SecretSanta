import json
import random
from datetime import datetime

# Load the data from the JSON file
with open('sample.json') as f:
    santa_list = json.load(f)


def is_valid_match(gifter, recipient):
    """Check if the recipient is valid for the gifter."""
    return recipient['name'] not in [match['name'] for match in gifter['previousMatches']] and gifter['name'] != \
        recipient['name']


def create_secret_santa(santa_data):
    """Create a valid Secret Santa matching that avoids previous matches."""
    for _ in range(100):  # Retry up to 100 times to find a valid combination
        potential_matches = santa_data.copy()
        random.shuffle(potential_matches)
        secret_santa_list = []
        valid = True

        for gifter in santa_data:
            # Filter out valid recipients for the current gifter
            valid_recipients = [recipient for recipient in potential_matches if is_valid_match(gifter, recipient)]

            if not valid_recipients:
                valid = False
                break  # Restart if no valid recipient is found

            # Choose a valid recipient and remove them from the potential pool
            recipient = random.choice(valid_recipients)
            secret_santa_list.append({
                "gifter": gifter['name'],
                "gifter_phone": gifter["phone"],
                "recipient": recipient['name']
            })
            potential_matches.remove(recipient)

        if valid:
            return secret_santa_list  # Return if valid

    raise ValueError("Couldn't find a valid matching after 100 attempts. Please review the data or try again.")


def update_previous_matches(santa_data, matches, year):
    # Update the previousMatches field in santa_data based on matches, with a year record.
    for match in matches:
        for person in santa_data:
            if person['name'] == match['gifter']:
                person['previousMatches'].append({"name": match['recipient'], "year": year})

    # Save the updated data back to sample.json for next year 
    with open('sample.json', 'w') as f:
        json.dump(santa_data, f, indent=4)

current_year = datetime.now().year

while True:
    try:
        matches = create_secret_santa(santa_list)
        print("Secret Santa Matching Results:")
        for gifter in matches:
            print(f"{gifter['gifter']} (Phone: {gifter['gifter_phone']}) is giving a gift to {gifter['recipient']}")

        # Does output look okay?
        user_input = input("\nDo you want to confirm this matching? (yes/no): ").strip().lower()
        if user_input == 'yes':
            update_previous_matches(santa_list, matches, current_year)
            print("Matches have been confirmed and updated in sample.json.")

            # Ouput format for extension
            print('Copy and past below into extension:')
            print('Hello there, your Secret Santa person is {name}.')
            for gifter in matches:
                print(f"{gifter['gifter_phone']}, {gifter['recipient']} ")
            break  # Exit the loop if confirmed
        elif user_input == 'no':
            print("Reshuffling and trying again...\n")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    except ValueError as e:
        print(e)
        break  # Exit if a valid match cannot be found
