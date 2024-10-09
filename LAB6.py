def calculate_registration_fee(age, is_member):
   
    if age < 18:
        if is_member:
            return 450.00
        else:
            return 650.00
    elif 18 <= age <= 65:
        if is_member:
            return 550.00
        else:
            return 750.00
    else:  # age > 65
        if is_member:
            return 400.00
        else:
            return 600.00


age = int(input("Enter the attendee's age: "))
membership_status = input("Is the attendee a member? (yes/no): ")

is_member = membership_status.lower() == "yes"

fee = calculate_registration_fee(age, is_member)

print(f"The registration fee is: {fee} pesos")
