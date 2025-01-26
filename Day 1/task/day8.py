# Create a function called life_in_weeks() using maths and f-Strings
# that tells us how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    whole_year = 90
    remain_year = whole_year - age
    # there are 52 weeks in a year
    left_week = remain_year * 52
    print(f"You have {left_week} weeks left.")


life_in_weeks(20)