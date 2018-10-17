import bs4
import json

response = """<div class="result c-container " id="3" srcid="1599" tpl="se_com_default"  data-click="{'rsv_bdr':'0' }"  ><h3 class="t"><a data-click="{'F':'778317EA','F1':'9D73F1E4','F2':'4CA6DD6B','F3':'54E5343F','T':'1539689471','y':'E65FEF7B'}" href = "http://www.baidu.com/link?url=bifmJxE0wOrt1hEQcNKzSZC-PIYz93vWhT5wv7W_l6vlcPkzuHCImTjnE_CbCVu03DqGskTDfvW1Cd9hp6CT9VugIyMNJLaa04rTP6BHRzC" target="_blank">在<em>linux</em>下安装抓包工具<em>fiddler</em>,图文并茂。 - CSDN博客</a></h3><div class="c-abstract"><span class=" newTimeFactor_before_abs m">2018年6月14日&nbsp;-&nbsp;</span>不多说,直奔主题,因为在<em>linux</em>上安装<em>fiddler</em>需要mono环境,所以先安装mono环境,sudo apt-get install mono-complete安装好环境后,下载<em>fiddler</em>,传送门 ...</div><div class="f13"><a target="_blank" href="http://www.baidu.com/link?url=bifmJxE0wOrt1hEQcNKzSZC-PIYz93vWhT5wv7W_l6vlcPkzuHCImTjnE_CbCVu03DqGskTDfvW1Cd9hp6CT9VugIyMNJLaa04rTP6BHRzC" class="c-showurl" style="text-decoration:none;">https://blog.csdn.net/weixin_4...&nbsp;</a><div class="c-tools" id="tools_4088562849132383107_3" data-tools='{"title":"在linux下安装抓包工具fiddler,图文并茂。 - CSDN博客","url":"http://www.baidu.com/link?url=bifmJxE0wOrt1hEQcNKzSZC-PIYz93vWhT5wv7W_l6vlcPkzuHCImTjnE_CbCVu03DqGskTDfvW1Cd9hp6CT9VugIyMNJLaa04rTP6BHRzC"}'><a class="c-tip-icon"><i class="c-icon c-icon-triangle-down-g"></i></a></div><span class="c-icons-outer"><span class="c-icons-inner"></span></span>&nbsp;-&nbsp;<a data-click="{'rsv_snapshot':'1'}" href="http://cache.baiducontent.com/c?m=9f65cb4a8c8507ed19fa950d100b8738440197634b86914323c3933fcf331d5c0231b8f17c7e0703a7c37e6d0aa94f5ce0ed6532715871e9ccd5de1d9be8c9766e952d367417824417d00dea960673ce74cb0cbff14ea7adf043cdf58e9495&p=90759a46d7c201e60fb1c7710f449f&newp=c962c80685cc43fe01bd9b7d0c1798231610db2151d6d4126b82c825d7331b001c3bbfb423261306d7c27e6106ae495be0f737743d0923a3dda5c91d9fb4c57479d97e&user=baidu&fm=sc&query=fiddler+linux&qid=a20ce7c20006d3cc&p1=3" target="_blank" class="m">百度快照</a></div></div>"""

bs_soup = bs4.BeautifulSoup(response, features="lxml")
div_c = bs_soup.find_all('div', class_='result c-container ')

for div_obj in div_c:
    print(json.loads(div_obj.find('div', class_='c-tools')['data-tools'])['url'])

# print(div_obj.a.string)
# print(div_obj.find('div', class_='c-abstract').string)
# print(div_obj.find('div', class_='c-tool')['data-tools'])
