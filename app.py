import sys

def analyze(numbers,sum):
    numbers = list(map(int, numbers.split(",")))
    frequency ={}
    pairs=[]
    for n in numbers:
        # print(frequency)
        if (sum-n) in numbers and n != sum-n and n not in frequency:
            pairs.append(str(n)+","+str(sum-n))
            frequency[n]= 1
            frequency[sum-n]=1
    return pairs
   
if __name__ == '__main__':
    pairs =analyze(sys.argv[1],int(int(sys.argv[2])))
    if pairs:
        for pair in pairs:
            print(pair)
    else:
        print("There isn't a pair of numbers that sum the given value")

