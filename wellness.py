# wellness tracker


print("Hi! Welcome to Wellness Tracker.")
print("ie Your personal daily health evalution system.")
print()
print()


# water consumption
      
water = int(input("Enter the amount of water in fluid ounces consumed today: "))

print()

water_goal = int(input("Enter your daily goal for water cosumption in fluid ounces: "))

print()


def evaluate(water):

    water_difference = 0

    if water < water_goal:

        water_difference = water_goal - water
        print("Water goal", water_difference, "fluid ounces away.")

    elif water > water_goal:

        water_difference = water - water_goal
        print("Water goal exceeded by", water_difference, "fluid ounces.")

    elif water == water_goal:

        water_difference = water - water_goal
        print("Water goal met exactly.")

evaluate(water)
print()
print()


# sleep received 

sleep = int(input("Enter the amount of sleep received last night. Round to the nearest hour: "))

print()

sleep_goal = int(input("Enter your daily goal for amount of sleep received to the nearest hour: "))

print()


def evaluate(sleep):

    sleep_difference = 0

    if sleep < sleep_goal:

        sleep_difference = sleep_goal - sleep
        print("Sleep goal", sleep_difference, "hours away.")

    elif water > water_goal:

        sleep_difference = sleep - sleep_goal
        print("Sleep goal exceeded by", sleep_difference, "hours.")

    elif water == water_goal:

        sleep_difference = sleep - sleep_goal
        print("Sleep goal met exactly.")

evaluate(sleep)
print()
print()


# exercise done

exercise = int(input("Enter the amount of exercise done today in minutes: "))

print()

exercise_goal = int(input("Enter your daily goal for the amount of exercise done in minutes: "))

print()


def evaluate(exercise):

    exercise_difference = 0

    if exercise < exercise_goal:

        exercise_difference = exercise_goal - exercise
        print("Exercise goal", exercise_difference, "minutes.")

    elif exercise > exercise_goal:

        exercise_difference = exercise - exercise_goal
        print("Exercise goal exceeded by", exercise_difference, "minutes.")

    elif exercise == exercise_goal:

        exercise_difference = exercise - exercise_goal
        print("Exercise goal met exactly.")

evaluate(exercise)
print()
print()


# active mind time spent

active_mind = int(input("Enter the amount of active mind time spent in hours: "))

print()

active_mind_goal = int(input("Enter your daily goal for the amount of active mind time spent in hours: "))

print()


def evaluate(active_mind):

    active_mind_difference = 0

    if active_mind < active_mind_goal:

        active_mind_difference = active_mind_goal - active_mind
        print("Active mind goal", active_mind_difference, "hours.")

    elif active_mind > active_mind_goal:

        active_mind_difference = active_mind - active_mind_goal
        print("Active mind goal exceeded by", active_mind_difference, "hours.")

    elif active_mind == active_mind_goal:

        exercise_difference = active_mind - active_mind_goal
        print("Active mind goal met exactly.")

evaluate(active_mind)
print()
print()

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np


# water consumption

data = {'Water Consumption':water, 'Water Goal':water_goal}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values, color ='blue',
        width = 0.4)
 
plt.xlabel("Today's Water Data")
plt.ylabel("Water Fluid oz")
plt.title("Water Goal vs Water Consumption")
plt.show()

# sleep received

data = {'Water Consumption':sleep, 'Water Goal':sleep_goal}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values, color ='purple',
        width = 0.4)
 
plt.xlabel("Today's Sleep Data")
plt.ylabel("Sleep Hours")
plt.title("Sleep Goal vs Sleep Received")
plt.show()

# exercise done

data = {'Exercise Done':exercise, 'Exercise Goal':exercise_goal}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values, color ='green',
        width = 0.4)
 
plt.xlabel("Today's Exercise Data")
plt.ylabel("Exercise Minutes")
plt.title("Exercise Goal vs Exercise Done")
plt.show()

# activemind time spent

data = {'Activemind Time Spent':active_mind, 'Activemind Goal':active_mind_goal}
courses = list(data.keys())
values = list(data.values())
  
fig = plt.figure(figsize = (10, 5))
 
plt.bar(courses, values, color ='red',
        width = 0.4)
 
plt.xlabel("Today's Activemind Data")
plt.ylabel("Activemind Goal Hours")
plt.title("Activemind Goal vs Activemind Time Spent")
plt.show()