## python django 链接mysql
### sql 语句
来源 当前目录下mysql.sql



### 报错
MysQL一个错误提示： #1264 - Out of range value adjusted for column 'mobile_phone' at row 1

insert into user_info (`name`, `mobile_phone`, `gender`, `email`) 
               VALUES ("孙悟天","12323232133", '男',"tiantain@163.com");
时出现错误: 
#1264 - Out of range value adjusted for column 'ID' at row 1 

原因： 
新版本的MySQL对字段的严格检查。 

解决方法（选择第三种即可）： 
1. （不推荐）修改my.ini,将sql-mode="STRICT_TRANS_TABLES,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION" 
改为sql-mode="NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"。
也就是去掉STRICT_TRANS_TABLES 这个东东就好了，然后重新启动MySQL。
推荐这个方法。下面个方法比较麻烦，会给以后的编程带来麻烦。。。》》》不推荐，但是还是在这里说一下。 
2. 在执行sql语句前，先执行以下语句： 
mysql_query("set sql_mode=''");

3. 最佳解决方案 
`desc user_info`  可以查看到type 规则 这边我设的int 类型  | `mobile_phone  | int(10) unsigned   `
刚给的值超过最大数量 报错可以理解 但手机号码正常都11 位 所以是自己建表设计有问题

