import math
from itertools import permutations

def data():
    data = []
    with open('data/day18.txt', 'r') as fil:
        for l in fil.readlines():
            l = l.replace('[', '(')
            l = l.replace(']', ')')
            data.append(eval(l))
    return data

def height(tup):
    match tup:
        case (l, r):
            return 1 + max(height(l), height(r))
        case _:
            return 0

def magnitude(pair):
    match pair:
        case (left, right):
            return 3 * magnitude(left) + 2 * magnitude(right)
        case num if isinstance(num, int):
            return num
        case _:
            raise Exception

def add(left, right):
    return (left, right)

def split(num):
    return (num // 2, math.ceil(num / 2))

def add_rightmost(num: int, tup: tuple):
    match tup:
        case (left, right):
            return (left, add_rightmost(num, right))
        case right:
            return right + num 

def add_leftmost(num: int, tup: tuple):
    match tup:
        case (left, right):
            return (add_leftmost(num, left), right)
        case left:
            return left + num

def explode(pair):
    match pair:
        case (((((l, r), rn), a),b),c): 
            rn=add_leftmost(r,rn)
            return ((((0, rn), a), b), c)

        case ((((ln, (l, r)),rn),a),b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return ((((ln, 0), rn), a),b)
        
        case (((ln, ((l,r), rn)),a),b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (((ln, (0, rn)), a),b)

        case (((a, (ln, (l,r))), rn),b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (((a, (ln,0)), rn),b)
 
        case ((ln, (((l,r), rn),a)), b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return ((ln, ((0, rn), a)), b)
 
        case ((a, ((ln, (l, r)), rn)), b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return ((a, ((ln, 0), rn)), b)

        case ((a, (ln, ((l, r), rn))), b): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return ((a, (ln, (0, rn))), b)

        case ((a, (b, (ln, (l, r)))), rn): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return ((a, (b, (ln, 0))), rn)

        case (ln, ((((l,r), rn),a), b)): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (ln, (((0, rn), a), b))
      
        case (a, (((ln, (l,r)),rn), b)): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, (((ln, 0), rn), b))
        
        case (a, ((ln, ((l,r), rn)), b)): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, ((ln, (0, rn)), b))

        case (a, ((b, (ln, (l,r))), rn)): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, ((b, (ln, 0)), rn))

        case (a, (ln, (((l,r), rn), b))): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, (ln, ((0, rn), b)))

        case (a, (b, ((ln, (l, r)), rn))): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, (b, ((ln, 0), rn)))

        case (a, (b, (ln, ((l, r), rn)))): 
            ln=add_rightmost(l,ln)
            rn=add_leftmost(r,rn)
            return (a, (b, (ln,(0, rn))))

        case (a, (b, (c, (ln, (l, r))))): 
            ln=add_rightmost(l,ln)
            return (a, (b, (c,(ln, 0))))

        case _:
            return pair

def flat(snailfish_number):
    match snailfish_number:
        case (left, right):
            return flat(left) + flat(right)
        case num:
            return (num,)

def split_leftmost(snailfish_number, done=False):
    match snailfish_number:
        case (left, right) if (splits := split_leftmost(left)) != left:
            return (splits, right)
        case (left, right):
            return (left, split_leftmost(right))
        case num if num > 9:
            return split(num)
        case num:
            return num

def applyExplode(num):
    match num:
        case tup if height(tup) == 5:
            return explode(tup)
        case (left, right) if height(tup) > 5:
            ex = applyExplode(left)
            if ex != left:
                return (ex, right)
            else:
                return (left, applyExplode(right))
        case _:
            return num

def reduce(snailfish_number):
    changed = True
    while changed:
        changed = False
        while ((exploded := applyExplode(snailfish_number)) != snailfish_number):
            snailfish_number = exploded
            changed = True
        if any(10 <= n for n in flat(snailfish_number)):
            snailfish_number = split_leftmost(snailfish_number)
            changed = True

    return snailfish_number

def calc(nums):
    num = nums[0]
    for addend in nums[1:]:
        num = add(num, addend)
        num = reduce(num)

    return num

if __name__ == '__main__':
    result = calc(data())
    print(f"Part1 {magnitude(result)=}")

    biggest = 0
    for a,b in permutations(data(), r=2):
        r = calc([a,b])
        m = magnitude(r)
        if m > biggest:
            biggest = m

    print(f"Part2 {biggest=}")
