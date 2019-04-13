# robotframework 框架   https://robotframework.org/#introduction 文档地址

***Settings***
Library     Selenium2Library

***Test Cases***
百度搜索
    [Setup]
        打开百度
    输入关键字
    [Teardown]
        Close Browser

***Keywords***
打开百度
    Open Browser    http://www.baidu.com    chrome
    Maximize Browser Window

输入关键字
    Input Text      id:kw   helloworld

    # 截屏
    Capture Page Screenshot     filename=helloworld.png