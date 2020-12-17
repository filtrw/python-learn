"""
Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов,
на которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов,
которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть,
за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
stepic
stepic.org
neerc.ifmo.ru
jj.ne-erc.if_mo.ru


Пример HTML файла:
<a href="http://stepic.org/courses">
<a href='https://stepic.org'>
<a href='http://neerc.ifmo.ru:1345'>
<a href="ftp://mail.ru/distib" >
<a href="ya.ru">
<a href="www.ya.ru">
<a href="../skip_relative_links">

Пример ответа:
mail.ru
neerc.ifmo.ru
stepic.org
www.ya.ru
ya.ru
"""

import requests
import re


def get_all_href_in_response(response_content):
    href_pattern = r"(<a.+href=\")(.*)(\")"
    all_href = re.findall(href_pattern, response_content)
    clean_hrefs = []
    for href in all_href:
        clean_hrefs.append(href[1])
    return clean_hrefs


resource_link = input()
pattern_protocol = r"^(\w+://)?(\w[\w\-_.]*\.\w+)"

link_response = requests.get(resource_link)
all_hrefs = get_all_href_in_response(link_response.text)
sites = []

for href in all_hrefs:
    http_link = re.findall(pattern_protocol, href)
    if (len(http_link) != 0 and http_link[0][1] not in sites):
        sites.append(http_link[0][1])

sites.sort()
print("\n".join(sites))
