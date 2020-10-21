# __hlju-maple T.A.__
hlju-maple T.A.是基于 python+selenium 自动化库写的自动刷上机高数题脚本

## __原理__

高数上机有一个生成 __答案__ 的接口：

<http://125.223.1.242:80/mapleta/modules/gradeProctoredTest.Login?currPage=1&"+testId+"&actionID=viewdetails>

当我们每切换一道题，答案接口会依次根据当前题目生成最新答案。所以关键地方就是要先提交到最后再返回第一题来确保答案最新。链接中的__testId__就是测试的章节id

## __Log__

* ***2020.10.21***  
  
  目前是敏捷开发，前两天抽了两个小时左右写了demo出来，没有太多功能，过阵子有空会持续优化和支持多用户同时刷课

## __用法__
安装python 我用的是3.7.7版本

        安装selenium
        pip install selenium
如果速度过慢建议使用阿里的中央库  <http://mirrors.aliyun.com/pypi/simple/>
        
        pip install selenium -i http://mirrors.aliyun.com/pypi/simple/

