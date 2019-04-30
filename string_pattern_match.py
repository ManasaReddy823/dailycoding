def count_pattern(input_string):
    count_x=0
    count_y=0
    if len(input_str)==1:
        status=0
    for i in range(len(input_str)-1):
        if input_str[i] == 'x':
            count_x=count_x+1

        elif input_str[i] == 'y':
            count_y=count_y+1

        if input_str[i + 1] != input_str[i]:
                if input_str[i] == 'x':
                    count_y=count_y+1
                if input_str[i] == 'y':
                    count_x=count_x+1
                if count_y==count_x:
                    status=1
                    count_y = 0
                    count_x = 0
                    continue
                else:
                    status=0
                    break
    return status


if __name__ == "__main__":
   test_cases=input()
   for i in range(int(test_cases)):
       input_str=input()
       print(count_pattern(input_str))