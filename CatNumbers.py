n = int(input())

for i in range(1,n+1):
    first_name = input()
    surname = input()
    birth_year = int(input())
    n -= 1

    print(str(birth_year) + str(ord(first_name[0])) + str(ord(surname[0])) + str(i))
