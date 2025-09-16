
voca_dict = {'chrom':'유전','some':'체','lith':'돌(결석)','protein':'단백질','hist':'근육','logist':'학자','adip':'지방','cyt':'세포','plasm':'질(조직,물질)','cyte':'세포(구)','erythr':'붉은','karyo':'핵','type':'형','end':'안쪽','leuk':'흰','granul':'과립','cerebell':'소뇌','cerebr':'대뇌(뇌)','dur':'경막','encephal':'뇌','gil':'신경아교세포','mening':'수막','my':'근육','pathy':'병증','neur':'신경','myel':'척수','hypo':'아래쪽','thalamus':'시상','emia':'혈병(피의 비정상적 상태)'}

while True:
    
    mediterm = input("\n\nINPUT: ")

    if mediterm == "!exit":
        break
    else:
        dajin = list(mediterm)
        brk = False
        oa = []

        while True:                         # 리스트에서 잘못 찾았을 경우 대비
            if brk:
                break
            else:
                result = []
                comb_str = dajin[0]
                for i in range(len(dajin)):
                    print(i)
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
                            print("ERROR!!!")
                            oa.append(result)
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
