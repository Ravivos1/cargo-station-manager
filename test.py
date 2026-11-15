import cargo_item
import special_cargo
import cargo_station
import file_helper

def main():
    item=special_cargo.SpecialCargo(1,"dss",43,"Mars",4,"true")
    item2=cargo_item.CargoItem(2,"lala",50,"Earth")
    items=cargo_station.CargoStation()
    items.add_item(item)
    # item2=cargo_item.CargoItem(1,"hghg",33,"Earth")
    items.add_item(item2)
    # print(items)
    file_helper.save_to_file("raviv",items.__str__())
    dupitems = file_helper.load_from_file("raviv")
    item3=cargo_item.CargoItem(40,"lilili",50,"Earth")
    item4=cargo_item.CargoItem(70,"lolololo",50,"Earth")
    dupitems.add_item(item3)
    items.add_item(item4)
    dupitems.remove_item(1)
    dupitems.remove_item(2432425)
    items.remove_item(2)
    dupitems.items[1].weight = 777777777
    file_helper.save_to_file("dupraviv",dupitems.__str__())
    # items.find_item(8)
    # items.remove_item(item)
    # items.get_total_weight()
    # items.find_item(8)
    # print(items.__str__())
    # print(items.find_item(1).__str__())

if __name__ == '__main__':
    main()