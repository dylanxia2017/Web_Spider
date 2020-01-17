import requests
from bs4 import BeautifulSoup
from lxml import html
import warnings
from time import sleep
import numpy as np
from scrapy import Selector
import pandas as pd
from datetime import datetime
import multiprocessing
import re
import json




headers = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
    'cookie':'_zap=1e6b2e76-6ab5-4ab2-b9d8-e3a6ad98cfc2; d_c0="AKDsnlj6QRCPTiFQJo66i-9gBoIH2lBKKAA=|1572085609"; _xsrf=a77b7f8a-5a83-4f58-91f5-fdf64f8d6435; q_c1=5a7f46732fd84eafbca34046acb715a5|1575900879000|1575900879000; capsion_ticket="2|1:0|10:1576404971|14:capsion_ticket|44:ZDhhMGUzN2U4ZmI1NDZlNmJlM2E0NTJlYjMwMzllZjk=|87411964e591977699938e5d4d5d130aaa6d4b58af761eb41038f4e2753a0708"; z_c0="2|1:0|10:1576405019|4:z_c0|92:Mi4xN24wMUNRQUFBQUFBb095ZVdQcEJFQ2NBQUFDRUFsVk5HNVVkWGdBNDZ4RTNZV0RPQ0pic0F6TTJGUGpjblBkTnV3|0bcfe437856978cb69dce5411169b232efdb83aac48b6d23912c2023a58b0cb9"; tshl=; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1577608790,1577725306,1577868950,1577869385; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1577869697; KLBRSID=81978cf28cf03c58e07f705c156aa833|1577870009|1577867491'
}
answers = []
links = []

def zhihu_spider():
    with open("知乎链接.txt","r") as filehandler:
        for url_space in filehandler:
            url = url_space[:-1]
            # print("现在正在爬取链接：{}".format(url))
            try:
                res = requests.get(url, headers = headers)
                res_json = json.loads(res.text)

                for data in res_json["data"]:
                    clean_text = BeautifulSoup(data["content"],"lxml").text
                    print(clean_text)
                    answers.append(clean_text)

                sleep(np.random.randint(1, 5))
            except:
                print("网页无法获取")

        with open("知乎回答.txt","a") as f:
            for ans in answers:
                f.writelines("%s\n" % ans)


def get_nextpage_link(url):
    res = requests.get(url, headers=headers)
    res_json = json.loads(res.text)
    return res_json["paging"]["next"]


if __name__ == "__main__":
    # url = "https://www.zhihu.com/api/v4/questions/313564280/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&platform=desktop&sort_by=default"
    # for i in range(800):
    #     print("正在爬取第{}页的数据".format(i))
    #     url = get_nextpage_link(url)
    #     links.append(url)
    #     sleep(np.random.randint(1, 5))
    #
    # with open("知乎链接.txt","w") as f1:
    #     for link in links:
    #         f1.writelines("%s\n" % link)

    zhihu_spider()
    print("结束")
