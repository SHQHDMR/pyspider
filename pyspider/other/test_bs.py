import bs4
import json
import pyspider.settings
import pyspider.other.html_src

response = pyspider.other.html_src.response_page

bs_soup = bs4.BeautifulSoup(response, features="lxml")
div_c = bs_soup.find('a', class_='n')['href']

print(div_c)

# for div_obj in div_c:
#     print(div_obj)


# print(div_obj.a.string)
# print(div_obj.find('div', class_='c-abstract').string)
# print(div_obj.find('div', class_='c-tool')['data-tools'])
