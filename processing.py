def process(total_area, floor, min_to_metro, construction_year, number_of_rooms,ceiling_height):
    price = min_to_metro * floor * total_area * construction_year * number_of_rooms * ceiling_height
    # TODO: Интегрировать модель машинного обучения
    return price
