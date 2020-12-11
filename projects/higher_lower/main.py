import art, data, random

print(art.logo)

# random choose a and b from data. store in variable
# print compare a first random choice data 
# print vs art
# print against b second random choice data 
# print and store in variable who has more followers a or b
# compare a and b which is greater, if user chose correct, add point to score. if not, user loses and game ends

choice_a = random.choice(data.data)
choice_b = random.choice(data.data)

print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}.")
print(art.vs)
print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}.")
user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
