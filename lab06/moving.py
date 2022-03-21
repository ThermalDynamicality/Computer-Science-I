"""
File: moving.py
Name: Stanley Goodwin
Date: 3/18/2022

Description:
    Using Dataclasses, we are exploring putting items into boxes efficiently
    whilst also using said dataclasses to be more readable and customizable.
"""
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str = None  # The name of the item in question
    weight: int = 0  # The weight of that item

@dataclass
class Box:
    capacity_max: int = 0  # The max capacity of the box
    capacity_cur: int = 0  # The current capacity of the box
    contents: dict = field(default_factory=list)  # The items stored within the box


def generate_empty_box(max_capacity) -> Box:
    """
    Generates an empty box with max capacity specified in parameters.

    :param max_capacity: The maximum capacity of the box.
    :return Box: The empty box-object
    """
    return Box(capacity_max=max_capacity)


def read_file(file_name):

    # Open box and read content
    with open(file_name, "r") as f:
        content = f.readlines()

    # Create boxes
    boxes_max_values = content[0].strip().split()
    boxes = []
    for capacity in boxes_max_values:
        boxes.append(Box(capacity_max=capacity))

    # Create items
    items = []
    for line in content[1:]:
        data = line.strip().split()
        name = data[0]
        weight = data[1]
        items.append(Item(name, weight))

    # Return data
    return boxes, items


def main():
    io_input_file = input("Enter data filename: ")

    print("Results of Greedy Strategy 1")
    print("Results of Greedy Strategy 2")
    print("Results of Greedy Strategy 3")