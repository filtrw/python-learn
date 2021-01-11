"""
Task-4.1.2
Первая строка содержит количество предметов 1≤n≤10^3 и вместимость рюкзака 0≤W≤2⋅10^6. Каждая из следующих n строк
задаёт стоимость 0≤c_i≤2⋅10^6 и объём 0<w_i≤2⋅10^6 предмета (n, W, c_i, w_i— целые числа). Выведите максимальную
стоимость частей предметов (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально
уменьшатся), помещающихся в данный рюкзак, с точностью не менее трёх знаков после запятой.

Sample Input:
3 50
60 20
100 50
120 30

Sample Output:
180.000

3 50
60 10
100 5
120 30
"""

thing_count, backpack_capacity = map(int, input().split())
thing_list = []

for thing in range(thing_count):
    thing_cost, thing_weight = map(int, input().split())
    thing_list.append({'thing_cost': thing_cost, 'thing_weight': thing_weight, 'unit_cost': thing_cost / thing_weight})

thing_list.sort(key=lambda element: element['unit_cost'], reverse=True)

backpack_cost = 0.0
backpack_weight = 0.0
thing_index = 0
while backpack_weight != backpack_capacity and thing_index < len(thing_list):
    proportion = (backpack_capacity - backpack_weight) / thing_list[thing_index]["thing_weight"]
    proportion = min(1, proportion)
    backpack_weight += proportion * thing_list[thing_index]["thing_weight"]
    backpack_cost += proportion * thing_list[thing_index]["thing_cost"]
    thing_index += 1

print(format(backpack_cost, '.3f'))
