#-*- coding: utf-8 -*-

'''
아래 소스 코드는 하청 관계에서 마진 및 사업비가 어떻게 바뀌는지 보여주는 것으로 한번 작성해 보았다.
물론, 실제 업계에서 발생하는 숫자와는 상관이 없다. 그냥 소설로 써본것이다.
'''

# DEBUG
DEBUG=True

# 계약 단계별 명칭
CONST_DEPTH = ( '갑', '을', '병', '정', '무', '기', '경', '신', '임', '계' )

# 최초 사업비
CONST_ORIGINAL_PROJECT_BUDGET = 100

# 사업비 단위
CONST_BUDGET='억'

# 마진율
margin_ratio=.1

# 사업비 계산
def calc_project_budget(budget, level):
    if level == 0:
        return budget
    else:
        if DEBUG == True:
            msg = "(사업비 날라가는 소리)'%s'이 사업비중 %5.1f %s을 꿀꺽했습니다."
            print(msg % (CONST_DEPTH[i-level+1], budget*margin_ratio, CONST_BUDGET))
        return calc_project_budget(budget - ( budget * margin_ratio ), level -1)

i = input("What is your position on the contract? ")

print("You are called '%s'" % (CONST_DEPTH[i]))

project = calc_project_budget(CONST_ORIGINAL_PROJECT_BUDGET, i)
margin = CONST_ORIGINAL_PROJECT_BUDGET - project

print("사업비 : %5.1f %s (마진:%5.1f %s)" % (project, CONST_BUDGET, margin, CONST_BUDGET))

