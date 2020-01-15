#dict contains the user's id and a name
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]
#list pairs of IDs, in a tuple that says that id0 is friends with id 1
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

#initialize the dict with an empty list for each user id:
friendships = {user["id"]: [] for user in users}

# and loop over the friendship pairs to populate it:
for i, j in friendship_pairs:
    friendships[i].append(j) # add j as a friend of user i
    friendships[j].append(i) # add i ad a friend of user j

def number_of_friends(user):
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)

total_connections = sum(number_of_friends(user)
                    for user in users) #24

num_users = len(users) # length of the users list
avg_connections = total_connections /num_users
# print(avg_connections) 2.4

#create a list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user))
                     for user in users]

#lambda arguments : expression

num_friends_by_id.sort(                                             # sort the list
    key = lambda id_and_friends: id_and_friends[1],                 # by num_friends
    reverse = True)                                                 # largest to smallest

