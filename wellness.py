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
        print("Exercise goal", exercise_difference, "fluid ounces away.")

    elif exercise > exercise_goal:

        exercise_difference = exercise - exercise_goal
        print("Exercise goal exceeded by", exercise_difference, "fluid ounces.")

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
        print("Active mind goal", active_mind_difference, "fluid ounces away.")

    elif active_mind > active_mind_goal:

        active_mind_difference = active_mind - active_mind_goal
        print("Active mind goal exceeded by", active_mind_difference, "fluid ounces.")

    elif active_mind == active_mind_goal:

        exercise_difference = active_mind - active_mind_goal
        print("Active mind goal met exactly.")

evaluate(active_mind)
print()
print()


# create backround screen + import image 

import turtle
import time

screen = turtle.Screen()
screen.title("Water Consumption")
screen.setup(width=400,height=400)
screen.bgpic("wellness_tracker/linegraph.gif") # image address: https://maaw.info/images/BlankGraph2.gif


# plot data collected 

def irma_setup():

    ...

irma_setup()
































    

    




