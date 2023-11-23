class SimpleDBMS:
    def __init__(self):
        self.records = {}

    def create_record(self, record_id, name, age, state, city):
        if record_id not in self.records:
            data = {"name": name, "age": age, "state": state, "city": city}
            self.records[record_id] = data
            print(f"Record with ID {record_id} created successfully.")
        else:
            print(f"Error: Record with ID {record_id} already exists.")

    def read_record(self, record_id):
        if record_id in self.records:
            print(f"Record ID: {record_id}, Data: {self.records[record_id]}")
        else:
            print(f"Error: Record with ID {record_id} not found.")

    def update_record(self, record_id, field, new_value):
        if record_id in self.records:
            if field in self.records[record_id]:
                self.records[record_id][field] = new_value
                print(f"Record with ID {record_id} updated successfully.")
            else:
                print(f"Error: Field '{field}' not found in the record.")
        else:
            print(f"Error: Record with ID {record_id} not found.")

    def delete_record(self, record_id):
        if record_id in self.records:
            del self.records[record_id]
            print(f"Record with ID {record_id} deleted successfully.")
        else:
            print(f"Error: Record with ID {record_id} not found.")

    def display_all_records(self):
        print("All Records:")
        for record_id, data in self.records.items():
            print(f"Record ID: {record_id}, Data: {data}")

# Example Usage with User Input
db = SimpleDBMS()

while True:
    print("\nOptions:")
    print("1. Add a new record")
    print("2. Read a record")
    print("3. Update a record")
    print("4. Delete a record")
    print("5. Display all records")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        record_id = int(input("Enter the record ID: "))
        name = input("Enter the name: ")
        age = int(input("Enter the age: "))
        state = input("Enter the state: ")
        city = input("Enter the city: ")
        db.create_record(record_id, name, age, state, city)
    elif choice == '2':
        record_id = int(input("Enter the record ID to read: "))
        db.read_record(record_id)
    elif choice == '3':
        record_id = int(input("Enter the record ID to update: "))
        field = input("Enter the field to update (name, age, state, city): ")
        new_value = input(f"Enter the new value for {field}: ")
        db.update_record(record_id, field, new_value)
    elif choice == '4':
        record_id = int(input("Enter the record ID to delete: "))
        db.delete_record(record_id)
    elif choice == '5':
        db.display_all_records()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
