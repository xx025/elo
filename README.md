#  竞技排名算法ELO实现和可视化

# ELO算法以及可视化实现


1. 如何计算等级分？
    ```
    ELO算法
    ```
2. 如何保证每人参赛次数尽量相等？
    ```
    1. 设置一个标志，记录参赛次数，每次取最小的参赛次数记录L
    ```
3. 
如何匹配对手？
    ```
    根据第二条原则产生一个随机数i
    1. i>0.5
        选择第一个大于等于L等级分的记录
    2. i<0.5
        选择第一个小于等于L等级分的记录
    ```
4. 如何进行展示？
    ```
    在窗口中进行匹配参比
    每一轮重新两位选手的等级分并存进数据库
    触动查看排行生成当前排行版
    ```
  
 5. 其他
    1. 数据库连接以及文件夹路径在src\setting.json设置
    2. 运行rebuild_db.py可对数据库存储的数据进行重建
    
 
 
```sql
-- --------------------------------------------------------
-- 主机:                           127.0.0.1
-- 服务器版本:                        5.5.27 - MySQL Community Server (GPL)
-- 服务器操作系统:                      Win64
-- HeidiSQL 版本:                  11.0.0.5919
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- 导出 beautgirl0x3 的数据库结构
CREATE DATABASE IF NOT EXISTS `beautgirl0x3` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `beautgirl0x3`;

-- 导出  表 beautgirl0x3.girls 结构
CREATE TABLE IF NOT EXISTS `girls` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `pothopath` varchar(77) DEFAULT NULL,
  `score` double DEFAULT '1400',
  `comNum` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- 数据导出被取消选择。

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;

```



参考资料：
1. 豆瓣电影：[《社交网络》](https://movie.douban.com/subject/3205624/)
2. 知乎专栏：[ELO算法的原理及应用](https://zhuanlan.zhihu.com/p/57480433)
2. 知乎专栏：[通俗讲义—游戏数值知识大全](https://zhuanlan.zhihu.com/p/28190267)
3. 百度百科：[等级分](https://baike.baidu.com/item/%E7%AD%89%E7%BA%A7%E5%88%86/8609967?fr=aladdin)
4. 百度百科：[Logistic分布](https://baike.baidu.com/item/Logistic%E5%88%86%E5%B8%83/22670718?fr=aladdin)

---

2020年11月1日：看了一下社交网络这个电影，综合上面的一些讲解资料ELO算法并不复杂

![??](20201101_090830.733.jpg)

我觉着应该把重点放在可视化上，参考电影中的做成了一个类似于投票网站，参赛选手是数据库中的女孩们，评分者是任何一个人

---

2020年11月10日：
1. 最近没什么进展，但我知道了一个工具`django`
2. 还知道一本书：《django入门与实践》
3. 当然，前些日子认为的重点并不正确，重点应该是组织这一个框架，前端的交互和后端的数据处理，以及这之间的相互关系

---

---

2020-12-12 23:32:05
用本地窗体完成了

---

**其他题目**：

1.创客服务平台  
2.基于视觉的植物生长尺寸测量  
3.大文件同步服务器  
4.规则引擎可视化管理器  
5.数据可视化编辑器  
6.课堂互动管理平台  
7.日志分析器：大文件读取，分割，高频词统计  
8.校园即时消息通信平台  
9.元数据服务器（类似ZooKeeper）  
10.高并发下载服务器  
11.基于redis的pub/sub系统  
12.代码规范检查器  
13.基于视觉的试卷内容提取  
14.宿舍自动查寝系统  
15.netflix推荐引擎  
16.竞技排名算法ELO实现和可视化（参考电影《社交网络》） 
17.物联数据采集平台  
18.名片分享app  
19.redis性能监控平台  
20.Tcp压力测试客户端  
21.机器学习算法管理平台 weka  
22.新闻聚合app  
23.跳一跳游戏开发  
24.汽车标识与车型识别器  
