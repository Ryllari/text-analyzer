import os

from utils import DATA_PARAMS, HashTable, save_data_to_csv, read_csv_to_hash_table, data_keys_to_csv, save_categories_data_to_csv
from db_control import get_filtered_data
from analyzer import classify_text, analyze_completeness


# Global Vars
data_table = HashTable()
category_table = HashTable()
completeness_table = HashTable()
id_keys = set()


def populate_data_table():
    db_data = get_filtered_data()
    for key, value in db_data.items():
        data_table.put(key, value)
        id_keys.add(key)
    return id_keys, data_table
    

def populate_category_table():
    for key in id_keys:
        data = data_table.get(key)
        data_description = data.get("description") or {}
        description_content = data_description.get("general")
        if not description_content:
            continue
        categories = classify_text(description_content)
        if categories:
            category_table.put(
                key,
                categories
            )
    return category_table


def populate_completeness_table():
    for key in id_keys:
        data = data_table.get(key)
        categories = analyze_completeness(data, DATA_PARAMS)
        if categories:
            completeness_table.put(
                key,
                categories
            )
    return completeness_table


def main():
    running = True
    while running:
        os.system('clear')

        print("************************************************")
        print("************** CONTENT ANALYZER *************")
        print("************************************************")
        print("\n\nWhat do you want?")
        print("\n1 - Populate data table from database")
        print("\n2 - Populate data table from csv file")
        print("\n3 - Analyze data categories")
        print("\n4 - Analyze data completeness")
        print("\n5 - Export data table as csv file")
        print("\n6 - Export data categories as csv file")
        print("\n7 - Export data completeness as csv file")
        print("0 - Exit")

        option = input("\Choose an option:")

        if option == '0':
            print("Bye!")
            running = False
            break

        elif option == "1":
            print("Populating data...")
            populate_data_table()
            print("Done!")

        elif option == "2":
            filename = input("Write the filename (with .csv): ")
            print("Populating data...")
            read_csv_to_hash_table(filename, data_table)
            print("Done!")

        elif option == "3":
            print("Analysing categories...")
            populate_category_table()
            print("Done!")

        elif option == "4":
            print("Analysing completeness...")
            populate_completeness_table()
            print("Done!")

        elif option == "5":
            filename = input("Write the destination filename (with .csv): ")
            keys = data_keys_to_csv()
            save_data_to_csv(id_keys, data_table, filename, keys)
            print("Done!")

        elif option == "6":
            filename = input("Write the destination filename (with .csv): ")
            save_categories_data_to_csv(id_keys, category_table, filename)
            print("Done!")

        elif option == "7":
            filename = input("Write the destination filename (with .csv): ")
            keys = ["id", "completeness", "filled_fields", "missing_fields"]
            save_data_to_csv(id_keys, completeness_table, filename, keys)
            print("Done!")

        else:
            print("Invalid option!")

        input("\Prees any key to back...")

        # Clear terminal
        if(os.name == 'posix'):
            os.system('clear')
        else:
            os.system('cls')


if __name__ == "__main__":
    main()