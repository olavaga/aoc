def data():
    with open('day17.txt', 'r') as fil:
        _, string = fil.read().strip().split('x=')
        x, y = string.split(', y=')
        target_area = (tuple(map(int, x.split('..'))), tuple(map(int, y.split('..'))))
        
    return target_area

def calcTrajectory(x_vel, y_vel):
    x,y = 0,0

    while True:
        x += x_vel
        y += y_vel
        if x_vel:
            x_vel = x_vel - 1 if x_vel > 0 else x_vel + 1
        y_vel -= 1

        yield x,y

def bounds(xs, ys):
    return lambda x,y: xs[0] <= x <= xs[1] and ys[0] <= y <= ys[1]


def calc(target_area):
    withinTarget = bounds(*target_area)
    highest = 0
    initial_vels = set()
    for x_vel in range(1, target_area[0][1] + 1):
        for y_vel in range(-500, 500):
            cur_highest = 0
            trajectory = iter(calcTrajectory(x_vel, y_vel))
            x, y = next(trajectory)
            while x <= target_area[0][1] and y >= target_area[1][0]:    
                cur_highest = max(y, cur_highest)
                if withinTarget(x, y):
                    highest = cur_highest if cur_highest > highest else highest
                    initial_vels.add((x_vel, y_vel))
                    break
                x,y = next(trajectory)

    return highest, len(initial_vels)

if __name__ == '__main__':
    print("Calculating example")    
    example = ((20,30), (-10,-5))
    highest, initial_vels = calc(example)
    print(f"{highest=} {initial_vels=}")
    assert(initial_vels == 112)
    
    highest, initial_vels = calc(data())
    print(f"{highest=} {initial_vels=}")
