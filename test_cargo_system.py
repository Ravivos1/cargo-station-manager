import cargo_station
import cargo_item
import special_cargo
import file_helper
import unittest
import os
from special_cargo import SpecialCargo

class Testcreate_new_cargo(unittest.TestCase):
    def test_create_valid_cargo_item(self):
        item = cargo_item.CargoItem(1,"hghg",33,"Earth")
        self.assertEqual(item.item_id, 1)
        self.assertEqual(item.name, "hghg")
        self.assertEqual(item.weight, 33)
        self.assertEqual(item.origin_planet, "Earth")

    def test_create_valid_new_special_cargo(self):
        sitem = special_cargo.SpecialCargo(1,"sdsd",78,"Mars",4,"true")
        self.assertEqual(sitem.item_id, 1)
        self.assertEqual(sitem.name, "sdsd")
        self.assertEqual(sitem.weight, 78)
        self.assertEqual(sitem.origin_planet, "Mars")
        self.assertEqual(sitem.danger_level, 4)
        self.assertEqual(sitem.requires_cooling, True)

    def test_create_invalid_weight_cargo(self):
        item = cargo_item.CargoItem(1,"haa",-33,"Earth")
        self.assertFalse(hasattr(item,"weight"))

    def test_create_invalid_name_cargo(self):
        sitem = special_cargo.SpecialCargo(1,"h",33,"Earth",3,True)
        self.assertFalse(hasattr(sitem,"name"))

    def test_create_duplicate_items_in_station(self):
        station = cargo_station.CargoStation()
        item1 = cargo_item.CargoItem(1,"raviv",33,"Earth")
        station.add_item(item1)
        item2 = special_cargo.SpecialCargo(1,"raviv",33,"Earth",3,True)
        station.add_item(item2)
        self.assertEqual(len(station.items), 1)
        self.assertIs(station.items[0], item1)
        self.assertIsNot(station.items[0], item2)

    def test_item_missing_item_from_cargo(self):
        station = cargo_station.CargoStation()
        item1 = cargo_item.CargoItem(1,"raviv",33,"Earth")
        item2 = special_cargo.SpecialCargo(2,"raviv",33,"Earth",3,True)
        station.add_item(item1)
        station.add_item(item2)
        station.remove_item(5)
        self.assertEqual(len(station.items), 2)

    def test_total_weight_empty_station(self):
        station = cargo_station.CargoStation()
        self.assertEqual(station.get_total_weight(), 0)

    def test_total_weight_cargo_station(self):
        station = cargo_station.CargoStation()
        item1 = cargo_item.CargoItem(1,"raviv",30,"Earth")
        item2 = special_cargo.SpecialCargo(2,"raviv",40,"Earth",3,True)
        station.add_item(item1)
        station.add_item(item2)
        self.assertEqual(station.get_total_weight(), 70)


    def test_save_and_load_file(self):
        station = cargo_station.CargoStation()
        item1 = cargo_item.CargoItem(1,"raviv",30,"Earth")
        item2 = special_cargo.SpecialCargo(2,"raviv",40,"Earth",3,True)
        station.add_item(item1)
        station.add_item(item2)
        file_helper.save_to_file("test_save_load", station.__str__())
        loaded_station = file_helper.load_from_file("test_save_load")
        self.assertEqual(len(loaded_station.items), len(station.items))
        for i in range(len(station.items)):
            self.assertEqual(str(station.items[i].item_id), str(loaded_station.items[i].item_id))
        os.remove("test_save_load.txt")

    def test_load_missing_file(self):
        loaded_station = file_helper.load_from_file("no_such_file_at_all")
        self.assertIsNone(loaded_station)