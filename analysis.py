import json

# 1. Function to load the data 
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

# 2. Display Users and their connections
def display_users_and_connections(data):
    user_names = {user["id"]: user["name"] for user in data["users"]}
    page_names = {page["id"]: page["name"] for page in data["pages"]}

    print('\n--- Users Information ---\n')

    for user in data['users']:

        friend_names = [
            user_names[friend_id]
            for friend_id in set(user['friends'])
            if friend_id in user_names
        ]

        liked_page_names = [
            page_names[page_id]
            for page_id in set(user['liked_pages'])
            if page_id in page_names
        ]

        print(
            f"ID: {user['id']}. {user['name']} is friend(s) with: "
            f"{friend_names} and likes pages: {liked_page_names}\n"
        )

# 3. Pages Information
def pages_information(data):
    print('--- Pages Information ---')
    
    for page in data['pages']:
        print(f"ID: {page['id']}. {page['name']}")

# 4. Display Information
def display_information(data, newfile):
    with open(newfile, "a") as f:

        f.write('\n--- Users Information ---\n\n')
        for user in data['users']:
            f.write(f"ID: {user['id']}. {user['name']} is friend(s) with: {list(set(user['friends']))} and likes pages: {list(set(user['liked_pages']))}\n")

        f.write('\n\n--- Pages Information ---\n\n')
        for page in data['pages']:
            f.write(f"ID: {page['id']}. {page['name']}\n")

# 5. Clean the Data if it's messy/unstrctured
def clean_data(data, filename):

    with open(filename, "w") as f:
        
        valid_user_ids = {user["id"] for user in data["users"]}
        valid_page_ids = {page["id"] for page in data["pages"]}

        for user in data["users"]:
           
            # Inactive user
            if user.get("active") == False:
                f.write(f"{user['name']} is an inactive user\n")

            # No friends
            if len(user["friends"]) == 0:
                f.write(f"{user['name']} has 0 friends\n")

            # No liked pages
            if len(user["liked_pages"]) == 0:
                f.write(f"{user['name']} doesn't like any page\n")

            # Duplicate friends
            if len(user["friends"]) != len(set(user["friends"])):
                f.write(f"{user['name']} has duplicate friends\n")

            # Duplicate liked pages
            if len(user["liked_pages"]) != len(set(user["liked_pages"])):
                f.write(f"{user['name']} has duplicate liked pages\n")

            # Self friend
            if user["id"] in user["friends"]:
                f.write(f"{user['name']} is a self friend\n")

            # Invalid friends
            for friend in user["friends"]:
                if friend not in valid_user_ids:
                    f.write(f"{user['name']} has invalid friend: {friend}\n")

            # Invalid pages
            for page in user["liked_pages"]:
                if page not in valid_page_ids:
                    f.write(f"{user['name']} has invalid page: {page}\n")

# 6. People You may know feature
def people_you_may_know(user_id, data):

    users = data["users"]

    user = next(user for user in users if user["id"] == user_id)

    recommendations = []

    for friend_id in user["friends"]:

        friend = next(user for user in users if user["id"] == friend_id)

        for person_id in friend["friends"]:

            if person_id != user_id and person_id not in user["friends"]:
                if person_id not in recommendations:
                    recommendations.append(person_id)

    for person_id in recommendations:

        person = next(user for user in users if user["id"] == person_id)

        print(person["name"])

# 7. Pages you may like
def pages_you_may_like(user_id, data):

    users = data["users"]
    pages = data["pages"]

    user = next(user for user in users if user["id"] == user_id)

    liked_pages = user["liked_pages"]
    recommendations = []

    for friend_id in user["friends"]:

        friend = next(user for user in users if user["id"] == friend_id)

        for page_id in friend["liked_pages"]:

            if page_id not in liked_pages and page_id not in recommendations:
                recommendations.append(page_id)

    for page_id in recommendations:

        page = next(page for page in pages if page["id"] == page_id)

        print(page["name"])

# Driver Code goes here...
if __name__ == "__main__":

    data = load_data("D:\\Study\\Data Science\\coders of delhi\\data.json") # Loading data using load_data function
    # display_users_and_connections(data) 
    # pages_information(data)
    # display_information(data, "D:\\Study\\Data Science\\coders of delhi\\Information.txt") # Displaying Information into a new file

    # people = people_you_may_know(2, data) # Running feature of People you may know on user id = 2
    # pages = pages_you_may_like(2, data) # Running feature of Pages you may like on user id = 2 

    data2 = load_data("D:\\Study\\Data Science\\coders of delhi\\uns_data.json") # loading messy data
    clean_data(data2, "D:\\Study\\Data Science\\coders of delhi\\messy_data_info.txt") # cleaning data
