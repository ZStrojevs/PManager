import json

with open("vault.json", "r") as f:
    vault = json.load(f)

def add(website, user, password):
    if website in vault:
        print("exists")
    else:
        vault[website] = {"username": user, "password": password}
        with open("vault.json", "w") as f:
            json.dump(vault, f)
def delete(website):
    if website in vault:
        del vault[website]
        with open("books.json", "w") as file:
            json.dump(vault, file)
        print("entry deleted")
def show_all():
    for website, info in vault.items():
        print(f"Site: {website}, Username: {info['username']}, Password: {'*' * len(info['password'])}")
