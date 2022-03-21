from dataclasses import dataclass
from typing import Union


# NODE DEFINITIONS


@dataclass(frozen=True)
class ImmutableNode:
    """
    A node that is unchangeable that contains a value and next node in line.
    """
    value: any
    next: Union["ImmutableNode", None]


@dataclass(frozen=False)
class MutableNode:
    """
    A node that is changeable that contains a value and next node in line.
    """
    value: any
    next: Union["MutableNode", None]


# STACK DEFINITIONS


@dataclass
class Stack:
    """
    Stack is an object that is the catalyst of immutable nodes in order.
    """
    size: int
    top: Union["ImmutableNode", "None"]


def gen_empty_stack() -> Stack:
    """
    Generates an empty stack object.
    :return Stack: The empty stack object.
    """
    return Stack(0, None)


def s_is_empty(stack: Stack) -> bool:
    """
    Returns a boolean for whether the stack is empty or not.

    :param stack: The stack in question.
    :return boolean: A true/false for if the stack is empty.
    """
    return stack.top is None


def s_pop(stack: Stack) -> any:
    """
    Pops the first node off the top of the list. Returns value of node.

    :param stack: The input stack to pop the item off of.
    :return value: The value of the popped item.
    """

    # Check if stack is empty
    if s_is_empty(stack):
        raise IndexError("The stack is empty.")

    # Get top node's value
    pop_value = stack.top.value

    # Start stack at next node
    stack.top = stack.top.next

    # Return node value
    return pop_value


def s_top(stack: Stack) -> any:
    """
    Reads the value at the top of the stack. Doesn't change stack.

    :param stack: The input stack to read the first item value of.
    :return value: The value of the item.
    """

    # Check if stack is empty
    if s_is_empty(stack):
        raise IndexError("The stack is empty.")

    # Return node value
    return stack.top.value


def s_push(stack: Stack, value: any) -> None:
    """
    Pushes a value onto the top of the parameter stack.

    :param stack: The stack to add the value to.
    :param value: The value to add to the stack.
    :return None:
    """
    stack.top = ImmutableNode(value, stack.top)
    stack.size += 1


def s_size(stack: Stack) -> int:
    """
    Returns the size of the stack queue.

    :param stack: The stack in question.
    :return size: The size of the stack.
    """
    return stack.size


# PROGRAM DEFINITIONS


def parser(stack: Stack, input_string: str):
    """
    Parses an input string to write to the stack.
    Catches illegals characters and strings on execution.

    :param stack: The stack to have the string added to.
    :param input_string: The 4-function math string.
    :return None:
    """

    # Split string into components
    phonemes = input_string.split()

    # For all components, add to stack frame if valid character/word
    for val in phonemes:
        if val.isdigit() or val in ["+", "-", "*", "/"]:
            s_push(stack, val)
        else:
            raise ValueError("Illegal character(s) in input string")


def main():
    """
    Make a queue equivalent.
    Make it solve the problem.
    Check the solutions are the same value.
    PARTY.

    Lecture:
    https://www.cs.rit.edu/~csci141/Lectures/10/StacksQueues-stu.pdf

    Homework:
    https://www.cs.rit.edu/~csci141/Homeworks/10/backwards_calc-stu.pdf

    :return:
    """

    # Empty Stack Generator
    stack_frame = gen_empty_stack()

    # Parse Console Input
    console_io = input("Expression: ")
    parser(stack_frame, console_io)

    # Print result
    print(stack_frame)


if __name__ == "__main__":
    main()
