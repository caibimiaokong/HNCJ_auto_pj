# 使用方法
- 复制代码到本地
- 在pycharm中下载DrissionPage库
- 根据控制台中的提示输入账号和密码
- 输入完成后，会自动打开浏览器自动评教
# 注意事项
- 请确保你的电脑已经安装了chrome内核的浏览器
- 如果找不到浏览器,在当前项目下新建一个临时文件,输入下面的内容
  ```python
   from DrissionPage.easy_set import set_paths
    set_paths(browser_path=r'这里修改为您的浏览器可执行文件路径')
```
