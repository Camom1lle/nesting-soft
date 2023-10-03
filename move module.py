import ezdxf

filename="shifted_file.dxf"

def move_rectangles_to_origin(filename):
    dwg = ezdxf.readfile(filename)
    modelspace = dwg.modelspace()

    # Находим минимальные и максимальные координаты по осям X и Y
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
    for entity in modelspace:
        if entity.dxftype() == 'POLYLINE':
            for vertex in entity.vertices():
                min_x = min(min_x, vertex[0])
                min_y = min(min_y, vertex[1])
                max_x = max(max_x, vertex[0])
                max_y = max(max_y, vertex[1])

    # Вычисляем сдвиг для перемещения к нулевым координатам
    shift_x = (max_x - min_x) / 2
    shift_y = (max_y - min_y) / 2

    # Перемещаем все прямоугольники к нулевым координатам
    for entity in modelspace:
        if entity.dxftype() == 'POLYLINE':
            for vertex in entity.vertices():
                vertex[0] -= shift_x
                vertex[1] -= shift_y

    # Сохраняем изменения в новом файле
    output_filename = "moved.dxf"
    dwg.saveas(output_filename)
    print(f"Файл сохранен как {output_filename}")

# Замените "input.dxf" на путь к вашему исходному файлу DXF
move_rectangles_to_origin("shifted_file.dxf")