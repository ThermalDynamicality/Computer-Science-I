"""
File: tools.py
Name: Stanley Goodwin
Date: 2/23/2022

A set of functions used later on for ease/simplicity of coding.
"""


def read_file(file_name: str) -> list[int]:
    """
    Reads a data file from file_name and returns a list
    of integers representing the distances of buildings.

    :param file_name: The file name being loaded.
    :return: List of Integers for the positions of buildings.
    """

    # Open file and read contents
    with open(file_name, "r") as f:
        _txt_list = f.readlines()

    # Strip \n from lines
    _txt_list = [i.strip() for i in _txt_list]

    # Returns number after the space (after "TEXT ")
    _txt_list = [i[i.index(" "):] for i in _txt_list]

    # Converts from list of strings to list of integers
    _txt_list = [int(i) for i in _txt_list]

    # Return list of positions
    return _txt_list


# Avoided using "or" vs "|" because of 3.9 -> 3.10 compatibility
def sum_distances(positions, location):
    """
    Takes in a list of positions and calculates the sum of the
    absolute distances between a given point and every position.

    :param positions: List of Integers or Floats for office positions.
    :param location: Integer or Float for a given location.
    :return:
    """
    _total_distance = 0
    for i in positions:
        _total_distance += abs(i + location)
    return _total_distance
