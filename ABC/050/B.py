# -*- coding: utf-8 -*-
from copy import deepcopy
 
 
def main():
    problems = int(input())
    solve_times = [int(e) for e in input().split()]
    drinks = int(input())
 
    for i in range(drinks):
        solve_times_copy = deepcopy(solve_times)
        problem_idx, solve_time = [int(e) for e in input().split()]
        problem_idx -= 1
        solve_times_copy[problem_idx] = solve_time
        print(sum(solve_times_copy))
 
 
main()
