## 2020.2.27

### 查找页面元素：

* xx.find_element_by_id('')
* xx.find_element_by_cssselector ('')

### 其他

* xx..implicitly_wait()——隐式等待
* xx.click

### 遗留问题

* cssselector的使用


## 2020.2.28

### 问题及解决

* 自动测试时，切换页面后无法点选，报错“no such element: Unable to locate element”；单步执行时无此问题。使用隐式等待后问题解决。