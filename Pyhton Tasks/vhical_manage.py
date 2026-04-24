# vehicle_list = []

# def add_vehicle():
#     manufacturer = input("Enter vehicle manufacturer: ")
#     model = input("Enter vehicle model: ")
#     vehicle = {'manufacturer': manufacturer, 'model': model}
#     vehicle_list.append(vehicle)
#     print("Vehicle added.")


# def delete_vehicle():
#     manufacturer = input("Enter manufacturer to delete: ")
#     model = input("Enter model to delete: ")
#     vehicle = {'manufacturer': manufacturer, 'model': model}

#     if vehicle in vehicle_list:

#         vehicle_list.remove(vehicle)
#         print("Vehicle deleted.")

#     else:
#         print("Vehicle not found.")


# def update_vehicle():
#     old_manufacturer = input("Enter old manufacturer: ")
#     old_model = input("Enter old model: ")
#     old_vehicle = {'manufacturer': old_manufacturer, 'model': old_model}

#     if old_vehicle in vehicle_list:
#         new_manufacturer = input("Enter new manufacturer: ")
#         new_model = input("Enter new model: ")
#         new_vehicle = {'manufacturer': new_manufacturer, 'model': new_model}
#         index = vehicle_list.index(old_vehicle)
#         vehicle_list[index] = new_vehicle

#         print("Vehicle updated.")
#     else:
#         print("Vehicle not found.")

# def search_vehicle():
#     manufacturer = input("Enter manufacturer to search: ")
#     model = input("Enter model to search: ")
#     vehicle = {'manufacturer': manufacturer, 'model': model}

#     if vehicle in vehicle_list:
#         print("Vehicle found.")

#     else:
#         print("Vehicle not found.")

# def display_vehicles():
#     if vehicle_list:
#         print("Vehicles:")
#         for vehicle in vehicle_list:
#             print(f"Manufacturer: {vehicle['manufacturer']}, Model: {vehicle['model']}")
#     else:
#         print("No vehicles available.")
# def main():
#     while True:
#         print("\nMenu")
#         print("1. Add Vehicle")
#         print("2. Delete Vehicle")
#         print("3. Update Vehicle")
#         print("4. Search Vehicle")
#         print("5. Display Vehicles")
#         print("6. Exit")
#         choice = int(input("Enter your choice: "))
#         match choice:
#             case 1:
#                 add_vehicle()
#             case 2:
#                 delete_vehicle()
#             case 3:
#                 update_vehicle()
#             case 4:
#                 search_vehicle()
#             case 5:
#                 display_vehicles()
#             case 6:
#                 print("Exiting the app.")
#                 break
#             case _:
#                 print("Invalid choice.")

# main()