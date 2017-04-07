#-*- coding: utf-8 -*-

# 초기 월급
initial_salary = 200

# 월간 적립 비율 50% 가정
monthly_invest_ratio = 0.5
#monthly_invest_ratio = 1.0
#monthly_invest_ratio = 0.3

# 연간 봉급 상승률 8% 가정
#yearly_salary_increase = 0.08
yearly_salary_increase = 0.05

# 연간 수익율 4% 가정
yearly_profit_ratio = 0.04

# 적립금
sum = 0

salary = initial_salary

for i in range(1, 26):
    deposit = salary * monthly_invest_ratio
    # 1.00 + 0.05 = 원금 + 이율이다.
    #year_deposit = ( deposit * 12 ) * ( 1.00 + yearly_profit_ratio )
    year_deposit = ( deposit * 12 )
    #sum += year_deposit
    sum += year_deposit
    sum *= ( 1.00 + yearly_profit_ratio )
    #if i % 5 == 0:
    #    monthly_invest_ratio *= .8
    #monthly_invest_ratio *= .95
    fmt = '%2d 년째 : 총 %12.4f 만원 (당해 연봉 : %10.4f 만원, 당해 적립 : %10.4f 만원)'
    print(fmt % (i, sum, salary*12, year_deposit))
    salary *= ( 1.00 + yearly_salary_increase )
