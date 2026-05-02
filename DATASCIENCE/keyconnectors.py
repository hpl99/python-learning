#things to do 
# count friend and their common connections 
# like we need to do friends of friend 
# then create a list for interests and connect usrrs with common intrests 
#then take the data for the salary and diff year of work exp
#then find the avg of salry and plot the graph of it
#also using if else group them and thn find the avg slary of the groups 
#then from the interest list find the words or interest which are the most common 
#segregate them 
# take help read documenntation but tday comp

users = [
    {"id": 0, "name": "Raju"},
    {"id": 1, "name": "Amit"},
    {"id": 2, "name": "Sita"},
    {"id": 3, "name": "Rahul"},
    {"id": 4, "name": "Priya"},
    {"id": 5, "name": "Neha"},
    {"id": 6, "name": "Vikas"},
    {"id": 7, "name": "Anjali"},
    {"id": 8, "name": "Karan"},
    {"id": 9, "name": "Pooja"},
]
friendships_pairs = [
    (0, 1),
    (0, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4, 6),
    (5, 7),
    (6, 8),
    (7, 9),
    (8, 9),
    (1, 4),
    (2, 6),
]
for i in range (len(users)):
    print(users[i]["id"], users[i]["name"], friendships_pairs[i])
friendships = {user["id"]:[] for user in users }
for i , j in friendships_pairs:
    friendships[i].append(j)
    friendships[j].append(i)
for i in range(len(users)) :
    print(i,friendships[i])

def summ(user):
    user_id = user["id"]
    frd_id = friendships[user_id]
    return len(frd_id)

total = sum(summ(user) for user in users)
print (total)
num_friends = [(user["id"],summ(user)) for user in users ]
num_friends.sort(key= lambda id_and_friends:id_and_friends[1], reverse=True)

print(num_friends)