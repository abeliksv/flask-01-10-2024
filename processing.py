def process(total_area, floor, min_to_metro, construction_year, number_of_rooms):
    price = min_to_metro * floor * total_area * construction_year * number_of_rooms
    # TODO: Интегрировать модель машинного обучения
    return price
