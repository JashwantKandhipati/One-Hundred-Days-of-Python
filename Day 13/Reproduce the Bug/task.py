from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)        # was (1,6) but changed it to (0,5) no out of scope/range error
print(dice_images[dice_num])
