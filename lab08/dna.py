"""
File: dna.py
Author: Stanley Goodwin
Last Updated: 4/1/2022

Description:
    This file contains all the functions in order to do operations on DNA,
    these functions are provided as to read from a string, determine matching
    DNA sequences, insert DNA into other DNA, and many other things.
"""
from immutable_list import FrozenNode


def convert_to_nodes(dna_strand: str) -> FrozenNode or None:
    """
    Convert a string of GCAT DNA into a linked list.
    :param dna_strand: A string of characters corresponding to DNA bases.
    :return FrozenNode or None: The node that the next part goes to.
    """
    if dna_strand == "":
        return None
    else:
        next_node = convert_to_nodes(dna_strand[1:])
        return FrozenNode(dna_strand[0], next_node)


def convert_to_string(dna_seq):
    pass


def length_rec(*args):
    pass


def is_match(dna_seq1: FrozenNode, dna_seq2: FrozenNode) -> bool:
    """
    Determines if 2 DNA sequences are similar.
    :param dna_seq1: A first linked sequence with data nodes representing a DNA sequence.
    :param dna_seq2: A second linked sequence with data nodes representing a DNA sequence.
    :return boolean: True or False.
    """
    if dna_seq1 is None and dna_seq2 is None:  # If both end, must be same.
        return True
    elif dna_seq1 is None ^ dna_seq2 is None:  # If one ends early, must be different
        return False
    else:  # If either are None, recursively test
        if dna_seq1.value == dna_seq2.value:  # If same value at place
            return is_match(dna_seq1.next, dna_seq2.next)
        else:  # Not same value at place
            return False


def is_pairing(*args):
    pass


def substitution(*args):
    pass


def insertion(dna_seq1: FrozenNode, dna_seq2: FrozenNode, idx: int) -> FrozenNode:
    """
    Inserts DNA sequence 2 into an index in DNA sequence.
    :param dna_seq1: The first sequence into which the second sequence is inserted.
    :param dna_seq2: The second sequence, which is inserted into the first.
    :param idx: The index before which the insertion occurs.
    :return FrozenNode:
    """
    pass


def deletion(*args):
    pass


def duplication(*args):
    pass
