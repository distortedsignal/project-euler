#! /usr/local/bin/python3.5

from enum import Enum
from copy import deepcopy

class CardinalDirection(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

class Cursor(object):

    def __init__(self, start_position, 
        start_direction=CardinalDirection.north.value, start_steps=0):
        self.position = start_position
        self.direction = start_direction
        self.steps = start_steps

    def add_step(self):
        self.steps += 1

    def forward(self):
        self.add_step()
        if self.direction == CardinalDirection.north.value:
            self.position[1] += 1
        elif self.direction == CardinalDirection.east.value:
            self.position[0] += 1
        elif self.direction == CardinalDirection.south.value:
            self.position[1] -= 1
        elif self.direction == CardinalDirection.west.value:
            self.position[0] -= 1

    def left(self):
        self.direction = (self.direction-1) % 4

    def right(self):
        self.direction = (self.direction+1) % 4

    def teleport(self, right_diff, forward_diff, turns, steps_added):
        '''Teleport relative to the current cursor'''
        new_cursor = Cursor(deepcopy(self.position), self.direction, self.steps)
        if new_cursor.direction == CardinalDirection.north.value:
            new_cursor.position = [new_cursor.position[0]+right_diff, new_cursor.position[1]+forward_diff]
        elif new_cursor.direction == CardinalDirection.east.value:
            new_cursor.position = [new_cursor.position[0]+forward_diff, new_cursor.position[1]-right_diff]
        elif new_cursor.direction == CardinalDirection.south.value:
            new_cursor.position = [new_cursor.position[0]-right_diff, new_cursor.position[1]-forward_diff]
        elif new_cursor.direction == CardinalDirection.west.value:
            new_cursor.position = [new_cursor.position[0]-forward_diff, new_cursor.position[1]+right_diff]

        new_cursor.direction = (new_cursor.direction+turns) % 4
        new_cursor.steps += steps_added
        return new_cursor

    def __str__(self):
        return "{position: " + str(self.position) + ", direction: " + \
            str(self.direction) + ", steps: " + str(self.steps) + "}"


def teleport_function_creator(right_diff, forward_diff, turns, steps_added):
    def teleport_function(current_cursor):
        return current_cursor.teleport(right_diff, forward_diff, turns, steps_added)
    return teleport_function

def calculate_a(level_plus_one_a, level_plus_one_b):
    new_cursor = Cursor([0, 0])
    new_cursor = level_plus_one_a(new_cursor)
    new_cursor.right()
    new_cursor = level_plus_one_b(new_cursor)
    new_cursor.forward()
    new_cursor.right()
    return teleport_function_creator(new_cursor.position[0], 
        new_cursor.position[1], new_cursor.direction, new_cursor.steps)

def calculate_b(level_plus_one_a, level_plus_one_b):
    new_cursor = Cursor([0, 0])
    new_cursor.left()
    new_cursor.forward()
    new_cursor = level_plus_one_a(new_cursor)
    new_cursor.left()
    new_cursor = level_plus_one_b(new_cursor)
    return teleport_function_creator(new_cursor.position[0], 
        new_cursor.position[1], new_cursor.direction, new_cursor.steps)

def build_descent_dictionary(levels, partial_descent_dict):
    if levels == -1:
        return partial_descent_dict

    if partial_descent_dict == {}:
        levels -= 1
        partial_descent_dict[levels] = {
            "a": teleport_function_creator(1, 0, 2, 1),
            "b": teleport_function_creator(-1, 0, 2, 1)
        }
    else:
        partial_descent_dict[levels] = {
            "a": calculate_a(partial_descent_dict[levels+1]['a'], partial_descent_dict[levels+1]['b']),
            "b": calculate_b(partial_descent_dict[levels+1]['a'], partial_descent_dict[levels+1]['b'])
        }

    return build_descent_dictionary(levels-1, partial_descent_dict)

def find_location_after_steps(descent_dict, steps, direction_string):
    level = 0
    cursor = Cursor([0, 0])
    while True:
        print("Iterating with cursor " + str(cursor) + 
            " and direction string '" + direction_string + "' on level " + 
            str(level) + ".")
        if cursor.steps == steps:
            return str(cursor.position)

        if direction_string == "":
            raise IndexError("Trying to empty an empty direction string.")

        if direction_string[0] in ['F', 'R', 'L']:
            if direction_string[0] == 'F':
                cursor.forward()
            elif direction_string[0] == 'R':
                cursor.right()
            elif direction_string[0] == 'L':
                cursor.left()
            direction_string = direction_string[1:]
            continue

        try:
            new_cursor = descent_dict[level][direction_string[0]](cursor)
            
            if new_cursor.steps > steps:
                print("New cursor " + str(new_cursor) + " has greater steps than we need.")
                level += 1
                if direction_string[0] == 'a':
                    direction_string = 'aRbFR'
                elif direction_string[0] == 'b':
                    direction_string = 'LFaLb'
            elif new_cursor.steps <= steps:
                print("New cursor " + str(new_cursor) + " is within the valid step count.")
                cursor = new_cursor
                direction_string = direction_string[1:]
        except KeyError:
            direction_string = direction_string[1:]

print("Defined functions and data structures.")

descent_dictionary = build_descent_dictionary(10, {})
print("Built descent dictionary.")
steps = 500

print(find_location_after_steps(descent_dictionary, steps, "Fa"))
