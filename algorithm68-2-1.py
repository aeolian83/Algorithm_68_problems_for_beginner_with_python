# op = ['*', ''] 이 어떤 리스트인지 확인
op = ['*', '']

print(op)

print()

op1 = ["*", ""]

print(op1)

import re

op = ['*', '']
print(op)
print(len(op))

for i in range(1000, 1002):
    c = str(i)
    for j in range(0, len(op)):
        for k in range(0, len(op)):
            for l in range(0, len(op)):
                val = c[3] + op[j] + c[2] + op[k] + c[1] + op[l] + c[0]

                # 0으로 시작하는 숫자가 있는지 확인하고 
                # 있는 경우 제거
                val = re.sub(r"0(\d+)", r"\1", val)

                # 연산자를 하나는 넣는 경우
                print(val)


# 정규표현식에 대한 공부가 필요하다
