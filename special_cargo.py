from finalProject.cargo_item import CargoItem
import exception_func
import error_action_logger


class SpecialCargo(CargoItem):

    def __init__(self, item_id, name, weight, origin_planet, danger_level, requires_cooling):
        super().__init__(item_id, name, weight, origin_planet)
        self.danger_level = danger_level
        self.requires_cooling = requires_cooling

    @property
    def danger_level(self):
        return getattr(self, "_danger_level")

    @property
    def requires_cooling(self):
        return getattr(self, "_requires_cooling")

    # validate danger level (must be an int between 1 and 5) and set it
    @danger_level.setter
    def danger_level(self, value):
        if type(value) is int and 1 <= value <= 5:
            self._danger_level = value
            if hasattr(self, "_requires_cooling"):
                error_action_logger.writeToActionLog(f"Danger level for item {self.item_id}# updated to {value}.")
        else:
            try:
                exception_func.checkForRaise(value, True, "Danger level must be between 1 and 5")
            except ValueError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","special_cargo, func danger_level.setter", type(e).__name__)

    # validate requires_cooling (bool, or "true"/"false" string in any letter case) and set it
    @requires_cooling.setter
    def requires_cooling(self, value):
        is_bool = type(value) is bool
        # a string counts as valid as long as lower-casing it gives "true" or "false"
        is_valid_string = type(value) is str and value.lower() in ["true", "false"]
        if not is_bool and not is_valid_string:
            try:
                exception_func.checkForRaise(value, True, "Requires cool must be a boolean value (true or false)")
            except ValueError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","special_cargo, func requires_cooling.setter", type(e).__name__)
            return
        new_value = value if is_bool else value.lower() == "true"
        # writes to log for all attrs if new item, or just the update if it is updating an item
        if hasattr(self, "_requires_cooling"):
            self._requires_cooling = new_value
            error_action_logger.writeToActionLog(f"Requires cooling for item {self.item_id}# updated to {self.requires_cooling}.")
        else:
            self._requires_cooling = new_value
            if hasattr(self, "_danger_level") and hasattr(self, "_weight") and hasattr(self, "_name") and hasattr(self, "_origin_planet"):
                error_action_logger.writeToActionLog(f"Name for item {self.item_id}# set to {self.name}.")
                error_action_logger.writeToActionLog(f"Weight for item {self.item_id}# set to {self.weight}.")
                error_action_logger.writeToActionLog(f"Origin planet for item {self.item_id}# set to {self.origin_planet}.")
                error_action_logger.writeToActionLog(f"Danger level for item {self.item_id}# set to {self.danger_level}.")
                error_action_logger.writeToActionLog(f"Requires cooling for item {self.item_id}# set to {self.requires_cooling}.")
                error_action_logger.writeToActionLog(f"Special item {self.item_id} created.")

    def __str__(self):
        if not (hasattr(self, "_name") and hasattr(self, "_weight") and hasattr(self, "_origin_planet")
                and hasattr(self, "_danger_level") and hasattr(self, "_requires_cooling")):
            try:
                exception_func.checkForRaise(self.item_id, True, "Item is invalid and cannot be displayed")
            except ValueError as e:
                return(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","special_cargo, func toString", type(e).__name__)
        return (
            super().__str__()
            + f"\nDanger level: {self.danger_level}\n"
            + f"Requires-cooling: {self.requires_cooling}")
