import hashlib

def get_md5_hash(password, salt):
    """Generate MD5 hash of the password combined with the salt."""
    return hashlib.md5(password.encode() + salt.encode()).hexdigest()

def main():
    hashPass = "d89eddeec748c49d5add2f8f347b8899"
    salt = "pepper"

    # Present options to the user
    print("Options:")
    print("1. Verify password")
    print("2. Get MD5 hash of a new password")
    choice = input("Choose an option (1 or 2): ")

    if choice == '1':
        # Verify password
        password = input("Enter password to verify: ")
        userHash = get_md5_hash(password, salt)
        if(hashPass == userHash):
            print("Password correct!")
        else:
            print("Password Incorrect.")
    elif choice == '2':
        # Generate hash for a new password
        password = input("Enter password to hash: ")
        print("MD5 hash of your password is:", get_md5_hash(password, salt))
    else:
        print("Invalid option selected.")

if __name__ == "__main__":
    main()
