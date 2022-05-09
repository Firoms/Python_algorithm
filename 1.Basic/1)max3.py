"""
returns maximum integer 
when it gets three integers.

:requirement:
don't use 'max' python function

<input 1>
1 8 5
<output 1>
8

<input 2>
5 3 1
<output 2>
5
"""


def max3(a: int, b: int, c: int) -> int:
    """
    funtion that returns maximum integer
    when it gets three integers.

    :param a: first integer input
    :param b: second integer input
    :param c: third integer input

    :return maximum: maximum integer from three input integers
    """
    maximum = a
    if maximum < b:
        maximum = b
    if maximum < c:
        maximum = c

    return maximum


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    result = max3(a, b, c)
    print(result)
