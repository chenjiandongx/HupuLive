# 虎扑篮球直播终端版  

作为一个加入虎扑快 700 天的 JRs，一直都是虎扑的铁粉。喜欢逛绿化街，喔不对，是步行街；喜欢看评论，搬好小板凳，欣赏段子手们的表演，前排偶尔还有出售瓜子和爆米花；喜欢虎扑的直播风格，幽默有趣，还能时不时蹦出金句，如上次的詹姆斯一个后撤步，后撤距离达到一个郭敬明。主播们都是被虎扑耽误了的作家，且节间中场还经常有福利图，需要定时补营养。毕竟随着身体一阵抽搐，整个帖子也就变得索然无味了。

**所以，我有了一个大胆的想法**  

平时也喜欢在终端下折腾东西，虽然没钱用 Mac 不过 Windows/Linux 下的也不错阿。所以就想来个虎扑文字直播终端版的，不过没有找到手机直播的数据，就只能将就找网页版的文字直播。有点可惜，因为发现网页版的直播语言太正式了，一点都不像我认识的虎扑，说好的我的三分剑，是地狱的火焰呢。 

时不我待，撸起袖子加油干  
在 debug 了又 debug 后，终于可以用来看直播了  

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
如果不想看了可以按 Ctrl-C 来中断直播，或者直接关闭终端就行了
