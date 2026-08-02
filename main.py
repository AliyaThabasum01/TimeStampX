from timestamp import show_timestamp, convert_timestamp

while True:
    print("\n===== TimeStampX =====")
    print("1. Current Timestamp")
    print("2. Convert Timestamp")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        show_timestamp()

    elif choice == "2":
        ts = int(input("Enter Unix timestamp: "))
        convert_timestamp(ts)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
