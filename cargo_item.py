import exception_func
import error_action_logger

class CargoItem:
    def __init__(self,item_id,name,weight,origin_planet):
        # strip the id
        self._item_id = item_id.strip() if isinstance(item_id, str) else item_id
        self.name=name
        self.weight=weight
        self.origin_planet =origin_planet

    @property
    def name(self):
        return self._name

    @property
    def weight(self):
        return self._weight

    @property
    def origin_planet(self):
        return self._origin_planet

    @property
    def item_id(self):
        return self._item_id

    # validate the name (min 2 characters) and set it
    @name.setter
    def name(self, name):
        if len(name) >= 2:
            self._name = name
            if hasattr(self, "_origin_planet"):
                error_action_logger.writeToActionLog(f"Name for item {self.item_id}# updated to {name}.")
                print(f"name for item {self.item_id}# updated to {name}")
        else:
            try:
                exception_func.checkForRaise(name, len(name) < 2, "Name must be at least 2 characters")
            except ValueError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_item, func name.setter", type(e).__name__)

    # validate the weight (must be a number and positive) and set it
    @weight.setter
    def weight(self, weight):
        if type(weight) in (int, float) and weight > 0:
            self._weight = weight
            if hasattr(self, "_origin_planet"):
                error_action_logger.writeToActionLog(f"Weight for item {self.item_id}# updated to {weight}.")
                print(f"weight for item {self.item_id}# updated to {weight}")

        else:
            try:
                exception_func.checkForRaise(weight, True, "Weight must be a positive number")
            except ValueError as e:
                print(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_item, func weight.setter", type(e).__name__)

    # set the origin planet; also logs the full "item created" message once name+weight are already set
    @origin_planet.setter
    def origin_planet(self, origin_planet):
        if hasattr(self, "_origin_planet"):
            self._origin_planet = origin_planet
            error_action_logger.writeToActionLog(
                f"Origin planet for item {self.item_id}# updated to {origin_planet}."
            )
        if hasattr(self, "_name") and hasattr(self, "_weight"):
            self._origin_planet = origin_planet
            if type(self).__name__ == "CargoItem":
                error_action_logger.writeToActionLog(f"Name for item {self.item_id}# set to {self.name}.")
                error_action_logger.writeToActionLog(f"Weight for item {self.item_id}# set to {self.weight}.")
                error_action_logger.writeToActionLog(f"Origin planet for item {self.item_id}# set to {origin_planet}.")
                error_action_logger.writeToActionLog(f"Item {self.item_id} created.")

    def __str__(self):
        if not (hasattr(self, "_name") and hasattr(self, "_weight") and hasattr(self, "_origin_planet")):
            try:
                exception_func.checkForRaise(self.item_id, True, "Item is invalid and cannot be displayed")
            except ValueError as e:
                return(f"Oops. {e}.")
                error_action_logger.writeToErrorsLog(f"Oops. {e}.","cargo_item, func toString", type(e).__name__)
        return (f"item_id: {self.item_id}\n"
                f"name: {self.name}\n"
                f"weight: {self.weight}\n"
                f"origin_planet: {self.origin_planet}")
