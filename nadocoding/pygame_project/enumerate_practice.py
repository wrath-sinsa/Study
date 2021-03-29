# lst = ["가", "나", "다"]

# for lst_idx, lst_val in enumerate(lst) :
#     print (lst_idx + 1, lst_val)

balls = [1,2,3,4]
weapons = [11,22,3,44]
for A, B in enumerate(balls) :
    print("ball:", B)
    for C, D in enumerate(weapons) :
        print ("weapons : ", D)
        if B == D :
            print ("공무기 충돌")
            break
    else : # for 문이 끝나면 거침
        continue # break를 안거치고 넘어감.
    break # for 문이 break 당하면 진행됨


    # if 조건 :
    #     동작
    # else : 
    #     동작