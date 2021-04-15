combinations=[]

for count_200 in range(1+1):
    for count_100 in range(2+1):
        for count_50 in range(4+1):
            for count_20 in range(10+1):
                for count_10 in range(20+1):
                    for count_5 in range(40+1):
                        for count_2 in range(100+1):
                            for count_1 in range(200+1):
                                if 200*count_200+100*count_100 + 50*count_50 + 20*count_20 + 10*count_10 + 5*count_5 + 2*count_2 + count_1 == 200:
                                    combinations.append([count_200, count_100, count_50, count_20, count_10, count_5, count_2, count_1])


len(combinations)
