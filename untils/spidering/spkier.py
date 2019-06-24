import pymysql  
db = pymysql.connect(host = 'localhost',port = 3306 ,user = 'root',password = 'root',db = 'meizi_db')##数据库的链接  
cur=db.cursor()#获取一个游标    

cur.execute("DROP TABLE IF EXISTS meizis")  ## 如果表存在则删除
    ## 创建表 sql语句
    createTab = """create table meizis(
      id int primary key auto_increment,
      mid varchar(10) not null,
      title varchar(50),
      picname varchar(10),
      page_url varchar(50),
      img_url varchar(50)
    );"""
  cur.execute(createTab)   ## 执行数据表操作

？
  html = self.request(url)
  all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='all').find_all('a')
  for index, a in enumerate(all_a):
    title = a.get_text()
    href = a['href']
    lists = self.html(href, title)
    for i in lists:
      print(i['meiziid'], i['title'], i['picname'], i['page_url'], i['img_url'])
      ## 插入数据到数据库sql语句， %s用作字符串占位
      sql = "INSERT INTO `meizi_db`(`mid`, `title`, `picname`, `page_url`, `img_url`) VALUES(%s,%s,%s,%s,%s)"
      try: 
        cur.execute(sql, (i['meiziid'], i['title'], i['picname'], i['page_url'], i['img_url']))
        db.commit()
        print(i[0] + " is success")
      except:
        db.rollback()

cur.close()#关闭游标    
db.close()#释放数据库资源    
except  Exception :print("发生异常") 