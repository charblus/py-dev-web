### spider001
+ 取豆瓣评价 编码unicode 需要转码   
+ 在爬虫过程中，使用的是lxml的xpath查找对应的字段。xpath('node()')匹配文本为lxml.etree.ElementUnicodeResult对象，节点为lxml.etree.Element对象。
+ `address=each.xpath('.//address/text()')[0].strip()`
+ 主要因为python2的蛋疼的编码原因,
+  lxml.etree._ElementUnicodeResult , _ElementUnicodeResult 是unicode的一个子类。
+ 那么可以直接将它转为unicode  address.encode('utf-8') 就可以了。
+ lxml的官方文档 --- http://lxml.de/api/lxml.etree._ElementUnicodeResult-class.html
+ 站长工具  -- 在线转码 ---  http://tool.chinaz.com/tools/unicode.aspx
