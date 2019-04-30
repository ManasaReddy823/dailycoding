def avg_asc(a):
    length=len(a)
    total = 0
    for i in range(length):

        total=total+ord(a[i])
    print(int(total/length))


if __name__ == "__main__":
    test_cases=input()
    for i in range(int(test_cases)):
        input_string=input()
        avg_asc(input_string)


