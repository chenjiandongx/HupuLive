# 虎扑篮球直播命令行版  

作为一个加入虎扑快 700 天的 JRs，一直都是虎扑的铁粉。喜欢逛绿化街，喔不对，是步行街；喜欢看评论，搬好小板凳，欣赏段子手们的表演，前排偶尔还有出售瓜子和爆米花；喜欢虎扑的直播风格，幽默有趣，还能时不时蹦出金句，比如詹姆斯一个后撤步，后撤距离达到一个郭敬明。主播们都是被虎扑耽误了的作家，且节间中场还经常有福利图，需要定时补营养。毕竟随着身体一阵抽搐，整个帖子也就变得索然无味了。

**所以，我有了一个大胆的想法**  

平时也喜欢在命令行下折腾东西，虽然没钱用 Mac 不过 Windows/Linux 下的也不错阿。所以就想来个虎扑文字直播命令行版的，不过没有找到手机直播的数据，就只能将就找网页版的文字直播。有点可惜，因为发现网页版的直播语言太正式了，一点都不像我认识的虎扑，说好的我的三分剑，是地狱的火焰呢。 

时不我待，来一个网易云的电音歌单配上一杯速溶咖啡  
时间悄悄地在流逝，然后项目就写好了  

### 如何安装
1. ``` git clone https://github.com/chenjiandongx/HupuLive.git ```
2. ``` cd HupuLive ```  
3. ``` python setup.py install ```  

### 使用指南  
```hupu -h``` 能够查看如何使用，明细各项参数功能  

![使用指南](https://github.com/chenjiandongx/HupuLive/blob/master/images/hupu-1.gif)  

### 获取比赛直播场次  
```hupu -l``` 查询当天比赛的直播的场次，结果返回比赛场次，包括对阵双方以及场次的序号  

![获取比赛直播场次](https://github.com/chenjiandongx/HupuLive/blob/master/images/hupu-2.gif)  

### 选取比赛开始直播  
```hupu -w``` 根据获得的场次序号来选择具体的比赛，比如这里的 0  

![选取比赛开始直播](https://github.com/chenjiandongx/HupuLive/blob/master/images/hupu-3.gif)  

对齐看起来很舒服有没有，强迫症的福音有没有！！！

### 获取比赛统计数据  
```hupu -d``` 根据获取的场次序号来选择具体比赛的统计数据  

![获取比赛统计数据](https://github.com/chenjiandongx/HupuLive/blob/master/images/hupu-4.gif)  
数据也是对齐的看起来也是很爽的有没有！！！  

### 获取比赛赛后新闻
```hupu -n``` 同样根据获取的场次序号来选择具体比赛的赛后新闻  

![获取比赛赛后新闻](https://github.com/chenjiandongx/HupuLive/blob/master/images/hupu-5.gif)

如果不想看了可以按 Ctrl-C 来中断直播，或者直接关闭终端就行了
