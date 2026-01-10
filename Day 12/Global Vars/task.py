# Modifying Global Scope

enemies = 1


def increase_enemies():
    global enemies # needed to modify something that is global scope
    enemies += 1
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


