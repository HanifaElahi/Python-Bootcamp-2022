#class User:
#    pass # dont have something now. just continue to next line of code


# Creating object
#user_1 = User()

# Adding Attributes
#user_1.id = "SE-001"
#user_1.username = "Hanifa Elahi"
#print(user_1.id)
#print(user_1.username)

# Creating object
#user_2 = User()

# Adding Attributes
#user_2.id = "SE-002"
#user_2.username = "Maroof Elahi"
#print(user_2.id)
#print(user_2.username)

# In this scenario, whenever we create any object we must provide user id and username

#### The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. ####

class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0 # we can also initialize or set value to default which could be updated 
        self.following = 0

    def follow(self, user):
        user.followers += 1
        user.following += 1

user_1 = User("SE-001", "Hanifa Elahi")
print(user_1.id, user_1.username, user_1.followers)

user_2 = User("SE-002", "Maroof Elahi")
print(user_2.id, user_2.username, user_2.followers)

user_1.follow(user_2)
print(user_1.followers, user_1.following)
print(user_2.followers, user_2.following)
        