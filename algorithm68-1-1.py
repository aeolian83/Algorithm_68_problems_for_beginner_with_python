# print(1)
# 진수변환_1
num = 1234567

num_8 = oct(num)

print(num_8)
print()

num_a = 0o177

num_10 = str(num_a)

print(num_10)

# 슬라이싱 연습
# 앞뒤가 같은지 여부 확인 중 슬라이싱 관련

num = 1234567
num = str(num)

num_a = num[::-1]
print(num_a)

# 진수 변환_2
print("{0:x}".format(273)) # 16진수 변환
print("{0:o}".format(273)) # 8진수 변환
print("{0:b}".format(273)) # 2진수 변환
