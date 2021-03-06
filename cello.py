# first I will create my own custom errors for user inputs

# my own defined exceptions for custom errors that I will use later
class Error(Exception):
    """Base class for other exceptions"""
    pass

class LeapYearError(Error): # for when feb has 29 days in a non leap year
    """Raised when february 29th is input on a non_leap year"""
    pass

# Next we start writting the program 
# Get year first
# limited the years to 1500-2020 just for test purpose

while True:
    try:
        birth_year = int(input("Enter your year of birth: "))
        if birth_year < 1500 or birth_year > 2020:  # limiting the years
            raise ValueError
        break
    except ValueError:  #error message shown when user inputs a value not within range
        print("Sorry that is not a valid year")

# function for calculating if input year is a leap year
def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

# first we get the values before executing the formula 
# Getting the birth month
while True:
    try:
        birth_month = int(input("Enter your birth month as a number between 1-12 : ")) # Placeholder message to the user
        if birth_month < 1 or birth_month > 12: #limiting the birthmonth to 12 since we only have 12 months
            raise ValueError
        break
    except ValueError:    # to prevent from strings and floats
        print("Sorry, that is not a valid Month. Birth month must be between 1-12")

# Next we get the date of birth from the user
# we also have to factor in the number of days each month has  or we might get errors
# E.g February has 28 or 29 days, January, March, May, July, August, october and dec have 31 days while others have 30

# we can create a dictionary to reference the keys for the birth months below
# #### this is not compulsory, just creating it to help with clarity when writting ...
# #### error messages to the users
# the user input month values act as the dictionary keys 
months = {1:"January", 2:"February", 3: "March", 4:"April", 5:"May", 6:"June", 
          7: "July", 8:"August", 9:"September", 10: "October", 11: "November", 12 : "December"}


# Now let's get the day of the month

while True:
    try:
        birth_date = int(input("Please enter the day of birth: "))
        #  create a list for the days with 30 and days with 31 days
        days_30 = [4, 6, 9, 11]
        days_31 = [1, 3, 5, 7, 8, 10, 12]
        #  start first with the days with 31 days, then 30 days then finally february 
        if birth_month in days_31:
            if birth_date not in range(1, 32):  #  Range is is 32 since python counts to the value before the last listed value
                raise ValueError
            break
        elif birth_month in days_30:
            if birth_date not in range(1, 31):
                raise ValueError
            break
        elif birth_month == 2 and leap_year(birth_year) == False and birth_date > 28:
            raise LeapYearError
        break
        if birth_month == 2 and birth_date<1 or birth_date > 29:
            raise ValueError
        break
    # Custom message for the error raised     
    except ValueError:
        print("That is not a valid date in the month of "+ months[birth_month])
    except LeapYearError:   # Calling the custom exception that I defined at the start of the code
        print("February cannot have 29 days in non leap years")

# After getting dates we now get the gender from the user
print("now select your gender")
gender = ""  # Give the gender an initial empty value then later assign 
            # it based on fullfilled condition from the loop below

# I use while loops because this is a commandline program hence allows the question to ...
# ...be asked several times without the programming exiting when wrong answer is given            
while True:    
    try:
        gender_selection = int(input("Select 1 for Male and 2 for Female: "))
        if gender_selection == 1:
            gender = "Male"
            break
        if gender_selection == 2:
            gender = "Female"
            break
        else:
            raise ValueError
        break
    except ValueError:
        print("That number is not a valid selection of either 1 or 2")

# Getting the century which we need in the final calculation
century = int(str(birth_year)[:2])   # converting the integer value to string before getting it's first characters
cc = century  #Assigning the value to a shorter variable name to help later with the formula

year_digits = int(str(birth_year)[2:])  #use same method for the last 2 digits
yy = year_digits   # asign it to a shorter variable name for clarity when using the formula

# same with these below, assigning the variable names to shorter names 
# to avoid cluttering the formula later
# This is optional 
dd = birth_date
mm = birth_month
by = birth_year

# apply the formula to find the days of the week
# the final answer is a float with lots of decimal points hence why I ...
# ....convert to int in the print, to remove the decimal point
# removing the decimals because we will use the int's as dictionary keys

day_of_the_week =  (((cc/4)- 2 * cc - 1) + ((5 * yy / 4)) + ((26 * (mm + 1) / 10)) + dd) % 7
print(int(day_of_the_week))
dotw = int(day_of_the_week)

# dictionary to save days of the week
# 0 corresponds to Sunday which is the first day of the week
# 6 corresponds to Saturday

days_of_week = { 0: "Sunday", 1:"Monday", 2: "Tuesday", 3:"Wednesday", 
4: "Thursday", 5:"Friday", 6:"Saturday"}

born_day = days_of_week[dotw]

# Now let's create another dictionary of the Akan names and the days of the week ..
# ...they correspond to
male_akan_name = { "Sunday": "Kwasi", "Monday": "Kwadwo", "Tuesday": "Kwabena", 
                    "Wednesday": "Kwaku", "Thursday": "Yaw", 
                    "Friday":"Kofi", "Saturday": "Kwame"}

female_akan_names =  { "Sunday": "Akosua", "Monday": "Adwoa ", "Tuesday": "Abenaa", 
                    "Wednesday": "Akua", "Thursday": "Yaa", 
                    "Friday":"Afua", "Saturday": "Ama"}


# Now let's tell the user their Akan name

if gender == "Male":
    print("Hello, your Akan name would be " + str(male_akan_name[born_day]))
elif gender == "Female":
    print("Hello, your Akan name would be "+ str(female_akan_names[born_day]) )