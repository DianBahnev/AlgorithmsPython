#!/usr/bin/env python


def reverse_string_while_loop(s):
    string = list(s)
    start = 0
    end = len(string) - 1
    while start < end:
        string[start], string[end] = string[end], string[start]
        start += 1
        end -= 1

    return ''.join(string)


def reverse_string_for_loop(s):
    string = list(s)
    for index in range(int(len(string)/2)):
        string[index], string[-index-1] = string[-index-1], string[index]

    return ''.join(string)
