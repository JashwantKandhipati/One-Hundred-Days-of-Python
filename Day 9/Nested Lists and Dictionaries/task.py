capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Stuttgart", "Berlin"],
# }

# Print Lille
# print(travel_log["France"][1])

# Nested list in a list
# nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][0])

# Nested Dictionary in Dictionary
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Stuttgart", "Berlin"],
        "total_visits": 5
    }
}

print(travel_log["Germany"]["cities_visited"][0])