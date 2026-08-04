# Problem Set 2 Solutions — Control Flow & Functions
# Similar to Problem Set 1, solutions are commented out.
# Uncomment the problem you're working on and run the script
# using `python path/to/script.py`

# You can comment/uncomment blocks of code by highlighting
# the lines and using 'Ctrl + /'

import math
import random  # needed for challenge problems

# #######################
# # Solution Problem 1 - Pizza Party Planner
# #######################


# def pizzas_needed(people, slices_per_person, slices_per_pizza):
#     """Calculate how many whole pizzas to order (always round up)."""
#     total_slices_needed = people * slices_per_person
#     pizzas = math.ceil(total_slices_needed / slices_per_pizza)
#     return pizzas


# def leftover_slices(people, slices_per_person, slices_per_pizza):
#     """Calculate how many slices will be leftover."""
#     total_slices_needed = people * slices_per_person
#     pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza)
#     total_slices_ordered = pizzas * slices_per_pizza
#     leftover = total_slices_ordered - total_slices_needed
#     return leftover


# print("=== PIZZA PARTY PLANNER ===")
# guests = int(input("How many guests? "))
# slices_pp = int(input("Slices per person: "))
# slices_pizza = int(input("Slices per pizza: "))
# print()

# pizzas = pizzas_needed(guests, slices_pp, slices_pizza)
# total = pizzas * slices_pizza
# leftover = leftover_slices(guests, slices_pp, slices_pizza)

# print("=== PARTY SUMMARY ===")
# print(f"Guests:           {guests}")
# print(f"Pizzas to order:  {pizzas}")
# print(f"Total slices:     {total}")
# print(f"Leftover slices:  {leftover}")

# #######################
# # Solution Problem 1 - Challenge
# #######################


# def pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent=0):
#     """Calculate how many whole pizzas to order with optional buffer."""
#     adjusted_people = people * (1 + extra_percent / 100)
#     total_slices_needed = adjusted_people * slices_per_person
#     pizzas = math.ceil(total_slices_needed / slices_per_pizza)
#     return pizzas


# def leftover_slices(people, slices_per_person, slices_per_pizza, extra_percent=0):
#     """Calculate how many slices will be leftover."""
#     adjusted_people = people * (1 + extra_percent / 100)
#     total_slices_needed = adjusted_people * slices_per_person
#     pizzas = pizzas_needed(people, slices_per_person, slices_per_pizza, extra_percent)
#     total_slices_ordered = pizzas * slices_per_pizza
#     leftover = total_slices_ordered - total_slices_needed
#     return int(leftover)  # return whole slices


# print("=== PIZZA PARTY PLANNER ===")
# guests = int(input("How many guests? "))
# slices_pp = int(input("Slices per person: "))
# slices_pizza = int(input("Slices per pizza: "))
# print()

# # Without buffer
# pizzas = pizzas_needed(guests, slices_pp, slices_pizza)
# print(f"Without buffer: {pizzas} pizzas")

# # With 15% buffer
# pizzas_buffered = pizzas_needed(guests, slices_pp, slices_pizza, extra_percent=15)
# print(f"With 15% buffer: {pizzas_buffered} pizzas")

# #######################
# # Solution Problem 2 - Space Station Oxygen Monitor
# #######################


# def o2_status(level):
#     """Return the status of oxygen level."""
#     if level < 15:
#         return "CRITICAL"
#     elif level <= 18:
#         return "LOW"
#     elif level <= 23:
#         return "NORMAL"
#     else:
#         return "HIGH"


# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

# # Track counts for each status
# status_counts = {"NORMAL": 0, "LOW": 0, "CRITICAL": 0, "HIGH": 0}

# # Process each reading
# for hour, reading in enumerate(readings, start=1):
#     status = o2_status(reading)
#     status_counts[status] += 1

#     print(f"Hour {hour:2d}:  {reading}%  —  {status}")

#     if status == "CRITICAL":
#         print("*** ALERT: TAKE ACTION IMMEDIATELY ***")

# print()
# print("=== STATUS SUMMARY ===")
# print(f"NORMAL:    {status_counts['NORMAL']} hours")
# print(f"LOW:       {status_counts['LOW']} hours")
# print(f"CRITICAL:  {status_counts['CRITICAL']} hours")
# print(f"HIGH:      {status_counts['HIGH']} hours")

# #######################
# # Solution Problem 2 - Challenge
# #######################


# def o2_status(level):
#     """Return the status of oxygen level."""
#     if level < 15:
#         return "CRITICAL"
#     elif level <= 18:
#         return "LOW"
#     elif level <= 23:
#         return "NORMAL"
#     else:
#         return "HIGH"


# def trend(readings):
#     """Analyze the last 3 readings to determine trend."""
#     if len(readings) < 3:
#         return "STABLE"

#     last_three = readings[-3:]

#     # Check if consistently improving
#     if last_three[0] < last_three[1] < last_three[2]:
#         return "IMPROVING"
#     # Check if consistently declining
#     elif last_three[0] > last_three[1] > last_three[2]:
#         return "DECLINING"
#     else:
#         return "STABLE"


# readings = [21, 20, 19, 17, 16, 14, 13, 15, 18, 21, 22, 21]

# status_counts = {"NORMAL": 0, "LOW": 0, "CRITICAL": 0, "HIGH": 0}

# for hour, reading in enumerate(readings, start=1):
#     status = o2_status(reading)
#     status_counts[status] += 1

#     print(f"Hour {hour:2d}:  {reading}%  —  {status}")

#     if status == "CRITICAL":
#         print("*** ALERT: TAKE ACTION IMMEDIATELY ***")

# print()
# print("=== STATUS SUMMARY ===")
# print(f"NORMAL:    {status_counts['NORMAL']} hours")
# print(f"LOW:       {status_counts['LOW']} hours")
# print(f"CRITICAL:  {status_counts['CRITICAL']} hours")
# print(f"HIGH:      {status_counts['HIGH']} hours")
# print(f"\nTrend: {trend(readings)}")

# #######################
# # Solution Problem 3 - RPG Character Battle
# #######################


# def attack(defender_hp, damage):
#     """Subtract damage from defender HP and return new HP (minimum 0)."""
#     new_hp = defender_hp - damage
#     return max(0, new_hp)  # ensure HP doesn't go negative


# def is_alive(hp):
#     """Return True if HP > 0."""
#     return hp > 0


# hero_hp = 100
# monster_hp = 90
# hero_damage = 18
# monster_damage = 12
# round_num = 0

# print("=== BATTLE START ===")

# while is_alive(hero_hp) and is_alive(monster_hp):
#     round_num += 1

#     # Hero attacks
#     monster_hp = attack(monster_hp, hero_damage)

#     # Monster counter-attacks if still alive
#     if is_alive(monster_hp):
#         hero_hp = attack(hero_hp, monster_damage)

#     print(f"Round {round_num}:  Hero HP: {hero_hp:<3}  |  Monster HP: {monster_hp}")

# print()
# if is_alive(hero_hp):
#     print("HERO WINS! The monster has been defeated.")
# else:
#     print("HERO DEFEATED! The monster prevails.")

# #######################
# # Solution Problem 3 - Challenge
# #######################


# def attack(defender_hp, damage):
#     """Subtract damage from defender HP and return new HP (minimum 0)."""
#     new_hp = defender_hp - damage
#     return max(0, new_hp)


# def is_alive(hp):
#     """Return True if HP > 0."""
#     return hp > 0


# def critical_hit(damage):
#     """Return double damage 20% of the time."""
#     roll = random.randint(1, 10)
#     if roll <= 2:  # 20% chance (1 or 2)
#         return damage * 2
#     return damage


# hero_hp = 100
# monster_hp = 90
# hero_damage = 18
# monster_damage = 12
# round_num = 0

# print("=== BATTLE START ===")

# while is_alive(hero_hp) and is_alive(monster_hp):
#     round_num += 1

#     # Hero attacks with potential critical hit
#     actual_damage = critical_hit(hero_damage)
#     if actual_damage > hero_damage:
#         print("*** CRITICAL HIT! ***")
#     monster_hp = attack(monster_hp, actual_damage)

#     # Monster counter-attacks if still alive
#     if is_alive(monster_hp):
#         hero_hp = attack(hero_hp, monster_damage)

#     print(f"Round {round_num}:  Hero HP: {hero_hp:<3}  |  Monster HP: {monster_hp}")

# print()
# if is_alive(hero_hp):
#     print("HERO WINS! The monster has been defeated.")
# else:
#     print("HERO DEFEATED! The monster prevails.")

# #######################
# # Solution Problem 4 - Mission Clearance System
# #######################


# def check_fitness(score):
#     """Cleared if score >= 70."""
#     return score >= 70


# def check_rank(rank):
#     """Cleared if rank is 'Corporal', 'Sergeant', or 'Lieutenant'."""
#     approved_ranks = ["Corporal", "Sergeant", "Lieutenant"]
#     return rank in approved_ranks


# def check_service_years(years):
#     """Cleared if years >= 2."""
#     return years >= 2


# # Collect input
# name = input("SOLDIER NAME: ")
# fitness_score = int(input("FITNESS SCORE: "))
# rank = input("RANK: ")
# years = int(input("YEARS OF SERVICE: "))

# # Run all checks
# fitness_pass = check_fitness(fitness_score)
# rank_pass = check_rank(rank)
# service_pass = check_service_years(years)

# # Determine overall clearance
# all_cleared = fitness_pass and rank_pass and service_pass

# # Print report
# print()
# print("=== MISSION CLEARANCE REPORT ===")
# print(f"Soldier: {name}")
# print()
# print(f"  Fitness check:    {'PASS' if fitness_pass else 'FAIL'}")
# print(f"  Rank check:       {'PASS' if rank_pass else 'FAIL'}")
# print(f"  Service check:    {'PASS' if service_pass else 'FAIL'}")
# print()
# if all_cleared:
#     print("FINAL STATUS: CLEARED FOR MISSION.")
# else:
#     print("FINAL STATUS: NOT CLEARED.")

# #######################
# # Solution Problem 4 - Challenge
# #######################


# def check_fitness(score):
#     """Cleared if score >= 70."""
#     return score >= 70


# def check_rank(rank):
#     """Cleared if rank is 'Corporal', 'Sergeant', or 'Lieutenant'."""
#     approved_ranks = ["Corporal", "Sergeant", "Lieutenant"]
#     return rank in approved_ranks


# def check_service_years(years):
#     """Cleared if years >= 2."""
#     return years >= 2


# # Collect input
# name = input("SOLDIER NAME: ")
# fitness_score = int(input("FITNESS SCORE: "))
# rank = input("RANK: ")
# years = int(input("YEARS OF SERVICE: "))

# # Store checks in a list of tuples
# checks = [
#     ("Fitness check", check_fitness, fitness_score),
#     ("Rank check", check_rank, rank),
#     ("Service check", check_service_years, years),
# ]

# # Run all checks using a loop
# all_cleared = True
# check_results = []

# for check_name, check_function, value in checks:
#     result = check_function(value)
#     check_results.append((check_name, result))
#     if not result:
#         all_cleared = False

# # Print report
# print()
# print("=== MISSION CLEARANCE REPORT ===")
# print(f"Soldier: {name}")
# print()
# for check_name, result in check_results:
#     print(f"  {check_name:18}{'PASS' if result else 'FAIL'}")
# print()
# if all_cleared:
#     print("FINAL STATUS: CLEARED FOR MISSION.")
# else:
#     print("FINAL STATUS: NOT CLEARED.")

# #######################
# # Solution Problem 5 - Sports Leaderboard
# #######################


# def goals_per_game(goals, games):
#     """Return goals per game rounded to 2 decimal places."""
#     if games == 0:
#         return 0.0
#     return round(goals / games, 2)


# def mvp_candidate(gpg):
#     """Return True if the rate is 0.25 or higher."""
#     return gpg >= 0.25


# athletes = [
#     ("Jordan", 82, 15),  # (name, games_played, goals_scored)
#     ("Patel", 78, 22),
#     ("Okonkwo", 90, 18),
#     ("Li", 65, 9),
#     ("Reyes", 88, 31),
#     ("Fischer", 72, 14),
# ]

# print("=== SEASON LEADERBOARD ===")
# print("  Athlete       Games   Goals   GPG     MVP?")
# print("  " + "-" * 42)

# top_scorer_name = ""
# top_scorer_goals = 0

# for name, games, goals in athletes:
#     gpg = goals_per_game(goals, games)
#     is_mvp = mvp_candidate(gpg)

#     mvp_marker = "*" if is_mvp else ""
#     print(f"  {name:12}  {games:<6}  {goals:<6}  {gpg:<6.2f}  {mvp_marker}")

#     # Track top scorer
#     if goals > top_scorer_goals:
#         top_scorer_goals = goals
#         top_scorer_name = name

# print()
# print(f"Top scorer: {top_scorer_name} ({top_scorer_goals} goals)")

# #######################
# # Solution Problem 5 - Challenge
# #######################


# def goals_per_game(goals, games):
#     """Return goals per game rounded to 2 decimal places."""
#     if games == 0:
#         return 0.0
#     return round(goals / games, 2)


# def mvp_candidate(gpg):
#     """Return True if the rate is 0.25 or higher."""
#     return gpg >= 0.25


# def grade(gpg):
#     """Return a letter grade based on GPG rate."""
#     if gpg >= 0.30:
#         return "A"
#     elif gpg >= 0.25:
#         return "B"
#     elif gpg >= 0.20:
#         return "C"
#     elif gpg >= 0.15:
#         return "D"
#     else:
#         return "F"


# athletes = [
#     ("Jordan", 82, 15),
#     ("Patel", 78, 22),
#     ("Okonkwo", 90, 18),
#     ("Li", 65, 9),
#     ("Reyes", 88, 31),
#     ("Fischer", 72, 14),
# ]

# print("=== SEASON LEADERBOARD ===")
# print("  Athlete       Games   Goals   GPG     Grade   MVP?")
# print("  " + "-" * 50)

# top_scorer_name = ""
# top_scorer_goals = 0
# grade_distribution = {}  # dictionary to count grades

# for name, games, goals in athletes:
#     gpg = goals_per_game(goals, games)
#     is_mvp = mvp_candidate(gpg)
#     letter_grade = grade(gpg)

#     # Count grades
#     if letter_grade in grade_distribution:
#         grade_distribution[letter_grade] += 1
#     else:
#         grade_distribution[letter_grade] = 1

#     mvp_marker = "*" if is_mvp else ""
#     print(f"  {name:12}  {games:<6}  {goals:<6}  {gpg:<6.2f}  {letter_grade:<6}  {mvp_marker}")

#     # Track top scorer
#     if goals > top_scorer_goals:
#         top_scorer_goals = goals
#         top_scorer_name = name

# print()
# print(f"Top scorer: {top_scorer_name} ({top_scorer_goals} goals)")
# print()
# print("Grade Distribution:")
# for grade_letter in ["A", "B", "C", "D", "F"]:
#     count = grade_distribution.get(grade_letter, 0)
#     if count > 0:
#         print(f"  {grade_letter}: {count} athlete(s)")
