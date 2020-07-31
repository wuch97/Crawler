
answer_template="https://www.zhihu.com/api/v4/questions/%s/answers?include=data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_
comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp;data[*].mark_infos[*].url;dat
a[*].author.follower_count,badge[?(type=best_answerer)].topics&limit=5&offset=%s&sort_by=default"
    def check_login(self, response):
         #从mysql中读取question的信息,来进行爬取
         db = MySQLdb.connect("localhost", "root", "", "crawl", charset='utf8' )
         cursor = db.cursor()
         selectsql="select questionid,answer_num from  zhihu_question where id in ( 251,138,93,233,96,293,47,24,288,151,120,311,214,33) ;"
         try:
             cursor.execute(selectsql)    
             results = cursor.fetchall()
             for row in results:
                 questionid = row[0]
                 answer_num = row[1]
                 fornum = answer_num/5 #计算需要访问答案接口的次数
                 print("questionid : "+ str(questionid)+"   answer_Num: "+str(answer_num))
                 for i in range(fornum+1):
                     answer_url = self.answer_template % (str(questionid), str(i*5))
                     yield scrapy.Request(answer_url,callback=self.parse_answer, headers=self.headers) 
         except Exception as e:
             print(e)
         db.close()
