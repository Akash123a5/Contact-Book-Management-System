def validate_string(value):
    try:
        if not value.isalpha():
            raise ValueError("Name must only letters.")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False

def validate_phone_number(value):
    try:
        if not value.isdigit():
            raise ValueError("Phone number must only digits.")
        if len(value) != 11:
            raise ValueError("Phone number must be 11 digits long.")
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
