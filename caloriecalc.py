class User:
    def __init__(self, weight, goal, maximum, minimum):
        self.weight = weight
        self.goal = goal
        self.maximum = maximum
        self.minimum = minimum

class Calculator:
    def __init__(self, breakfast, lunch, dinner, snacks):
        self.breakfast = breakfast
        self.lunch = lunch
        self.dinner = dinner
        self.snacks = snacks
    def calculate(self):
        total = self.breakfast + self.lunch + self.dinner + self.snacks
        return total

class avgCalculator(Calculator):
    def __init__(self, breakfast, lunch, dinner, snacks):
        super().__init__(breakfast, lunch, dinner, snacks)
    def calculate(self):
        total = super().calculate()
        average = total / 4
        return average

def user_info():

    weight = int(input('What is your current weight?: '))
    goal = int(input('What is your goal weight?: '))
    maximum = int(input('What is your calorie maximum?: '))
    minimum = int(input('What is your calorie minimum?: '))
    return User(weight, goal, maximum, minimum)

def calorie_info():
    breakfast = int(input("Breakfast: "))
    lunch = int(input("Lunch: "))
    dinner = int(input("Dinner: "))
    snacks = int(input("Snacks: "))
    return (Calculator(breakfast, lunch, dinner, snacks), avgCalculator(breakfast, lunch, dinner, snacks))

if __name__ == "__main__":
    while True:
        print("1. Enter calorie information")
        print("2. Exit")
        choice = int(input("Enter 1 or 2: "))
        if choice == 2:
            check = False
            break

        user = user_info()
        calculator = calorie_info()
        totalcalc = calculator[0]
        average = calculator[1]
        total = totalcalc.calculate()
        avg = average.calculate()

        print("Your average calorie intake for today was", avg, "calories.")
        print("Your current weight is", user.weight, "lbs and your goal weight is ", user.goal, "lbs.")
        print("Your total calorie intake for the day was", total, "calories.")
        print("Your calorie maximum for the day is", user.maximum, "calories.")
        print("Your calorie minimum for the day is", user.minimum, "calories.")

        if (total) > user.maximum:
            print ("You are exceeding your calorie limit.")
        elif (total) < user.minimum:
            print ("You are below your calorie limit.")
        continue








