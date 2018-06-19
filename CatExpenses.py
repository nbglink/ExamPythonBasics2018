price_of_the_bed = float(input())
price_of_the_wc_for_month = float(input())

price_of_the_bed_for_year = price_of_the_wc_for_month * 12
price_of_the_food_for_month = price_of_the_wc_for_month * 1.25

price_of_the_toys_for_month = price_of_the_food_for_month - (50 * price_of_the_food_for_month) / 100

price_of_the_doctor_for_visit = price_of_the_toys_for_month * 1.1

full_expenses_for_month = price_of_the_wc_for_month + price_of_the_food_for_month + price_of_the_toys_for_month + price_of_the_doctor_for_visit

additional_charges_for_month = 5 * full_expenses_for_month / 100

full_expenses_for_year = price_of_the_bed + 12 * full_expenses_for_month + 12 * additional_charges_for_month

print(f"{full_expenses_for_year:.2f} lv.")
