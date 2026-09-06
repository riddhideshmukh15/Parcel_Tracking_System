parcels = {}

parcel_count = 1

while True:
    print("\n==== PARCEL TRACKING SYSTEM ====")
    print("1. Add parcel")
    print("2. View parcels")
    print("3. Track parcel")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sender = input("Enter sender's name: ")
        receiver = input("Enter receiver's name: ")
        address = input("Enter delivery address: ")

        parcel_id = "P" + str(parcel_count)
        parcel_count += 1

        parcels[parcel_id] = {
            "sender": sender,
            "receiver": receiver,
            "address": address,
            "status": "Booked"
        }

        print("\nParcel added successfully!")
        print("Tracking ID:", parcel_id)

    elif choice == "2":
        if not parcels:
            print("\nNo parcels found!")
        else:
            print("\n==== ALL PARCELS ====")

            for parcel_id, parcel in parcels.items():
                print("\nTracking ID:", parcel_id)
                print("Sender:", parcel["sender"])
                print("Receiver:", parcel["receiver"])
                print("Address:", parcel["address"])
                print("Status:", parcel["status"])

    elif choice == "3":
        parcel_id = input("Enter tracking ID: ")

        if parcel_id in parcels:
            parcel = parcels[parcel_id]

            print("\n==== PARCEL DETAILS ====")
            print("Tracking ID:", parcel_id)
            print("Sender:", parcel["sender"])
            print("Receiver:", parcel["receiver"])
            print("Address:", parcel["address"])
            print("Status:", parcel["status"])

        else:
            print("Parcel not found!")

    elif choice == "4":
        print("Thank you for using Parcel Tracking System!")
        break

    else:
        print("Invalid choice!")