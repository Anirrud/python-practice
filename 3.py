n = int(input("Enter a number: "))

sum1, sum2, stop_point, digit = 0, 0, 0, 0
org_num = n

for i in range(1, 10):
    sum1 += i * 9 * pow(10, i - 1)
    digit += 1
    if sum1 >= org_num:
        stop_point += 1
    if stop_point == 1:
        break

val = digit * 9 * pow(10, digit - 1)
sum2 = sum1 - val

n1 = pow(10, digit - 1) + (n - sum2 - 1) // digit
digit_index = (n - sum2 - 1) % digit

n1_str = str(n1)
ans = int(n1_str[digit_index])

print(ans)