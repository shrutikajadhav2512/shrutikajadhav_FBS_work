from vehicle import TwoWheeler, ThreeWheeler, FourWheeler, HeavyVehicle
def menu():
    while True:
        print("\n--- TOLL SYSTEM ---")
        print("1. Two Wheeler")
        print("2. Three Wheeler")
        print("3. Four Wheeler")
        print("4. Heavy Vehicle")
        print("5. Exit")
        choice = input("choose one: ")
        if choice == '5':
            print("System close.")
            break
        persons = int(input("Enter total persons: "))
        vehicle = None
        if choice == '1':
            vehicle = TwoWheeler(persons)
        elif choice == '2':
            vehicle = ThreeWheeler(persons)
        elif choice == '3':
            vehicle = FourWheeler(persons)
        elif choice == '4':
            vehicle = HeavyVehicle(persons)
        else:
            print("Wrong choice!")
            continue
        print(f"Total Toll = Rs {vehicle.calculate_toll()}")
menu()