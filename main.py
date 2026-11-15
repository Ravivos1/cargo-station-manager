from cargo_item import CargoItem
from cargo_station import CargoStation
from file_helper import load_from_file, save_to_file
from special_cargo import SpecialCargo


def main():
    # let the user start with new station or load an existing station; keep asking until a valid station
    cargost = None
    while cargost is None:
        load_choice = input("Press 1 to start a new cargo station, press 2 to load an existing one:\n")
        while load_choice not in ("1", "2"):
            load_choice = input("please choose 1 or 2:\n")

        if load_choice == "2":
            filename = input("please enter the filename to load:\n")
            cargost = load_from_file(filename)
        else:
            cargost = CargoStation()

    # menu bar starts
    while True:
        choice = input("/////////////////////Welcome to Cargo Station main menu///////////////////// \n" +
              "To add a cargo press 1 \n" +
              "To remove a cargo press 2 \n" +
              "To find a specific cargo press 3 \n" +
              "To show the total weight press 4 \n" +
              "To show number of dangerous cargo press 5 \n" +
              "To save and exit press 6 \n")

        match choice:
            case "1":
                print("/////////////////////To add a cargo/////////////////////")
                # asks the user if it is a special cargo ir cargo item and adds all attrs
                cargo_type = input("if its a regular cargo press 1:\n"
                                    "if its a special cargo press 2:\n")
                while cargo_type not in ("1", "2"):
                    cargo_type = input("please choose 1 or 2:\n")

                item_id = input("please enter cargo Id:")
                name = input("please enter cargo Name:")
                weight_input = input("please enter cargo Weight:")
                try:
                    weight = float(weight_input)
                except ValueError:
                    weight = weight_input
                origin_planet = input("please enter cargo Original Planet:")

                if cargo_type == "1":
                    cargo = CargoItem(item_id, name, weight, origin_planet)
                else:
                    danger_input = input("please enter cargo Danger level between 1 and 5:")
                    try:
                        danger = int(danger_input)
                    except ValueError:
                        danger = danger_input
                    cool = input("please enter True or False if the cargo needs Cooling :")
                    cargo = SpecialCargo(item_id, name, weight, origin_planet, danger, cool)

                cargost.add_item(cargo)

            case "2":
                print("/////////////////////To remove a cargo/////////////////////")
                item_id = input("please enter cargo Id:")
                cargost.remove_item(item_id)

            case "3":
                print("/////////////////////To find a cargo/////////////////////")
                item_id = input("please enter cargo Id:")
                found = cargost.find_item(item_id)
                if found is not None:
                    print(found)

            case "4":
                print(f"the total weight: {cargost.get_total_weight()}")

            case "5":
                print(f"total dangerous cargo that rank 3+ is: {cargost.count_dangerous_cargo()}")

            case "6":
                filename = input("please enter a filename to save the cargo station:\n")
                save_to_file(filename, str(cargost))
                break

            case _:
                print("please choose a number from 1 to 6")

if __name__ == '__main__':
    main()
