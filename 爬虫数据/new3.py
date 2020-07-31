import requests
import time
import datetime
import os
import json
import uuid
from pyquery import PyQuery as pq

# 地址 https://www.zhihu.com/question/34243513
def start(offset, sort):
    url = 'https://www.zhihu.com/api/v4/questions/286837417/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=5&platform=desktop&sort_by=default' + str(
        offset) + '&platform=desktop&sort_by=' + sort
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
        'cookie': '_zap=2cbb824f-cc61-4253-a152-052e73594d6a; d_c0="AOAuC9kmtA-PTkLqug-HDNyw47M-N6CV9Lk=|1562567817"; _xsrf=urr5zL6UDhHj0O1gkNXdt8GfI6PZovJx; tst=r; capsion_ticket="2|1:0|10:1563270043|14:capsion_ticket|44:YTNhYWYzMjg5OGQ0NGE1ZWJhMzg0ZTgxZTRiMGViODE=|f8d3a966592fb47423a7e81343b85e55865c8143ffb6c27b5d699c49b00f0e14"; z_c0="2|1:0|10:1563270048|4:z_c0|92:Mi4xM2wwekFBQUFBQUFBNEM0TDJTYTBEeVlBQUFCZ0FsVk5vT2thWGdEWnoyLUpWU1ZlRk54U3lHanRlSWEyeFdWNk9R|9c85dcf1f88f8de185e08287d189edaf7fae58c4fa670b192011ff1bc0c83d44"; q_c1=da1ebc6555ba4499b4ddacb36206a06b|1563276805000|1563276805000; __utma=51854390.2002523387.1563276808.1563276808.1563276808.1; __utmc=51854390; __utmz=51854390.1563276808.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100-1|2=registration_date=20140202=1^3=entry_date=20140202=1; tgw_l7_route=73af20938a97f63d9b695ad561c4c10c'
    }
    res = requests.get(url, headers=headers).text
    data = json.loads(res)
    picRepo = 'picRepo'
    if not os.path.exists(picRepo):
        os.makedirs(picRepo)
    if data.get("data"):
        for i, item in enumerate(data['data']):
            content = pq(item['content'])
            imgUrls = content.find('noscript img').items()
            for imgTag in imgUrls:
                src = imgTag.attr("src")
                strIndex = src.rfind('.')
                suffix = src[strIndex:]
                with open(f"{picRepo}/{uuid.uuid4()}{suffix}", 'wb') as f:
                    f.write(requests.get(src).content)


if __name__ == '__main__':
    starttime = datetime.datetime.now()
    strTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    stime = print(f'开始抓取,当前时间: {strTime}')
    for i in range(6):  # 偏移量单位是5，循环3次
        start(offset=((i * 6) if i != 0 else 0), sort='updated')  # updated:按时间降序，default：默认排序
        # 这里先睡一会，如果太快可能有些图片下载后会查看不了，
        # 越慢，下载的图片可以查看的越多。原因大概是知乎的反爬虫机制，
        # 看不了的图片其实返回的是一个400的badRequest的状态码
        time.sleep(6)
    endtime = datetime.datetime.now()
    print(f'抓取完毕,用时 {((endtime - starttime).seconds)} 秒:')