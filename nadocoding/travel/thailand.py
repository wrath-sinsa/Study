class thailandP :
    def detail(self) :
        print ("[태국 패키지] 50만원")

if __name__ == "__main__" : # 모듈 이름(__name__)이 지금 실행하는 모듈(__main__)과 같은지
    print ("thailand 모듈 직접 실행")
    print ("모듈 직접 실행시 출력되는 구문")
    trip_to = thailandP()
    trip_to.detail()
else :
    print ("thailand 외부에서 모듈 호출")