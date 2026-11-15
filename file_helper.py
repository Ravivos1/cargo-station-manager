import os
import re
import cargo_item
import special_cargo
import cargo_station
import error_action_logger
import exception_func


# write the cargo station's string form to a text file; asks before overwriting an existing file
def save_to_file(filename, cargolist):
    while os.path.exists(filename + ".txt"):
        answer = input(f"The file {filename} already exists, are you sure you want to overwrite it? (yes/no): ").strip().lower()
        while answer not in ("yes", "no"):
            answer = input("please answer yes or no: ").strip().lower()
        if answer == "yes":
            break
        filename = input("please enter a different filename: ")
    with open(filename + ".txt", "w", encoding="utf-8") as file:
        file.write(cargolist + "\n")
    error_action_logger.writeToActionLog(f"File {filename} saved successfully for the current cargo station.")


# read a saved file back into a new CargoStation, rebuilding each item from its text block
def load_from_file(filename):
    if not os.path.exists(filename + ".txt"):
        try:
            exception_func.checkForRaise(filename, True, f"There is no such file named: {filename}")
        except ValueError as e:
            print(f"Oops. {e}.")
            error_action_logger.writeToErrorsLog(f"Oops. {e}.", "file_helper, func load_from_file", type(e).__name__)
    else:
        with open(filename + ".txt", "r", encoding="utf-8") as file:
            content = file.read()
        station = cargo_station.CargoStation()
        # split the file into per-item text blocks and parse each one's fields
        for block in re.split(r"Item number \d+\n", content):
            fields = dict(line.partition(": ")[::2] for line in block.strip().splitlines() if ": " in line)
            if block.strip() and all(k in fields for k in ("item_id", "name", "weight", "origin_planet")):
                # item_id stays a string (ids can be letters and numbers, not just numbers)
                item_id = fields["item_id"]
                if "Danger level" in fields and "Requires-cooling" in fields:
                    item = special_cargo.SpecialCargo(item_id, fields["name"], float(fields["weight"]),
                                                      fields["origin_planet"], int(fields["Danger level"]),
                                                      fields["Requires-cooling"].strip().lower() == "true")
                else:
                    item = cargo_item.CargoItem(item_id, fields["name"], float(fields["weight"]),
                                                fields["origin_planet"])
                station.add_item(item)
        error_action_logger.writeToActionLog(f"File {filename} loaded successfully to a cargo station.")
        return station
