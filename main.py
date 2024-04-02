

import re
def main():
    s = open("test.txt").read()
    mass = {}
    m = re.findall(r'\b\d+\b', s, re.M)
    m = [int(x) for x in m]
    for x in m:
        if x not in mass:
            mass[x] = 1
        else:
            mass[x] += 1
    print(mass)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
