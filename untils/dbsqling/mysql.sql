CREATE TABLE user_info(
  `id` INT UNSIGNED AUTO_INCREMENT NOT NULL COMMENT '自增主键ID',
  `name` VARCHAR(20) NOT NULL COMMENT '用户姓名',
  `mobile_phone` INT UNSIGNED COMMENT '手机号',
  `gender` CHAR(1) COMMENT '性别',
  `email` VARCHAR(50) COMMENT '邮箱',
  `register_time` TIMESTAMP NOT NULL COMMENT '注册时间',
  PRIMARY KEY ( `id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT '用户信息表';

insert into user_info (`name`, `gender`, `email`) 
               VALUES ("孙悟饭", '男',"oahcoay@163.com");
insert into user_info (`name`, `mobile_phone`, `gender`, `email`) 
               VALUES ("孙悟天","119120", '男',"tiantain@163.com");