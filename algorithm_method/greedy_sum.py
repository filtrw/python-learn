"""
Task-4.1.3
По данному числу n 1≤n≤10^9 найдите максимальное число k, для которого n можно представить как
сумму k различных натуральных слагаемых. Выведите в первой строке число k, во второй — k слагаемых.

Sample Input 1:
4

Sample Output 1:
2
1 3

Sample Input 2:
6

Sample Output 2:
3
1 2 3
"""

input_number = int(input())
sum_element = 0
summary = 0

while summary <= input_number:
    sum_element += 1
    summary += sum_element

diff = summary - input_number

print(sum_element - min(1, diff))
for i in range(1, sum_element + 1):
    if i != diff:
        print(i, end=' ')
