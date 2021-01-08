"""
По данным n отрезкам необходимо найти множество точек минимального размера, для которого каждый из отрезков
содержит хотя бы одну из точек.
В первой строке дано число 1≤n≤100 отрезков. Каждая из последующих n строк содержит по два числа  0≤l≤r≤10^9,
задающих начало и конец отрезка. Выведите оптимальное число m точек и сами m точек. Если таких множеств точек
несколько, выведите любое из них.

Sample Input 1:
3
1 3
2 5
3 6

Sample Output 1:
1
3

Sample Input 2:
4
4 7
1 3
2 5
5 6

Sample Output 2:
2
3 6
"""
segment_count = int(input())
segment_list = []

for segment in range(segment_count):
    left, right = (int(i) for i in input().split())
    segment_list.append({'segment': segment, 'left': left, 'right': right})

segment_list.sort(key=lambda element: element['right'])

m_points = []

while len(segment_list) != 0:
    m_point_value = segment_list[0]['right']
    m_points.append(m_point_value)
    segment_list = list(filter(lambda element: element['left'] > m_point_value, segment_list))

print(len(m_points))
print(" ".join(map(str, m_points)))
