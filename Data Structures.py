#2D+ Lists

#Write a program that uses 2D lists. You should have a function named create_board with one parameter: 
# board. This function will update a 2D list such that it prints out like the below output. 
# The two characters used are the capital letters X and O, not zero. 
# A template has been included for you to start with:
    
def create_board(board):
    # Update the 2D list here
    # Repeat for all other indexes
    board[0][0] = 'X'
    board[1][1] = 'X'
    board[1][2] = 'X'
    board[2][1] = 'X'
    board[2][2] = 'X'
    # Print it out
    for row in board:
        print('{} {} {}'.format(
          row[0],
          row[1],
          row[2],
        ))

    # Return the updated board
    return board

#Write a program that will put two things in a dictionary, and return it. You should have a function named make_dict that has two parameters (use something like name, and age). It should create a dictionary with those two items, and then return the dictionary. The keys should be 'name' and 'age'.

#Here is an example of what is returned with make_dict('Bob', 36):

#{
 #   'name': 'Bob',
#  'age': 36,
#}

def make_dict(name, age):
    
    dict = {
    'name': 'bob',
    'age': '36',
}

    return dict


#Write a program that will put three things in a set, and return it. You should have a function named make_set that has three parameters (use something like x, y, z). It should create a set with those three items, and then return the set.

#Here is an example of what is returned with make_set('Bob', 'Bob', 'Sam'):

def make_set(x, y, z):
    
    set = {x, 
           y, 
           z}
    
    return set