minutes_walks_day = int(input())
count_walks_day = int(input())
calories_day = int(input())

summary_minutes_for_walk = minutes_walks_day * count_walks_day

summary_calories_burned = summary_minutes_for_walk * 5

half_of_taken_calories = calories_day - (50 * calories_day) / 100

if summary_calories_burned >= half_of_taken_calories:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {summary_calories_burned}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {summary_calories_burned}.")
