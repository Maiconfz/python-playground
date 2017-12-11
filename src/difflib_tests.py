from difflib import get_close_matches

data = ["apple", "orange", "pineapple"]

print(get_close_matches("app", data, cutoff=0.8))
print(get_close_matches("app",data))
