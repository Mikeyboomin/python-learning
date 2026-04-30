def register_user(data):
    try:
        name = data[0]
        age = int(data[1])
        email = data[2]

        if age < 18:
            print("User must be 18 or older.")
            return
        else:
            print(f"User {name} registered successfully with email {email}.")
            
    except ValueError:
        print("Age must be a valid number.")
        return
    except IndexError:
        print("Missing required fields.")
        return

register_user(["Boomin", "25", "boomin@email.com"])
register_user(["Alice", "sixteen", "alice@email.com"])
register_user(["Bob"])
register_user(["Charlie", "17", "charlie@email.com"])
register_user(["Diana", "30"])