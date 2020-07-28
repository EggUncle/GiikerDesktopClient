# GiikerDesktopClient
详细的分析，晚点儿再发，这里简单说一下使用方法

## 使用方式
替换get_service.py 脚本中这两个字段的为自己的蓝牙魔方即可，我的是i3S，其它的固件不一定是一样的其实。。
```
MODEL_NBR_UUID = '50430B3B-0437-485E-8D91-3862CE188C31'
address = 'db:d4:9e:88:24:c2'
```
修改完之后直接运行get_service.py 就可以了，记得安装蓝牙库bleak

## 运行效果
之前录的视频转的gif，控制台输出的颜色有限，不是和魔方颜色完全对应的，看看效果就好。

![](https://github.com/EggUncle/Demo/blob/master/markdownimg/IMG_2508.GIF?raw=true)
