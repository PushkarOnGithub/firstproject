from verify_email import verify_email

email_address = ""
with open("NearByColleges.csv") as f:
    count_exists = 0
    count_not_exists = 0
    email = f.readline()
    while(email != ""):
        is_valid = verify_email(email)

        if is_valid:
            print(f"{email[:-1]} exists")
            count_exists+=1
        else:
            print(f"{email[:-1]} does not exist")
            count_not_exists+=1
        email = f.readline()
    print("exists : ", count_exists, " not exists : ", count_not_exists)

# is_valid = verify_email(email_address)

# if is_valid:
#     print("Email address exists")
# else:
#     print("Email address does not exist")
