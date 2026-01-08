# function with an output using the return statement
def format_name(f_name, l_name):
    formatted_f_name = (f_name.title())
    formatted_l_name = (l_name.title())

    return f"{formatted_f_name} {formatted_l_name}"

print(format_name("jAy", "ViCK"))
