def arctan(x):
    result = x
    exp = 3
    denominator = 3
    add = False
    for i in range(500):
        if add == True:
            result += (x ** exp) / denominator
            exp += 2
            denominator += 2
            add = False
        else: 
            result -= (x ** exp) / denominator
            exp += 2
            denominator += 2
            add = True
    return result

def pi():
    return (16*arctan(1/5)) - (4*arctan(1/239))

def main():
    print(pi())

if __name__ == "__main__":
    main()