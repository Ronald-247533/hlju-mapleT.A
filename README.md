# __hlju-maple T.A.__

  python中有selenium这样一个库
  而hlju-maple T.A.是基于 python+selenium 自动化库写的自动刷上机高数题脚本
  如果觉得好用可以star一下~也可以分享给同学！

## __原理__

高数上机有一个生成 __答案__ 的接口：

<http://125.223.1.242:80/mapleta/modules/gradeProctoredTest.Login?currPage=1&"+testId+"&actionID=viewdetails>

当我们每切换一道题，答案接口会依次根据当前题目生成最新答案。所以关键地方就是要先提交到最后再返回第一题来确保答案最新。链接中的__testId__就是测试的章节id

## __Log__

* 写在最前面
  
  因为我只有本专业的高数上机练习题作为测试样例，无法保证所有题型都涵盖，如果出现答题错误/失败现象，欢迎大家继续issue来一起完善这个脚本

* ***2020.10.21***  
  
  目前是敏捷开发，前两天抽了两个小时左右写了demo出来，没有太多功能，过阵子有空会持续优化和支持多用户同时刷课

* ***2020.12.09***
  
  增加了控制超时等待时间选项，修改了填空题有多个空无法作答的bug
  增加了刷取指定章节的功能

* ***2021.04.03***

  增强稳定性，修改读取班级时webdriverWait的until条件
  增加选择指定班级的功能  

## __食用方法__

  如果您已配置好python+selenium，那么可以直接clone到本地使用
  如果没有，那就可以经过一些简单操作就可以来使用这个脚本！

  * 1.官网下载安装与电脑相对应的python 我用的是3.7.7版本，其他版本应该没有太大影响
    <https://www.python.org/downloads/>

  * 2.安装selenium库
  
        pip install selenium

    如果速度过慢建议使用阿里的中央库<http://mirrors.aliyun.com/pypi/simple/> 即

        pip install selenium -i http://mirrors.aliyun.com/pypi/simple/
      
  * 3.下载chrome/火狐浏览器和对应的浏览器driver
    具体内容可以百度，很多方法和资源。需要注意的是,一定要使驱动和浏览器版本相对应好,不然会出现预期外的错误！

  * 3.5.如果找不到第三步的下载地址，可以查看这篇大佬写的，很详细<https://www.jianshu.com/p/1531e12f8852>
    也包括了selenium介绍和基本用法

  * 4.git clone <https://github.com/zsmlqlj/hlju-mapleT.A.git>即可运行使用
    如果没安装git，可以下载zip的形式

    如果zip下载过慢，建议使用国内的码云<https://gitee.com/>

    注册登录后，点击左下角创建仓库，拉到页面最下方，有一个导入已有仓库

    输入<https://github.com/zsmlqlj/hlju-mapleT.A.git>创建后再用码云的下载即可

  * 5.运行程序,视角请切换回你的编译器而不是浏览器,根据提示操作

  * 6.享受一键满分高数

## __注意__

  本脚本只作为学习交流技术使用，不可商用

  不可用此方法的手操版进行 __考试作弊__！经测试，考试是无法获取到答案页面的，请好好复习，珍惜大学时光


