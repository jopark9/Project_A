# def profile(name, age, main_lang):
#     print("이름 : {0}\t 나이 : {1}\t  주 사용 언어 : {2}"
#           .format(name, age, main_lang))


# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은반  같은 수업
# def profile(name, age=17, main_lang="파이썬"):
#     print("이름 : {0}\t 나이 : {1}\t  주 사용 언어 : {2}"
#           .format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)
    
# profile(name = "유재석",  main_lang = "파이썬", age = 20)
# profile(main_lang = "자바", age =  25, name = "김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t 나이 : {1}\t" .format(name,age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language): #가변인자
#     print("이름 : {0}\t 나이 : {1}\t" .format(name,age), end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()
# profile("유재석", 20, "python", "java", "c", "c++", "c#","Html")
# profile("김태호", 25, "Kotlin", "Swift" )

#지역변수

gun = 10

def checkpoint(soldiers): #경계근무
    # gun = 20 #지역변수
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}" .format(gun))
    
print("전체 총 : {0}".format(gun))
checkpoint(2) #2명이 경겨 근무 나감
print("남은 총 : {0}".format(gun))