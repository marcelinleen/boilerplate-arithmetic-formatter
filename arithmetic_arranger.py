import math
import re
from execute_str import execute_str

def arithmetic_arranger(problems, res = False):

    error = execute_str(problems)

    if error != 'False':
        tabs = error
        return tabs
    else:
        top = ''
        bottom = ''
        dashes = ''
        for problem in problems:
            first, operator, second = problem.split( )
            if len(first) >= len(second):
                x = 2 + len(first)
            else:
                x = 2 + len(second)
            top += (' ')*int(x - len(first)) + first + (' ')* 4
            bottom += operator + (' ')*int(x - (len(second) + 1)) + second + (' ')* 4
            dashes += ('-')*x + (' ')* 4
        top = top.rstrip()
        bottom = bottom.rstrip()
        dashes = dashes.rstrip()

        if res == True:
            res_line = ''
            for problem in problems:
                first, operator, second = problem.split( )
                if len(first) >= len(second):
                    x = 2 + len(first)
                else:
                    x = 2 + len(second)
                sum = '+'
                if operator == sum:
                    res_int = int(first) + int(second)
                else:
                    res_int = int(first) - int(second)
                res_line += (' ')*(x - (len(str(res_int)))) + str(res_int) + (' ')* 4
            res_line = res_line.rstrip()

        tabs = f'{top}\n{bottom}\n{dashes}'

        if res == True:
            tabs = f'{top}\n{bottom}\n{dashes}\n{res_line}'

        return(tabs)

