# -*- coding: utf-8 -*-


def main():
    s = input()
    i = int(input())
    i = i if i else 0
    return s[i - 1]

print(main())