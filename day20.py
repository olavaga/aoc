from aocd import data
from collections import defaultdict

def count_pixels(data_dict):
    return sum(v for k,v in data_dict.items())

def img_to_dict(img):
    d = defaultdict(int)
    for i, r in enumerate(img):
        for j, ch in enumerate(r):
            if ch == '#':
                d[(i,j)] = 1

    return d

def transform(input_dict, dims, translation_string):
    output_dict = defaultdict(int)
    neighbours = ((-1,-1), (-1,0), (-1,1), 
                   (0,-1),  (0,0),  (0,1), 
                   (1,-1),  (1,0),  (1,1))
    
    for x in range( - 150, dims[0] + 150):
        for y in range( - 150, dims[1] + 150):
            index = "".join(str(input_dict[(x+nx,y+ny)]) for nx,ny in neighbours)
            assert(len(index) == 9)
            dec = int(index, 2)
            assert(0 <= dec < 512)
            if '#' == translation_string[dec]:
                output_dict[(x+1,y+1)] = 1

    return output_dict

if __name__ == '__main__':
    trans = data.split()[0].strip()
    img = data.split()[1:]

    d = img_to_dict(img)

    d = transform(d, (len(img) + 20, len(img[0]) + 20), trans)
    d = transform(d, (len(img) + 20, len(img[0]) + 20), trans)

    part1 = 0
    for i in range(-1, 110):
        for j in range(-1, 110):
            part1 += d[(i,j)]
    print(f"{part1=}")

    for i in range(48):
        d = transform(d, (len(img) + 20, len(img[0]) + 20), trans)
        
    part2 = 0
    for i in range(-30, 210):
        for j in range(-30, 210):
            part2 += d[(i,j)]
    print(f"{part2=}")



