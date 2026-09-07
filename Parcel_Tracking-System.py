parcels = {}

parcel_count = 1

while True:
    print("\n==== PARCEL TRACKING SYSTEM ====")
    print("1. Add parcel")
    print("2. View parcels")
    print("3. Track parcel")
    print("4. Update parcel")
    print("5. Exit")

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
        tracking_id = input("Enter tracking ID: ")

        if tracking_id in parcels:
            status = parcels[tracking_id]["status"]

            print("\n==== TRACKING STATUS ====")
            print("Tracking ID:", tracking_id)
            print("Current Status:", status)

            print("\nDelivery Progress:")

            if status == "Booked":
                print("✓ Booked")
                print("○ In Transit")
                print("○ Out for Delivery")
                print("○ Delivered")

            elif status == "In Transit":
                print("✓ Booked")
                print("✓ In Transit")
                print("○ Out for Delivery")
                print("○ Delivered")

            elif status == "Out for Delivery":
                print("✓ Booked")
                print("✓ In Transit")
                print("✓ Out for Delivery")
                print("○ Delivered")

            elif status == "Delivered":
                print("✓ Booked")
                print("✓ In Transit")
                print("✓ Out for Delivery")
                print("✓ Delivered")

        else:
            print("Parcel Not Found!")

    elif choice == "4":
        tracking_id = input("Enter tracking ID: ")

        if tracking_id in parcels:
            print("\n1. Booked")
            print("2. In Transit")
            print("3. Out for Delivery")
            print("4. Delivered")

            status_choice = input("Select the new status: ")

            statuses = {
                "1": "Booked",
                "2": "In Transit",
                "3": "Out for Delivery",
                "4": "Delivered"
            }

            if status_choice in statuses:
                parcels[tracking_id]["status"] = statuses[status_choice]
                print("Status Updated Successfully!")
            else:
                print("Invalid status choice!")

        else:
            print("Parcel Not Found!")

    elif choice == "5":
        print("Thank you for using Parcel Tracking System!")
        break

    else:
        print("Invalid Choice!")