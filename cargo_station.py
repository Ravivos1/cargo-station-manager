import cargo_item
import special_cargo
import exception_func
import error_action_logger
import inspect


class CargoStation:

    def __init__(self):
        self._items = []
        error_action_logger.writeToActionLog("New empty cargo station list was created.")

    @property
    def items(self):
        return self._items

    # validate and add a cargo item to the station (rejects invalid items and duplicate ids)
    def add_item(self, item):
        if ((type(item).__name__ != "CargoItem" and type(item).__name__ != "SpecialCargo")):
            try:
                exception_func.checkForRaise(item, True, "You tried to add an invalid item to the cargo station")
            except ValueError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func add_item", type(e).__name__)
        else:
            is_cargo = type(item).__name__ == "CargoItem"
            is_valid = (hasattr(item, "_name") and hasattr(item, "_weight") and hasattr(item, "_origin_planet"))
            if not is_cargo:
                is_valid = is_valid and hasattr(item, "_danger_level") and hasattr(item, "_requires_cooling")
            if not is_valid:
                try:
                    exception_func.checkForRaise(item, True,
                                                f"Item {item.item_id} is invalid and cannot be added to the station")
                except ValueError as e:
                    print(f"Oops. {e}.")
                    error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func add_item", type(e).__name__)
                return
            found = self.find_item(item.item_id)
            if found is None:
                self._items.append(item)
                print("Item added successfully")
                error_action_logger.writeToActionLog(f"Item {item.item_id} added successfully to cargo station list.")
            else:
                try:
                    exception_func.checkForRaise(item, found is not None, "Item already exists", exception_func.DuplicateCargoError)
                except exception_func.DuplicateCargoError as e:
                    print(f"Oops. {e}.")
                    error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func add_item", type(e).__name__)

    # remove an item by id, if it exists
    def remove_item(self, item_id):
        item_id = item_id.strip() if isinstance(item_id, str) else item_id
        found = self.find_item(item_id)
        if found is not None:
            self._items.remove(found)
            print("Item removed successfully")
            error_action_logger.writeToActionLog(f"Item {item_id} removed successfully from cargo station list.")
        else:
            try:
                exception_func.checkForRaise(item_id, found is None, "Item does not exist", exception_func.CargoNotFoundError)
            except exception_func.CargoNotFoundError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func remove_item", type(e).__name__)

    # find an item by id, returns None if not found
    def find_item(self, item_id):
        # strip stray whitespace so a lookup id always matches a stored id
        item_id = item_id.strip() if isinstance(item_id, str) else item_id
        # check the caller, so internal calls (add_item/remove_item/etc.) don't print "not found" twice
        caller = inspect.stack()[1].function
        if len(self._items) == 0:
            try:
                exception_func.checkForRaise(self, len(self._items) == 0, "No items in Station", exception_func.CargoNotFoundError)
            except exception_func.CargoNotFoundError as e:
                if caller not in ["add_item", "remove_item", "get_total_weight", "count_dangerous_cargo", "__str__"]:
                    print(f"Item {item_id}# not in Station, the station is empty.")
                    error_action_logger.writeToErrorsLog(f"Item {item_id}# not in Station, the station is empty.","cargo_station, func find_item", type(e).__name__)
                return None
        for item in self._items:
            if item.item_id == item_id:
                return item
        try:
            exception_func.checkForRaise(self, True, f"Item {item_id}# not in Station", exception_func.CargoNotFoundError)
        except exception_func.CargoNotFoundError as e:
            if caller not in ["add_item", "remove_item", "get_total_weight", "count_dangerous_cargo", "__str__"]:
                print(f"Item {item_id}# not in Station.")
                error_action_logger.writeToErrorsLog(f"Item {item_id}# not in Station.","cargo_station, func find_item", type(e).__name__)
        return None

    # sum the weight of all items in the station
    def get_total_weight(self):
        if len(self._items) == 0:
            try:
                exception_func.checkForRaise(self, len(self._items) == 0, "Cannot calculate weight, no items in Station", exception_func.CargoNotFoundError)
            except exception_func.CargoNotFoundError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func get_total_weight", type(e).__name__)
                return 0
        else:
            total_weight = 0
            for item in self._items:
                total_weight += item.weight
            return total_weight

    # count cargo items with a danger level of 3 or higher (regular cargo items have no danger level, so they're skipped)
    def count_dangerous_cargo(self):
        if len(self._items) == 0:
            try:
                exception_func.checkForRaise(self, len(self._items) == 0, "Cannot count dangerous cargo, no items in Station", exception_func.CargoNotFoundError)
            except exception_func.CargoNotFoundError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func count_dangerous_cargo", type(e).__name__)
                return 0
        else:
            counter = 0
            for item in self._items:
                if hasattr(item, "danger_level") and item.danger_level >= 3:
                    counter += 1
            return counter

    def __str__(self):
        if len(self._items) == 0:
            try:
                exception_func.checkForRaise(self, len(self._items) == 0, "Cannot print station, no items in Station", exception_func.CargoNotFoundError)
            except exception_func.CargoNotFoundError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_station, func toString", type(e).__name__)
                return "Station is empty."
        else:
            res = []
            for number, item in enumerate(self._items, start=1):
                res.append(f"Item number {number}\n{item}")
            return "\n".join(res)
