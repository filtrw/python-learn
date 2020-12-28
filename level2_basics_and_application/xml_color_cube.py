"""
Task-3.6.1
Вам дано описание пирамиды из кубиков в формате XML.
Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.

Пример:

<cube color="blue">
  <cube color="red">
    <cube color="green">
    </cube>
  </cube>
  <cube color="red">
  </cube>
</cube>

Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками,
имеют ценность 3. И т. д.

Ценность цвета равна сумме ценностей всех кубиков этого цвета.

Выведите через пробел три числа: ценности красного, зеленого и синего цветов.
Sample Input:
<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>

Sample Output:
4 3 1
"""
from xml.etree import ElementTree

pyramid = input()
pyramid_tree = ElementTree.fromstring(pyramid)
value = 0
color_value = {"red": 0, "green": 0, "blue": 0}
pyramid_level = [pyramid_tree]
while len(pyramid_level) > 0:
    set_next_level = []
    value += 1
    for element in pyramid_level:
        color = element.attrib["color"]
        color_value[color] += value
        set_next_level += element.findall(path="cube")
    pyramid_level = set_next_level

print(color_value["red"], color_value["green"], color_value["blue"])
