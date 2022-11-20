num=int(input("Enter the number: "))

def PerfectNum():
    sum = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            sum += i
        #print(sum)

    if sum == num:
        return True
    return False


if PerfectNum():
    print("Введенное число: ", num, " Совершенное")
else:
    print("Введенное число: ", num, " не совершенное")