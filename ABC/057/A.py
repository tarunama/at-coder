# -*- coding: utf-8 -*-
 
 
def main():
    a, b = [int(e) for e in input().split()]
    answer = (a + b) % 24
    return answer
 
 
print(main())
