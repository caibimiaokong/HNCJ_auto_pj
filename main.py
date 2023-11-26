from DrissionPage import ChromiumPage

#存储所有的评教按钮
a = []

account = input('请输入学号：')
password = input('请输入密码：')
#定义评教函数
def pingjiao(link):
    link.click()
    for inputField in page.eles('xpath://input[@name="sz"]'):
        inputField.input(20)
    page.ele('@value=提交').click()
    page.ele('text=确认').click()
    page.ele('text=确定').click()
    page.ele('text=关闭').click()
    findlink(page)

#获取链接
def findlink(page):
    for link in page.eles('@class=btn btn-xs btn-success'):
        if link.attr('onclick').__contains__('评价'):
            pingjiao(link)
        else:
            print('已评教')
            continue




# 创建页面对象，并启动或接管浏览器
page = ChromiumPage()
# 跳转到登录页面
page.get('http://jwglxt.huuc.edu.cn:8061/admin/caslogin')


if (
    page.url == 'https://icas.huuc.edu.cn/cas/login?service=http%3A%2F%2Fjwglxt.huuc.edu.cn%3A8061%2Fadmin%2Fcaslogin'):
    # 填写用户名和密码   http://jwglxt.huuc.edu.cn:8061/admin/?loginImage1=&loginImage2=&loginImage4=52a06e87b3424ebc80782dbe16a56615&sfkqcas=1
    page.ele('@placeholder=请输入学工号-账号/安全手机').input(account)
    page.ele('@placeholder=请输入登录密码').input(password)
    page.ele(
        '@class=el-button login-btn el-button--primary el-button--default is-round').click()
    page.ele('text=去评教').click()
    findlink(page)
elif (page.url.__contains__('http://jwglxt.huuc.edu.cn:8061/admin')):
    page.ele('text=去评教').click()
    findlink(page)





