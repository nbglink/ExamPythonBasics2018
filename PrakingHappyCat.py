days_count = int(input())
hours_count_for_each_day = int(input())

total_amount = 0
for day in range(1, days_count+1):
    sum_for_the_day = 0

    if day % 2 == 0:
        for hour in range(1, hours_count_for_each_day +1):
            if hour % 2 != 0:
                sum_for_the_day += 2.50
            else:
                sum_for_the_day += 1.00
    elif day % 2 != 0:
        for hour in range(1, hours_count_for_each_day +1):
            if hour % 2 == 0:
                sum_for_the_day += 1.25
            else:
                sum_for_the_day += 1.00

    total_amount += sum_for_the_day
    print(f"Day: {day} - {sum_for_the_day:.2f} leva")

print(f"Total: {total_amount:.2f} leva")
