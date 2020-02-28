#2019.2.27
#导入模块
from selenium import webdriver
#启动浏览器驱动及浏览器
driver = webdriver.Chrome()
#打开网页
driver.get('https://www.51job.com/')
#按元素查找文本输入框
ele = driver.find_element_by_id('kwdselectid')
#输入内容
ele.send_keys('python')
#打开地区选择页面
ele = driver.find_element_by_id()
#点击
ele.click()
#清除已选中选项
  #ele = driver.find_element_by_id('work_position_click_ip_location_000000_120500')
  #ele.click()
#查找并点选上海
ele = driver.find_element_by_id('work_position_click_center_right_list_category_000000_020000')
ele.click()

pass
