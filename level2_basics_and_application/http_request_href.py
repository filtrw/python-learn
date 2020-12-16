"""
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с
дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и
из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 1:
Yes

Sample Input 2:
https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html

Sample Output 2:
No

Sample Input 3:
https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html

Sample Output 3:
Yes
"""

import requests
import re


def get_all_href_in_response(response_content):
    href_pattern = r"(<a.*href=\")(.*)(\")"
    all_href = re.findall(href_pattern, response_content)
    clean_hrefs = []
    for href in all_href:
        clean_hrefs.append(href[1])
    return clean_hrefs


first_resource = input()
second_resource = input()

first_response = requests.get(first_resource)
first_resource_href = get_all_href_in_response(first_response.text)
have_second_resource = False

for href in first_resource_href:
    second_response = requests.get(href)
    second_response_href = get_all_href_in_response(second_response.text)
    if second_resource in second_response_href:
        have_second_resource = True
        print("Yes")
        break

if not (have_second_resource):
    print("No")
