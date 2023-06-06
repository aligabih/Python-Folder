import random

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan', 'In my childhood', 'During the Renaissance']
who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat', 'a lion', 'a penguin']
name = ['Ali', 'Miriam', 'Daniel', 'Hoouk', 'Starwalker', 'Samantha', 'Max']
residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England', 'Australia', 'Japan']
went = ['cinema', 'university', 'seminar', 'school', 'laundry', 'restaurant', 'beach']
happened = ['made a lot of friends', 'ate a burger', 'found a secret key', 'solved a mystery', 'wrote a book', 'discovered a hidden treasure', 'won a championship']

print(
    random.choice(when) + ', ' +
    random.choice(who) + ' named ' +
    random.choice(name) + ', who lived in ' +
    random.choice(residence) + ', went to the ' +
    random.choice(went) + ' and ' +
    random.choice(happened)
)
