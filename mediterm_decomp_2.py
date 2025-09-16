
voca_dict = {'hemat':'피(혈)','oma':'종양'}

while True:
    
    mediterm = input("\n\nINPUT: ")

    if mediterm == "!exit":
        break
    else:
        dajin = list(mediterm)
        brk = False
        oa = False

        while True:                         # 리스트에서 잘못 찾았을 경우 대비
            if brk:
                break
            else:
                result = []
                if oa:
                    comb_str = dajin[len(dajin)-1]
                    for i in range(len(dajin)):
                        print(comb_str)
                        if comb_str in voca_dict:
                            result.insert(0, comb_str)
                            # comb_str 초기화
                            if i == len(dajin)-1:
                                brk = True                # 단어 끝: 마무리
                            else:
                                comb_str = dajin[len(dajin)-i-2]
                        else:
                            if i == len(dajin)-1:
                                print("\n\nERROR! Program Terminated.")
                                exit()
                            else:
                                comb_str = dajin[len(dajin)-i-2]+comb_str

                else:
                    comb_str = dajin[0]
                    for i in range(len(dajin)):
                        print(comb_str)
                        if comb_str in voca_dict:
                            result.append(comb_str)
                            # comb_str 초기화
                            if i == len(dajin)-1:
                                brk = True                # 단어 끝: 마무리
                            else:
                                comb_str = dajin[i+1]
                        else:
                            if i == len(dajin)-1:
                                print("Wrong Initializing - Decomposing Again...")
                                oa = True
                            else:
                                comb_str = comb_str+dajin[i+1]


        # 결과 출력
        print(f"\n\n\n{result}")
        print("RESULT: ", end='')
        for j in range(len(result)):
            if j+1 == len(result):
                print(f"{voca_dict[result[j]]}")
            else:
                print(f"{voca_dict[result[j]]}/", end='')
