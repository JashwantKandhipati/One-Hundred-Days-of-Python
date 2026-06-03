enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# LOCAL scope
# def basketball():
#     num_of_basketball = 2
#     print(num_of_basketball)
#
# basketball()
# print(num_of_basketball)  # can't print it out because it is outside the scope

# GLOBAL Scope
# num_of_basketball = 2
#
# def basketball():
#     num_of_players = 5
#     print(num_of_basketball)
#
# basketball()