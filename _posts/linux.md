---
layout:       post
title:        "Linux"
subtitle:     " \"Linux.md note.\""
date:         2023-05-06 17:01:00
author:       "王川"
header-img:   "img/bg-Jordan_Solo.jpg"
catalog:      true
tags:
    - 笔记
---

[TOC]

# jupyter和用户目录 密码

```
1234

drose1111

涛涛用户名密码：
leitao
aXAtKE22

conda env:chuan
http://192.168.2.153:8009/tree/m
```



# meituan jumper

```
pip install  -i http://data-source-newpip.sankuai.com/simple --trusted-host data-source-newpip.sankuai.com

ssh wangchuan16@jumper.sankuai.com
password:Bomi.9

pip conda源
https://km.sankuai.com/page/456000330

# 可用端口号
# https://docs.sankuai.com/mt/data/gpu-docs/master/docker_jupyter/

# mlp pc docker
http://set-zw05-kubernetes-pc302.mt:44406/tree?
http://set-zw05-kubernetes-pc302.mt:44407/

# https://km.sankuai.com/page/139872366
1卡 cuda10.1
40G
ssh hadoop-mtai@10.164.2.27
http://set-zw04-kubernetes-pc995.mt:44392/tree/
http://set-zw04-kubernetes-pc995.mt:44393/
2*16G
ssh hadoop-mtai@10.138.158.41
http://set-zw05-kubernetes-pc391.mt:44388/tree?      （.wangchuan16/）
http://set-zw05-kubernetes-pc391.mt:44406      (users/)

2卡
ssh hadoop-mtai@10.138.205.138
http://set-zw05-kubernetes-pc396.mt:44407/tree
# pip install --trusted-host pip.sankuai.com tensorflow-gpu==2.3.0
2卡
ssh hadoop-mtai@10.138.206.20
http://set-zw05-kubernetes-pc394.mt:44406/tree/

password:mtai123456

临时llm：
http://set-zw04-kubernetes-pc82.mt:44401/tree/llm-fine-tuning/models/public
http://set-zw04-kubernetes-pc82.mt:44400/tree/meituan/large_language_model

llm 2 卡：
http://set-zw04-kubernetes-pc108.mt:44390/tree/meituan
http://set-zw04-kubernetes-pc108.mt:44391/tree/llm-fine-tuning

单独llm1卡：
http://set-zw04-nlu-llm01.mt:44392/tree/meituan


root地址:
/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai/users/.wangchuan16/meituan/

cephfs路径在 /opt/meituan/cephfs/user/hadoop-mtai
dolphinfs路径在 /mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai/users/

cd /home/hadoop-mtai/cephfs/data/wangchuan16
conda activate wc
jupyter notebook
password:11

nohup后台挂起jupyter notebook:
nohup jupyter notebook &

netstat -nltp | grep 8083
1卡地址：(cuda 10.0)
http://set-zw-yarn-training479684.mt:44405/
2卡地址：(cuda 11.0)
http://set-zw-yarn-training468894.mt:44402/tree?
4卡地址：(cuda 10.0)
http://set-zw-yarn-training422854.mt:44404/tree?

kernel记录：
2卡机器：
chuan：复制的yfy的env  py3.6 b4k:0.7.7
wc：		自己新建的env   py3.7 b4k:0.10.6

# spark机器
ssh wangchuan16@jumper.sankuai.com
ssh xr-ai-kg-sparkclient01
sudo -iu sankuai



fuser -v /dev/nvidia*
```



## sftp上传文件到hdfs

```
本地电脑 cd到目标文件所在的目录 然后
sftp wangchuan16@jumper.sankuai.com
sftp> put xxx.txt # 文件
sftp> put -r xxx # 文件夹

然后在hdfs 即spark机器上
sftp wangchuan16@jumper.sankuai.com
sftp> ls
sftp> get xxx.txt  # 文件
sftp> get -r xxx  # 文件夹

```



# meituan 单卡机器ananconda3安装

```
https://km.sankuai.com/page/456000330

安装前需要cd ~ 然后ls -a 删除.condara 和.conda
wget http://data-source-conda.sankuai.com/Anaconda3-2020.02-Linux-x86_64.sh
bash Ananconda3xxx
（注意：安装到地址的时候 安装在/workdir/anaconda3 然后只按一次回车 不然后面就不会自动安装环境变量了 ，后面环境变量出输入 yes 就ok了）
source .bashrc   (很重要)

conda init

step2:conda源和pip源
直接复制我的配置文件到~/.condarc 和~/.pip/pip.conf就ok了

conda create -n chuan python=3.7(tf1 python3.7;tf2 python3.8)


step3:jupyter配置 https://www.jianshu.com/p/444c3ae23035
pip install jupyter
jupyter notebook --generate-config
jupyter notebook password
vim ~/.jupyter/jupyter_notebook_config.py
或者python：
from notebook.auth import passwd
passwd()
Out[2]: 'argon2:$argon2id$v=19$m=10240,t=10,p=8$AdoCOmLKckIbnBbdX8bA1g$SFarsv6v6OaWWqR1v+2P4+87J1W96aODm2NloSHSepQ'

vim ~/.jupyter/jupyter_notebook_config.py
复制我的配置文件的端口就ok了
c.NotebookApp.ip='*'
c.NotebookApp.notebook_dir = '/mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai/users/.wangchuan16'
c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$ry+/GT+Yn/LoOgs0UbMHNQ$xRqwQEstVxRjL6LscLzzcQKsIuyOWIcWtWh9TxcMzfM'
c.NotebookApp.open_browser = False
c.NotebookApp.port =44406 # 目前GPU集群可用端口有{8410-8420, 8080, 44388-44407}

# 不装nb_conda仅用ipykernel在自己的虚拟环境下装自己的kernel
conda activate chuan_tf2
python -m ipykernel install --user --name chuan --display-name chuan
python -m ipykernel install --user --name chuan_tf2 --display-name chuan_tf2

python -m ipykernel install --user --name llm_fine_tune --display-name llm_fine_tune

# 删除kernel
jupyter kernelspec remove XXX


# 装nb_conda
conda activate base
conda install nb_conda
conda activate chuan
conda install nb_conda
conda install ipykernel

# nohup
nohup jupyter notebook &
```



## tensorflow安装

tensorflow1.14

```
conda install tensorflow-gpu==1.14
pip install h5py==2.10 -i http://data-source-newpip.sankuai.com/simple --trusted-host data-source-newpip.sankuai.com

print(tf.test.is_gpu_available())
```

tensorflow2.30

```
pip install tensorflow-gpu==2.3.0
```

tensorflow与cuda、cudnn、python的版本对应

```
https://tensorflow.google.cn/install/source?hl=en#linux
```



## pytorch安装

```
# cuda 10.0 下 不知道为啥可以安装10.2的命令。。。
pip install torch==1.7.1 torchvision==0.8.2 torchaudio==0.7.2
pip install sentence_transformers
```



# meituan Jupiter 端口

```
/home/hadoop-mtai/.jupyter/jupyter_notebook_config.py

文件中修改端口号从8080编程8082才行

端口号8082 
```



# linux非root用户通过top查看pid后找到对应进程的目录以用户

```
# https://www.cnblogs.com/jie-fang/p/7686521.html

top
ps -aux |grep 1303823
或者
(chuan) [hadoop-mtai@zw03-data-hdp-dn-gpu0254 rider_quality_inspection]$ ps -aux |grep -v grep|grep 1303823
hadoop-+ 1303823  0.0 14.5 65791752 12167460 pts/4 Sl+ 16:59  23:18 python text2embedding.py

cd /proc/1303823
ls -ail
```



# meituan nohup的后台进程要kill掉，找不到，多种方法，其中可以用的是监听网络端口

```
ps -aux | grep wc

a:显示所有程序
u:以用户为主的格式来显示
x:显示所有程序，不以终端机来区分

(wc是我的conda虚拟环境，所以这样来找，jupyter、python都试过，但是列出太多了，因为服务器很多人用，找不到我的)
但是可惜也不管用


询问鑫哥以后，找到了：
先打开jupyter的页面，然后找到端口号是8082
# 监听端口号是8082的进程
netstat -nltp | grep 8082

(wc) [hadoop-mtai@zw03-data-hdp-dn-gpu0339 meituan]$ netstat -nltp | grep 8082
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 0.0.0.0:8082            0.0.0.0:*               LISTEN      1857661/python
tcp6       0      0 :::8082                 :::*                    LISTEN      1857661/python

kill -9 xxx

ps -ef | grep xxxx

# 补充 查看GPU, cuda,显卡被哪个进程占用
fuser -v /dev/nvidia*

# 总结
step1:
fuser -v /dev/nvidia*

step2:ssh
cd /proc/pid
lis -ail

step3:
kill -9 pid  # 占着茅坑不拉屎 杀无赦
```



# meituan开发机服务器安装linux命令

```
https://km.sankuai.com/page/456000330

docker-util yum --disablerepo=* --enablerepo=$ENABLED_YUM_REPOS install tmux

channels:
   - http://data-source-conda.sankuai.com/pkgs/main/
   - http://data-source-conda.sankuai.com/pkgs/free/
   - http://data-source-conda.sankuai.com/cloud/pytorch/
   - http://10.26.58.35/pkgs/main/
   - http://10.26.58.35/pkgs/free/
   - http://10.26.58.35/cloud/pytorch/
   - http://data-source-conda.sankuai.com/pkgs/free/
   - http://data-source-conda.sankuai.com/pkgs/main/
   - http://data-source-conda.sankuai.com/cloud/pytorch/       # 添加pytorch channel
show_channel_urls: true
```

channels:
    - http://data-source-conda.sankuai.com/pkgs/main/
    3   - http://data-source-conda.sankuai.com/pkgs/free/
    4   - http://data-source-conda.sankuai.com/cloud/pytorch/
    5   - http://10.26.58.35/pkgs/main/
    6   - http://10.26.58.35/pkgs/free/
    7   - http://10.26.58.35/cloud/pytorch/
    8 show_channel_urls: true



# meituan GIT仓库公钥配置等

```
通过
https://km.sankuai.com/page/353027126
找到自己的 name和email

然后通过
https://km.sankuai.com/page/173710298
进行配置

1、初次使用Git问题
1.1、获得了git的clone地址
例如：http://git.sankuai.com/v1/bj/projects/~xxx/repos/xxxx

1.2、尝试下载git文件
git clone http://git.sankuai.com/v1/bj/projects/~xxx/repos/xxxx

1.3、错误提示
Warning: Permanently added 'git.sankuai.com,xx.xx.xx.xx' (RSA) to the list of known hosts.
git@git.sankuai.com: Permission denied (publickey).
fatal: Could not read from remote repository.
Please make sure you have the correct access rights
and the repository exists.

2、解决方法
2.1、设置用户名和邮箱
git config --global user.name  "username"

git config --global user.email  username@meituan.com

2.2、生成密钥对
1）ssh-keygen -t rsa

2）回车确认

Generating public/private rsa key pair.

Enter file in which to save the key (/root/.ssh/id_rsa): 

Enter passphrase (empty for no passphrase): 

Enter same passphrase again: 

Your identification has been saved in /root/.ssh/id_rsa.

3）提示生成本地秘钥对的工作完成

2.3、添加公钥到git账户
1）查看生成的公钥：cat ~/.ssh/id_rsa.pub

2）登陆git：http://git.sankuai.com/v2/ssh/detail

3）点击“Add Key”

4）复制公钥内容并添加

2.4、验证
1）git clone http://git.sankuai.com/v1/bj/projects/~xxx/repos/xxxx

2）成功下载git文件，验证配置成功
```



# SQL语句积累

## JOIN的方式

```
https://www.cnblogs.com/reaptomorrow-flydream/p/8145610.html

```



## left semi join 和 left join的区别

```
https://www.cnblogs.com/erlou96/p/14321459.html

left_semi:
C = A.join(B, Seq("id"), "left_semi")
A有列 a, b, id
B有列 id, d, e, f
则结果C为，A中所有id为B中的id的行（且不重复，即B中某id有多行,但只筛选一次A中对应的id），列为A的列（没有B的列）

left join，当B中有重读键时，结果可以重复，但都是A表中的内容，然后列包括A与B的列
left semi join不会重复，然后列只包括A的列
```



## select case when end

```
SELECT
start_date,
CASE 
WHEN second_category_name LIKE '%跑腿%' THEN '跑腿'
WHEN second_category_name LIKE '%企客%' THEN '企客'
WHEN bu_name = '骑手服务' AND third_category_name LIKE '%专送%'     THEN '专送外卖'
WHEN bu_name = '骑手服务' AND third_category_name NOT LIKE '%专送%' THEN '众包外卖'
WHEN bu_name = '外卖商服' THEN '外卖商服'
ELSE '其他'
END AS buname,
CASE 
WHEN source IN (1,11,13,-3)   THEN '电话'
WHEN  source in (2,12,-4)      THEN '在线'
WHEN (source = 20 OR (source = 29 AND case_result_desc = '客户直接诉求D')) THEN '自助建单'
ELSE '其他'
END AS source,
case_id,
```



## LIKE：筛选某个字段含有某些字符串

```
%CSO%表示 正则中的*CSO*
WHERE (case_type_desc LIKE '%CSO%' OR case_type_desc LIKE '%cso%')
```



## IN：查询多种状态值

```
SELECT * FROM jxdx_leave l
WHERE 1=1 
AND l.deleted=0
AND l.`status` IN ('0','1');
```



## LIKE ：判断字段是否含有某字符串

```
SELECT
        start_date,
        CASE 
            WHEN second_category_name LIKE '%跑腿%' THEN '跑腿'
            WHEN second_category_name LIKE '%企客%' THEN '企客'
            WHEN bu_name = '骑手服务' AND third_category_name LIKE '%专送%'     THEN '专送外卖'
            WHEN bu_name = '骑手服务' AND third_category_name NOT LIKE '%专送%' THEN '众包外卖'
            WHEN bu_name = '外卖商服' THEN '外卖商服'
            ELSE '其他'
            END AS buname,
        CASE 
            WHEN source IN (1,11,13,-3)   THEN '电话'
            WHEN  source in (2,12,-4)      THEN '在线'
            WHEN (source = 20 OR (source = 29 AND case_result_desc = '客户直接诉求D')) THEN '自助建单'
            ELSE '其他'
            END AS source,
        case_id,
        lifecycle,
        concat(case_id,'-',lifecycle) as key,
        start_time,
        close_time,
        first_category_name,
        second_category_name,
        third_category_name,
        fourth_category_name,
        fifth_category_name,
        question_id,
        question_name, 
        customer_id,
        status_name,
        content,
        owner_id,
        owner_login_name,
        owner_real_name,
        onwer_dep_name,
        is_upgrade is_upgrade_raw,
        partition_close_date
    FROM mart_csp.topic_pacific_case_lifecycle
    WHERE partition_is_closed IN (0,1)
    AND first_category_name IN ('美团骑手服务','配送骑手服务','外卖骑手服务','跑腿骑手服务','跑腿','跑腿商家服务')
    AND bu_name in ('骑手服务')
    AND (content IS NULL OR (content NOT LIKE '%测试%忽略%' AND content NOT LIKE '%新人测试%' AND content NOT LIKE '%培训测试%' AND (content NOT LIKE '%测试%' OR LENGTH(content) > 5)))
    AND case_type_desc NOT LIKE '%CSO%'
    AND (source IN (1,2,11,12,13,-3,-4,20) OR (source=29 AND case_result_desc='客户直接诉求D'))
    AND (partition_close_date between "$begin_date_1day" and "$last_date" or partition_close_date = "9999-12-31")
    AND (close_time >= "$begin_time" or partition_close_date = "9999-12-31")
```



# Spark 函数技巧积累

## scala取json字段内容

```scala
val click = spark.sql(
    s"""
    select
        partition_date,
        login_id,
        stat_time,
        unix_timestamp(stat_time) as stat_time_1,
        department,
        event_id,
        event_name,
        event_attribute,
        get_json_object(event_attribute['custom'], '$$.chatId') as chatId,
        get_json_object(event_attribute['custom'], '$$.messageId') as messageId,
        concat_ws("<->",get_json_object(event_attribute['custom'], '$$.adoptionIndex'),get_json_object(event_attribute['custom'], '$$.adoptionContent.from'),get_json_object(event_attribute['custom'], '$$.adoptionContent.content')) as content
    from 
        mart_csp.std_flow_mv
    where
        where partition_date between "$data_begin" and "$data_end"
    and
        event_id = 'b_cs_fizdwjsl_mc'  -- 点击
    """).show(5, false)
```

```scala
val view_click_data = spark.sql(
    s"""
      |SELECT
      |*
      |FROM
      |(select login_id,
      |     unix_timestamp(stat_time) as stat_time,
      |     department,
      |     event_id,
      |     event_name,
      |     get_json_object(event_attribute['custom'], '$$.chatId') as chatId,
      |     get_json_object(event_attribute['custom'], '$$.messageId') as messageId,
      |     concat_ws("<->",get_json_object(event_attribute['custom'], '$$.adoptionIndex'),get_json_object(event_attribute['custom'], '$$.adoptionContent.from'),get_json_object(event_attribute['custom'], '$$.adoptionContent.content')) as content
      |from mart_csp.std_flow_mv
      |where partition_date between '${date1}' and '${date2}'
      |and event_id = 'b_cs_fizdwjsl_mc' -- 点击
      |
      |UNION All
      |SELECT
      |login_id,stat_time,department,event_id,event_name,chatId,messageId,content
      |FROM
      |(SELECT
      |       login_id,
      |       unix_timestamp(stat_time) as stat_time,
      |       department,
      |       event_id,
      |       event_name,
      |       chatId,
      |       messageId,
      |       traceId,
      |       concat_ws(";;;",collect_list(content)) as content
      |FROM
      |(select login_id,
      |       stat_time,
      |       department,
      |       event_id,
      |       event_name,
      |       get_json_object(event_attribute['custom'], '$$.chatId') as chatId,
      |       get_json_object(event_attribute['custom'], '$$.messageId') as messageId,
      | 	   get_json_object(view_message, '$$.traceId') as traceId,
      |       concat_ws("<->",get_json_object(view_message, '$$.statistics.showIndex'),get_json_object(view_message, '$$.from'),get_json_object(view_message, '$$.content')) as content
      |  from mart_csp.std_flow_mv lateral view explode(split(regexp_replace(regexp_replace (get_json_object(event_attribute['custom'], '$$.associationList'), '\\\\[|\\\\]', ''), -- 将 Json 数组两边的中括号去掉
      | '\\\\}\\\\,\\\\{', -- 将 Json 数组元素之间的逗号换成分号
      | '\\\\}\\\\;\\\\{'), '\\\\;')) tb as view_message
      |where partition_date between '${date1}' and '${date2}'
      |   and event_id = 'b_cs_c4ajjk5j_mc'  -- 曝光
      |)t_view
      |GROUP BY 1,2,3,4,5,6,7,8)t_view_1
      |
      |UNION All
      |
      |select login_id,
      |     unix_timestamp(stat_time) as stat_time,
      |     department,
      |     event_id,
      |     event_name,
      |     get_json_object(event_attribute['custom'], '$$.chatId') as chatId,
      |     get_json_object(event_attribute['custom'], '$$.messageId') as messageId,
      |     get_json_object(event_attribute['custom'], '$$.content') as content
      |from mart_csp.std_flow_mv
      |where partition_date between '${date1}' and '${date2}'
      | and event_id = 'b_cs_zahblbo5_mc' -- 发送消息
      |)t
      |""".stripMargin)
```



## bugs

```
org.apache.spark.sql.catalyst.errors.package$TreeNodeException: execute, tree:

一般是变量从内存中丢了，重新运行一遍就好
或者var xxx时，xxx.persist()
可以将变量暂存于内存中

```



## 提速操作-排序：scala 取数时排序比不排序速度快约50倍

```
// asr内容表：asr通话具体内容的表
// 操作：转res_index为int且>=0 方便后序排序，删除空text，以call_id为维度依据res_index对通话text进行排序
// 注意：该表需要选择时间时用的时间格式为before_dt 如20211228
val asr_data = spark.sql(
    s"""
    SELECT
        call_id, 
        speaker_channel, 
        asr_start_time, 
        asr_end_time, 
        get_json_object(asr_data, '$$.text') text, 
        get_json_object(asr_data, '$$.res_index') res_index
    FROM
        mart_mtai.nlu_cicada_log_etl
    WHERE
        asr_data is not null
    AND
        dt between "$before_dt" and "$end_dt"
    """).
    withColumn("res_index", $"res_index".cast("int")).
    filter("res_index >= 0").
    na.drop("any", Seq("text")).
    filter("text != ''").
    withColumn("sort", row_number.over(Window.partitionBy($"call_id").orderBy($"res_index")))
asr_data.persist()
asr_data.count()

可以看到有排序操作：
withColumn("sort", row_number.over(Window.partitionBy($"call_id").orderBy($"res_index")))
该操作实际比不排序速度快非常非常多
```



## udf：用户自定义函数UserDefineFunction

```
def getScenario(faq2: String, faq6: String) : String = {
    if (xinzi_faq6.contains(faq6) && faq2 == "专送账号问题") {
        "薪资"
    } else if (baoxian_faq6.contains(faq6)) {
        "保险"
    } else if (jiaotong_faq6.contains(faq6)) {
        "交通事故"
    } else {
        "其它"
    }
}

getScenario("专送账号问题", "合作商少发薪资")

val udf_getScenario = udf(getScenario _)

val x = spark_sql(
	"""
	sql
	"""
).withColumn("scenario", udf_getScenario($"second_category_name", $"question_name"))
```



## union：联合函数

```
https://www.yiibai.com/spark/apache-spark-union-function.html

val unionfunc = data1.union(data2)
```



## $：筛选时赋值变量

```
val data_begin = "2021-06-01"
val data_end = "2021-08-01"

AND (partition_close_date between "$data_begin" and "$data_end" or partition_close_date = "9999-12-31")
```



## orderby：排序表

```
orderBy("partition_close_date", "case_id", "lifecycle")
```



## drop：删除某列

```
val case_service_rela = case_call_rela.
    union(case_chat_rela).
    join(case_detail, Seq("case_id"), "left_semi").
    selectExpr("*", "COUNT(case_id) OVER(partition by service_id) as dup_count").
    filter("dup_count >= 2").
    drop("dup_count")
```



## coalesce：分区保存

```
.coalesce(20).write.parquet("/user/hadoop-hmart-mtai/wangchuan16/kg/cso/pacific")
```



## 窗口函数 over(partition by)和对应的api

```
https://blog.csdn.net/weixin_30693683/article/details/95667483

count(...) over(partition by ... order by ...)--求分组后的总数。
sum(...) over(partition by ... order by ...)--求分组后的和。
max(...) over(partition by ... order by ...)--求分组后的最大值。
min(...) over(partition by ... order by ...)--求分组后的最小值。
avg(...) over(partition by ... order by ...)--求分组后的平均值。
rank() over(partition by ... order by ...)--rank值可能是不连续的。
dense_rank() over(partition by ... order by ...)--rank值是连续的。
first_value(...) over(partition by ... order by ...)--求分组内的第一个值。
last_value(...) over(partition by ... order by ...)--求分组内的最后一个值。
lag() over(partition by ... order by ...)--取出前n行数据。　　
lead() over(partition by ... order by ...)--取出后n行数据。
ratio_to_report() over(partition by ... order by ...)--Ratio_to_report() 括号中就是分子，over() 括号中就是分母。
percent_rank() over(partition by ... order by ...)--
```



## 窗口函数Window：实现分组取topN 

```
https://blog.csdn.net/Android_xue/article/details/105796733

    val df = spark.read.textFile("./data/test")
      .map(_.split(","))
      .map(x => (x(0), x(1), x(2)))
      .toDF("company", "app", "vst_times")
      .cache()
    val windows = Window.partitionBy("company").orderBy(col("vst_times").desc)
    //取出BAT三大公司访问量Top2的app
    df.select("company", "app", "vst_times")
      .withColumn("row_number", row_number().over(windows))
      .where("row_number <= 2 ")
      .select("company", "app", "vst_times")
      .show()

```



## join的方式 left_semi只保留左表中存在的

```
SQL的join：https://www.cnblogs.com/yanglang/p/8780722.html

HIVE中join left_semi:https://blog.csdn.net/helloxiaozhe/article/details/87910386
```



## withColumn新增一列

```
val case_detail = spark.sql(
	"""
	select * from tableA
	""").
	withColumn("scenario", udf_getScenario($"second_category_name", $"question_name")).
  filter("scenario != '其它'")
case_detail.persist()  # persist()可以保存在内存中 长时间不动也不会消失
case_detail.count()
```



## withColumnRenamed修改列名

```
https://spark.apache.org/docs/latest/api/python/reference/api/pyspark.sql.DataFrame.withColumnRenamed.html


```



## (好)select和selectExpr选择表达式

```
https://blog.csdn.net/stan1111/article/details/107738320

小技巧：传入"*"选择所有列。
```



## 聚合函数 COUNT OVER等

```
https://juejin.cn/post/6844903950232059911
```



## lit：使用lit()增加常量（固定值）

```
https://www.cnblogs.com/yy3b2007com/p/9872492.html
lit()是spark自带的函数，需要import org.apache.spark.sql.functions

# 将type这一列全部置为1
case_chat_relation.withColumn("type", lit(1)).

scala> df.withColumn("sinurl", lit(12)).show 
```



## row_number()实现分组

```
https://blog.csdn.net/bokzmm/article/details/79659430

row_number的格式：
    ROW_NUMBER() OVER (PARTITION BY 'xxx' ORDER BY 'xxx' DESC) rank
```



# Spark (version:2.2.0) meituan数据获取

```SPARQL
ssh wangchuan16@jumper.sankuai.com
ssh zw-ai-kg-sparkclient01
sudo -iu sankuai
cd /opt/meituan/wanghansen
cp -a spark_shell.sh ../wangchuan16/
vim spark_shell.sh
# 改了名字wangchuan16 删了第十行的jar  双击dd
sh spark_shell.sh
# 等半分钟

# 在spark机器上输入：
# 这些scala代码只会检查语法和逻辑 不会实际查出数据，只是生成一个视图
val asr_data = spark.sq(
   """
   select
     call_id,
     speaker_channel,
     asr_start_time,
     asr_end_time,
     get_json_object(asr_data,'$.text') text,
     get_json_object(asr_data,'$.res_index') res_index,
     dt
   from
     mart_mtai.nlu_cicada_log_etl
   where
     asr_data is not null
   and
     dt between '20210427' and '20210427'
   """)

# 查看所有结果列
asr_data.printSchema()

# 显示前五个数据
asr_data.show(5)

# 选出从DataFrame中的text
val textData = asr_data.select("text")

# map跟python map差不多 都是对textData的每一行进行map操作
# e => e.getring(0)获取第一行，
# (e.getString(0), 1)就 每一列都变成了【xxx, 1】
# rdd.reduceByKey是去重操作
val textDup = textData.map(e => (e.getString(0), 1)).rdd.reduceByKey((e, f) => f).map(e => e._1)

# /user/hadoop-mtai在hdfs上，如果要访问hdfs，需要用hadoop fs命令访问 
# 如果saveAsTextFile报错，可能是需要.rdd.saveAsTextFile
textDup.repartition(100).saveAsTextFile("/user/hadoop-mtai/wangchuan16/kg/kefu/call_20210712")
# 这一命令是在分区成100个去 自动寻找那些可以并行，最后就会有100个文件
# 如果不容新分区，就是1000个分区，最后会有1000条
# 在http://data.sankuai.com/mthdpmgr/jobsearch  查看 输入 wangchuan16
# 然后点applicationmaster 可以查看详细的内容

# 这样就将spark机器中的数据保存到了文件中转机器，他们是分布式的，所以可以直接保存
# 接下来登录服务器，然后利用hadoop命令下载数据
# 因为有100条数据，要全部下载 需要用-getmerge
hadoop fs -getmerge /user/hadoop-hmart-mtai/wanghansen/kg/kefu/chuan/date_temp_20210427 ./data.mingzi
```



## hdfs 读取文件然后get到本地文件夹【全量质检欠薪二线】

```
# 创建文件夹要在spark的服务器上，在双卡的服务器上面没有权限。（只有双卡的服务器有hadoop客户端），原因是双卡的服务器是一个中卫机群，不是一台机器，当然没有写的权限啦。

# 登录spark服务器 有hadoop客户端
ssh wangchuan16@jumper.sankuai.com
ssh zw-ai-kg-sparkclient01
sudo -iu sankuai

# hdfs hadoop写文件
(base) [sankuai@xr-ai-kg-sparkclient01 ~]$ hadoop fs -mkdir wangchuan16/kg/quality_inspection

# 读欠薪二线文件  在双卡/四卡 的服务器上
(chuan) [hadoop-mtai@zw03-data-hdp-dn-gpu0246 check]$ cd /home/hadoop-mtai/cephfs/data/wangchuan16/meituan/rider_quality_inspection/qianxin/分类代码ready/check

(chuan) [hadoop-mtai@zw03-data-hdp-dn-gpu0246 check]$ pwd
/home/hadoop-mtai/cephfs/data/wangchuan16/meituan/rider_quality_inspection/qianxin/分类代码ready/check

(chuan) [hadoop-mtai@zw03-data-hdp-dn-gpu0246 check]$ hadoop fs -ls /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/

(chuan) [hadoop-mtai@zw03-data-hdp-dn-gpu0246 check]$ hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20210927/ ./

hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211129/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211130/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211201/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211202/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211203/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211224/ ./
hadoop fs -get /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/20211225/ ./


# 读个数
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211222/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211223/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211224/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211225/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211226/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211204/part-00000
hadoop fs -cat /user/hadoop-hmart-mtai/maqiao02/kefu/raw_data/qianxin_second_calls/count_20211205/part-00000


```



## Spark---DataFrame学习(二)——select、selectExpr函数

```
https://blog.csdn.net/stan1111/article/details/107738320

```




## spark filter

```
https://www.jianshu.com/p/8ac9778eb4bd
```



## spark依据list筛选 left_semi

```
val case_selected = spark.read.parquet("/user/hadoop-hmart-mtai/wangchuan16/kg/tmp/case_id")

case_selected.show(1)

val case_detail = spark.sql(
   s"""
   SELECT
       case_id,
       customer_id,
       customer_type_desc,
       partition_close_date
   FROM mart_csp.topic_pacific_case_lifecycle
   WHERE partition_close_date between "2021-10-01" and "2021-10-21" or partition_close_date = "9999-12-31"
   """).
   join(case_selected, Seq("case_id"), "left_semi")
   
case_detail.printSchema
case_detail.show()
// case_detail.count()

case_detail.coalesce(10).write.parquet("/user/hadoop-hmart-mtai/wangchuan16/kg/tmp/case_detail")
```



## spark 去重

```
https://www.cnblogs.com/wwxbi/p/6102085.html
https://towardsdatascience.com/distinct-vs-dropduplicates-in-spark-3e28af1f793c

df.distinct().show()
+---+------+---+
| id|  name|age|
+---+------+---+
|  1|Andrew| 26|
|  2| Maria| 30|
|  1|Andrew| 25|
+---+------+---+

df.dropDuplicates(['id', 'name']).show()
+---+------+---+
| id|  name|age|
+---+------+---+
|  2| Maria| 30|
|  1|Andrew| 25|
+---+------+---+

```



## spark 读写dataset为parquet文件

```
var call_cso = spark.read.parquet("/user/hadoop-hmart-mtai/wangchuan16/kg/cso/call_cso_0818_1018")

chat_cso.coalesce(10).write.parquet("/user/hadoop-hmart-mtai/wangchuan16/kg/cso/chat_cso_0818_1018")

```



## spark filter 筛选liist中的内容

```
https://stackoverflow.com/questions/33981487/filter-spark-dataframe-by-checking-if-value-is-in-a-list-with-other-criteria

val list = List("x","y","t") 
xdf.filter($"column".isin(list:_*))
```



## spark dataset filter 筛选数据包含字符串

```
>>> mac_df = spark.createDataFrame([
...   ('5C-C3-07-99-C7-44', '44039604011420100002'),
...   ('88-25-93-4F-E7-37', '44039604011420100002')
...   ], 'struct<MAC:string,gbNo:string>')
>>> mac_df2 = mac_df.filter("substring(MAC, 8, 1) in ('2', '3', 'A')")
>>> mac_df.show()
+-----------------+--------------------+
|              MAC|                gbNo|
+-----------------+--------------------+
|5C-C3-07-99-C7-44|44039604011420100002|
|88-25-93-4F-E7-37|44039604011420100002|
+-----------------+--------------------+

>>> mac_df2.show()
+-----------------+--------------------+
|              MAC|                gbNo|
+-----------------+--------------------+
|88-25-93-4F-E7-37|44039604011420100002|
+-----------------+--------------------+
```



## spark dataset dataframe rdd的转换

```
https://blog.csdn.net/qq_40180229/article/details/105681379

RDD (Spark1.0) —> Dataframe(Spark1.3) —> Dataset(Spark1.6)
如果同样的数据都给到这三个数据结构，他们分别计算之后，都会给出相同的结果。不同是的他们的执行效率和执行方式。在后期的Spark版本中，DataSet有可能会逐步取代RDD和DataFrame成为唯一的API接口。
```



## spark dataset保存csv

```
https://blog.csdn.net/qq_42346574/article/details/118972367

chat_cso.coalesce(1).write.option("header", "true").csv("/user/hadoop-hmart-mtai/wangchuan16/kg/cso/chat_cso_0904.csv")

# 遇到重复列名会报错
org.apache.spark.sql.AnalysisException: Duplicate column(s): "add_time", "staff_id" found, cannot save to file.;

# debug
https://www.cnblogs.com/Gxiaobai/p/9589622.html
https://stackoverflow.com/questions/48296677/spark-dataframe-join-duplicate-column-non-joined-column
大致的意思就是说，要保存的表中有相同的name字段，这样是不行的，那么解决方案就很明显了，让两个那么字段名称不相同么，那就分别给他们其别名。

val df1Cols = pacific_chat.columns
val df2Cols = chat_text.columns

// prefixes to column names
val df1pf = pacific_chat.select(df1Cols.map(n => col(n).as("df1_"+n)):_*)
val df2pf = chat_text.select(df2Cols.map(n => col(n).as("df2_"+n)):_*)

df1pf.join(df2pf,
    $"df1_dept_id"===$"df2_id",
 )
```



## spark 查看变量类型和dataframe每列类型

```
https://blog.csdn.net/bowenlaw/article/details/99673051

println(chat_cso.getClass)


val data = Array(("1", "2", "3", "4", "5"), ("6", "7", "8", "9", "10"))
val df = spark.createDataFrame(data).toDF("col1", "col2", "col3", "col4", "col5")

df.dtypes
```



## spark查看dataset大小

```
chat_cso.count()
```







## 魔数看第一行

```
select hare
from mart_mtai.fact_es_hare_full_esbiz
where dt="20210813"
limit 1  # 取第一行
```



## spark文档和meituan数据、spark进度查询

https://spark.apache.org/docs/2.2.0/quick-start.html

https://bi.sankuai.com/sql/edit

http://data.sankuai.com/mthdpmgr/jobsearch

## RDD sc.parallelize()  &  makeRDD

rdd 就是 key,value形式的数据集(也可以是单一的list 就是只有数值不是元组)



sc.parallelize() 和 makeRDD(seq())一样，具体区别：

*Spark主要提供了两种函数：parallelize和makeRDD：1）parallelize的声明：def parallelize[T: ClassTag](seq: Seq[T],numSlices: Int = defaultParallelism): RDD[T]2）makeRDD的声明：def makeRDD[T: ClassTag](seq: Seq[T],numSlices: Int = defaultParallelism): RDD[T]def makeRDD[T: ClassTag](seq: Seq[(T, Seq[String])]): RDD[T]3）区别：A）makeRDD函数比parallelize函数多提供了数据的位置信息。B）两者的返回值都是ParallelCollectionRDD，但parallelize函数可以自己指定分区的数量，而makeRDD函数固定为seq参数的size大小。*

```
通过调用SparkContext的parallelize方法，在一个已经存在的Scala集合上创建的（一个Seq对象）。集合的对象将会被拷贝，创建出一个可以被并行操作的分布式数据集。

data = [1, 2, 3, 4, 5]  
distData = sc.parallelize(data)  

一旦分布式数据集（distData）被创建好，它们将可以被并行操作。例如，我们可以调用distData.reduce(lambda a, b: a + b)来将数组的元素相加。我们会在后续的分布式数据集运算中进一步描述。
并行集合的一个重要参数是slices，表示数据集切分的份数。Spark将会在集群上为每一份数据起一个任务。典型地，你可以在集群的每个CPU上分布2-4个slices. 一般来说，Spark会尝试根据集群的状况，来自动设定slices的数目。然而，你也可以通过传递给parallelize的第二个参数来进行手动设置。（例如：sc.parallelize(data, 10)).
```

## RDD输出值

```
# https://blog.csdn.net/u012102306/article/details/51993519

pairRdd.collect.foreach(println)  # 逐行打印pairRdd

pairRdd.collect() # 不推荐

take()  # 输出  无排序
top()  # 输出   按降序排序
takeOrdered()  # 输出  按升序排序

例子：
take()  # 输出前几个 无排序

def take(num: Int): Array[T]

take用于获取RDD中从0到num-1下标的元素，不排序。
例如：
scala> var rdd1 = sc.makeRDD(Seq(10, 4, 2, 12, 3))
rdd1: org.apache.spark.rdd.RDD[Int] = ParallelCollectionRDD[40] at makeRDD at :21

scala> rdd1.take(1)
res0: Array[Int] = Array(10)                                                   

scala> rdd1.top(1)
res2: Array[Int] = Array(12)

scala> rdd1.top(1)
res4: Array[Int] = Array(2)

总结：
pairRdd.collect.foreach(println)  # 逐行打印pairRdd
take()  # 输出  无排序
top()  # 输出   按降序排序
takeOrdered()  # 输出  按升序排序
```



## reduceByKey()

```
# 好
https://www.cnblogs.com/zzhangyuhang/p/9001523.html

# _+_的用法 其实类似python中的_ 也是省略的一种
https://blog.csdn.net/lucasmaluping/article/details/103114091


```

## =>  和 _

```
https://blog.csdn.net/datadev_sh/article/details/79854273

=>
左边是参数
右边是返回类型

例如 rdd数据集中
rdd.reduceByKey((e,f) => f)
作用就是对相同key的两个value 分别是e,f做function操作，操作的返回就是f（即保留一个）
因为这里rdd是(string,int),因此value的值无关紧要。
因此达到了去重的作用。

_
是取第几个的意思，N从1开始

例如
scala> val pair = (99, "Luftballons")
pair: (Int, String) = (99,Luftballons)

scala> println(pair._1)
99

scala> println(pair._2)
Luftballons

```

## map

```
跟python一样 不过要结合=>，python里面是lambda x:x*2

map(e => (e.getString(0), 1))
e是一个参数，可以改成line等等
返回是pair元组 ：首先对e进行getString(0) 即取第一个，然后再和 int数字1组成元组pair
即返回是（string， int）
```



## 【好】flatMapvalues、map、mapPartitions

```
【好】
https://blog.csdn.net/helloxiaozhe/article/details/80492933


```



## RDD中基本转化操作union、intersection、subtract

```
http://lxw1234.com/archives/2015/07/345.htmc'd
```



## scala中:::等操作符

```
https://blog.csdn.net/datadev_sh/article/details/79854273

```

<img src="linux.assets/image-20210805160440931.png" alt="image-20210805160440931" style="zoom:50%;" />



## spark filter： 对RDD进行筛选

```
https://blog.csdn.net/star5610/article/details/106379609

import java.util.Calendar

import scala.collection.mutable.ListBuffer

object Test1 {

  def main(args: Array[String]): Unit = {

    var list:ListBuffer[Tuple3[String,String,Int]]=ListBuffer()
    list.+=(("张三", "男", 1998))
    list.+=(("李四", "女", 1997))
    list.+=(("王五", "男", 1997))
    list.+=(("宫六", "女", 1999))
    list.+=(("何七", "女", 1993))
    list.+=(("周八", "男", 1992))
    list.+=(("申九", "女", 1999))
    list.+=(("rose", "女", 2011))
    list.+=(("Jhon", "男", 2010))

    list.foreach(println)
    println()

    //筛选男生
    val boyList=list.filter(a => a._2=="男")
    boyList.foreach(println)
    println()

    //获取当前 年
    val  year=Calendar.getInstance().get(Calendar.YEAR)
    //获取年龄大于等于18的
    val gt18List=list.filter(a => year-a._3 >=18)
    gt18List.foreach(println)
    println()
    //获取年龄小于18的
    val lt18List=list.filter(a => year-a._3 <18)
    lt18List.foreach(println)
    
  }
}

```



# hadoop命令

hadoop其实是和linux差不多的，hadoop的存在就是为了大数据文件传输的。

当有hadoop客服端时，就能输入hadoop命令来进行操作。

hadoop的基本命令都是 hadoop fs -xxx



## 常用命令

https://blog.csdn.net/zgaoq/article/details/81945402



## hadoop删除文件夹

```
hadoop fs -rm -r -skipTrash /folder_name
```



## meituan组内的两个hadoop目录

hdfs://hadoop-meituan/user/hadoop-hmart-mtai/

hdfs://hadoop-meituan/user/hadoop-mtai/

他们其实都是同一台机器的不同目录。 

下面的命令中可以省略hdfs://hadoop-meituan，客户端会自动查询到这里。



## mkdir

```
(base) [sankuai@xr-ai-kg-sparkclient01 /]$ hadoop fs -ls /user/hadoop-hmart-mtai/
Found 40 items
...

# 在两个目录中分别创建自己的文件夹
(base) [sankuai@xr-ai-kg-sparkclient01 /]$ hadoop fs -mkdir /user/hadoop-hmart-mtai/wangchuan16
(base) [sankuai@xr-ai-kg-sparkclient01 /]$ hadoop fs -ls /user/hadoop-hmart-mtai/
Found 41 items

(base) [sankuai@xr-ai-kg-sparkclient01 /]$ hadoop fs -mkdir /user/hadoop-mtai/wangchuan16
(base) [sankuai@xr-ai-kg-sparkclient01 /]$ hadoop fs -ls /user/hadoop-mtai/
Found 67 items
```



## -getmerge 合并多个partition来下载

```
https://blog.csdn.net/power0405hf/article/details/50596233

hadoop fs -getmerge /user/hadoop-hmart-mtai/wanghansen/kg/kefu/chuan/date_temp_20210427 ./data.mingzi
这里因为之前有100个分区，所以有100条结果，都要下载，一个一个不现实，因此用getmerge来。
```

# hive

## get_json_object

```
https://www.cnblogs.com/drjava/p/10486134.html

对于jsonArray（json数组），如person表的xjson字段有数据：

[{"name":"王二狗","sex":"男","age":"25"},{"name":"李狗嗨","sex":"男","age":"47"}]
取出第一个json对象，那么hive sql为：

SELECT get_json_object(xjson,"$.[0]") FROM person;
 结果是：

{"name":"王二狗","sex":"男","age":"25"}
取出第一个json的age字段的值：

SELECT get_json_object(xjson,"$.[0].age") FROM person;
结果

25
```



# 正则表达式

## re.sub:相当于python的replace

```
import re
def resub(x):
    '''re.sub来替换字符串
    '''
    x = re.sub("&nbsp;", "", x)  # 去除html标记
    x = re.sub("\[..\]", "", x)  # 去除[鲜花]等emoji
    x = re.sub("\<div\>.*?\</div\>", "", x)  # 去除<div></div>
    x = re.sub("\<img.*?\"\>", " ", x)  # 去除<img src...>
    x = re.sub("\x20+", " ", x)  # 多个空格转为1个空格
#     x = re.sub("\s+", " ", x)  # 多个空格（包括换行符\n \t等）转为1个空格
#     x = re.sub("^.*?(&nbsp;).*?$", "\\1", x)
    return x
```



## 正则表达式：只匹配空格，不匹配换行等其余空白字符

```
\s	// 匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
\x20	// 匹配一个空格。
\f	// 匹配一个换页符。
\n	// 匹配一个换行符。
\r	// 匹配一个回车符。
```



# LLM

## TP PP DP与NNODE NGPU_PER_NODE的关系

**总GPU数量=TP x PP x DP**

**总GPU数量=NNODE x NGPU_PER_NODE**

```
https://zhuanlan.zhihu.com/p/611325149
总GPU数量=NNODE * NGPU_PER_NODE
总GPU数量=TP*PP*DP
每x张GPU同享同一部分模型参数， x = 总GPU / TP*PP

如果不考虑DP，那么TP*PP==总GPU
因为PP是从模型层数维度考虑，比如8层模型，PP=2,那么就是2张GPU，每张GPU放4层layer的参数
TP是从模型参数计算维度考虑，比如TP=2，那么就是参数w的计算纵向一分为二，每张GPU计算一半w的参数
DP则是复制数据，属于纯加速，PP和TP当NNODE！=1时，必然涉及不同机器之间的通信耗时。
DP则是复制数据DP份，如DP=2，就把数据复制2分，分别给两个GPU
```

## bf16和fp16的区别

```
https://zhuanlan.zhihu.com/p/449345588
就是16为的划分，在整数部分和小数部分的区别。
```



## 生成模型在生成时的四个参数，temperature、TopP、Frequency Penalty 和 Presence Penalty

```
https://huggingface.co/docs/transformers/main_classes/text_generation

在生成式语言模型中，设置参数可以影响到模型的生成结果，其中常见的四个参数是 temperature、TopP、Frequency Penalty 和 Presence Penalty。

Temperature
Temperature参数控制了生成文本的多样性，是通过对模型的softmax输出进行缩放来实现的。较高的temperature值可以使得模型更多地探索不同的输出可能性，而较低的值会使得模型更加保守，更倾向于生成高概率的词。一般来说，temperature值在[0.5, 1.0]范围内比较常用，较高的值可以用来产生更多的变化，但是较低的值可以产生更加稳定和可控的结果。

TopP
TopP（Top Probability）参数控制了生成文本时可以选择的候选词汇的概率总和的上限。该参数的范围通常为[0, 1]，表示从所有候选词中，选取概率累计值大于TopP的词作为备选。TopP参数可以帮助减少无意义的文本生成，避免生成重复、不相关或冗余的文本内容。在一些生成任务中，TopP参数可以与temperature一起使用，以产生更多样化、自然的输出。

Frequency Penalty
Frequency Penalty参数是一种基于词频的约束，用于惩罚高频词的出现。通常来说，高频词出现的概率很大，而在生成文本的过程中，过多的高频词可能会导致生成的文本质量下降，变得单调乏味。Frequency Penalty参数可以通过对高频词的概率进行惩罚，强制模型更多地探索低频词，以产生更加多样化、新颖的文本内容。

Presence Penalty
Presence Penalty参数是一种基于语法、逻辑约束的控制方式，它可以惩罚模型产生与先前上下文不一致的文本，以减少生成不合理或无意义的文本内容。Presence Penalty参数可以通过对模型中生成文本的词序列进行约束，使得模型生成的文本更符合先前上下文的语义和逻辑。这个参数可以在一些需要生成严谨、合理文本的任务中使用，例如文本摘要、机器翻译等任务。

总之，这些参数都是用于调整模型在生成文本时的行为，通过设置不同的参数值，可以控制模型生成的文本多样性、准确性和一致性。在使用这些参数时，需要根据具体的任务需求和生成结果进行不断调优和改进。
```



## BLOOMZ-7B1 SFT训练日志

```
[default7]: iteration     2542/    9765 | consumed samples:      5206016 | consumed tokens:  10661920768 | elapsed time per iteration (s): 23.69 | learning rate: 2.467E-06 | global batch size:  2048 | lm loss: 1.202895E+00 | loss scale: 16384.0 | grad norm: 0.540 | num zeros: 0.0 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 86.451 | TFLOPs: 161.87 |
[default7]: iteration     2543/    9765 | consumed samples:      5208064 | consumed tokens:  10666115072 | elapsed time per iteration (s): 23.56 | learning rate: 2.467E-06 | global batch size:  2048 | lm loss: 1.201239E+00 | loss scale: 16384.0 | grad norm: 0.519 | num zeros: 0.0 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 86.936 | TFLOPs: 162.77 |
[default7]: iteration     2544/    9765 | consumed samples:      5210112 | consumed tokens:  10670309376 | elapsed time per iteration (s): 23.54 | learning rate: 2.466E-06 | global batch size:  2048 | lm loss: 1.195018E+00 | loss scale: 16384.0 | grad norm: 0.558 | num zeros: 0.0 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 86.993 | TFLOPs: 162.88 |
[default7]: iteration     2545/    9765 | consumed samples:      5212160 | consumed tokens:  10674503680 | elapsed time per iteration (s): 23.62 | learning rate: 2.466E-06 | global batch size:  2048 | lm loss: 1.199704E+00 | loss scale: 16384.0 | grad norm: 0.504 | num zeros: 0.0 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 86.706 | TFLOPs: 162.34 |
[default7]: iteration     2546/    9765 | consumed samples:      5214208 | consumed tokens:  10678697984 | elapsed time per iteration (s): 23.58 | learning rate: 2.466E-06 | global batch size:  2048 | lm loss: 1.196612E+00 | loss scale: 16384.0 | grad norm: 0.515 | num zeros: 0.0 | number of skipped iterations:   0 | number of nan iterations:   0 | samples per second: 86.862 | TFLOPs: 162.63 |

```



## GLM工程组部署

```
环境准备
1.下载TritonServerClient：
pip3 install TritonServerClient -i http://pypi.sankuai.com/simple --trusted-host pypi.sankuai.com —upgrade

1.1 TritonServerClient需要打下补丁，找到TritonServerClient的安装路径，并替换该包根路径的__init__.py

2.获取客户端代码

2.1 git clone ssh://git@git.sankuai.com/mtmlp/llm_inference_examples.git

> cd llm_inference_examples/glm

2.2 修改client代码，指定服务端ip

line 135修改为：
with TritonServerClient(appkey, appkey, 1000000, server_targets=["10.163.42.82:26381"]) as client:

3.启动客户端demo
> cd llm_inference_examples/glm
>  python3 client/glm_client.py --hf_model_location icetk_glm_130B/  --appkey com.sankuai.data.hadoop.gongsongshan  --model_name glm130b_ft
```



## ☆【重要】GLM与UniLM/T5的区别

```
结论：
GLM是Decoder-Only
UniLM是Encoder-Only
T5是Encoder-Decoder架构

GLM主打的是预训练中的blank infilling，即以自回归的方式去预测mask的内容，是依赖上一个时间戳结果然后生成的；相比UniLM是纯Encoder，通过MASK的方式，经过SELF-ATT后直接输出全部结果，因此UniLM是encoder-only；而相比T5，它之所以是encoder-decoder，是因为他有encoder和decoder中间的cross attention。而GLM只有self-attention，并且是逐个token生成的，是自回归的方式，因此是decoder-only。
```



## GLM为什么要用PreLN+DeepNorm

```
https://www.zhihu.com/question/555433259/answer/2955859073

post-norm和pre-norm其实各有优势，post-norm在残差之后做归一化，对参数正则化的效果更强，进而模型的鲁棒性也会更好；pre-norm相对于post-norm，因为有一部分参数直接加在了后面，不需要对这部分参数进行正则化，正好可以防止模型的梯度爆炸或者梯度消失，因此，这里笔者可以得出的一个结论是如果层数少post-norm的效果其实要好一些，如果要把层数加大，为了保证模型的训练，pre-norm显然更好一些。

为什么Layer Normalization要加在F的前面，而不是F的后面呢？

因为做完Layer Normalization之后的数据不能和平常的数据加在一起，如果这样做的话残差中从上一层出来的信息会占很大比重，这显然并不合理。

说白了，Pre Norm结构无形地增加了模型的宽度而降低了模型的深度，而我们知道深度通常比宽度更重要，所以是无形之中的降低深度导致最终效果变差了！
```



## ☆【重要】Encoder-only与Decoder-only的区别

```
https://www.zhihu.com/question/592545459/answer/2996029455

Encoder和Decoder都是由多个Transformer堆叠而成的。在Encoder中，每个Transformer都会对输入数据进行一次处理，然后将处理结果传递给下一个Transformer。这样，经过多次处理后，输入数据就被编码成了一个高维向量，可以用于后续的任务。在Decoder中，也是类似的过程，只不过它的输入是来自上一个时间步的输出，而不是原始输入数据。虽然Encoder和Decoder都是由Transformer堆叠而成的，但它们的作用是不同的。Encoder主要用于将输入数据编码成一个高维向量，这个向量包含了输入数据的所有信息，可以用于后续的任务。而Decoder则主要用于根据输入向量生成输出数据，它的输入是来自上一个时间步的输出，因此可以生成具有上下文信息的输出。另外，Encoder和Decoder在堆叠Transformer的时候，也有一些细微的差别。在Encoder中，每个Transformer都是独立的，它们之间没有任何联系，因此可以并行处理。而在Decoder中，每个Transformer的输入都依赖于上一个时间步的输出，因此必须按照时间顺序依次处理，无法并行处理。总之，Encoder和Decoder都是由Transformer堆叠而成的，它们的作用和处理方式略有不同。Encoder主要用于将输入数据编码成一个高维向量，而Decoder则主要用于根据输入向量生成输出数据。在堆叠Transformer的时候，Encoder可以并行处理，而Decoder必须按照时间顺序依次处理。
```



# 炼丹日记

## tensorflow保存saved_model

```
from bert4keras.backend import keras, K
from tensorflow.python.saved_model import signature_constants
from tensorflow.python.saved_model import tag_constants

def save2pb(model,export_dir):
    sigs = {}
    sess=K.get_session()
    in_token=model.inputs[0]
    in_segment=model.inputs[1]
    out=model.outputs[0]

    sigs[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY] = \
        tf.saved_model.signature_def_utils.predict_signature_def(
            inputs={'in_token':in_token,'in_segment':in_segment},outputs={'outputs':out})

    builder = tf.saved_model.builder.SavedModelBuilder(export_dir)
    builder.add_meta_graph_and_variables(sess,
                                             [tag_constants.SERVING],
                                             signature_def_map=sigs)

    builder.save()
    print('【!】pb model saved in '+export_dir)
    
    
save2pb(model,"models/dar.Baseline.m256.b32.rbt12.savedmodel")
```



## tensorflow 查看saved_model 的模型结构saved_model_cli

```
saved_model_cli show --all --dir dar.Baseline.m256.b32.rbt12.savedmodel/
```



## chrome新变化

```
chrome://whats-new/
```



## bert句向量表示各向异性

```
像“BERT+[CLS]”的句向量模型，在初始阶段具有严重的各向异性，这个“各向异性”用白话文怎么理解呢？

最朴素的一个表现是全体向量的均值向量明显偏离零向量；其次，你可以想象为将全体向量的点画在空间中，所呈现的立体图形明显不是一个球体。
```



## scala取数ls

```sql
1.当sql代码里面有变量时，即用到了$，sql需要用 s"""sql""" 来包围，必须有s。
此时get_json，的变量用$$.key来表示，必须为两个 $$.
2. join时应该注意，按照join的关键字是否类型一致，如chat_id进行join时，有的表可能是bigint，有的表可能是string，此时就可能join后为空。
应该首先将string变为bigint，如下：

SELECT 
	CAST(get_json_object(event_attribute['custom'], '$$.chatId') as bigint) chat_id
...

```



## TF：

### 模型转换ckpt to pb

```python
"""方法一：推荐
（mlp可用，生成.pb+variables，推荐）最终生产mlp可用PB模型的实际使用代码（保存pb+variables）
"""
export_path = os.path.join(out_dir, "saved_model")  # 模型保存的路径
if not os.path.exists(export_path):
    # 从网络的输入输出创建预测的签名
    model_signature = tf.saved_model.signature_def_utils.predict_signature_def(
        inputs={'input_ids': input_ids_p,
                'input_mask': input_mask_p,
                "segment_ids": segment_ids_p,
                "stroke_ids": stroke_ids_p},
        outputs={'fusion_prob': fusion_prob})
    # 使用utf-8编码将 字节或Unicode 转换为字节

    builder = tf.saved_model.builder.SavedModelBuilder(export_path)  # 生成"savedmodel"协议缓冲区并保存变量和模型
    builder.add_meta_graph_and_variables(  # 将当前元图添加到savedmodel并保存变量
        sess=sess,  # 返回一个 session 默认返回tf的sess,否则返回keras的sess,两者都没有将创建一个全新的sess返回
        tags=[tf.saved_model.tag_constants.SERVING],  # 导出模型tag为SERVING(其他可选TRAINING,EVAL,GPU,TPU)
        clear_devices=True,  # 清除设备信息
        signature_def_map={  # 签名定义映射
            tf.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:  # 默认服务签名定义密钥
                model_signature  # 网络的输入输出策创建预测的签名
        })
    builder.save()  # 将"savedmodel"协议缓冲区写入磁盘.               

    
"""方法二：不推荐
(可测试，只生成.pb，但不能用mlp，不推荐)保存.pb模型，只生成.pb文件，可以调用，但是不符合MLP上线要求，要求为.pb+variables
"""
from tensorflow.python.framework import graph_util

constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ["loss/fusion_prob"])
output_graph_name = os.path.join(out_dir, "model.pb")
pb_file_path = os.path.join("", output_graph_name)
with tf.gfile.GFile(pb_file_path, mode="wb") as f:
    f.write(constant_graph.SerializeToString())
   
```

方法二的调用

```python
# 只适用于方法二的调用（只生成.pb的方法）
import tensorflow as tf
from tensorflow.python.platform import gfile

def load_model(path_to_model):
    model_graph = tf.Graph()
    with model_graph.as_default():
        od_graph_def = tf.GraphDef()
        with tf.gfile.GFile(path_to_model, 'rb') as fid:
            serialized_graph = fid.read()
            od_graph_def.ParseFromString(serialized_graph)
            tf.import_graph_def(od_graph_def,name='')

    return model_graph

graph = load_model('datas/check/w39_r11_result/single_text_output/model.pb')

# 获取图变量
input_ids_p = graph.get_tensor_by_name('input_ids:0')
input_mask_p = graph.get_tensor_by_name('input_mask:0')
segment_ids_p = graph.get_tensor_by_name('segment_ids:0')
# label_ids_p = graph.get_tensor_by_name('label_ids:0')
stroke_ids_p = graph.get_tensor_by_name('stroke_ids:0')
# lmask_p = graph.get_tensor_by_name('lmask:0')
fusion_prob = graph.get_tensor_by_name('loss/fusion_prob:0')

feed_dict_dev = {
            input_ids_p: input_ids,
            input_mask_p: input_mask,
            segment_ids_p: segment_ids,
#             label_ids_p: label_ids,
            stroke_ids_p: stroke_ids
#             lmask_p: lmask
        }
    
# model 计算结果
sess = tf.Session(graph=graph)
fusion_pred = sess.run(fusion_prob, feed_dict=feed_dict_dev)
print(fusion_pred)
```



### 模型保存为savedmodel（.pb+variables）

保存好后查看pb的输入输出

```
saved_model_cli show --dir ./saved_model --all

Out：
signature_def['serving_default']:
  The given SavedModel SignatureDef contains the following input(s):
    inputs['input_ids'] tensor_info:
        dtype: DT_INT32
        shape: (1, 180)
        name: input_ids:0
    inputs['input_mask'] tensor_info:
        dtype: DT_INT32
        shape: (1, 180)
        name: input_mask:0
    inputs['segment_ids'] tensor_info:
        dtype: DT_INT32
        shape: (1, 180)
        name: segment_ids:0
    inputs['stroke_ids'] tensor_info:
        dtype: DT_INT32
        shape: (1, 180)
        name: stroke_ids:0
  The given SavedModel SignatureDef contains the following output(s):
    outputs['fusion_prob'] tensor_info:
        dtype: DT_FLOAT
        shape: (180, 21128)
        name: loss/fusion_prob:0
  Method name is: tensorflow/serving/predict
```

测试保存好的pb

```
saved_model_cli run --dir saved_model/ --tag_set serve --signature_def serving_default \
--input_exprs 'input_ids=np.array([[101, 779, 779, 3221, 3125, 7397, 6756, 1469, 6756, 6775, 5356, 1384, 1036, 4638, 4212, 4275, 1036, 2398, 102, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);input_mask=np.array([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);segment_ids=np.array([[0, 267, 267, 146, 2, 18, 59, 386, 59, 373, 296, 326, 135, 228, 40, 290, 135, 84, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]);stroke_ids=np.array([[0, 5065, 5065, 2163, 1114, 6554, 1906, 3318, 1906, 1922, 6900, 2445, 4241, 3788, 2458, 3568, 4241, 1858, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])'

Out:
[[1.2427459e-09 3.3699017e-08 4.4885137e-10 ... 2.6581143e-10
  2.5931635e-10 6.1772304e-10]
 [1.6709365e-18 3.1284468e-16 5.7042598e-18 ... 9.0444755e-19
  1.1853236e-18 1.3743385e-18]
 [1.8661123e-17 4.0088190e-16 3.5800714e-17 ... 7.1023498e-18
  1.2865428e-17 4.8654640e-18]
 ...
 [8.0036373e-11 1.5555814e-08 2.1155744e-10 ... 8.1106413e-11
  1.7173143e-10 1.5245440e-10]
 [8.5592333e-19 1.6036492e-16 4.1085370e-18 ... 9.5388483e-19
  8.6510953e-19 3.0378065e-18]
 [1.3743420e-15 7.5828693e-14 4.1436555e-15 ... 2.2852559e-15
  1.5548819e-15 2.4647655e-15]]
  
  
代码中的结果：
[[1.2427459e-09 3.3699017e-08 4.4885137e-10 ... 2.6581143e-10
  2.5931635e-10 6.1772304e-10]
 [1.6709365e-18 3.1284468e-16 5.7042598e-18 ... 9.0444755e-19
  1.1853236e-18 1.3743385e-18]
 [1.8661123e-17 4.0088190e-16 3.5800714e-17 ... 7.1023498e-18
  1.2865428e-17 4.8654640e-18]
 ...
 [8.0036373e-11 1.5555814e-08 2.1155744e-10 ... 8.1106413e-11
  1.7173143e-10 1.5245440e-10]
 [8.5592333e-19 1.6036492e-16 4.1085370e-18 ... 9.5388483e-19
  8.6510953e-19 3.0378065e-18]
 [1.3743420e-15 7.5828693e-14 4.1436555e-15 ... 2.2852559e-15
  1.5548819e-15 2.4647655e-15]]
```



### tensorboard

```
# 内网跳板机因无法连接外网，无法使用tensorboard ，需要将log文件传输至本地
tensorboard --logdir=/Users/wangchuan/Downloads/tmp_log

```



## 文本生成类：数据构成

**数据构成**:必须要有一致的文本

当使用UniLM做训练时，数据构成应该是有正确，有错误的。

原理在于，BERT做MLM任务是，也是需要对于MASK替换做10%的保留操作。

同理，https://aclanthology.org/2021.acl-long.233.pdf 这篇纠错任务上的paper，在MASK替换时也有10%的概率不做替换。

目的都是为了防止模型认为字符都是拼错的。



## markdown语法

```
https://www.jianshu.com/p/191d1e21f7ed
```



## 数据结构：后缀自动机--字符串神器

```
https://www.luogu.com.cn/blog/Kesdiael3/hou-zhui-zi-dong-ji-yang-xie
https://blog.csdn.net/qq_35649707/article/details/66473069

后缀自动机（单词的有向无环图）——是一种强有力的数据结构，让你能够解决许多字符串问题。

例如，使用后缀自动机可以在某一字符串中搜索另一字符串的所有出现位置，或者计算不同子串的个数——这都能在线性时间内解决。
```



## keras之多输入多输出（多任务）模型

```
# https://www.jb51.net/article/188935.htm
```



## keras  metrics：accuracy 

```
https://blog.csdn.net/Roaddd/article/details/121296336

acc是0和1都计算，所以多标签分类时可能准确率很低 但是acc很高，因为很多0也算入其中了
```



## why Prompt(提示)

```
比如情感分析中
预测I like eating apple的情感是good,bad
bert：I like eating apple. CLS二分类
prompt： I like eating apple, it was ___MASK___.(good, bad)

其实就是 
之前都是改变不同的BERT的训练方式来将BERT适配于不同的任务，比如做句子相似度时，SentenceBERT就是对BERT做适配于做句子相似度的loss设计然后finetune。
但是prompt是用任务去适配BERT，BERT预训练之处就是MASK任务，因此还是通过MASK任务，通过prompt（提示）的方式，去做训练，比如句子相似度时，就是 sentenceA and sentenceB is __MASK__.(similar, not similar)。

因此prompt tuning的核心在于模版的设计，就是如何设计适配于当前任务的提示模版。
```



## 通用语料与垂域语料 在垂域的效果

```
结论：垂域好很多，其实可以类比bert直接用来做句向量的效果远不如simcse等专门为句向量设计的模型，因为 术业有专攻！

以 kenlm 统计语言模型为例子，

202111-202112
zh_giga通用数据训练的模型
before	纠正:163		过纠:619
after 	纠正:73		过纠:185

lm_5gram垂域数据训练的模型
before	纠正:163		过纠:619
after 	纠正:143		过纠:223

```





## kenlm统计语言模型的原理、训练、使用&pycorrector的安装

ngram语言模型原理：https://blog.csdn.net/asrgreek/article/details/81979194

**垂直领域数据构建**

1. 105w数据过滤
2. 做char级别的 因此以空格间隔，如：“我 爱 你”（word则为  “我们 是 一个 社畜”）
3. 构建txt文件

**pre**

1. 必须以编译的方式安装Kenlm
2. 需要在mac中 编译安装
3. 安装时需要cmake和bost

**install**

1. 下载kenlm.tar.gz
2. brew install cmake
3. brew install boost
4. mkdir kenlm/build 
5. cd kenlm/build 
6. cmake .. 
7. make -j 4

**训练（必须在build目录下）**

1. cd kenlm/build

2. bin/lmplz -o 3 --verbose_header --text /Users/wangchuan/Downloads/train_data_kenlm.txt --arpa /Users/wangchuan/Downloads/LM.arpa

   其中参数的大致意义：

   ```
   -o n:最高采用n-gram语法
   -verbose_header:在生成的文件头位置加上统计信息
   --text text_file:指定存放预料的txt文件
   --arpa:指定输出的arpa文件
   -S [ --memory ] arg (=80%)  Sorting memory内存预占用量
   --skip_symbols : Treat <s>, </s>, and <unk> as whitespace instead of throwing an  exception
   ```

3. 转为2进制文件 加速inference

   bin/build_binary -s /Users/wangchuan/Downloads/lm_5gram.arpa /Users/wangchuan/Downloads/lm_5gram.bin

**Refs**

1. https://blog.csdn.net/Nicholas_Wong/article/details/80013547
2. 理论：https://zhuanlan.zhihu.com/p/270516015
3. kenlm模型详解：https://github.com/mattzheng/py-kenlm-model
4. kenlm原理：https://blog.csdn.net/asrgreek/article/details/81979194

```
# 训练统计语言模型
bin/lmplz -o 5 --verbose_header --text /Users/wangchuan/Downloads/train_data_kenlm_1kw.txt --arpa /Users/wangchuan/Downloads/statistics_lm_asr_send_1kw.arpa

# 转为二进制bin
bin/build_binary -s /Users/wangchuan/Downloads/statistics_lm_asr_send_1kw.arpa /Users/wangchuan/Downloads/statistics_lm_asr_send_1kw.bin
```



## ModelCheckpoint：每个epoch都保存模型

```
# https://blog.csdn.net/NewComerSyt/article/details/106398881
# https://www.jb51.net/article/188935.htm

# 需要tf2，不然会报错编码错误，气死我了！！！

checkpoint_filepath = 'model/tmp/checkpoint'
model_checkpoint_callback = tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_filepath,
    save_weights_only=True,
    monitor='val_prc',
    mode='max',
    save_best_only=False)

callbacks=[early_stopping, model_checkpoint_callback],
```



## 指标计算

### Recall@K指标在检索与推荐系统中的计算

```
https://zhuanlan.zhihu.com/p/143296492
```

### MRR

```
https://blog.csdn.net/weixin_44110392/article/details/123319189

MRR最早是在搜索场景下衡量，返回结果的质量。
其基于一个假设“每一个query Q只有一个与其相关(relevant)的结果A”
指标反应的是我们找到的这些item是否摆在用户更明显的位置，强调位置关系，顺序性。公式如下，N表示推荐次数，1/p表示用户真实访问的item在结果列表中的位置，如果没在结果序列中，则p为无穷大，1/p为0。
```



## TF-IDF和BM25的区别

```
# https://my.oschina.net/stanleysun/blog/1617727

1. BM25中的k的解释：
传统 TF Score = sqrt(tf)
BM25的 TF Score = ((k + 1) * tf) / (k + tf)
当 tf 增加时，TF Score 跟着增加，但是 BM25 的 TF Score 会被限制在 0~k+1 之间。它可以无限逼近 k+1，但永远无法触达它。这在业务上可以理解为某一个因素的影响强度不能是无限的，而是有个最大值，这也符合我们对文本相关性逻辑的理解。 在 Lucence 的默认设置里，k＝1.2，使用者可以修改它。

2. BM25 如何对待文档长度
    BM25 还引入了平均文档长度的概念，单个文档长度对相关性的影响力与它和平均长度的比值有关系。BM25 的 TF 公式里，除了 k 外，引入另外两个参数：L 和 b。L 是文档长度与平均长度的比值。如果文档长度是平均长度的 2 倍，则 L＝2。b 是一个常数，它的作用是规定 L 对评分的影响有多大。加了 L 和 b 的公式变为：

TF Score = ((k + 1) * tf) / (k * (1.0 - b + b * L) + tf)

文档越短，它逼近上限的速度越快，反之则越慢。这是可以理解的，对于只有几个词的内容，比如文章 “标题”，只需要匹配很少的几个词，就可以确定相关性。而对于大篇幅的内容，比如一本书的内容，需要匹配很多词才能知道它的重点是讲什么。

    上文说到，参数 b 的作用是设定 L 对评分的影响有多大。如果把 b 设置为 0，则 L 完全失去对评分的影响力。b 的值越大，L 对总评分的影响力越大。此时，相似度最终的完整公式为：

simlarity = IDF * ((k + 1) * tf) / (k * (1.0 - b + b * (|d|/avgDl)) + tf)

3. 传统 TF-IDF vs. BM25
    传统的 TF-IDF 是自然语言搜索的一个基础理论，它符合信息论中的熵的计算原理，虽然作者在刚提出它时并不知道与信息熵有什么关系，但你观察 IDF 公式会发现，它与熵的公式是类似的。实际上 IDF 就是一个特定条件下关键词概率分布的交叉熵。

    BM25 在传统 TF-IDF 的基础上增加了几个可调节的参数，使得它在应用上更佳灵活和强大，具有较高的实用性。

4.为什么 BM25 的 TF Score 计算要用 d/avgDl, 而不是用平方根、log 或者其它计算方法？它背后是否有理论支持？
	BM25是一种常用的信息检索算法，用于评估查询与文档之间的相关性得分。其中，TF部分用于计算查询词项在文档中的重要性得分。在BM25中，TF Score的计算采用的是如下公式：

TF Score = ((k+1)tf) / (k * ((1-b) + b(d/avgDl)) + tf)

其中，d表示文档的长度，avgDl表示所有文档的平均长度，tf表示词项在文档中的出现次数，k和b是调节因子。

您提到为什么BM25的TF Score计算中要使用d/avgDl，而不是使用平方根。这是因为使用d/avgDl可以更好地平衡长文档和短文档之间的影响，同时也考虑了词项在整个文集中的出现频率。相比之下，使用平方根可能会导致文档长度较短的文档受到过多的惩罚，而文档长度较长的文档则会受到过少的惩罚，因此会导致评分不够准确。

因此，在BM25算法中，使用d/avgDl作为TF Score计算的一部分，可以更好地平衡文档长度和词项出现频率的影响，得到更准确的相关性得分。
答案二：
①BM25的TF部分是基于BM11的TF-IDF改进而来的，它旨在平衡文档长度和词项频率的影响，而 d/avgDl 这个做法是一种平滑的方式，可以更好地达到这个目的。

②d/avgDl 能够反映词项的文集频率。例如，在一个文集中，某个词项在所有文档中都出现过，此时它对于区分不同文档的作用就比较小，因为它无法为不同文档提供更多的区分信息。而如果一个词项只在少数文档中出现，那么它对于区分不同文档的作用就会更大。因此，将 d/avgDl 纳入计算公式可以更好地反映词项的重要性。

③平方根、log等计算方法也被用于TF Score的计算，但是这些方法在平衡文档长度和词项频率的影响方面不如 d/avgDl 优秀。例如，平方根方法可能会导致文档长度较短的文档受到过多的惩罚，而文档长度较长的文档则会受到过少的惩罚，因此会导致评分不够准确。

总之，BM25算法中使用 d/avgDl 作为TF Score计算的一部分是有理论支持的，它可以更好地平衡文档长度和词项出现频率的影响，得到更准确的相关性得分。
```



## 如何理解梯度累加

好的，我再尝试一下更详细地解释一下梯度累加。

首先，让我们回顾一下SGD的更新公式：

$$\theta_{t+1} = \theta_{t} - \alpha\nabla f(\theta_{t})$$

其中，$\theta_{t}$是在时间步$t$时模型的参数，$\alpha$是学习率，$\nabla f(\theta_{t})$是在$\theta_{t}$处计算的损失函数$f$的梯度。SGD每次更新模型参数时，只考虑一个batch的数据，计算出一个梯度值并使用它来更新参数。

但是，当我们处理大规模数据集时，一个batch的数据可能会非常大，导致一个batch的梯度值也非常大，这会占用大量的GPU内存。为了解决这个问题，我们可以将多个batch的梯度值进行累加，然后再一次性更新参数。例如，假设我们需要处理一个大小为$B$的batch，那么我们可以累加$N$个大小为$B$的batch的梯度值，然后在更新参数时使用这个累加梯度：

$$\theta_{t+1} = \theta_{t} - \alpha\frac{1}{N}\sum_{i=1}^{N}\nabla f(\theta_{t}, x_{i})$$

其中，$x_{i}$是第$i$个batch的数据。

这样做的好处是，我们可以将大量的数据分成多个batch进行处理，然后再累加它们的梯度值，从而减少每个batch的梯度值的大小。同时，由于梯度值的累加可以降低梯度下降方向的随机性，因此可以提高模型的稳定性和性能。

需要注意的是，梯度累加的缺点是会导致参数更新的延迟，因为我们需要等到多个batch的梯度值都累加完毕之后，才能更新模型参数。此外，梯度累加的效果取决于累加的batch数和学习率的设置，需要进行合理的调参才能取得好的效果。

希望这次解释可以更好地帮助您理解梯度累加的含义和作用。



# 优选用户画像

| 分层         | 优选用户画像                                                 |
| ------------ | ------------------------------------------------------------ |
| **C端用户**  | 空闲精力相对较多，30岁以上的已婚已育女性；年龄层面，30-50岁占总用户比超70%；地域层面，3-4线城市 |
| **消费驱动** | 实惠度>便捷度(**T+1自提**)                                   |
| **B端用户**  | 团长：线下零售店主/社区宝妈                                  |
| **经营壁垒** | 通过社区优势资源组建的社区用户群、代收点位置便利度及区域饱和度、服务丰富度 |
| **利益驱动** | 商品推广佣金、增量用户拓展激励奖金（拉新激励）、商品差价     |



## 代码开头

```
import warnings
warnings.filterwarnings("ignore")

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "1"
# https://blog.csdn.net/c20081052/article/details/90230943
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # or any {'0', '1', '3'}

# jupyter内显示多个变量
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"  # 默认值是：'last_expr'
# https://www.cnblogs.com/grace731/articles/14805455.html

import pandas as pd
# 设置显示全部行，不省略
pd.set_option('display.max_rows',None)
# 设置显示全部列，不省略
pd.set_option('display.max_columns',None)
# 显示数据帧以拉伸页面
pd.set_option('display.expand_frame_repr',None)
# 显示每一格数据的最大内容
pd.set_option('display.max_colwidth',None)

# jupyter内画图 且输出矢量图 这样就不会放大图片变模糊了
%matplotlib inline
%config InlineBackend.figure_format = 'svg'

import tensorflow as tf
import bert4keras

config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5 # 占用GPU90%的显存
session = tf.Session(config=config)

print(bert4keras.__version__, tf.__version__)


import pickle
import json

def save_pkl(obj, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_pkl(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)
    
def jdump(filepath, dic):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(dic, f)
        print(f"dump {filepath} 完成")

def jload(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        load_dict = json.load(f)
        print(f"load {filepath} 完成")
        return load_dict
```



## 划分训练集代码 train_valid_test_split

```
def split_dataset(punctuation=True):
    '''
    punctuation:是否保留标点符号 coding
    '''
    data = pd.read_csv("data/asr_correct_labeled_data.txt", 
                   error_bad_lines=False, 
                   names=["key", "asr", "label"], 
                   sep=" ")
    data["equal"] = data.apply(lambda x: x["asr"] == x["label"], axis=1)
    data = data.loc[data["equal"]==False].drop(columns=["equal", "key"])
    data = data.reset_index(drop=True)

    n = len(data)
    train_data, valid_data, test_data = [], [], []
    for i, (asr, label) in enumerate(zip(data["asr"].values, data["label"].values)):
        if i <= 0.8 * n:
            train_data.append((asr, label))
        elif 0.8 * n < i <= 0.9 * n:
            valid_data.append((asr, label))
        elif 0.9 * n < i:
            test_data.append((asr, label))
    return train_data, valid_data, test_data
```



## 训练集和测试集表现差异大+过拟合solution

```
https://stackoverflow.com/questions/60595200/high-precision-recall-for-train-data-but-very-poor-for-test-data-in-classificati

https://stats.stackexchange.com/questions/412135/how-to-prevent-overfitting/412136#412136
```



## 类别不平衡 focal loss

```
实例见gitee

focal loss
参考链接：
https://blog.csdn.net/dendi_hust/article/details/116655739?spm=1001.2101.3001.6650.1&utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7ECTRLIST%7Edefault-1.no_search_link

https://towardsdatascience.com/a-loss-function-suitable-for-class-imbalanced-data-focal-loss-af1702d75d75

代码：

class WeightedFocalLoss(nn.Module):
    "Non weighted version of Focal Loss"    
    def __init__(self, alpha=.25, gamma=2):
            super(WeightedFocalLoss, self).__init__()        
            self.alpha = torch.tensor([alpha, 1-alpha]).cuda()        
            self.gamma = gamma
            
    def forward(self, inputs, targets):
            BCE_loss = F.binary_cross_entropy_with_logits(inputs, targets, reduction='none')        
            targets = targets.type(torch.long)        
            at = self.alpha.gather(0, targets.data.view(-1))        
            pt = torch.exp(-BCE_loss)        
            F_loss = at*(1-pt)**self.gamma * BCE_loss        
            return F_loss.mean()

总结：

调制因子（modulating factor）,从以上公式可得出如下推论：
趋于0的时候（样本分类错误，属于难分类样本），调制因子趋于1，该部分损失在总loss中基本不受影响。
当趋于1的时候（样本分类正确，属于易分类样本），调制因子趋于0，该部分损失在总loss中的权重变小。
参数γ \gammaγ平滑的降低易分类样本损失在总损失的比例，使样本更加专注于学习难分类样本的特征。当γ = 0 \gamma =0γ=0的时候，focal loss就是传统的交叉熵损失，可以通过调整γ \gammaγ实现调制因子的改变。
```



## 二分类时metrics输出P/R/PRC/LOSS等

```
前提条件：
Dense(units=1, activation='sigmoid',...)
loss="binary_crossentropy"

代码：
METRICS = [
      keras.metrics.TruePositives(name='tp'),
      keras.metrics.FalsePositives(name='fp'),
      keras.metrics.TrueNegatives(name='tn'),
      keras.metrics.FalseNegatives(name='fn'), 
      keras.metrics.BinaryAccuracy(name='accuracy'),
      keras.metrics.Precision(name='precision'),
      keras.metrics.Recall(name='recall'),
      keras.metrics.AUC(name='auc'),
      keras.metrics.AUC(name='prc', curve='PR'), # precision-recall curve
]

# 派生为带分段线性学习率的优化器。
# 其中name参数可选，但最好填入，以区分不同的派生优化器。
AdamLR = extend_with_piecewise_linear_lr(Adam, name='AdamLR')

model.compile(
#     loss='sparse_categorical_crossentropy',
    loss='binary_crossentropy',
    optimizer=Adam(1e-5),  # 用足够小的学习率
#     optimizer=AdamLR(learning_rate=1e-4, lr_schedule={
#         1000: 1,
#         2000: 0.1
#     }),
    metrics=METRICS,
)

# 转换数据集
train_generator = data_generator(train_data, batch_size)
valid_generator = data_generator(valid_data, batch_size)
test_generator = data_generator(test_data, batch_size)

# 基于PRF1的evaluate
def evaluate(data):
    tp, tn, fp, fn = 0, 0, 0, 0
    for x_true, y_true in data:
        y_pred = model.predict(x_true).round()
        y_pred = y_pred.reshape(y_pred.shape[0])
        for pred, truth in zip(y_pred, y_true):
            if pred == 1:
                if pred == truth:
                    tp += 1
                else:
                    fp += 1
            elif pred == 0:
                if pred == truth:
                    tn += 1
                else:
                    fn += 1
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1 = 2*precision/(precision+recall) if precision+recall > 0 else 0
    return f1, precision, recall
                
class Evaluator(keras.callbacks.Callback):
    """评估与保存
    """
    def __init__(self):
        self.best_val_recall = 0.

    def on_epoch_end(self, epoch, logs=None):
        f1, precision, recall = evaluate(valid_generator)
        if recall > self.best_val_recall:
            self.best_val_recall = recall
            model.save_weights('model/end2end_model/best_model.weights')
        print(
            'valid:  f1: %.5f, precision: %.5f, recall: %.5f, best recall: %.5f\n' %
            (f1, precision, recall, self.best_val_recall)
        )
        f1, precision, recall = evaluate(test_generator)
        print(
            'test:  f1: %.5f, precision: %.5f, recall: %.5f\n' %
            (f1, precision, recall)
        )


# 制作早停callbacks
early_stopping = tf.keras.callbacks.EarlyStopping(
    monitor='val_prc', 
    verbose=1,
    patience=10,
    mode='max',
    restore_best_weights=True)

# 制作valid data
valid_token_ids, valid_segment_ids, valid_labels = [], [], []
for text, label in valid_data:
    token_ids, segment_ids = tokenizer.encode(text[-510:], maxlen=maxlen)
    valid_token_ids.append(token_ids)
    valid_segment_ids.append(segment_ids)
    valid_labels.append([label])
valid_token_ids = sequence_padding(valid_token_ids)
valid_segment_ids = sequence_padding(valid_segment_ids)
valid_labels = sequence_padding(valid_labels)
valid_x = [valid_token_ids, valid_segment_ids]
valid_y = valid_labels
print(np.array(valid_x).shape, np.array(valid_y).shape)
输出：(2, 100, 508) (100, 1)

bert_resampled_history = model.fit(
    train_generator.forfit(),
    steps_per_epoch=len(train_generator),
    epochs=3,
#     callbacks=[evaluator]
    callbacks=[early_stopping],
    validation_data=(valid_x, valid_y)
)

model.load_weights('model/end2end_model/best_model.weights')
print(u'final test acc: %05f\n' % (evaluate(test_generator)))
```



## f1 recall precion 代码

```
def evaluate(data):
    tp, tn, fp, fn = 0, 0, 0, 0
    for x_true, y_true in data:
        y_pred = model.predict(x_true).round()
        y_pred = y_pred.reshape(y_pred.shape[0])
        for pred, truth in zip(y_pred, y_true):
            if pred == 1:
                if pred == truth:
                    tp += 1
                else:
                    fp += 1
            elif pred == 0:
                if pred == truth:
                    tn += 1
                else:
                    fn += 1
    precision = tp / (tp + fp) if tp + fp > 0 else 0
    recall = tp / (tp + fn) if tp + fn > 0 else 0
    f1 = 2*precision/(precision+recall) if precision+recall > 0 else 0
    return f1, precision, recall
                

class Evaluator(keras.callbacks.Callback):
    """评估与保存
    """
    def __init__(self):
        self.best_val_recall = 0.

    def on_epoch_end(self, epoch, logs=None):
        f1, precision, recall = evaluate(valid_generator)
        if recall > self.best_val_recall:
            self.best_val_recall = recall
            model.save_weights('model/end2end_model/best_model.weights')
        print(
            'valid:  f1: %.5f, precision: %.5f, recall: %.5f, best recall: %.5f\n' %
            (f1, precision, recall, self.best_val_recall)
        )
        f1, precision, recall = evaluate(test_generator)
        print(
            'test:  f1: %.5f, precision: %.5f, recall: %.5f\n' %
            (f1, precision, recall)
        )

```

可以参考的自定义代码 但是本次运行没有生效

```
import keras.backend as K

# 写法一
def matthews_correlation(y_true, y_pred):
    y_pred_pos = K.round(K.clip(y_pred, 0, 1))
    y_pred_neg = 1 - y_pred_pos

    y_pos = K.round(K.clip(y_true, 0, 1))
    y_neg = 1 - y_pos

    tp = K.sum(y_pos * y_pred_pos)
    tn = K.sum(y_neg * y_pred_neg)

    fp = K.sum(y_neg * y_pred_pos)
    fn = K.sum(y_pos * y_pred_neg)

    numerator = (tp * tn - fp * fn)
    denominator = K.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))

    return numerator / (denominator + K.epsilon())

def cal_base(y_true, y_pred):
    y_pred_positive = K.round(K.clip(y_pred, 0, 1))
    y_pred_negative = 1 - y_pred_positive

    y_positive = K.round(K.clip(y_true, 0, 1))
    y_negative = 1 - y_positive

    TP = K.sum(K.round(K.clip(y_pred, 0, 1)) * K.round(K.clip(y_true, 0, 1)))
    TP = K.sum(y_positive * y_pred_positive)
    TN = K.sum(y_negative * y_pred_negative)

    FP = K.sum(y_negative * y_pred_positive)
    FN = K.sum(y_positive * y_pred_negative)

    return TP, TN, FP, FN

# 写法二
def metric_precision(y_true,y_pred): 
    TP=tf.reduce_sum(y_true*tf.round(y_pred))
    TN=tf.reduce_sum((1-y_true)*(1-tf.round(y_pred)))
    FP=tf.reduce_sum((1-y_true)*tf.round(y_pred))
    FN=tf.reduce_sum(y_true*(1-tf.round(y_pred)))
    precision=TP/(TP+FP)
    return precision

def metric_recall(y_true,y_pred): 
    TP=tf.reduce_sum(y_true*tf.round(y_pred))
    TN=tf.reduce_sum((1-y_true)*(1-tf.round(y_pred)))
    FP=tf.reduce_sum((1-y_true)*tf.round(y_pred))
    FN=tf.reduce_sum(y_true*(1-tf.round(y_pred)))
    recall=TP/(TP+FN)
    return recall

def metric_F1score(y_true,y_pred): 
    TP=tf.reduce_sum(y_true*tf.round(y_pred))
    TN=tf.reduce_sum((1-y_true)*(1-tf.round(y_pred)))
    FP=tf.reduce_sum((1-y_true)*tf.round(y_pred))
    FN=tf.reduce_sum(y_true*(1-tf.round(y_pred)))
    precision=TP/(TP+FP)
    recall=TP/(TP+FN)
    F1score=2*precision*recall/(precision+recall)
    return F1score

# 写法三
def precision(y_true, y_pred):
    # Calculates the precision
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def recall(y_true, y_pred):
    # Calculates the recall
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall
```





## 过采样代码

```
bool_train_labels = char_y_train != 0

pos_features = char_x_train[bool_train_labels]
neg_features = char_x_train[~bool_train_labels]

pos_labels = char_y_train[bool_train_labels]
neg_labels = char_y_train[~bool_train_labels]

ids = np.arange(len(pos_features))
choices = np.random.choice(ids, len(neg_features))

res_pos_features = pos_features[choices]
res_pos_labels = pos_labels[choices]

res_pos_features.shape
```



## 分类时，“其他”类是否需要加入

```
建议不加
然后通过阈值来卡，获得召回
```



## 归一化SKLearn StandardScaler

```
https://blog.csdn.net/wzyaiwl/article/details/90549391
```



## fit和fit_generator的区别

```
https://zhuanlan.zhihu.com/p/165188660

fit只需传入参数batch_size
fit_generator不需要传入batch_size 而需要传入steps_pre_epoch

不同于fit()一次性加载所有的train数据集，遍历一遍就可以作为一轮epoch的结束，generator是可以从给定的数据集中“无限”生成数据的，并且因为一次只加载数据集的一部分（generator就是为了解决数据集过大无法一次性加载到内存的问题），所以他并不知道什么时候才是一轮epoch的结束。同样的，batch_size也没有作为参数传递给fit_generator()，所以必须有机制来判断：(1)什么时候结束一轮epoch (2)batch_size是多少。

这时候steps_per_epoch就顺理成章的出现了。这个参数实际上就是指定了每一轮epoch需要执行多少steps，也就是多少steps，才能认为一轮epoch结束。那么衍生问题就是，一个step是怎么度量？其实就是规定每个step加载多少数据，也就是batch_size。他们的关系如下：

steps_per_epoch=len(x_train)/batch_size

一句话概括，就是对于整个训练数据集，generator要在多少步内完成一轮遍历（epoch），从而也就规定了每步要加载多少数据（batch_size）。

```



## 正则化手段

添加随机噪声这一常规的正则化手段：https://kexue.fm/archives/7466

l1/l2等正则，可参考：

https://mp.weixin.qq.com/s/32tcqdEvHBKaLsnC6_RAlg



## 【好！】文本分类中初始数据获取、数据扩充、异常数据处理办法等

```
https://www.jiqizhixin.com/articles/2019-07-11-8
```



## bert的获得局向量

```
https://blog.csdn.net/weixin_39548832/article/details/112173297

在做文本匹配任务时，通常是将两个句子进行拼接输入，然后将其作为一个二分类任务来微调。拼接方式是[CLS] sent_a [SEP] sent_b。

之所以说这样是不行的，因为模型无法单独获取 sent_a 和 sent_b 的句向量表达。原因在于多头 attention 会把 sent_b 的信息编码到 sent_a 之中，把sent_a 的信息编码到 sent_b 之中，也就是这种做法不适合用来对（question，answer）中的question进行单独编码存储。于是有研究人员自然想到使用 bert 来来搭建孪生网络[1]，如下图所示，使用两个bert分别对sent_a 和 sent_b 进行编码，然后得到句子向量之后计算余弦相似度。


这样训练出来的模型就可以单独对一句话进行向量表达了，比如我要得到sent_a 的向量，那么就把 sent_b 置为空字符串就行，因为不管 sent_b 是什么都不影响模型对 sent_a 的最终表达。然而，这个模型明显太复杂了，平时训练一个 bert 机器就很吃劲了，这还训练两个 bert？而且在推理阶段我们也不能忍受多余的一个bert带来的时间消耗。那么有没有更好的模型呢！？

我们看看 UniLM 模型[2]，它是一个融合 NLU 和 NLG 能力的 Transformer 模型，是微软在2019年5月份提出来。下图是该模型的主体框架。




下文借鉴苏建林大佬的文章中[3]相关内容。UniLM的核心是通过特殊的Attention Mask 机制来赋予模型具有 Seq2Seq 的能力。假如输入是“你想吃啥”，目标句子是“白切鸡”，那 UNILM 将这两个句子拼成一个：[CLS] 你 想 吃 啥 [SEP] 白 切 鸡 [SEP]，然后接如图的Attention Mask：


换句话说，[CLS] 你 想 吃 啥 [SEP]这几个 token 之间是双向的 Attention，而白 切 鸡 [SEP]这几个token则是单向 Attention，从而允许递归地预测白 切 鸡 [SEP]这几个token，所以它具备文本生成能力。


因为UniLM特殊的Attention Mask，所以[CLS] 你 想 吃 啥 [SEP]这6个token 只在它们之间相互做Attention，而跟白 切 鸡 [SEP]完全没关系，这就意味着，尽管后面拼接了白 切 鸡 [SEP]，但这不会影响到前6个编码向量。再说明白一点，那就是前6个编码向量等价于只有[CLS] 你 想 吃 啥 [SEP]时的编码结果，如果[CLS]的向量代表着句向量，那么它就是你 想 吃 啥的句向量，而不是加上白 切 鸡后的句向量。

我们可以看到，虽然UniLM的输入也是两个句子，但是却通过特殊的Attention Mask机制，使得模型能单独得到 sent_a 的向量表达，从而能够使得模型能对所有 question 进行事先编码成向量进行保存，从而使得使用向量进行深层语义相似性检索成为可能。我使用该模型在蚂蚁金服的数据上进行微调后，将测试集中的数据进行了向量编码，然后借助 faiss 向量检索工具进行问句的向量相似性召回，下图展示了召回的效果。
```

## Encoding 层参数共享与不共享

https://github.com/wangle1218/deep_text_matching

由于模型需要对输入的左右两个句子进行建模，因此需要编码器分别对两个句子进行编码，我们可以选择是否共享左右编码器的参数，下面两段代码分别表示不共享与共享的写法。

```
rep_left = keras.layers.Bidirectional(keras.layers.LSTM(
    self._params['lstm_units'],
    return_sequences=True,
    dropout=self._params['dropout_rate']
))(embed_left)
rep_right = keras.layers.Bidirectional(keras.layers.LSTM(
    self._params['lstm_units'],
    return_sequences=True,
    dropout=self._params['dropout_rate']
))(embed_right)
```

```
bilstm = keras.layers.Bidirectional(keras.layers.LSTM(
    self._params['lstm_units'],
    return_sequences=True,
    dropout=self._params['dropout_rate']
))
rep_left = bilstm(embed_left)
rep_right = bilstm(embed_right)
```

不共享参数的情况其实就是分别初始化两个双向LSTM网络，然后分别对左右两个句子进行编码；而共享参数是只初始化一个双向LSTM网络，然后左右句子都使用它来编码。在计算文本相似度这个任务时，从实验中发现共享参数的编码对模型更有帮助，比如 mvlstm和 bimpm 两个模型共享Encoding 层参数比不共享参数准确率要高 7-8个百分点，这两个模型都是使用 rnn 网络做编码器的；而使用cnn 网络做编码器的 arcii 模型共享参数后比不共享参数准确率高2个百分点左右。

## 矩阵乘法 numpy

```
https://blog.csdn.net/u012300744/article/details/80423135

```

## 相似度

```
余弦相似度 sklearn cosine_similarity
https://blog.csdn.net/zhangtingduo/article/details/108565161


```

## 正则表达式：保留中文

```
tmp["asr"] = tmp["asr"].apply(lambda x: re.sub('[^\u4e00-\u9fa5^0-9]+','',x))  # 只保留中文和数字

```



## sklearn train_test_split

```
# https://www.cnblogs.com/Yanjy-OnlyOne/p/11288098.html
'''
random_state：可以为整数、RandomState实例或None，默认为None

①若为None时，每次生成的数据都是随机，可能不一样

②若为整数时，每次生成的数据都相同

stratify：可以为类似数组或None

①若为None时，划分出来的测试集或训练集中，其类标签的比例也是随机的

②若不为None时，划分出来的测试集或训练集中，其类标签的比例同输入的数组中类标签的比例相同，可以用于处理不均衡的数据集

'''
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
```

##  美团场景下MBERT效果最好

```

```

## Keras AUC

```python
# https://blog.csdn.net/xwd18280820053/article/details/78740379

# AUC for a binary classifier
def auc(y_true, y_pred):
    ptas = tf.stack([binary_PTA(y_true,y_pred,k) for k in np.linspace(0, 1, 1000)],axis=0)
    pfas = tf.stack([binary_PFA(y_true,y_pred,k) for k in np.linspace(0, 1, 1000)],axis=0)
    pfas = tf.concat([tf.ones((1,)) ,pfas],axis=0)
    binSizes = -(pfas[1:]-pfas[:-1])
    s = ptas*binSizes
    return K.sum(s, axis=0)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# PFA, prob false alert for binary classifier
def binary_PFA(y_true, y_pred, threshold=K.variable(value=0.5)):
    y_pred = K.cast(y_pred >= threshold, 'float32')
    # N = total number of negative labels
    N = K.sum(1 - y_true)
    # FP = total number of false alerts, alerts from the negative class labels
    FP = K.sum(y_pred - y_pred * y_true)
    return FP/N
#-----------------------------------------------------------------------------------------------------------------------------------------------------
# P_TA prob true alerts for binary classifier
def binary_PTA(y_true, y_pred, threshold=K.variable(value=0.5)):
    y_pred = K.cast(y_pred >= threshold, 'float32')
    # P = total number of positive labels
    P = K.sum(y_true)
    # TP = total number of correct alerts, alerts from the positive class labels
    TP = K.sum(y_pred * y_true)
    return TP/P
 
#接着在模型的compile中设置metrics
#如下例子，我用的是RNN做分类
from keras.models import Sequential
from keras.layers import Dense, Dropout
import keras
from keras.layers import GRU
 


model = Sequential()
model.add(keras.layers.core.Masking(mask_value=0., input_shape=(max_lenth, max_features))) #masking用于变长序列输入
model.add(GRU(units=n_hidden_units,activation='selu',kernel_initializer='orthogonal', recurrent_initializer='orthogonal',
              bias_initializer='zeros', kernel_regularizer=regularizers.l2(0.01), recurrent_regularizer=regularizers.l2(0.01),
              bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None,
              bias_constraint=None, dropout=0.5, recurrent_dropout=0.0, implementation=1, return_sequences=False,
              return_state=False, go_backwards=False, stateful=False, unroll=False))   
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=[auc])  #写入自定义评价函数

接下来就自己作预测了...


方法二：



from sklearn.metrics import roc_auc_score
import keras
class RocAucMetricCallback(keras.callbacks.Callback):
    def __init__(self, predict_batch_size=1024, include_on_batch=False):
        super(RocAucMetricCallback, self).__init__()
        self.predict_batch_size=predict_batch_size
        self.include_on_batch=include_on_batch
 
    def on_batch_begin(self, batch, logs={}):
        pass
 
    def on_batch_end(self, batch, logs={}):
        if(self.include_on_batch):
            logs['roc_auc_val']=float('-inf')
            if(self.validation_data):
                logs['roc_auc_val']=roc_auc_score(self.validation_data[1], 
                                                  self.model.predict(self.validation_data[0],
                                                                     batch_size=self.predict_batch_size))
 
    def on_train_begin(self, logs={}):
        if not ('roc_auc_val' in self.params['metrics']):
            self.params['metrics'].append('roc_auc_val')
 
    def on_train_end(self, logs={}):
        pass
 
    def on_epoch_begin(self, epoch, logs={}):
        pass
 
    def on_epoch_end(self, epoch, logs={}):
        logs['roc_auc_val']=float('-inf')
        if(self.validation_data):
            logs['roc_auc_val']=roc_auc_score(self.validation_data[1], 
                                              self.model.predict(self.validation_data[0],
                                                                 batch_size=self.predict_batch_size))
 
 
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.layers import GRU
import keras
from keras.callbacks import EarlyStopping
from sklearn.metrics import roc_auc_score
from keras import metrics
 
cb = [
    my_callbacks.RocAucMetricCallback(), # include it before EarlyStopping!
    EarlyStopping(monitor='roc_auc_val',patience=300, verbose=2,mode='max')
]
model = Sequential()
model.add(keras.layers.core.Masking(mask_value=0., input_shape=(max_lenth, max_features)))
# model.add(Embedding(input_dim=max_features+1, output_dim=64,mask_zero=True))
model.add(GRU(units=n_hidden_units,activation='selu',kernel_initializer='orthogonal', recurrent_initializer='orthogonal',
              bias_initializer='zeros', kernel_regularizer=regularizers.l2(0.01), recurrent_regularizer=regularizers.l2(0.01),
              bias_regularizer=None, activity_regularizer=None, kernel_constraint=None, recurrent_constraint=None,
              bias_constraint=None, dropout=0.5, recurrent_dropout=0.0, implementation=1, return_sequences=False,
              return_state=False, go_backwards=False, stateful=False, unroll=False))   #input_shape=(max_lenth, max_features),
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))
 
model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=[auc]) #这里就可以写其他评估标准
model.fit(x_train, y_train, batch_size=train_batch_size, epochs=training_iters, verbose=2,
          callbacks=cb,validation_split=0.2,
          shuffle=True, class_weight=None, sample_weight=None, initial_epoch=0)

```

## Keras 自定义loss 这里是类别不均衡的学习互信息

```
# https://spaces.ac.cn/archives/7615

import numpy as np
import keras.backend as K


def categorical_crossentropy_with_prior(y_true, y_pred, tau=1.0):
    """带先验分布的交叉熵
    注：y_pred不用加softmax
    """
    prior = np.array([0.99, 0.01])  # 自己定义好prior，shape为[num_classes]
    log_prior = K.constant(np.log(prior + 1e-8))
    for _ in range(K.ndim(y_pred) - 1):
        log_prior = K.expand_dims(log_prior, 0)
    y_pred = y_pred + tau * log_prior
    return K.categorical_crossentropy(y_true, y_pred, from_logits=True)


def sparse_categorical_crossentropy_with_prior(y_true, y_pred, tau=1.0):
    """带先验分布的稀疏交叉熵
    注：y_pred不用加softmax
    """
    prior = xxxxxx  # 自己定义好prior，shape为[num_classes]
    log_prior = K.constant(np.log(prior + 1e-8))
    for _ in range(K.ndim(y_pred) - 1):
        log_prior = K.expand_dims(log_prior, 0)
    y_pred = y_pred + tau * log_prior
    return K.sparse_categorical_crossentropy(y_true, y_pred, from_logits=True)

```

## keras 多输出add和concate

```
https://blog.csdn.net/LiQingBB/article/details/84935478

add和concat的解释：https://blog.csdn.net/qq_43703185/article/details/105020076
```

## 将函数值域从0,1映射到任何空间

```
https://blog.csdn.net/sdu_hao/article/details/94764405

```



# 项目记录

## 文本纠错

### github资源

```
https://github.com/liushulinle/PLOME/tree/main/finetune_src

https://github.com/shibing624/pycorrector
https://github.com/taishan1994/pytorch_bert_chinese_spell_correction
https://github.com/fushengwuyu/chinese_spelling_correction
https://github.com/iqiyi/FASPell/blob/master/README-CN.md
```



# pycorrector

## 安装

```
1. pip install pycorrector
2. pip install kenlm
3. 下载klm模型，github上面有
20M模型：https://github.com/shibing624/pycorrector/wiki/%E8%AE%AD%E7%BB%83BERT%E6%A8%A1%E5%9E%8B
3G模型：https://deepspeech.bj.bcebos.com/zh_lm/zh_giga.no_cna_cmn.prune01244.klm
4. 放到~/.pycorrector/datasets/zh_giga.no_cna_cmn.prune01244.klm
```



# 知识

## BERT

### vocab.txt中[PAD], [UNK], [CLS], [SEP]

```
token2id(注意 在源文件中全部都是夹着中括号的)
[PAD]: 0 , 
[UNK]: 100, 
[CLS]: 101, 
[SEP]: 102
```

 

## BPE算法与文本正规化Text Normalization

https://www.1024sou.com/article/109591.html



## SBERT

### SBERT中(u,v,|u-v|)为什么用|u-v|的绝对值

```
# http://140.238.201.79/articles/CoSENT%EF%BC%9A%E6%AF%94SentenceBERT%E6%9B%B4%E6%9C%89%E6%95%88%E7%9A%84%E5%8F%A5%E5%90%91%E9%87%8F%E6%96%B9%E6%A1%88_7580084_csdn.html

一般情况下，哪怕负样本对是“困难样本”，总体而言正样本对的字面相似度是大于负样本对的，这样一来，哪怕是对于初始模型，正样本对的差距 总体较小，而负样本对的差距 总体较大，我们可以想象正样本对的 主要分布在一个半径较小的球面附近，而负样本对的 分布在一个半径较大的球面附近，也就是说，初始阶段 本身就有聚类倾向，我们接下来只需要根据标签信息强化这种聚类倾向，使得正样本对的 依然保持更小，负样本对的 保持更大。一个直接的做法就是 后面接一个 Dense 分类器，然而常规的分类器是基于内积的，它没法区分两个分布在不同球面的类别，所以我们加上绝对值变成 ，将球面变为锥形，此时就可以用 Dense 分类层来分类了。这就是笔者认为的 的来源。
```

### SBERT速度快的原因

```
# https://blog.csdn.net/fengxinlinux/article/details/109195762

首先这个快，其实是针对多个句子之间判断相似度而言的，比如我们有10个句子，需要判断这10个句子中两两句子之间的相似度，如果用传统的BERT，我们需要两两句子进行组合，拼接成一个长句子，输入到模型中，然后模型输出相似度。这样组合的话，排列组合C10/2的样本数可是远大于10个的。而用sbert，我们主需要向SBERT中输入10次句子，得的每个句子的embedding，然后利用embedding使用距离函数判断相似度即可。
```



## CoSENT：样本对的对比学习

### 背景

SimCSE基于对比学习的无监督学习表现优秀

但在有监督学习时，需要“(原始句子, 相似句子, 不相似句子)”的三元组数据，不适配句子对的数据集

因此，CoSENT通过修改loss实现了基于句子对的有监督的对比学习方法。



### 各向异性与|u-v|有效性

直接采取BERT生成向量，无法区分“难区分的”的不相似句。（如：我可能爱你，我可能不爱你。 res应趋向于0，实际却趋向于1。）

对比向量u/v之间的相似性时，SentenceBERT在train与inference采用了不一致的方式，但却收获了较好的效果。

原因在于train时采用了concatenate(u, v, |u-v|)，而inference时直接使用 cosine_similarity(u, v)。



#### |u-v|有效性解释

u与v相似时，向量（u-v）应该分布在靠近原点的球面上；

u与v不相似时，向量（u-v）应该分布在远离原点的球面上；

如果需要区分u与v是否相似，则通过将向量（u-v）连接全连接层。

但全连接层无法区分处于两个不同球面的向量。



**因此将 |u-v| 取绝对值，将不同球面的向量压缩在同一正向维度空间，变为一个多维度锥形，此时dense可以更好的学习 u与v 之间的相似性，因此  |u-v| 取绝对值有效。**

#### 各向异性

**什么是各向异性？**

Anisotropy(各向异性) - language models trained with tied input/output embeddings lead to anisotropic word embeddings. 

通俗来说就是在我们熟悉的预训练模型训练过程中会导致word embeddings的各维度的特征表示不一致。导致我们获取的句子级别的特征向量也无法进行直接比较。

https://zhuanlan.zhihu.com/p/369075953

https://blog.csdn.net/weixin_45839693/article/details/116302914

https://www.zhihu.com/question/460991118

通过concatenate(u, v, |u-v|)，在train的过程中将u, v本身也拼接，通过dense进行不断优化，**使得u, v不断远离各向异性的分布。**

因此SentenceBERT可以较好的将模型通过train已有语料而有效应用于未知预料的inference，缓解各向异性问题。



### CoSENT句子对的对比学习

#### loss

上述背景中解释了SimCSE在有监督学习中的受限制，CoSENT则是利用原有loss启发

简单来说，就是如果你希望最终实现si<sj，那么就往log里边加入*e**s**i*−*s**j*一项。https://spaces.ac.cn/archives/8847

在有监督的句子对数据中，我们的数据格式为（句子A，句子B，相似度），因此天然得到排序：相似的句子对的相似度>不相似的句子对的相似度

因此有loss：

*l**o**g*(1+(*i*,*j*)*i**n**p**o**s*,(*k*,*l*)*i**n**n**e**g*∑*e**λ*(*c**o**s*(*u**k*,*u**l*)−*c**o**s*(*u**i*−*u**j*)))

\lambda为温度系数，类似SimCSE中的t

#### 对比学习

可以看到通过有标签的句子对的相似度，使得一个训练样本中是相似的句子对与不相似的句子对之间的对比学习。

但区别于SimCSE的两次dropout在一个batch内不同样本之间的对比学习，SimCSE更优雅，CoSENT则弥补了在有监督学习中句子对的学习方法。

#### 效果

在中文上表现了优秀的有监督学习效果。



### REFs

https://spaces.ac.cn/archives/8847



# chrome

## whta's new

```
chrome://whats-new/
```



# nohup

```
nohup jupyter notebook &
单击回车

查看 nohup.out的日志
在 nohup.out 文件目录下输入        tail -fn 50 nohup.out

如何查看 nohup.out 最后几行的日志
在 nohup.out 文件目录下输入        tail -n 50 nohup.out
```



# 最近TODO

1. 代码上传github git使用
2. debug使用
3. 论文合理性验证 模型合理性验证

4. 小论文
5. 演示dp时 模型直接打开



# 注意

```
词性标注数据集 哪来的 权威吗
```



# 关系表示

```
关系表示
> > abbrev: abbreviation modifier，缩写
> > acomp: adjectival complement，形容词的补充；
> > advcl : adverbial clause modifier，状语从句修饰词
> > advmod: adverbial modifier状语
> > agent: agent，代理，一般有by的时候会出现这个
> > amod: adjectival modifier形容词
> > appos: appositional modifier,同位词
> > attr: attributive，属性
> > aux: auxiliary，非主要动词和助词，如BE,HAVE SHOULD/COULD等到
> > auxpass: passive auxiliary 被动词
> > cc: coordination，并列关系，一般取第一个词
> > ccomp: clausal complement从句补充
> > complm: complementizer，引导从句的词好重聚中的主要动词
> > conj : conjunct，连接两个并列的词。
> > cop: copula。系动词（如be,seem,appear等），（命题主词与谓词间的）连系
> > csubj : clausal subject，从主关系
> > csubjpass: clausal passive subject 主从被动关系
> > dep: dependent依赖关系
> > det: determiner决定词，如冠词等
> > dobj : direct object直接宾语
> > expl: expletive，主要是抓取there
> > infmod: infinitival modifier，动词不定式
> > iobj : indirect object，非直接宾语，也就是所以的间接宾语；
> > mark: marker，主要出现在有“that” or “whether”“because”, “when”,
> > mwe: multi-word expression，多个词的表示
> > neg: negation modifier否定词
> > nn: noun compound modifier名词组合形式
> > npadvmod: noun phrase as adverbial modifier名词作状语
> > nsubj : nominal subject，名词主语
> > nsubjpass: passive nominal subject，被动的名词主语
> > num: numeric modifier，数值修饰
> > number: element of compound number，组合数字
> > parataxis: parataxis: parataxis，并列关系
> > partmod: participial modifier动词形式的修饰
> > pcomp: prepositional complement，介词补充
> > pobj : object of a preposition，介词的宾语
> > poss: possession modifier，所有形式，所有格，所属
> > possessive: possessive modifier，这个表示所有者和那个’S的关系
> > preconj : preconjunct，常常是出现在 “either”, “both”, “neither”的情况下
> > predet: predeterminer，前缀决定，常常是表示所有
> > prep: prepositional modifier
> > prepc: prepositional clausal modifier
> > prt: phrasal verb particle，动词短语
> > punct: punctuation，这个很少见，但是保留下来了，结果当中不会出现这个
> > purpcl : purpose clause modifier，目的从句
> > quantmod: quantifier phrase modifier，数量短语
> > rcmod: relative clause modifier相关关系
> > ref : referent，指示物，指代
> > rel : relative
> > root: root，最重要的词，从它开始，根节点
> > tmod: temporal modifier 时间修饰语
> > xcomp: open clausal complement
> > xsubj : controlling subject 掌控者
> > 中心语为谓词
> > subj — 主语
> > nsubj — 名词性主语（nominal subject） （同步，建设）
> > top — 主题（topic） （是，建筑）
> > npsubj — 被动型主语（nominal passive subject），专指由“被”引导的被动句中的主语，一般是谓词语义上的受事 （称作，镍）
> > csubj — 从句主语（clausal subject），中文不存在
> > xsubj — x主语，一般是一个主语下面含多个从句 （完善，有些）
> > 中心语为谓词或介词
> > obj — 宾语
> > dobj — 直接宾语 （颁布，文件）
> > iobj — 间接宾语（indirect object），基本不存在
> > range — 间接宾语为数量词，又称为与格 （成交，元）
> > pobj — 介词宾语 （根据，要求）
> > lobj — 时间介词 （来，近年）？位置宾语localizer objcet
> > 中心语为谓词
> > comp — 补语
> > ccomp — 从句补语，一般由两个动词构成，中心语引导后一个动词所在的从句(IP) （出现，纳入）
> > xcomp — x从句补语（xclausal complement），不存在
> > acomp — 形容词补语（adjectival complement）
> > tcomp — 时间补语（temporal complement） （遇到，以前）
> > lccomp — 位置补语（localizer complement） （占，以上）
> > — 结果补语（resultative complement）
> > 中心语为名词
> > mod — 修饰语（modifier）
> > pass — 被动修饰（passive）
> > tmod — 时间修饰（temporal modifier）
> > rcmod — 关系从句修饰（relative clause modifier） （问题，遇到）
> > numod — 数量修饰（numeric modifier） （规定，若干）
> > ornmod — 序数修饰（numeric modifier）
> > clf — 类别修饰（classifier modifier） （文件，件）
> > nmod — 复合名词修饰（noun compound modifier） （浦东，上海）
> > amod — 形容词修饰（adjetive modifier） （情况，新）
> > advmod — 副词修饰（adverbial modifier） （做到，基本）
> > vmod — 动词修饰（verb modifier，participle modifier）
> > prnmod — 插入词修饰（parenthetical modifier）
> > neg — 不定修饰（negative modifier） (遇到，不)
> > det — 限定词修饰（determiner modifier） （活动，这些）
> > possm — 所属标记（possessive marker），NP
> > poss — 所属修饰（possessive modifier），NP
> > dvpm — DVP标记（dvp marker），DVP （简单，的）
> > dvpmod — DVP修饰（dvp modifier），DVP （采取，简单）
> > assm — 关联标记（associative marker），DNP （开发，的）
> > assmod — 关联修饰（associative modifier），NP|QP （教训，特区）
> > prep — 介词修饰（prepositional modifier） NP|VP|IP（采取，对）
> > clmod — 从句修饰（clause modifier） （因为，开始）
> > plmod — 介词性地点修饰（prepositional localizer modifier） （在，上）
> > asp — 时态标词（aspect marker） （做到，了）
> > partmod– 分词修饰（participial modifier） 不存在
> > etc — 等关系（etc） （办法，等）
> > 中心语为实词
> > conj — 联合(conjunct)
> > cop — 系动(copula) 双指助动词？？？？
> > cc — 连接(coordination)，指中心词与连词 （开发，与）
> > 其它
> > attr — 属性关系 （是，工程）
> > cordmod– 并列联合动词（coordinated verb compound） （颁布，实行）
> > mmod — 情态动词（modal verb） （得到，能）
> > ba — 把字关系
> > tclaus — 时间从句 （以后，积累）
> > — semantic dependent
> > cpm — 补语化成分（complementizer），一般指“的”引导的CP （振兴，的）
```

https://my.oschina.net/u/4393724/blog/4258422



# MOMO

## 连接服务器 和 软连接

```python
ssh gw1
ssh-agent
ssh-add
ssh bjrw-platform-kube-node-di-gpu004.prod.bjrw.momo.com
sudo su - recommend_molive
cd /data/recommend_molive/
cd wang.chuan/
source /home/recommend_molive/wang.chuan/setup.sh（记得执行）
#source setup.sh(已执行)

# 软连接
ln –s /data/recommend_molive/wang.chuan wang.chuan
```

## git一些操作记录

```
➜  cd 0_Projects
➜  git remote add origin git@git.wemomo.com:wang.chuan_201253/graph_embedding_demo.git
fatal: remote origin already exists.
➜  0_Projects git:(master) ✗ git remote -v
origin	git@git.wemomo.com:wang.chuan_201253/graph_embedding_demo.gi (fetch)
origin	git@git.wemomo.com:wang.chuan_201253/graph_embedding_demo.gi (push)

➜  0_Projects git:(master) ✗ git status
➜  0_Projects git:(master) ✗ git add ../统计学习方法.pdf
➜  0_Projects git:(master) ✗ git status
➜  0_Projects git:(master) ✗ git commit
➜  0_Projects git:(master) ✗ git status
➜  0_Projects git:(master) ✗ git push origin master
```

```
~ ~/.ssh/
➜  .ssh ls
config      id_rsa      id_rsa.pub  known_hosts
➜  .ssh ls -a
.           ..          config      id_rsa      id_rsa.pub  known_hosts
➜  .ssh vi id_rsa.pub
➜  .ssh cd ~
```

# linux操作 查看文件cat 和Vim操作快捷键

```python
wc -lcw filename
cat filename | head(tail) -n 1000

vim
gg顶端
shift+g底端
/+要查找的字符串
```

# VIM

```
:q! 不保留退出
:wq 保留退出

c.NotebookApp.ip='*' #设置访问notebook的ip，*表示所有IP，这里设置ip为都可访问
c.NotebookApp.notebook_dir = '/home/hadoop-mtai/cephfs/data/'#共享目录
c.NotebookApp.password = u'sha1:960e1173565f:79614608d9884021d155c3f34039489357137940' #填写刚刚生成的密文
c.NotebookApp.open_browser = False # 禁止notebook启动时自动打开浏览器(在linux服务器一般都是ssh命令行访问，没有图形界面的。
    所以，启动也没啥用)
c.NotebookApp.port =8082 #指定访问的端口，默认是8899

c.NotebookApp.allow_remote_access = True
```



# ACT服务器连接

## 查看GPU IP

```
cat  /etc/hosts
```



## 配置jupyter 密码1111

```
conda activate chatbot
然后

第一步：
https://blog.csdn.net/z124665532/article/details/109198243
https://blog.csdn.net/langyw98/article/details/79573523

'sha1:0efa8d63ddae:93727fb41e482fd5c0ad7f4d084f0fcc00a73db9'
第二步：
权限错误时 输入：
export XDG_RUNTIME_DIR=""
源自：https://stackoverflow.com/questions/35878178/jupyter-notebook-permission-error

第三步：
如果还有错误  KeyError: 'allow_remote_access'
https://blog.csdn.net/w5688414/article/details/82927564
jupyter都是常规方法配置的，后面发现在配置jupyter_notebook_config.py的时候少加了下面的东西，于是输入

vim ~/.jupyter/jupyter_notebook_config.py  //ubuntu 16.04
添加如下代码行：

c.NotebookApp.allow_remote_access = True

第四步：
输入jupyter notebook
然后成功了
然后就根据cat  /etc/hosts中GPU的IP 比如sugon-gpu-1就是http://192.168.5.181:8008


tmux时  先conda activate chatbot
```

| **窗口大小** | **动态窗口** | **子采样** | **低频词阈值** | **迭代次数** | **负采样\*** |
| ------------ | ------------ | ---------- | -------------- | ------------ | ------------ |
| 5            | 是           | 1e-5       | 10             | 5            | 5            |

## 连接dell

```python
ssh wangc18@219.224.171.201
srun --gres=gpu:1 --pty bash
conda info -e

英文：
data/TF/train.conll  
data/TF/dev.conll
data/TF/test.conll    
data/glove.6B.100d.txt  
train: 39832 sentences, 214 batches, 32 buckets
dev:    1700 sentences,  32 batches, 32 buckets
test:   2416 sentences,  33 batches, 32 buckets

  
中文：
data/ctb/train.ctb51.conll    
data/ctb5_dep/train.ctb51.conll    
data/ctb8_dep/train.ctb51.conll    
   
```

## 连接sugon

```python
srun -p sugon --gres=gpu:1 --pty bash
srun -p sugon --gres=gpu:V100:1 --pty bash
pip3 install xxx -U
# mac传输文件
scp stanford-parser-3.3.0-models.jarr wangc18@192.168.5.201:/home/LAB/wangc1801_graduate

source /home/LAB/anaconda3/etc/profile.d/conda.sh
conda activate
```



# conda新建的虚拟环境但是pip仍是全局的

即 在虚拟环境中不能使用pip list中的包

```python
python -m pip install xxx
# 这样就安装到当前的pip中了

python -m pip list
# 用conda和pip隔离Python环境
```



# conda创建删除复制克隆环境

```python
# Anaconda创建环境：

# 下面是创建python=3.6版本的环境，取名叫py36
conda create -n py36 python=3.6 


# 删除环境（不要乱删啊啊啊）

conda remove -n py36 --all

# 克隆环境
conda info -e  # 查看环境对应的path
conda create -n chuan --clone /workdir/anaconda3/envs/chuang_py36_tf1

# 个别bug的解决如下：
# 在用conda建立虚拟环境后，未指定python版本

conda create -n env_name
conda remove -n env_name --all
出现：PackagesNotFoundError: The following packages are missing from the target environment:

# 采用以下命令即可：

conda env remove -n env_name



#创建一个和原python环境一样的虚拟环境

conda create --name my_env_name --clone root
```



# CUDA版本与CUDNN版本不一致问题

```
https://blog.csdn.net/li57681522/article/details/82491617

报错:
InternalError: cudaGetDevice() failed. Status: CUDA driver version is insufficient for CUDA runtime version

因为tf-gpu安装过程中,conda发现没有cudatoolkit,就自动安装了最新版的,可能与cuda的版本一样,一看确实是的.
cuda=10.0.130
cudatoolkit=10.1.243(x)
于是conda install cudatoolkit==10.0.130
解决！
```



# keras报错 AttributeError: 'str' object has no attribute 'decode'

```
h5py版本不一致导致的，更换即可。

pip install h5py==2.10
```



# jupyter添加不同虚拟环境、查看删除kernel

```
https://blog.csdn.net/qq_38526623/article/details/107297573

[看这个]https://blog.csdn.net/qq_35654046/article/details/106972448

具体步骤：
conda activate chuan
(chuan)conda install nb_conda
(chuan)conda install -n chuan ipykernel



1. jupyter 增加和删除kernel
查看当前 jupyter 中有哪些 kernel
jupyter kernelspec list

2. 删除指定 kernel
jupyter kernelspec remove kernel_name

```



# Dependency Parsing毕设记录

## CTB5.0 feat=tag

```
数据：CTB5.0

数据预处理代码：
https://github.com/hankcs/TreebankPreprocessing

代码：
tmp.py   :添加unk 到embedding中
修改args.file:   exp/ctb8/   exp就是产出

(torch1.3) wangc18@dell-gpu-18:~/01_graduate/biaffine-parser$ python run.py train
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |            10
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb8.0-dep/train.conll
fdev            | data/ctb8.0-dep/dev.conll
ftest           | data/ctb8.0-dep/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |         exp/ctb8
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |      exp/ctb8/fields
model           |      exp/ctb8/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 16083 sentences, 102 batches, 32 buckets
dev:     803 sentences,  32 batches, 32 buckets
test:   1910 sentences,  32 batches, 32 buckets
Create the model
Model(
  (word_embed): Embedding(17542, 300)
  (feat_embed): Embedding(35, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=47, bias_x=True, bias_y=True)
  (pretrained): Embedding(1254554, 300)
)

Epoch 1 / 10:
train: Loss: 1.4581 UAS: 66.53% LAS: 62.26%
dev:   Loss: 1.5046 UAS: 66.94% LAS: 62.03%
test:  Loss: 1.5560 UAS: 66.37% LAS: 61.77%
0:00:24.248933s elapsed

Epoch 2 / 10:
train: Loss: 0.9605 UAS: 77.26% LAS: 74.31%
dev:   Loss: 0.9957 UAS: 77.10% LAS: 74.08%
test:  Loss: 1.0317 UAS: 76.60% LAS: 73.56%
0:00:22.868819s elapsed

Epoch 3 / 10:
train: Loss: 0.8348 UAS: 80.25% LAS: 77.34%
dev:   Loss: 0.9087 UAS: 79.91% LAS: 76.90%
test:  Loss: 0.8987 UAS: 80.08% LAS: 76.93%
0:00:22.820854s elapsed

Epoch 4 / 10:
train: Loss: 0.7128 UAS: 83.12% LAS: 80.40%
dev:   Loss: 0.7849 UAS: 82.75% LAS: 79.81%
test:  Loss: 0.7839 UAS: 82.53% LAS: 79.68%
0:00:22.881911s elapsed

Epoch 5 / 10:
train: Loss: 0.6759 UAS: 83.12% LAS: 80.33%
dev:   Loss: 0.7804 UAS: 82.23% LAS: 79.33%
test:  Loss: 0.7876 UAS: 82.34% LAS: 79.52%
0:00:22.767479s elapsed

Epoch 6 / 10:
train: Loss: 0.5962 UAS: 85.75% LAS: 83.14%
dev:   Loss: 0.6997 UAS: 84.85% LAS: 81.98%
test:  Loss: 0.7208 UAS: 84.91% LAS: 82.19%
0:00:22.818915s elapsed

Epoch 7 / 10:
train: Loss: 0.5916 UAS: 85.84% LAS: 83.46%
dev:   Loss: 0.7110 UAS: 84.92% LAS: 82.37%
test:  Loss: 0.7412 UAS: 84.56% LAS: 82.08%
0:00:23.046129s elapsed

Epoch 8 / 10:
train: Loss: 0.5245 UAS: 87.42% LAS: 85.04%
dev:   Loss: 0.6484 UAS: 85.95% LAS: 83.23%
test:  Loss: 0.6459 UAS: 86.02% LAS: 83.57%
0:00:22.937882s elapsed

Epoch 9 / 10:
train: Loss: 0.5076 UAS: 87.98% LAS: 85.58%
dev:   Loss: 0.6368 UAS: 86.14% LAS: 83.46%
test:  Loss: 0.6292 UAS: 86.25% LAS: 83.77%
0:00:22.765566s elapsed

Epoch 10 / 10:
train: Loss: 0.4754 UAS: 88.57% LAS: 86.19%
dev:   Loss: 0.6399 UAS: 86.68% LAS: 84.02%
test:  Loss: 0.6247 UAS: 86.64% LAS: 84.21%
0:00:22.793197s elapsed

Traceback (most recent call last):
  File "run.py", line 59, in <module>
    cmd(args)
  File "/home/LAB/wangc18/01_graduate/biaffine-parser/parsers/cmds/train.py", line 145, in __call__
    self.model = Model.load(args.model)
  File "/home/LAB/wangc18/01_graduate/biaffine-parser/parsers/model.py", line 121, in load
    state = torch.load(path, map_location=device)
  File "/home/LAB/wangc18/.conda/envs/torch1.3/lib/python3.7/site-packages/torch/serialization.py", line 525, in load
    with _open_file_like(f, 'rb') as opened_file:
  File "/home/LAB/wangc18/.conda/envs/torch1.3/lib/python3.7/site-packages/torch/serialization.py", line 212, in _open_file_like
    return _open_file(name_or_buffer, mode)
  File "/home/LAB/wangc18/.conda/envs/torch1.3/lib/python3.7/site-packages/torch/serialization.py", line 193, in __init__
    super(_open_file, self).__init__(open(name, mode))
FileNotFoundError: [Errno 2] No such file or directory: 'exp/ctb8/model'
(torch1.3) wangc18@dell-gpu-18:~/01_graduate/biaffine-parser$ Connection to 192.168.5.201 closed by remote host.
Connection to 192.168.5.201 closed.
```

## ctb5.0 结果记录  原来文件名是ctb8.0-dep 后来发现错了是ctb5.0

```
(torch1.3) wangc18@sugon-gpu-2:~/01_graduate/biaffine-parser$ python run.py train
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            20
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb8.0-dep/train.conll
fdev            | data/ctb8.0-dep/dev.conll
ftest           | data/ctb8.0-dep/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |         exp/ctb8
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |      exp/ctb8/fields
model           |      exp/ctb8/model
----------------+--------------------------

Run the subcommand in mode train
Without preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 16083 sentences, 102 batches, 32 buckets
dev:     803 sentences,  32 batches, 32 buckets
test:   1910 sentences,  32 batches, 32 buckets
Create the model
Model(
  (word_embed): Embedding(17542, 300)
  (feat_embed): Embedding(35, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=47, bias_x=True, bias_y=True)
  (pretrained): Embedding(1254554, 300)
)

Epoch 1 / 1000:
train: Loss: 1.5091 UAS: 64.69% LAS: 60.26%
dev:   Loss: 1.5542 UAS: 65.14% LAS: 60.17%
test:  Loss: 1.6162 UAS: 64.26% LAS: 59.50%
train log: epoch=1, args.patience=20
0:00:24.540482s elapsed

Epoch 86 / 1000:
train: Loss: 0.1208 UAS: 97.03% LAS: 95.61%
dev:   Loss: 0.5136 UAS: 90.47% LAS: 88.59%
test:  Loss: 0.5162 UAS: 90.42% LAS: 88.63%
train log: epoch=86, args.patience=20
0:00:24.383988s elapsed (saved)

Epoch 106 / 1000:
train: Loss: 0.1003 UAS: 97.63% LAS: 96.33%
dev:   Loss: 0.5094 UAS: 90.51% LAS: 88.51%
test:  Loss: 0.5221 UAS: 90.62% LAS: 88.85%
train log: epoch=106, args.patience=20
0:00:24.245800s elapsed

max score of dev is 88.59% at epoch 86
the score of test at epoch 86 is 88.63%
average time of each epoch is 0:00:24.271650s
0:42:52.794889s elapsed
```

##  CTB8.0 数据处理 treebank2conllu

```python
处理CTB8.0语料为CONLLU
(base)  wangchuan@wangchuandeMacBook-Pro  ~/Downloads/TreebankPreprocessing-master   master  python ctb8.py ./ctb8/ ./
usage: ctb8.py [-h] --ctb CTB --output OUTPUT [--task TASK]
ctb8.py: error: the following arguments are required: --ctb, --output
(base)  ✘ wangchuan@wangchuandeMacBook-Pro  ~/Downloads/TreebankPreprocessing-master   master  python ctb8.py --ctb ./ctb8/ --output ./
Importing to nltk...

Generating ./train.txt
2403 files...
100.00%
55679 sentences.

Generating ./dev.txt
301 files...
100.00%
7920 sentences.

Generating ./test.txt
303 files...
100.00%
7774 sentences.

(base)  ✘ ⚙ wangchuan@wangchuandeMacBook-Pro  ~/Downloads/TreebankPreprocessing-master   master  python tb_to_stanford.py --input ./ctb8_raw --lang cn --output ./
Generating ./train.conllx...
31.41%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
34.86%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
38.33%Correcting error: "他" under PU tag; tag changed to PN: (PU 他)
38.89%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (FRAG PU)
39.93%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
39.95%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
45.26%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
63.56%Correcting error: NN phrasal tag changed to NP: NN
71.07%Correcting error: NN phrasal tag changed to NP: NN
71.14%Correcting error: NN phrasal tag changed to NP: NN
75.40%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU 。)
75.78%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU ）)
83.73%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU ，)
91.78%Correcting error: "tw" under PU tag; tag changed to NN: (PU tw)
92.05%Correcting error: "33" under PU tag; tag changed to CD: (PU 33)
100.00%
Generating ./dev.conllx...
43.19%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (PU －－)
50.27%Correcting error: NN phrasal tag changed to NP: NN
79.81%Correcting error: seriously messed up tree in CTB6: (S (IP (NP (CP (ROOT CP (IP (NP (NN 地方) (NN 当局)) (VP (ADVP (AD 正在)) (VP (VV 组织)))) (DEC 的))) (ADJP (JJ 紧急)) (NP(PU ，) (ADVP (AD 但是)) (PP (P 据) (NP (NN 报道))) (PU ，) (NP (CP (IP (VP (QP (CD １多)) (VP (VA 深)))) (DEC 的)) (NP (NN 大雪))) (VP (PP (P 给) (NP (NN 求援) (NN 工作))) (VP (VVP (IP (VP (ADVP (AD 极)) (VP (VA 大)))) (DEC 的)) (NP (NN 困难))))) (PU 。)))
  Corrected as:                                     (S (IP (NP (CP (IP (NP (NN 地方) (NN 当局)) (VP (ADVP (AD 正在)) (VP (VV 组织)))) (DEC 的)) (ADJP (JJ 紧急)) (NP (NN 求援))) (PU 但是)) (PP (P 据) (NP (NN 报道))) (PU ，) (NP (CP (IP (VP (QP (CD １多)) (VP (VA 深)))) (DEC 的)) (NP (NN 大雪))) (VP (PP (P 给) (NP (NN 求援) (NN 工作))) (VP (VV 造成) (AS 了) (N(AD 极)) (VP (VA 大)))) (DEC 的)) (NP (NN 困难))))) (PU 。)))
94.20%Correcting error: "半穴式" under PU tag; tag changed to NN: (PU 半穴式)
100.00%
Generating ./test.conllx...
37.57%Correcting error: treebank tree is not phrasal; wrapping in FRAG: (FRAG PU)
100.00%

```

## CTB8

### CTB8.0 feat=tag

```python
CTB8.0  feat=tag

Epoch 244 / 500:
train: Loss: 0.1495 UAS: 96.65% LAS: 95.07%
dev:   Loss: 0.4832 UAS: 90.75% LAS: 88.60%
test:  Loss: 0.4840 UAS: 90.76% LAS: 88.70%
train log: epoch=244, args.patience=50
0:00:54.771953s elapsed (saved)

Epoch 294 / 500:
train: Loss: 0.1474 UAS: 96.71% LAS: 95.13%
dev:   Loss: 0.4830 UAS: 90.73% LAS: 88.57%
test:  Loss: 0.4852 UAS: 90.77% LAS: 88.73%
train log: epoch=294, args.patience=50
0:00:54.616164s elapsed

max score of dev is 88.60% at epoch 244
the score of test at epoch 244 is 88.70%
average time of each epoch is 0:00:54.336419s
4:26:14.907178s elapsed
```

```python
$ python run.py train -p -d=0 -f=exp/ctb8/tag --feat=tag --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

ctb8 feat=tag

Epoch 105 / 1000:
train: Loss: 0.1860 UAS: 95.73% LAS: 94.03%
dev:   Loss: 0.4760 UAS: 90.60% LAS: 88.43%
test:  Loss: 0.4705 UAS: 90.70% LAS: 88.65%
0:01:45.664758s elapsed (saved)
```

```python
(torch1.3) wangc18@sugon-gpu-4:~/01_graduate/biaffine-parser$

Epoch 215 / 500:
train: Loss: 0.1511 UAS: 96.60% LAS: 95.01%
dev:   Loss: 0.4800 UAS: 90.74% LAS: 88.61%
test:  Loss: 0.4838 UAS: 90.88% LAS: 88.82%
train log: epoch=215, args.patience=30
0:01:00.061814s elapsed (saved)

max score of dev is 88.61% at epoch 215
the score of test at epoch 215 is 88.82%
average time of each epoch is 0:01:00.029283s
4:05:07.174289s elapsed
```

### CTB8.0 feat=tag patience=100 epochs=50000 ✅

```python
Epoch 491 / 50000:
train: Loss: 0.1456 UAS: 96.75% LAS: 95.18%
dev:   Loss: 0.4793 UAS: 90.74% LAS: 88.61%
test:  Loss: 0.4833 UAS: 90.91% LAS: 88.85%
train log: epoch=491, args.patience=100
0:01:03.167307s elapsed

max score of dev is 88.63% at epoch 391
the score of test at epoch 391 is 88.84%
average time of each epoch is 0:01:02.735351s
8:33:23.057356s elapsed
```



### CTB8.0 feat=bert



```python
(torch1.3) wangc18@sugon-gpu-5:~/01_graduate/biaffine-parser$ python run.py train --feat=bert
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |            500
patience        |            20
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb8_dep/train.conllx
fdev            | data/ctb8_dep/dev.conllx
ftest           | data/ctb8_dep/test.conllx
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |       exp/ctb8/bert
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |           bert
fields          |   exp/ctb8/bert/fields
model           |    exp/ctb8/bert/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(bert): BertField(pad=[PAD], bos=[CLS])
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 55679 sentences, 288 batches, 32 buckets
dev:    7920 sentences,  51 batches, 32 buckets
test:   7774 sentences,  49 batches, 32 buckets
Create the model
Model(
  (word_embed): Embedding(33043, 300)
  (feat_embed): BertEmbedding(n_layers=4, n_out=300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=47, bias_x=True, bias_y=True)
  (pretrained): Embedding(1256918, 300)
)

Epoch 1 / 500:
train: Loss: 1.7618 UAS: 63.78% LAS: 53.17%
dev:   Loss: 1.8322 UAS: 63.45% LAS: 52.70%
test:  Loss: 1.8284 UAS: 63.75% LAS: 52.76%
train log: epoch=1, args.patience=20
0:04:41.635744s elapsed

Epoch 41 / 500:
train: Loss: 0.4181 UAS: 90.98% LAS: 87.01%
dev:   Loss: 0.6811 UAS: 86.36% LAS: 81.55%
test:  Loss: 0.6852 UAS: 86.48% LAS: 81.81%
train log: epoch=41, args.patience=20
0:04:37.304399s elapsed (saved)
```

### CTB8.0 bert

```
Epoch 52 / 500:
train: Loss: 0.3829 UAS: 91.71% LAS: 87.88%
dev:   Loss: 0.6773 UAS: 86.63% LAS: 81.91%
test:  Loss: 0.6820 UAS: 86.74% LAS: 82.13%
train log: epoch=52, args.patience=20
0:04:30.683468s elapsed (saved)

Epoch 195 / 500:
train: Loss: 0.2562 UAS: 94.64% LAS: 91.43%
dev:   Loss: 0.6538 UAS: 87.48% LAS: 83.00%
test:  Loss: 0.6628 UAS: 87.59% LAS: 83.23%
train log: epoch=195, args.patience=20
0:04:30.414569s elapsed (saved)
```

### CTB8.0 feat=char

#### CTB8.0 n_char_embed=50

```python
$ python run.py train -p -d=0 -f=exp/ctb8/char --feat=char --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

# -p 表示要处理数据 如果处理过了就不需要-p
$ python run.py train -d=0 -f=exp/ctb8/char --feat=char --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk


Epoch 484 / 1000:
train: Loss: 0.1457 UAS: 97.32% LAS: 94.90%
dev:   Loss: 0.6772 UAS: 87.92% LAS: 83.65%
test:  Loss: 0.6870 UAS: 88.05% LAS: 83.87%
0:02:29.608617s elapsed

Epoch 485 / 1000:
train: Loss: 0.1457 UAS: 97.32% LAS: 94.90%
dev:   Loss: 0.6771 UAS: 87.92% LAS: 83.65%
test:  Loss: 0.6869 UAS: 88.05% LAS: 83.87%
0:02:31.998006s elapsed
```

#### CTB8.0 n_char_embed=300

```python

```

## CTB5

### feat=tag patience=100

```python
Epoch 321 / 50000:
train: Loss: 0.0339 UAS: 99.41% LAS: 98.75%
dev:   Loss: 0.5824 UAS: 90.58% LAS: 88.75%
test:  Loss: 0.6000 UAS: 90.91% LAS: 89.22%
train log: epoch=321, args.patience=100
0:00:22.463679s elapsed

max score of dev is 88.87% at epoch 221
the score of test at epoch 221 is 89.12%
average time of each epoch is 0:00:22.483686s
2:00:17.263230s elapsed
```



### feat=tag

```python
$ python run.py train -p -d=0 -f=exp/ctb5/tag --feat=tag --ftrain=data/ctb5_dep/train.conll --fdev=data/ctb5_dep/dev.conll --ftest=data/ctb5_dep/test.conll --fembed=data/sgns.merge.char.txt --unk=unk

evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb5_dep/train.conll
fdev            |  data/ctb5_dep/dev.conll
ftest           | data/ctb5_dep/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |       exp/ctb5/tag
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/ctb5/tag/fields
model           |    exp/ctb5/tag/model
----------------+--------------------------

Epoch 341 / 1000:
train: Loss: 0.0336 UAS: 99.42% LAS: 98.79%
dev:   Loss: 0.5639 UAS: 90.53% LAS: 88.69%
test:  Loss: 0.5738 UAS: 90.91% LAS: 89.24%
0:00:40.417331s elapsed

max score of dev is 88.83% at epoch 241
the score of test at epoch 241 is 89.02%
average time of each epoch is 0:00:41.513501s
3:55:56.103878s elapsed
```



### CTB5.0 feat=char

#### CTB5.0 feat=char n_char_embed=50

```
$ python run.py train -p -d=0 -f=exp/ctb5/char --feat=char --ftrain=data/ctb5_dep/train.conll --fdev=data/ctb5_dep/dev.conll --ftest=data/ctb5_dep/test.conll --fembed=data/sgns.merge.char.txt --unk=unk

Epoch 219 / 1000:
train: Loss: 0.0409 UAS: 99.40% LAS: 98.42%
dev:   Loss: 0.8773 UAS: 87.76% LAS: 83.65%
test:  Loss: 0.8979 UAS: 87.56% LAS: 83.65%
0:00:54.170549s elapsed

Epoch 220 / 1000:
train: Loss: 0.0404 UAS: 99.42% LAS: 98.48%
dev:   Loss: 0.8655 UAS: 87.74% LAS: 83.70%
test:  Loss: 0.8949 UAS: 87.63% LAS: 83.71%
0:00:53.632855s elapsed

Epoch 221 / 1000:
train: Loss: 0.0409 UAS: 99.42% LAS: 98.46%
dev:   Loss: 0.8532 UAS: 87.81% LAS: 83.71%
test:  Loss: 0.8899 UAS: 87.56% LAS: 83.60%
0:00:53.037597s elapsed
```

#### CTB5.0 feat=char n_char_embed=300

修改config.ini的n_char_embed=300：

```python
$ python run.py train -p -d=0 -f=exp/ctb5/char_300 --feat=char --ftrain=data/ctb5_dep/train.conll --fdev=data/ctb5_dep/dev.conll --ftest=data/ctb5_dep/test.conll --fembed=data/sgns.merge.char.txt --unk=unk

evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb5_dep/train.conll
fdev            |  data/ctb5_dep/dev.conll
ftest           | data/ctb5_dep/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |     exp/ctb5/char_300
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |           char
fields          | exp/ctb5/char_300/fields
model           |  exp/ctb5/char_300/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data

Epoch 336 / 1000:
train: Loss: 0.0227 UAS: 99.77% LAS: 99.23%
dev:   Loss: 0.9186 UAS: 88.08% LAS: 84.11%
test:  Loss: 0.9674 UAS: 87.89% LAS: 84.09%
0:00:53.671918s elapsed (saved)

Epoch 397 / 1000:
train: Loss: 0.0190 UAS: 99.82% LAS: 99.36%
dev:   Loss: 0.9358 UAS: 87.89% LAS: 83.86%
test:  Loss: 0.9853 UAS: 87.92% LAS: 84.20%
0:00:54.232827s elapsed

Epoch 445 / 1000:
train: Loss: 0.0169 UAS: 99.85% LAS: 99.44%
dev:   Loss: 0.9578 UAS: 87.94% LAS: 83.92%
test:  Loss: 1.0049 UAS: 87.79% LAS: 84.09%
0:00:57.324708s elapsed
```



## CTB51

```python
python run.py train -p -d=0 -f=exp/ctb/tag --feat=tag --ftrain=data/ctb/train.ctb51.conll --fdev=data/ctb/dev.ctb51.conll --ftest=data/ctb/test.ctb51.conll --fembed=data/sgns.merge.char.txt --unk=unk
```



### feat=tag patience=100 epoch=50000

```
(base) drose@ubuntu:~/jupyter/0001_graduate/biaffine-parser$ python run.py train -p -d=0 -f=exp/ctb/tag --feat=tag --ftrain=data/ctb/train.ctb51.conll --fdev=data/ctb/dev.ctb51.conll --ftest=data/ctb/test.ctb51.conll --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           50000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          | data/ctb/train.ctb51.conll
fdev            | data/ctb/dev.ctb51.conll
ftest           | data/ctb/test.ctb51.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/ctb/tag
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/ctb/tag/fields
model           |     exp/ctb/tag/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 16085 sentences, 100 batches, 32 buckets
dev:     803 sentences,  32 batches, 32 buckets
test:   1910 sentences,  32 batches, 32 buckets
Create the model
Model(
  (word_embed): Embedding(17502, 300)
  (feat_embed): Embedding(33, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=13, bias_x=True, bias_y=True)
  (pretrained): Embedding(1254552, 300)
)

Epoch 1 / 50000:
train: Loss: 1.4999 UAS: 60.48% LAS: 57.44%
dev:   Loss: 1.5679 UAS: 60.38% LAS: 57.06%
test:  Loss: 1.7229 UAS: 60.74% LAS: 57.47%
0:00:32.843606s elapsed

Epoch 553 / 50000:
train: Loss: 0.0133 UAS: 99.76% LAS: 99.60%
dev:   Loss: 0.6274 UAS: 90.39% LAS: 89.22%
test:  Loss: 0.6730 UAS: 90.74% LAS: 89.49%
0:00:31.673905s elapsed

max score of dev is 89.38% at epoch 453
the score of test at epoch 453 is 89.48%
average time of each epoch is 0:00:31.215098s
4:47:41.949275s elapsed
```



### feat=tag patience=100

```python
Epoch 369 / 50000:
train: Loss: 0.0187 UAS: 99.63% LAS: 99.40%
dev:   Loss: 0.5800 UAS: 90.46% LAS: 89.27%
test:  Loss: 0.6214 UAS: 90.85% LAS: 89.58%
train log: epoch=369, args.patience=100
0:00:23.626916s elapsed

max score of dev is 89.45% at epoch 269
the score of test at epoch 269 is 89.51%
average time of each epoch is 0:00:23.634424s
2:25:21.102284s elapsed
```



### PREDICT

```
python run.py predict -d=0 -f=exp/ctb/tag --tree --fdata=data/ctb/check.conll --fpred=checkpred.conll

23*14
试用期80%
12%
全额五险一金
17餐补 300交通补助
宿舍+班车+餐汀
双人间960 双人套件1440 单人间1920
9.30-16.30 每天9小时
三年合同 最长6个月试用期 一般3个月试用期
违约金3000
会有出差 但比较少
户口可能解决 SP全部解决 白菜部分 目前是白菜

```



## HIT

### feat=tag

```
(torch1.3) wangc18@sugon-gpu-5:~/01_graduate/biaffine-parser$ python run.py train -d=0 -f=exp/HIT/tag --feat=tag --ftrain=data/HIT/train.conll --fdev=data/HIT/dev.conll --ftest=data/HIT/test.conll --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |            500
patience        |            30
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          |   data/HIT/train.conll
fdev            |    data/HIT/dev.conll
ftest           |    data/HIT/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/HIT/tag
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/HIT/tag/fields
model           |     exp/HIT/tag/model
----------------+--------------------------

Run the subcommand in mode train
Without preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train:  4480 sentences,  40 batches, 32 buckets
dev:     534 sentences,  32 batches, 32 buckets
test:    534 sentences,  32 batches, 32 buckets

Epoch 215 / 500:
train: Loss: 0.2135 UAS: 98.31% LAS: 88.68%
dev:   Loss: 1.2953 UAS: 86.17% LAS: 67.09%
test:  Loss: 1.3316 UAS: 86.17% LAS: 67.09%
train log: epoch=215, args.patience=30
0:00:11.169364s elapsed

max score of dev is 67.58% at epoch 185
the score of test at epoch 185 is 67.58%
average time of each epoch is 0:00:11.201405s
0:40:08.302058s elapsed
```

## THU

### feat=tag

```
python run.py train -p -d=0 -f=exp/THU/tag --feat=tag --bucket=16 --ftrain=data/THU/train.conllx --fdev=data/THU/dev.conllx --ftest=data/THU/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

(torch1.3) wangc18@sugon-gpu-5:~/01_graduate/biaffine-parser$ python run.py train -d=0 -f=exp/THU/tag --feat=tag --bucket=16 --ftrain=data/THU/train.conllx --fdev=data/THU/dev.conllx --ftest=data/THU/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |            500
patience        |            30
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            16
punct           |           False
ftrain          |   data/THU/train.conllx
fdev            |    data/THU/dev.conllx
ftest           |   data/THU/test.conllx
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/THU/tag
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/THU/tag/fields
model           |     exp/THU/tag/model
----------------+--------------------------

Run the subcommand in mode train
Without preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 20000 sentences,  45 batches, 16 buckets
dev:    2000 sentences,  16 batches, 16 buckets
test:   2000 sentences,  16 batches, 16 buckets

# patience=30
Epoch 160 / 500:
train: Loss: 0.1009 UAS: 99.14% LAS: 96.41%
dev:   Loss: 0.8974 UAS: 87.29% LAS: 79.67%
test:  Loss: 0.9495 UAS: 87.29% LAS: 79.67%
train log: epoch=160, args.patience=30
0:00:05.693064s elapsed

max score of dev is 80.08% at epoch 130
the score of test at epoch 130 is 80.08%
average time of each epoch is 0:00:05.733544s
0:15:17.367052s elapsed

# patience=100
Epoch 230 / 50000:
train: Loss: 0.0627 UAS: 99.56% LAS: 97.87%
dev:   Loss: 0.9599 UAS: 87.22% LAS: 79.75%
test:  Loss: 1.0445 UAS: 87.22% LAS: 79.75%
train log: epoch=230, args.patience=100
0:00:05.724180s elapsed

max score of dev is 80.08% at epoch 130
the score of test at epoch 130 is 80.08%
average time of each epoch is 0:00:05.732417s
0:21:58.455809s elapsed
```

## 补充数据集 

http://nlp.nju.edu.cn/tanggc/tools/DependencyViewer.html



## 训练

### feat=tag

```python
$ python run.py train -p -d=0 -f=exp/ctb8/tag --feat=tag --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

# -p 表示要处理数据 如果处理过了就不需要-p
$ python run.py train -d=0 -f=exp/ctb8/tag --feat=tag --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

python run.py train -d=0 -f=exp/ctb5/tag --feat=tag --ftrain=data/ctb5_dep/train.conll --fdev=data/ctb5_dep/dev.conll --ftest=data/ctb5_dep/test.conll --fembed=data/sgns.merge.char.txt --unk=unk

python run.py train -d=0 -f=exp/ctb/tag/patience=100,epochs=50000 --feat=tag --ftrain=data/ctb/train.ctb51.conll --fdev=data/ctb/dev.ctb51.conll --ftest=data/ctb/test.ctb51.conll --fembed=data/sgns.merge.char.txt --unk=unk

```

### feat=char

```python
$ python run.py train -p -d=0 -f=exp/ctb8/char --feat=char --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

# -p 表示要处理数据 如果处理过了就不需要-p
$ python run.py train -d=0 -f=exp/ctb8/char --feat=char --ftrain=data/ctb8_dep/train.conllx --fdev=data/ctb8_dep/dev.conllx --ftest=data/ctb8_dep/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk


```

### hit feat=tag

```
python run.py train -p -d=0 -f=exp/HIT/tag --feat=tag --ftrain=data/HIT/train.conll --fdev=data/HIT/dev.conll --ftest=data/HIT/test.conll --fembed=data/sgns.merge.char.txt --unk=unk

python run.py train -p -d=0 -f=exp/HIT/tag --feat=tag --ftrain=data/HIT/train.conll --fdev=data/HIT/dev.conll --ftest=data/HIT/test.conll --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          |   data/HIT/train.conll
fdev            |    data/HIT/dev.conll
ftest           |    data/HIT/test.conll
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/hit/tag
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/HIT/tag/fields
model           |     exp/HIT/tag/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data
```

### THU FEAT=TAG

```
python run.py train -p -d=0 -f=exp/THU/tag --feat=tag --bucket=16 --ftrain=data/THU/train.conllx --fdev=data/THU/dev.conllx --ftest=data/THU/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk

(base) drose@ubuntu:~/jupyter/0001_graduate/biaffine-parser$ python run.py train -p -d=0 -f=exp/THU/tag --feat=tag --ftrain=data/THU/train.conllx --fdev=data/THU/dev.conllx --ftest=data/THU/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            32
punct           |           False
ftrain          |   data/THU/train.conllx
fdev            |    data/THU/dev.conllx
ftest           |   data/THU/test.conllx
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/THU/tag
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/THU/tag/fields
model           |     exp/THU/tag/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data

BUG:
Traceback (most recent call last):
  File "run.py", line 60, in <module>
    cmd(args)
  File "/home/LAB/wangc18/01_graduate/biaffine-parser/parsers/cmds/train.py", line 93, in __call__
    train = TextDataset(train, self.fields, args.buckets)
  File "/home/LAB/wangc18/01_graduate/biaffine-parser/parsers/utils/data.py", line 48, in __init__
    self.buckets = dict(zip(*kmeans(self.lengths, n_buckets)))
  File "/home/LAB/wangc18/01_graduate/biaffine-parser/parsers/utils/alg.py", line 18, in kmeans
    assert len(d) >= k, f"unable to assign {len(d)} datapoints to {k} clusters"
AssertionError: unable to assign 29 datapoints to 32 clusters

DEBUG:
Epoch 289 / 1000:
train: Loss: 0.0437 UAS: 99.75% LAS: 98.60%
dev:   Loss: 0.9884 UAS: 87.26% LAS: 79.75%
test:  Loss: 1.1187 UAS: 87.26% LAS: 79.75%
0:00:08.724237s elapsed

Epoch 290 / 1000:
train: Loss: 0.0435 UAS: 99.76% LAS: 98.63%
dev:   Loss: 0.9840 UAS: 87.28% LAS: 79.66%
test:  Loss: 1.1118 UAS: 87.28% LAS: 79.66%
0:00:08.845598s elapsed

max score of dev is 80.11% at epoch 190
the score of test at epoch 190 is 80.11%
average time of each epoch is 0:00:09.952241s
0:48:06.150021s elapsed
```

```
python run.py train -p -d=0 -f=exp/THU/tag --feat=tag --bucket=16 --ftrain=data/THU/train.conllx_ch --fdev=data/THU/dev.conllx_ch --ftest=data/THU/test.conllx_ch --fembed=data/sgns.merge.char.txt --unk=unk

(torch1.3) wangc18@sugon-gpu-1:~/01_graduate/biaffine-parser$ python run.py train -p -d=0 -f=exp/THU/tag --feat=tag --bucket=16 --ftrain=data/THU/train.conllx --fdev=data/THU/dev.conllx --ftest=data/THU/test.conllx --fembed=data/sgns.merge.char.txt --unk=unk
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            50
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |            500
patience        |            30
min_freq        |             2
fix_len         |            20
mode            |           train
buckets         |            16
punct           |           False
ftrain          |   data/THU/train.conllx
fdev            |    data/THU/dev.conllx
ftest           |   data/THU/test.conllx
fembed          | data/sgns.merge.char.txt
unk             |            unk
conf            |        config.ini
file            |        exp/THU/tag
preprocess      |           True
device          |           cuda
seed            |             1
threads         |            16
tree            |           False
feat            |            tag
fields          |    exp/THU/tag/fields
model           |     exp/THU/tag/model
----------------+--------------------------

Run the subcommand in mode train
Preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
train: 20000 sentences,  45 batches, 16 buckets
dev:    2000 sentences,  16 batches, 16 buckets
test:   2000 sentences,  16 batches, 16 buckets
Create the model
Model(
  (word_embed): Embedding(8514, 300)
  (feat_embed): Embedding(23, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=70, bias_x=True, bias_y=True)
  (pretrained): Embedding(1253068, 300)
)

Epoch 1 / 500:
train: Loss: 3.3971 UAS: 41.25% LAS: 21.38%
dev:   Loss: 3.5255 UAS: 39.40% LAS: 19.79%
test:  Loss: 3.6345 UAS: 39.40% LAS: 19.79%
train log: epoch=1, args.patience=30
0:00:08.491021s elapsed

Epoch 130 / 500:
train: Loss: 0.1290 UAS: 98.77% LAS: 95.39%
dev:   Loss: 0.8616 UAS: 87.14% LAS: 79.79%
test:  Loss: 0.9224 UAS: 87.14% LAS: 79.79%
train log: epoch=130, args.patience=30
0:00:07.431853s elapsed

max score of dev is 79.79% at epoch 100
the score of test at epoch 100 is 79.79%
average time of each epoch is 0:00:07.342131s
0:15:54.477093s elapsed
```



## predict

```
python run.py predict -d=0 -f=exp/ptb.char --feat=char --tree  \
      --fdata=data/naive.conllx  \
      --fpred=naive.conllx
      
      # 实际如下：
python run.py predict -d=0 --feat=tag



```

### CTB8-TAG

```
# CTB8-TAG
python run.py predict -d=0 -f=exp/ctb8/tag --feat=tag --tree --fdata=check/origin/check.conllx --fpred=check/result/result_ctb8_tag.conllx

python run.py predict -d=0 -f=exp/ctb8/tag --feat=tag --tree --fdata=check/origin/check.conll --fpred=check/result/result.conll
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |          predict
fdata           | check/origin/check.conll
fpred           | check/result/result.conll
conf            |        config.ini
file            |       exp/ctb8/tag
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           True
feat            |            tag
fields          |    exp/ctb8/tag/fields
model           |    exp/ctb8/tag/model
----------------+--------------------------

Run the subcommand in mode predict
Without preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
Load the dataset
5 sentences, 1 batches
Load the model
Model(
  (word_embed): Embedding(33043, 300)
  (feat_embed): Embedding(37, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=47, bias_x=True, bias_y=True)
  (pretrained): Embedding(1256918, 300)
)

Make predictions on the dataset
Save the predicted result to check/result/result.conll
0:00:01.018958s elapsed, 4.91 Sents/s

```

```
# 树结构
python run.py predict -d=0 -f=exp/ctb8/tag --feat=tag --tree --fdata=check/origin/check.conllx --fpred=check/result/result_ctb8_tag_tree.conllx
python run.py predict -d=0 -f=exp/ctb5/tag --feat=tag --tree --fdata=check/origin/check.conllx --fpred=check/result/result_ctb5_tag_tree.conllx

# 非树结构
python run.py predict -d=0 -f=exp/ctb8/tag --feat=tag --fdata=check/origin/check.conllx --fpred=check/result/result_ctb8_tag.conllx
python run.py predict -d=0 -f=exp/ctb5/tag --feat=tag --fdata=check/origin/check.conllx --fpred=check/result/result_ctb5_tag.conllx
```



### CTB5-TAG

```
python run.py predict -d=0 -f=exp/ctb5/tag --feat=tag --tree --fdata=check/origin/check.conll --fpred=check/result/result_ctb5_tag.conll

python run.py predict -d=0 -f=exp/ctb5/tag --feat=tag --tree --fdata=check/origin/check.conll --fpred=check/result/result_ctb5_tag.conll
evaluate
Set the max num of threads to 16
Set the seed for generating random numbers to 1
Set the device with ID 0 visible
Override the default configs with parsed arguments
----------------+--------------------------
Param           |           Value
----------------+--------------------------
bert_model      |      bert-base-cased
n_embed         |            300
n_char_embed    |            300
n_bert_layers   |             4
embed_dropout   |           0.33
n_lstm_hidden   |            400
n_lstm_layers   |             3
lstm_dropout    |           0.33
n_mlp_arc       |            500
n_mlp_rel       |            100
mlp_dropout     |           0.33
lr              |           0.002
mu              |            0.9
nu              |            0.9
epsilon         |           1e-12
clip            |            5.0
decay           |           0.75
decay_steps     |           5000
batch_size      |           5000
epochs          |           1000
patience        |            100
min_freq        |             2
fix_len         |            20
mode            |          predict
fdata           | check/origin/check.conll
fpred           | check/result/result_ctb5_tag.conll
conf            |        config.ini
file            |       exp/ctb5/tag
preprocess      |           False
device          |           cuda
seed            |             1
threads         |            16
tree            |           True
feat            |            tag
fields          |    exp/ctb5/tag/fields
model           |    exp/ctb5/tag/model
----------------+--------------------------

Run the subcommand in mode predict
Without preprocess the data
(words): Field(pad=<pad>, unk=<unk>, bos=<bos>, lower=True)
(tags): Field(bos=<bos>)
(heads): Field(bos=<bos>, use_vocab=False)
(rels): Field(bos=<bos>)
Load the dataset
5 sentences, 1 batches
Load the model
Model(
  (word_embed): Embedding(17542, 300)
  (feat_embed): Embedding(35, 300)
  (embed_dropout): IndependentDropout(p=0.33)
  (lstm): BiLSTM(600, 400, num_layers=3, dropout=0.33)
  (lstm_dropout): SharedDropout(p=0.33, batch_first=True)
  (mlp_arc_h): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_arc_d): MLP(
    (linear): Linear(in_features=800, out_features=500, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_h): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (mlp_rel_d): MLP(
    (linear): Linear(in_features=800, out_features=100, bias=True)
    (activation): LeakyReLU(negative_slope=0.1)
    (dropout): SharedDropout(p=0.33, batch_first=True)
  )
  (arc_attn): Biaffine(n_in=500, n_out=1, bias_x=True)
  (rel_attn): Biaffine(n_in=100, n_out=47, bias_x=True, bias_y=True)
  (pretrained): Embedding(1254554, 300)
)

Make predictions on the dataset
Save the predicted result to check/result/result_ctb5_tag.conll
0:00:01.011317s elapsed, 4.94 Sents/s
```

### HIT-TAG

```
python run.py predict -d=0 -f=exp/HIT/tag --feat=tag --tree --fdata=check/origin/check.conllx --fpred=check/result/result_HIT_tag.conllx
```

#### THU-TAG

```
python run.py predict -d=0 -f=exp/THU/tag --feat=tag --tree --fdata=check/origin/check.conllx --fpred=check/result/result_THU_tag.conllx
```



# POS

## RoBERTa 12层

```python
Transformer-11-FeedForward-Norm (None, None, 1024)   2048        Transformer-11-FeedForward-Add[0]
__________________________________________________________________________________________________
bidirectional_1 (Bidirectional) (None, None, 256)    1180672     Transformer-11-FeedForward-Norm[0
__________________________________________________________________________________________________
dropout_1 (Dropout)             (None, None, 256)    0           bidirectional_1[0][0]
__________________________________________________________________________________________________
dense_145 (Dense)               (None, None, 91)     23387       dropout_1[0][0]
__________________________________________________________________________________________________
conditional_random_field_1 (Con (None, None, 91)     8281        dense_145[0][0]
==================================================================================================
Total params: 174,530,484
Trainable params: 174,530,484
Non-trainable params: 0
__________________________________________________________________________________________________
WARNING:tensorflow:From /home/LAB/wangc18/.local/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

Epoch 1/5
2021-03-25 20:22:17.908996: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10
2305/2305 [==============================] - 1743s 756ms/step - loss: 14.3888 - sparse_accuracy: 0.8308
[[-0.8398175  -2.9562573  -2.6101131  ... -1.7061106  -1.1136358
  -0.84707165]
 [-2.532334   -0.8596185  -0.9279335  ... -1.8495795  -1.5365251
  -2.8290594 ]
 [-2.6038847  -0.88541853 -0.8860897  ... -1.9843099  -1.4814205
  -2.583396  ]
 ...
 [-0.5298114  -2.274083   -1.8396348  ... -2.8286846  -0.3838133
   0.14281662]
 [-1.2168766  -1.9145058  -1.7840377  ... -2.8499262  -1.8868415
  -1.0301656 ]
 [-0.22328676 -2.5767722  -2.7059865  ... -0.38473377  0.20037197
   0.37794283]]
100%|███████████████████████████████████████| 7875/7875 [05:00<00:00, 26.20it/s]
valid:  f1: 0.92746, precision: 0.92818, recall: 0.92675, best f1: 0.92746

100%|███████████████████████████████████████| 7741/7741 [04:52<00:00, 26.44it/s]
test:  f1: 0.92635, precision: 0.92642, recall: 0.92628

Epoch 2/5
2305/2305 [==============================] - 1726s 749ms/step - loss: 4.3073 - sparse_accuracy: 0.9023
[[-0.7212448  -3.555844   -3.161266   ... -1.8298198  -1.2496753
  -0.59902734]
 [-3.0409222  -0.8930837  -0.9670407  ... -2.33439    -2.0354953
  -3.3746543 ]
 [-3.1224036  -0.91805005 -0.9265153  ... -2.4630024  -1.9829178
  -3.0997999 ]
 ...
 [-0.6661172  -2.7736888  -2.3442333  ... -2.8972037  -0.1594657
   0.16783284]
 [-1.6943111  -2.475818   -2.409404   ... -3.1027737  -1.8989507
  -1.1340806 ]
 [-0.21881412 -3.1092916  -3.2873428  ... -0.4667868   0.08857843
   0.60842854]]
100%|███████████████████████████████████████| 7875/7875 [05:02<00:00, 26.00it/s]
valid:  f1: 0.93429, precision: 0.93510, recall: 0.93349, best f1: 0.93429

100%|███████████████████████████████████████| 7741/7741 [04:57<00:00, 25.98it/s]
test:  f1: 0.93320, precision: 0.93336, recall: 0.93304

Epoch 3/5
2305/2305 [==============================] - 1729s 750ms/step - loss: 3.2248 - sparse_accuracy: 0.9166
[[-1.0208043  -4.0884624  -3.6785862  ... -1.9253261  -1.2931827
  -0.78297585]
 [-3.563808   -0.91930425 -1.0003374  ... -2.84626    -2.540501
  -3.8471289 ]
 [-3.6235194  -0.9439945  -0.9614481  ... -2.9304087  -2.4610236
  -3.5513353 ]
 ...
 [-0.6653545  -3.2203782  -2.8327305  ... -2.5774288  -0.6890974
  -0.08779996]
 [-1.6832088  -2.979541   -2.9911754  ... -3.3462317  -1.9341186
  -1.0916276 ]
 [-0.3969101  -3.5427108  -3.7982302  ... -0.36612082 -0.04015524
   0.58335954]]
100%|███████████████████████████████████████| 7875/7875 [04:58<00:00, 26.40it/s]
valid:  f1: 0.93727, precision: 0.93761, recall: 0.93694, best f1: 0.93727

100%|███████████████████████████████████████| 7741/7741 [04:53<00:00, 26.34it/s]
test:  f1: 0.93683, precision: 0.93640, recall: 0.93727

Epoch 4/5
2305/2305 [==============================] - 1728s 750ms/step - loss: 2.4877 - sparse_accuracy: 0.9285
[[-1.2077148  -4.6350636  -4.2131324  ... -2.4547737  -1.3806995
  -0.73351985]
 [-4.1843686  -0.9493752  -1.0374194  ... -3.4312336  -3.119289
  -4.396908  ]
 [-4.1334763  -0.9705453  -0.99602526 ... -3.435885   -2.9529157
  -3.997279  ]
 ...
 [-0.9601038  -3.7004826  -3.3472266  ... -3.0150266  -0.5596351
   0.13186549]
 [-1.6050283  -3.4999244  -3.5563774  ... -3.5859115  -1.7356389
  -1.4418731 ]
 [-0.44355267 -4.0007505  -4.2737484  ... -0.34953827 -0.09541524
   0.6234355 ]]
100%|███████████████████████████████████████| 7875/7875 [05:01<00:00, 26.11it/s]
valid:  f1: 0.93757, precision: 0.93758, recall: 0.93756, best f1: 0.93757

100%|███████████████████████████████████████| 7741/7741 [04:58<00:00, 25.94it/s]
test:  f1: 0.93727, precision: 0.93645, recall: 0.93809

Epoch 5/5
2305/2305 [==============================] - 1731s 751ms/step - loss: 1.9147 - sparse_accuracy: 0.9383
[[-1.297097   -5.1409526  -4.766965   ... -2.2095013  -1.5065309
  -0.9117031 ]
 [-4.8982515  -0.9826147  -1.0815073  ... -4.114712   -3.8238027
  -5.030411  ]
 [-4.6700244  -0.9983401  -1.0330135  ... -3.9559636  -3.4916673
  -4.471005  ]
 ...
 [-0.9186603  -4.1615324  -3.8458512  ... -3.2203176  -0.8110306
   0.2347301 ]
 [-1.7550335  -3.9860597  -4.117471   ... -3.846619   -1.703564
  -1.4013345 ]
 [-0.62499654 -4.4282947  -4.7574472  ... -0.5872244   0.05935174
   0.6125496 ]]
100%|███████████████████████████████████████| 7875/7875 [05:01<00:00, 26.15it/s]
valid:  f1: 0.93803, precision: 0.93754, recall: 0.93852, best f1: 0.93803

100%|███████████████████████████████████████| 7741/7741 [04:56<00:00, 26.08it/s]
test:  f1: 0.93768, precision: 0.93632, recall: 0.93905

Epoch 20/20
2305/2305 [==============================] - 1747s 758ms/step - loss: 0.1225 - sparse_accuracy: 0.9840
[[ -3.2695057  -13.457734   -11.451238   ...  -3.522724    -3.1877246
   -1.8395756 ]
 [-17.306313    -6.4877534   -4.4661984  ... -15.303897   -14.462513
  -16.084755  ]
 [-14.554267    -2.9686952   -2.851505   ... -12.250205   -11.699487
  -12.725654  ]
 ...
 [ -1.5487769  -11.778606    -9.9925165  ...  -4.084093    -0.9679436
   -0.5043607 ]
 [ -2.967956   -10.472299    -9.826692   ...  -4.3876376   -2.706433
   -1.8629463 ]
 [ -1.9889965  -12.909898   -11.274801   ...  -1.5527765   -0.70885223
   -0.48904878]]
100%|███████████████████████████████████████| 7875/7875 [05:04<00:00, 25.85it/s]
valid:  f1: 0.93818, precision: 0.93837, recall: 0.93799, best f1: 0.93829

100%|███████████████████████████████████████| 7741/7741 [04:59<00:00, 25.83it/s]
test:  f1: 0.93863, precision: 0.93830, recall: 0.93895
```



# 多卡训练

https://www.tensorflow.org/tutorials/distribute/keras

/home/LAB/wangc18/01_graduate/chatbot/unilm-chatbot 这个代码是多卡训练  有bug。。。



# chatbot

## UniLM

前5个epoch -> loss: 3.1113



后来集群的卡申请时间到了 就加载模型继续训练了

所以下面这个1 实际上是1+5=6   6/30 Epoch



### 训练记录

Epoch 1/30
2021-03-29 14:42:40.848339: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10
   208/106571 [..............................] - ETA: 16:39:54 - loss: 3.1113

```
Epoch 1/30
2021-03-29 14:42:40.848339: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10
  208/106571 [..............................] - ETA: 16:39:54 - loss: 3.1113

# 目前7epochs了 ： 2021年04月01日15:32:34


   208/106571 [..............................] - ETA: 16:39:54 - loss: 3.1113
426282/426282 [==============================] - 52072s 122ms/step - loss: 3.0555
Epoch 2/30
426282/426282 [==============================] - 52146s 122ms/step - loss: 3.0308
Epoch 3/30
426282/426282 [==============================] - 52506s 123ms/step - loss: 3.0097
Epoch 4/30
426282/426282 [==============================] - 52506s 123ms/step - loss: 2.9917
Epoch 5/30
386605/426282 [==========================>...] - ETA: 1:21:20 - loss: 2.9757srun: Force Terminated job 199580
386606/426282 [==========================>...] - ETA: 1:21:19 - loss: 2.9757srun: Job step aborted: Waiting up to 32 seconds for job step to finish.
386847/426282 [==========================>...] - ETA: 1:20:50 - loss: 2.9757srun: error: dell-gpu-32: task 0: Killed

# 目前11epoch ： 时间： 20210404 loss:2.9917


Epoch 1/30
2021-04-05 15:07:19.036032: I tensorflow/stream_executor/platform/default/dso_loader.cc:42] Successfully opened dynamic library libcublas.so.10

目前12epochs loss:2.9909

13/30:
36930/426282 [=>............................] - ETA: 14:28:21 - loss: 2.9619
```





### 网络结构

```
_________________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==================================================================================================
Input-Token (InputLayer)        (None, None)         0
__________________________________________________________________________________________________
Input-Segment (InputLayer)      (None, None)         0
__________________________________________________________________________________________________
Embedding-Token (Embedding)     multiple             10432512    Input-Token[0][0]
                                                                 MLM-Norm[0][0]
__________________________________________________________________________________________________
Embedding-Segment (Embedding)   (None, None, 768)    1536        Input-Segment[0][0]
__________________________________________________________________________________________________
Embedding-Token-Segment (Add)   (None, None, 768)    0           Embedding-Token[0][0]
                                                                 Embedding-Segment[0][0]
__________________________________________________________________________________________________
Embedding-Position (PositionEmb (None, None, 768)    393216      Embedding-Token-Segment[0][0]
__________________________________________________________________________________________________
Embedding-Norm (LayerNormalizat (None, None, 768)    1536        Embedding-Position[0][0]
__________________________________________________________________________________________________
Embedding-Dropout (Dropout)     (None, None, 768)    0           Embedding-Norm[0][0]
__________________________________________________________________________________________________
Attention-UniLM-Mask (Lambda)   (None, 1, None, None 0           Input-Segment[0][0]
__________________________________________________________________________________________________
Transformer-0-MultiHeadSelfAtte (None, None, 768)    2362368     Embedding-Dropout[0][0]
                                                                 Embedding-Dropout[0][0]
                                                                 Embedding-Dropout[0][0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-0-MultiHeadSelfAtte (None, None, 768)    0           Transformer-0-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-0-MultiHeadSelfAtte (None, None, 768)    0           Embedding-Dropout[0][0]
                                                                 Transformer-0-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-0-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-0-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-0-FeedForward (Feed (None, None, 768)    4722432     Transformer-0-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-0-FeedForward-Dropo (None, None, 768)    0           Transformer-0-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-0-FeedForward-Add ( (None, None, 768)    0           Transformer-0-MultiHeadSelfAttent
                                                                 Transformer-0-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-0-FeedForward-Norm  (None, None, 768)    1536        Transformer-0-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-1-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-0-FeedForward-Norm[0]
                                                                 Transformer-0-FeedForward-Norm[0]
                                                                 Transformer-0-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-1-MultiHeadSelfAtte (None, None, 768)    0           Transformer-1-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-1-MultiHeadSelfAtte (None, None, 768)    0           Transformer-0-FeedForward-Norm[0]
                                                                 Transformer-1-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-1-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-1-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-1-FeedForward (Feed (None, None, 768)    4722432     Transformer-1-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-1-FeedForward-Dropo (None, None, 768)    0           Transformer-1-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-1-FeedForward-Add ( (None, None, 768)    0           Transformer-1-MultiHeadSelfAttent
                                                                 Transformer-1-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-1-FeedForward-Norm  (None, None, 768)    1536        Transformer-1-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-2-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-1-FeedForward-Norm[0]
                                                                 Transformer-1-FeedForward-Norm[0]
                                                                 Transformer-1-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-2-MultiHeadSelfAtte (None, None, 768)    0           Transformer-2-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-2-MultiHeadSelfAtte (None, None, 768)    0           Transformer-1-FeedForward-Norm[0]
                                                                 Transformer-2-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-2-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-2-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-2-FeedForward (Feed (None, None, 768)    4722432     Transformer-2-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-2-FeedForward-Dropo (None, None, 768)    0           Transformer-2-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-2-FeedForward-Add ( (None, None, 768)    0           Transformer-2-MultiHeadSelfAttent
                                                                 Transformer-2-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-2-FeedForward-Norm  (None, None, 768)    1536        Transformer-2-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-3-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-2-FeedForward-Norm[0]
                                                                 Transformer-2-FeedForward-Norm[0]
                                                                 Transformer-2-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-3-MultiHeadSelfAtte (None, None, 768)    0           Transformer-3-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-3-MultiHeadSelfAtte (None, None, 768)    0           Transformer-2-FeedForward-Norm[0]
                                                                 Transformer-3-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-3-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-3-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-3-FeedForward (Feed (None, None, 768)    4722432     Transformer-3-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-3-FeedForward-Dropo (None, None, 768)    0           Transformer-3-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-3-FeedForward-Add ( (None, None, 768)    0           Transformer-3-MultiHeadSelfAttent
                                                                 Transformer-3-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-3-FeedForward-Norm  (None, None, 768)    1536        Transformer-3-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-4-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-3-FeedForward-Norm[0]
                                                                 Transformer-3-FeedForward-Norm[0]
                                                                 Transformer-3-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-4-MultiHeadSelfAtte (None, None, 768)    0           Transformer-4-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-4-MultiHeadSelfAtte (None, None, 768)    0           Transformer-3-FeedForward-Norm[0]
                                                                 Transformer-4-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-4-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-4-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-4-FeedForward (Feed (None, None, 768)    4722432     Transformer-4-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-4-FeedForward-Dropo (None, None, 768)    0           Transformer-4-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-4-FeedForward-Add ( (None, None, 768)    0           Transformer-4-MultiHeadSelfAttent
                                                                 Transformer-4-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-4-FeedForward-Norm  (None, None, 768)    1536        Transformer-4-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-5-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-4-FeedForward-Norm[0]
                                                                 Transformer-4-FeedForward-Norm[0]
                                                                 Transformer-4-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-5-MultiHeadSelfAtte (None, None, 768)    0           Transformer-5-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-5-MultiHeadSelfAtte (None, None, 768)    0           Transformer-4-FeedForward-Norm[0]
                                                                 Transformer-5-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-5-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-5-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-5-FeedForward (Feed (None, None, 768)    4722432     Transformer-5-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-5-FeedForward-Dropo (None, None, 768)    0           Transformer-5-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-5-FeedForward-Add ( (None, None, 768)    0           Transformer-5-MultiHeadSelfAttent
                                                                 Transformer-5-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-5-FeedForward-Norm  (None, None, 768)    1536        Transformer-5-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-6-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-5-FeedForward-Norm[0]
                                                                 Transformer-5-FeedForward-Norm[0]
                                                                 Transformer-5-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-6-MultiHeadSelfAtte (None, None, 768)    0           Transformer-6-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-6-MultiHeadSelfAtte (None, None, 768)    0           Transformer-5-FeedForward-Norm[0]
                                                                 Transformer-6-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-6-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-6-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-6-FeedForward (Feed (None, None, 768)    4722432     Transformer-6-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-6-FeedForward-Dropo (None, None, 768)    0           Transformer-6-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-6-FeedForward-Add ( (None, None, 768)    0           Transformer-6-MultiHeadSelfAttent
                                                                 Transformer-6-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-6-FeedForward-Norm  (None, None, 768)    1536        Transformer-6-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-7-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-6-FeedForward-Norm[0]
                                                                 Transformer-6-FeedForward-Norm[0]
                                                                 Transformer-6-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-7-MultiHeadSelfAtte (None, None, 768)    0           Transformer-7-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-7-MultiHeadSelfAtte (None, None, 768)    0           Transformer-6-FeedForward-Norm[0]
                                                                 Transformer-7-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-7-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-7-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-7-FeedForward (Feed (None, None, 768)    4722432     Transformer-7-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-7-FeedForward-Dropo (None, None, 768)    0           Transformer-7-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-7-FeedForward-Add ( (None, None, 768)    0           Transformer-7-MultiHeadSelfAttent
                                                                 Transformer-7-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-7-FeedForward-Norm  (None, None, 768)    1536        Transformer-7-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-8-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-7-FeedForward-Norm[0]
                                                                 Transformer-7-FeedForward-Norm[0]
                                                                 Transformer-7-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-8-MultiHeadSelfAtte (None, None, 768)    0           Transformer-8-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-8-MultiHeadSelfAtte (None, None, 768)    0           Transformer-7-FeedForward-Norm[0]
                                                                 Transformer-8-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-8-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-8-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-8-FeedForward (Feed (None, None, 768)    4722432     Transformer-8-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-8-FeedForward-Dropo (None, None, 768)    0           Transformer-8-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-8-FeedForward-Add ( (None, None, 768)    0           Transformer-8-MultiHeadSelfAttent
                                                                 Transformer-8-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-8-FeedForward-Norm  (None, None, 768)    1536        Transformer-8-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-9-MultiHeadSelfAtte (None, None, 768)    2362368     Transformer-8-FeedForward-Norm[0]
                                                                 Transformer-8-FeedForward-Norm[0]
                                                                 Transformer-8-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-9-MultiHeadSelfAtte (None, None, 768)    0           Transformer-9-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-9-MultiHeadSelfAtte (None, None, 768)    0           Transformer-8-FeedForward-Norm[0]
                                                                 Transformer-9-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-9-MultiHeadSelfAtte (None, None, 768)    1536        Transformer-9-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-9-FeedForward (Feed (None, None, 768)    4722432     Transformer-9-MultiHeadSelfAttent
__________________________________________________________________________________________________
Transformer-9-FeedForward-Dropo (None, None, 768)    0           Transformer-9-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-9-FeedForward-Add ( (None, None, 768)    0           Transformer-9-MultiHeadSelfAttent
                                                                 Transformer-9-FeedForward-Dropout
__________________________________________________________________________________________________
Transformer-9-FeedForward-Norm  (None, None, 768)    1536        Transformer-9-FeedForward-Add[0][
__________________________________________________________________________________________________
Transformer-10-MultiHeadSelfAtt (None, None, 768)    2362368     Transformer-9-FeedForward-Norm[0]
                                                                 Transformer-9-FeedForward-Norm[0]
                                                                 Transformer-9-FeedForward-Norm[0]
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-10-MultiHeadSelfAtt (None, None, 768)    0           Transformer-10-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-10-MultiHeadSelfAtt (None, None, 768)    0           Transformer-9-FeedForward-Norm[0]
                                                                 Transformer-10-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-10-MultiHeadSelfAtt (None, None, 768)    1536        Transformer-10-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-10-FeedForward (Fee (None, None, 768)    4722432     Transformer-10-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-10-FeedForward-Drop (None, None, 768)    0           Transformer-10-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-10-FeedForward-Add  (None, None, 768)    0           Transformer-10-MultiHeadSelfAtten
                                                                 Transformer-10-FeedForward-Dropou
__________________________________________________________________________________________________
Transformer-10-FeedForward-Norm (None, None, 768)    1536        Transformer-10-FeedForward-Add[0]
__________________________________________________________________________________________________
Transformer-11-MultiHeadSelfAtt (None, None, 768)    2362368     Transformer-10-FeedForward-Norm[0
                                                                 Transformer-10-FeedForward-Norm[0
                                                                 Transformer-10-FeedForward-Norm[0
                                                                 Attention-UniLM-Mask[0][0]
__________________________________________________________________________________________________
Transformer-11-MultiHeadSelfAtt (None, None, 768)    0           Transformer-11-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-11-MultiHeadSelfAtt (None, None, 768)    0           Transformer-10-FeedForward-Norm[0
                                                                 Transformer-11-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-11-MultiHeadSelfAtt (None, None, 768)    1536        Transformer-11-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-11-FeedForward (Fee (None, None, 768)    4722432     Transformer-11-MultiHeadSelfAtten
__________________________________________________________________________________________________
Transformer-11-FeedForward-Drop (None, None, 768)    0           Transformer-11-FeedForward[0][0]
__________________________________________________________________________________________________
Transformer-11-FeedForward-Add  (None, None, 768)    0           Transformer-11-MultiHeadSelfAtten
                                                                 Transformer-11-FeedForward-Dropou
__________________________________________________________________________________________________
Transformer-11-FeedForward-Norm (None, None, 768)    1536        Transformer-11-FeedForward-Add[0]
__________________________________________________________________________________________________
MLM-Dense (Dense)               (None, None, 768)    590592      Transformer-11-FeedForward-Norm[0
__________________________________________________________________________________________________
MLM-Norm (LayerNormalization)   (None, None, 768)    1536        MLM-Dense[0][0]
__________________________________________________________________________________________________
MLM-Bias (BiasAdd)              (None, None, 13584)  13584       Embedding-Token[1][0]
__________________________________________________________________________________________________
MLM-Activation (Activation)     (None, None, 13584)  0           MLM-Bias[0][0]
__________________________________________________________________________________________________
cross_entropy_1 (CrossEntropy)  (None, None, 13584)  0           Input-Token[0][0]
                                                                 Input-Segment[0][0]
                                                                 MLM-Activation[0][0]
==================================================================================================
Total params: 96,488,976
Trainable params: 96,488,976
Non-trainable params: 0
```



## ROUGE指标

https://zhuanlan.zhihu.com/p/108630305



## 人工评价

192.168.2.153:5003

Chatbot1：GPT

Chatbot2：UniLM



## （好）解码方法：非常好的文章，包括集束搜索、随机采样等

https://blog.csdn.net/Kaiyuan_sjtu/article/details/105387819



# 论文搜索

 

```
图 表 x 节 小节 小结
脚注右上角
引用右上角

图 表  布局合理一下
表格框线
```



# 研究生毕设演示

```
srun -p sugon --gres=gpu:1 --pty bash

conda activate chatbot

cd 01_graduate/new_flask/

python app.py
```



# 美团

## 跳板机

```python
#秘钥登陆 https://km.sankuai.com/page/269469752
source ~/.bash_profile
```

## 服务器 Jupyter

```python
ssh wangchuan16@jumper.sankuai.com
ssh hadoop-mtai@zw03-data-hdp-dn-gpu0122.mt -p 4321
(可能会变，在这里：https://km.sankuai.com/page/139872366)
密码mtai123456
jupyter：http://10.137.132.3:8080/tree?
我的目录：http://zw03-data-hdp-dn-gpu0122.mt:8080/tree/wangchuan16
（GPU使用https://km.sankuai.com/page/135843568）
```



# Linux

## Linux修改服务器用户登录的默认目录

```
vim ~/.bashrc
增加下列一行
cd /mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai/users/
然后
source ~/.bashrc
```



## Linux查看文件夹大小并排序

```
# https://blog.csdn.net/jiaobuchong/article/details/50272761

常用的查看文件大小的命令（llm时文件很大，du -h一般不显示，需要用这个）
du -bsh

du -sh * | sort -nr 从小打到
du -s * | sort -nr 从大到小
```



## Linux chmod修改权限

```
RWX:421
https://www.runoob.com/linux/linux-comm-chmod.html

https://www.cnblogs.com/huangjianping/p/8118432.html

文件夹：
chmod -R 777 xxx

WARNING: The repository located at pypi.sankuai.com is not a trusted or secure host and is being ignored. If this repository is available via HTTPS we recommend you use HTTPS instead, otherwise you may silence this warning and allow it anyway with '--trusted-host pypi.sankuai.com'.
```



## Linux 压缩与解压缩

```python
解压.tar.gz
tar -zxvf pythontab.tar.gz


tar命令可以用来压缩打包单文件、多个文件、单个目录、多个目录。
常用格式：
单个文件压缩打包 tar czvf my.tar file1
多个文件压缩打包 tar czvf my.tar file1 file2,...
单个目录压缩打包 tar czvf my.tar dir1
多个目录压缩打包 tar czvf my.tar dir1 dir2
解包至当前目录：tar xzvf my.tar
如果报错则用 tar cvzf my.tar ./

压缩文件夹./每类200/ 到 ./每类200.tar.gz
tar -zcvf ./每类200.tar.gz ./每类200/

将 /home/html/ 这个目录下所有文件和文件夹打包为当前目录下的 html.zip：
zip -q -r html.zip /home/html
unzip file.conf.zip -d /data/bak
```


## Linux 内网传输文件

```
如果需要从本机上传文件到服务器，可以使用nc命令。命令格式为：
1: 在服务器端用 nc -l 44386 | tar xzvf -
2. 在客户端用 tar czvf - someFiles | nc 10.138.206.20 44386
```



## Linux 传输文件

```python
scp  SS.tar drose@192.168.2.153:/home/drose/jupyter/012_projects
  
scp albert_tiny_google_zh_489k.zip wangc18@192.168.5.201:/home/LAB/wangc18
```



## Linux查看文件前几行

```
一、使用cat、tail、head组合

1、查看最后1000行的数据

cat filename | tail -n 1000
2、查看1000到3000行的数据

cat filename | head -n 3000 | tail -n +1000

  1、cat filename 打印文件所有内容
  2、tail -n 1000 打印文件最后1000行的数据
  3、tail -n +1000 打印文件第1000行开始以后的内容
  4、head -n 1000 打印前1000的内容
```



## Linux查看文件大小 and各目录使用

```python
du -h model

df -hl 
```


## Linux查看文件行数

```
使用wc命令 具体通过wc --help 可以查看。

如：wc -l filename 就是查看文件里有多少行

       wc -w filename 看文件里有多少个word。

       wc -L filename 文件里最长的那一行是多少个字。
```



## Linux查看gpu的PID

```
fuser -v /dev/nvidia*

ps aux|grep root|grep python

ps aux|grep python
```



## Linux GPU使用情况定时查看watch -n

```
https://www.cnblogs.com/ftl1012/p/watch.html

https://www.cnblogs.com/a5idc/p/13703865.html

watch -n 3 nvidia-smi

```



## Linux 后台神器TMUX

```
https://blog.csdn.net/luhao19980909/article/details/89718899

tmux new -s jupyter
ctrl b + d

tmux kill-session -t 会话名

上下分屏：
ctrl b + " (shift+')
```



# pycharm快捷键

shift + cmd + o 搜索文件



# 面试

## HR

```python
自己喜欢这个部门和工作  并且干劲满满 有加班的动力
喜欢这个工作和部门
班长：乐于沟通，善于学习
对自己的技术很有信心
应用实际有成就感
```

## PDD

```
链表的快排
```

## 快手

```
自己的简历没有更新 要单独发一下 希望帮忙在系统里面更新一下
```



# LOSS画图 模型画图

https://github.com/soutsios/pos-tagger-bert/blob/master/pos_tagger_bert.ipynb

```
plot_model
```

# biaffine jupyter

```
http://www.cse.chalmers.se/~richajo/nlp2019/l7/Biaffine%20dependency%20parsing.html
http://www.cse.chalmers.se/~richajo/nlp2019/l8/Transition-based%20parsing.html
```



# dp综合论述 和数据

```
https://github.com/NLP-LOVE/Introduction-NLP/blob/master/chapter/12.%E4%BE%9D%E5%AD%98%E5%8F%A5%E6%B3%95%E5%88%86%E6%9E%90.md

```



# dp画图

https://github.com/Unipisa/diaparser

https://blog.csdn.net/jclian91/article/details/97695387

https://github.com/KoichiYasuoka/UniDic2UD



# matplotlib

## 显示中文

```
step1: 下载字体包
https://www.codeleading.com/article/90675494691/
https://blog.csdn.net/Neutionwei/article/details/108311811

step2:找到当前环境的mat包位置
import matplotlib
print(matplotlib.matplotlib_fname())
output:
/workdir/anaconda3/envs/chuan_tf2/lib/python3.7/site-packages/matplotlib/mpl-data/matplotlibrc

step3:复制字体包到该位置
cd /workdir/anaconda3/envs/chuan/lib/python3.7/site-packages/matplotlib/mpl-data/fonts/ttf

cp -a /mnt/dolphinfs/hdd_pool/docker/user/hadoop-mtai/users/wangchuan16/meituan/SimHei.ttf ./

step4:找到mat缓存
import matplotlib
matplotlib.get_cachedir()
output:
'/home/hadoop-mtai/.cache/matplotlib'

step5:删除该缓存
rm -rf /home/hadoop-mtai/.cache/matplotlib

step6:在代码添加中文字体包的代码 即可正常显示
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'SimHei'
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）


```



## 配色方案

```
https://blog.csdn.net/weixin_39617470/article/details/112395015
```



## 饼图仅显示部分标签

```
https://stackoverflow.com/questions/34035427/conditional-removal-of-labels-in-matplotlib-pie-chart/34035864
```



## legend位置调整

```
# https://blog.csdn.net/RobertChenGuangzhi/article/details/49719467

plt.legend(loc='upper center', bbox_to_anchor=(0.6,0.95),ncol=3,fancybox=True,shadow=True)
上面bbox_to_anchor被赋予的二元组中，第一个数值用于控制legend的左右移动，值越大越向右边移动，第二个数值用于控制legend的上下移动，值越大，越向上移动。
```



## title位置调整

```
ax.set_title('发音相似度分桶占比', y=1.12, loc="center")  # y=1.12来设置title的位置，1.12在图例的上方
```



## barh 水平柱状图显示数据百分比

```
# https://stackoverflow.com/questions/52080991/how-to-display-percentage-above-grouped-bar-chart

# 下面这个循环用于注释的方式 显示数据的百分比
    for i, p in enumerate(ax.patches):
        width = p.get_width()
        height = p.get_height()
        x, y = p.get_xy() 
#         print(width, height, x, y, x + width/2, y + height*0.98)
        if i < 5:
            ax.annotate(f'{round(width/54885 * 100, 1)}%', (x + width/2, y + height*0.9), ha='center')
        elif i >= 5:
            ax.annotate(f'{round(width/41064 * 100, 1)}%', (x + width/2, y + height*0.9), ha='center')
    
```



# 纠错pycorrector安装

```
1. pip install pycorrector
2. 安装kenlm
pip install https://github.com/kpu/kenlm/archive/master.zip

如果没有外网，则先下载zip包 然后pip install ./kenlm.zip
```



# pandas

## pandas describe()显示分位数更细粒度

```
pd.DataFrame(history["全部上文"].apply(lambda x: len(x)).describe(percentiles=[0.1*i for i in range(1, 10, 1)]))
```



## pandas apply 用tqdm显示进度：progress_apply

```
#启动对紧跟着的apply过程的监视
from tqdm import tqdm
tqdm.pandas(desc='apply')
data['BMI'] = data.progress_apply(BMI,axis=1)
```



## pandas read_csv的index_col=0：读取保存的index列Unnamed: 0

```
df = pd.read_csv("data/df_processed.csv", index_col=0)

```



## 新建DataFrame

```
test_dict = {'id':[1,2,3,4,5,6],'name':['Alice','Bob','Cindy','Eric','Helen','Grace '],'math':[90,89,99,78,97,93],'english':[89,94,80,94,94,90]}
#[1].直接写入参数test_dict
test_dict_df = pd.DataFrame(test_dict)
#[2].字典型赋值
test_dict_df = pd.DataFrame(data=test_dict)
```



## pandas to_pickle read_pickle：解决存储读写csv后list编程str的问题

```
to_csv 然后 read_csv时会使得某些为list类型的列变为string类型。
使用 to_pickle和read_pickle可解决。
```



## pandas 判断哪些列为空isnull

```
df.isnull().sum()
```



## pandas 修改列名

```
https://blog.csdn.net/weixin_42044037/article/details/81475247

# 两种方法
# 直接修改
df1.columns=['a','B','c']  

# 修改指定列名
chat_cso.rename(columns={'partition_date':'partition_close_date'},inplace=True) 
```



## pandas 删除某列和删除某行

```
https://blog.csdn.net/songyunli1111/article/details/79306639

df.drop(columns=['B', 'C'])
```



## pandas drop_duplicates

```
df_res_agent = df_res_agent.drop_duplicates(["call_id"])
```



## pandas某列为空删除整行

```
# https://zhuanlan.zhihu.com/p/344842290

DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)

参数说明：

axis:
axis=0: 删除包含缺失值的行
axis=1: 删除包含缺失值的列


how: 与axis配合使用
how=‘any’ :只要有缺失值出现，就删除该行货列
how=‘all’: 所有的值都缺失，才删除行或列


thresh： axis中至少有thresh个非缺失值，否则删除。比如 axis=0，thresh=10：标识如果该行中非缺失值的数量小于10，将删除改行
subset: list，在哪些列中查看是否有缺失值
inplace: 是否在原数据上操作。如果为真，返回None否则返回新的copy，去掉了缺失值

>>> data
     d    e    f
a  1.0  6.5  3.0
b  1.0  NaN  NaN
c  NaN  NaN  NaN
d  6.5  3.0  NaN

>>> data.dropna(axis=0,subset=['e'], inplace=True) #axis=0,删除行，subset的列选择
     d    e    f
a  1.0  6.5  3.0
d  6.5  3.0  NaN
```



## pandas指定行列修改值（包括增删改查）

```python
# https://blog.csdn.net/zhangchuang601/article/details/79583551


for idx, wt1, wt2, wt3, wt4 in zip(dz1["callId"], dz1["wentiyi"], dz1["wentier"], 
                                   dz1["wentisan"], dz1["wentisi"]):
    print(dz1.loc[dz1["callId"] == idx, "ansyi"])
    dz1.loc[dz1["callId"] == idx, "ansyi"] = dz1res[0]
    break
dz1.head()

# 需要重置索引
# 重置索引   后续定位方便
df = df.reset_index(drop=True)

for i, (case_id, lifecycle, staff_id, add_time, lz_op, bh_op, op, res, a_d, r_d, d) in enumerate(zip(
        df["case_id"].values, 
        df["lifecycle"].values,
        df["staff_id"].values, 
        df["add_time"].values, 
        df["liuzhuan_ops"].values, 
        df["rejuect_ops"].values,
        df["call后坐席是否流转"].values,
        df["模型分析结果值"].values,
        df["agent_dialogue"].values,
        df["rider_dialogue"].values,
        df["dialogue"].values,
    )):
        simle_flag, complain_flag, prepay_flag = 0, 0, 0
        if op == 0 and res > 0.5:  # 实际没有流转 并且 模型判定需要流转
            if "微笑行动" in d:
                df.loc[i, "模型分析结果值"] = -12.1
```



## pandas read_csv 跳过错误的行

```
https://blog.csdn.net/weixin_39657662/article/details/110054620

pandas.read_csv(filePath,error_bad_lines=False)  # 来忽略掉其中出现错乱(例如，由于逗号导致多出一列)的行。
```



## pandas .where 依据两列的值生成第三列

```
df["dialogue"] = df["text"].where(df["text"] == "", df["speaker_channel"] + ":" + df["text"])
```



## Pandas筛选行：根据两列的值筛选行

```
https://blog.csdn.net/u011675334/article/details/100782022

# 解决率类
def f(x, y):
    if any(i in x for i in ["解决", "一解"]) or any(i in y for i in ["解决率", "一解率"]):
        return True
    return False
df.loc[df.apply(lambda x: f(x["专项名称"], x["专项背景&原因"]), axis=1)]  # 必须要有axis=1
```



## Pandas 依据两列的值生成第三列，同时对两列的数据类型做改变

```
df["key"] = df["case_id"].astype(str) + "-" + df["lifecycle"].astype(str)
df.head(1)
```



## pandas apply

```
df["speaker_channel"] = df["speaker_channel"].apply(lambda x: "骑手:" if x == 1 else "客服:")
df.head()

df["dialogue"] = df["speaker_channel"] + df["text"]
df.head()
```



## pandas groupby分组，结合apply

## groupby 天坑

```
【正确做法】chat_cso["dialogue"] = chat_cso["case_chat_id"].apply(lambda x: chat_dialogue[x])

【错误做法】chat_cso["dialogue"] = list(chat_dialogue)
=================================================
groupby以后返回的是dict
例如
chat_dialogue = chat_cso.groupby("case_chat_id").apply(lambda x: "\n".join(x["dialogue"].values))

返回的是 k=case_chat_id v=apply完成的内容
case_chat_id
1027887986    2:您好，请问有什么可以帮您？小美会尽力帮您解决的~\n1:超...
1027889154    1:车辆故障扣我的行车卡次数了\n1:嗯，是这个订单\n2:请...

此时不能通过 list该变量完成赋值，因为顺序会变化！！！
比如：chat_cso["dialogue"] = list(chat_dialogue)
这样是完全错误的，虽然不会报错，但是内容会差别特别大！！！

对同一个case_chat_id，所对应的dialogue完全不一致
应该通过字典对应的方式！！！

【正确做法】chat_cso["dialogue"] = chat_cso["case_chat_id"].apply(lambda x: chat_dialogue[x])

【错误做法】chat_cso["dialogue"] = list(chat_dialogue)

惨痛经验！！！
错误方法：！！！
chat_cso["dialogue"] = list(chat_dialogue)
chat_cso.loc[chat_cso["case_id"]==1058658818]["dialogue"].values
输出为：array(['1:你好\n2:亲亲有什么可以帮您的吗？\n1...

正确方法：！！！
chat_cso["dialogue"] = chat_cso["case_chat_id"].apply(lambda x: chat_dialogue[x])
chat_cso.loc[chat_cso["case_id"]==1058658818]["dialogue"].values
输出为：array(['2:亲亲，辛苦您提供一下订单号，小美查询一下。\n1:59501...
```

 

### 按列A分组，然后合并列B的字符串的内容

```python
# 列A=case_id 列B=dialogue

！！！！！ 还原原dataframe
# 因为df = df.groupby('case_id').dialogue.apply(list).apply(lambda x: ",".join(x)).reset_index()之后得到的只会是两列的df，一列为case_id，另一列是dialogue，缺失了原DF中的所有列，因此需要转为values然后填写
dialogue = df.groupby('case_id')["dialogue"].apply(lambda x: x.str.cat(sep=',')).values
    df = df.drop_duplicates(["case_id"])
    df["dialogue"] = dialogue
# 另一种写法
dialogue = df.groupby(group).apply(lambda x: ",".join(x["dialogue"].values))
# 或者
dialogue = df.groupby(group)["dialogue"].apply(lambda x: ",".join(x.values))
    
简要方法
method1：    
df = df.groupby('case_id').dialogue.apply(list).apply(lambda x: ",".join(x)).reset_index()


method2：
https://blog.csdn.net/d1240673769/article/details/106038811/

import pandas as pd

file_name='test.xlsx'

df=pd.read_excel(file_name)
data=df.groupby('id')['skill'].apply(lambda x:x.str.cat(sep=':')).reset_index()
print(data)


```

实例：

```
# https://blog.csdn.net/y15518325965/article/details/79463598
dict_obj = {
    'key1':['a','b','a','b','a','b','a','b'],
    'key2':['one','two','three','one','three','three','two','one'],
    'data1':[5,6,5,2,3,3,2,4],
    'data2':[3,4,5,6,3,5,2,5]
}
t1 = pd.DataFrame(dict_obj)
print(t1)


print("====")
t2 = t1.groupby('key1').sum().add_prefix('sum_')
print(t2)


# * 方法1：merge()函数
#     * 作用是将两个或多个DataFrame对象链接到一起

pd.merge(t1,t2,left_on='key1',right_index=True)
# left_on：指左侧的df，这的DataFrame对象，使用哪一个列名进行链接
# right_index：True 值的是是否使用右侧的t2这个DataFrame对象的索引作为链接 
```



### 按列A分组，分组后按列B的值大小排序

```python
# https://blog.csdn.net/leokingszx/article/details/103774406

tt = hour_count.groupby("hour").apply(lambda x:x.sort_values("count",ascending=False)).reset_index(drop=True)

如果报错某一列already exist，那么就设置参数.reset_index(drop=True)
```



## 将某一列的字符串计算其长度，并获得其统计信息

```
A	B	L
0	上一级给我处理一下到现在也没给我回电	他那个说要发短信给我那个申请退款的我没有收到短信啊	1
1	被教练	这个用户已挂机	1
2	然后准时宝会给您一个满意的回复的这个您可以放心先生	给您回电然后给您一个满意的一个解释可以吗	1
3	微商用户已挂机	睡觉用户已发	1
4	啊啊这个五十元给您补到美团钱包余额您可以提现也可以在美	那个五点一的这个优惠补到咱们账户里面以立减金的方式补到您的账户里面可以吗	1

test["la"] = test["A"].map(lambda x:len(x))
test["lb"] = test["B"].map(lambda x:len(x))
test.describe()
```



## pandas concat合并多个df

```
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
参数含义

objs：Series，DataFrame或Panel对象的序列或映射。如果传递了dict，则排序的键将用作键参数，除非它被传递，在这种情况下，将选择值（见下文）。任何无对象将被静默删除，除非它们都是无，在这种情况下将引发一个ValueError。
axis：{0,1，...}，默认为0。沿着连接的轴。
join：{'inner'，'outer'}，默认为“outer”。如何处理其他轴上的索引。outer为联合和inner为交集。
ignore_index：boolean，default False。如果为True，请不要使用并置轴上的索引值。结果轴将被标记为0，...，n-1。如果要连接其中并置轴没有有意义的索引信息的对象，这将非常有用。注意，其他轴上的索引值在连接中仍然受到尊重。
join_axes：Index对象列表。用于其他n-1轴的特定索引，而不是执行内部/外部设置逻辑。
keys：序列，默认值无。使用传递的键作为最外层构建层次索引。如果为多索引，应该使用元组。
levels：序列列表，默认值无。用于构建MultiIndex的特定级别（唯一值）。否则，它们将从键推断。
names：list，default无。结果层次索引中的级别的名称。
verify_integrity：boolean，default False。检查新连接的轴是否包含重复项。这相对于实际的数据串联可能是非常昂贵的。
copy：boolean，default True。如果为False，请勿不必要地复制数据。
In [1]: df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
   ...:                     'B': ['B0', 'B1', 'B2', 'B3'],
   ...:                     'C': ['C0', 'C1', 'C2', 'C3'],
   ...:                     'D': ['D0', 'D1', 'D2', 'D3']},
   ...:                     index=[0, 1, 2, 3])
   ...: 
 
In [2]: df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
   ...:                     'B': ['B4', 'B5', 'B6', 'B7'],
   ...:                     'C': ['C4', 'C5', 'C6', 'C7'],
   ...:                     'D': ['D4', 'D5', 'D6', 'D7']},
   ...:                      index=[4, 5, 6, 7])
   ...: 
 
In [3]: df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
   ...:                     'B': ['B8', 'B9', 'B10', 'B11'],
   ...:                     'C': ['C8', 'C9', 'C10', 'C11'],
   ...:                     'D': ['D8', 'D9', 'D10', 'D11']},
   ...:                     index=[8, 9, 10, 11])
   ...: 
 
In [4]: frames = [df1, df2, df3]
 
In [5]: result = pd.concat(frames)
```



## pandas判断i行j列的数值是否为nan

```
https://blog.csdn.net/lost0910/article/details/106724566
np.isnan(np.nan)， 返回值为True。
```



## pandas str.startswith删除指定字符开头的内容&删除指定内容的行

```
# 删除订单链接 "{"开头的内容
chat_cso = chat_cso[~chat_cso["message_content"].str.startswith("{")]
```

```
# 删除机器自动发送的内容
chat_cso = chat_cso[chat_cso["contact_type"]!=4]
# tmp = chat_cso[chat_cso['contact_type']==4]  
# chat_cso = chat_cso.drop(tmp.index)
# chat_cso.head()
```



## pandas fillna 填补nan

```
指定列填补nan
values = {"A": 0, "B": 1, "C": 2, "D": 3}
df.fillna(value=values, inplace=True)
    A   B   C   D
0   0.0 2.0 2.0 0
1   3.0 4.0 2.0 1
2   0.0 1.0 2.0 5
3   0.0 3.0 2.0 4

传入inplace=True直接修改原对象：
df1.fillna("#", inplace=True)

不修改：
d = df1.fillna("#")
```



## Pandas 对某一列做字典map

```
frame = pd.DataFrame({'item':['ball', 'mug', 'pen', 'pencil', 'ashtray'],
                      'price':[1, 2, 3, 4, " "]})
frame

	item	price
0	ball	1
1	mug	2
2	pen	3
3	pencil	4
4	ashtray	

dic = {1:"a", 2:"b", 3:"c", " ":"e"}
frame["price"] = frame["price"].map(dic)
frame

	item	price
0	ball	a
1	mug	b
2	pen	c
3	pencil	NaN
4	ashtray	e
```

## pandas显示所有行 所有列

```
# 设置显示全部行，不省略
pd.set_option('display.max_rows',None)
# 设置显示全部列，不省略
pd.set_option('display.max_columns',None)
# 显示数据帧以拉伸页面
pd.set_option('display.expand_frame_repr',None)
# 显示每一格数据的最大内容
pd.set_option('display.max_colwidth',None)
```

## pandas进行数据筛选，选择特定行、列

```python
#使用DataFrame中的loc[]和iloc[]方法选择指定的行和列
import pandas as pd
import numpy as np
from pandas import Series, DataFrame
data = {'H':['后','生','仔'],'S':['young','duty','dream'],'Z':[10,11,12]}
DF = DataFrame(data)
print(DF)
# 使用loc或者iloc时，逗号前面代表行操作，逗号后面代表列操作
#使用loc选择特定的列 
print(DF.loc[:,['H','S']])
#使用iloc选择特定的列
print(DF.iloc[:,[1,2]])


#使用已经转换的数据
tmp['xxxxx变化'] = pd.to_numeric(tmp['xxxxx变化'].astype(float))
#选择tmp中"选择列"大于0.2，小于0.3的数据，并选择  tmp中指定列1,tmp中指定列2
print(tmp[(tmp['选择列']>0.2) & (tmp['选择列']< 0.3)]['tmp中指定列1'，'tmp中指定列2'])
#还可以使用这种方式
print(tmp[tmp['选择列']>0.2][tmp['选择列']< 0.3]['tmp中指定列1'，'tmp中指定列2'])

```

```python
t = tmp["通话ID"].values
t[:2]
array(['07cd28181b944b4aa8f68587fe4d2cbc',
       '1232cc1b110741ee8d02b0426ccbd984'], dtype=object)
       
tt = pd.DataFrame()
for i in t:
    tt = tt.append(base.loc[base["call_id"]==i])
    
tt.to_csv("../qianxin/分类代码ready/check/test3/0815-0819.csv", index=False, sep="\t")
```



### pandas .isin():依据列值是否在list中筛选

```
https://blog.csdn.net/weixin_43064185/article/details/91374033

>>> df
  countries
0        US
1        UK
2   Germany
3     China
>>> countries
['UK', 'China']
>>> df.countries.isin(countries)
0    False
1     True
2    False
3     True
Name: countries, dtype: bool
>>> df[df.countries.isin(countries)]
  countries
1        UK
3     China
>>> df[~df.countries.isin(countries)]
  countries
0        US
2   Germany
```



## pandas 依据某列的内容筛选出符合的所有行

```
# 实际已流转工单
done = np.hstack((df[df["当前call后staff是否进行了流转"].apply(lambda x: x == 1)]["case_id"].values, 
df[df["当前call后staff是否进行了驳回"].apply(lambda x: x == 1)]["case_id"].values))

done = set(list(done))
```



## Pandas根据字符串长度过滤字符串数据

```
# https://www.itranslater.com/qa/details/2583873767713801216

df=df[df.A.apply(lambda x: len(str(x))==10]
df=df[df.B.apply(lambda x: len(str(x))==10]

df=df[(df.A.apply(lambda x: len(str(x))==10) & (df.B.apply(lambda x: len(str(x))==10)]

df=df[(df.A.astype(str).str.len()==10) & (df.B.astype(str).str.len()==10)]
```



## pandas依据列A是否符合条件来修改列B的值：列A的字符串长度更改列B的值

```
# 过短的对话认为是机器人对话， 强制置为0 
df.loc[df["dialogue"].str.len() < 60, '模型分析结果值'] = 0.


checkout.loc[checkout["模型分析结果值"].apply(lambda x: float_equal(x, 2.1)), "问题分类"] = "话术不合规"
```



## drop_duplicates()

```
https://blog.csdn.net/csefrfvdv/article/details/100770965

df.drop_duplicates(subset=['y','z'],keep='first',inplace=True)
df
```



## BUGS

```
read_parquet报错：
1. Found files in an intermediate directory:
debug：
fastparquet == 0.7.2
pyarrow=6.0.1
```

# Numpy

## Numpy 空数组循环添加 利用empty[注意有坑]

```
# 利用np.empty创建空数组可以循环添加，但是后续vstack添加的内容都是基于empty设置的，比如dtype就算添加的是float16，vstack后也是float32，需要特殊制定！！！

kb_vectors = np.empty(shape=(0, 768), dtype="float16")
for l in sorted(os.listdir("话术库/13_daily_kb_and_vecs/")):
if len(l) != 33: continue
if l > end or l < begin: continue
print(l)
kb_vectors = np.vstack((kb_vectors, np.load("话术库/13_daily_kb_and_vecs/" + l).astype('float16')))

# https://www.delftstack.com/zh/howto/numpy/python-numpy-empty-array-append/
```



## vstack循环添加数组

```
a = [[1,2,3], [2,3,4], [3,4,5]]
a = np.vstack(a)
a.shape
a
```

## list变numpy array 数据类型变化 dtype=object

```
a = [["我好", "我很好", 1], ["早安", "午安", 0]]
b = np.array(a)
print(b)
[["我好", "我很好", "1"], ["早安", "午安", "0"]]

b = np.array(a, dtype=object)
print(b)
[["我好", "我很好", 1], ["早安", "午安", 0]]
```



## np.argsort索引排序

```
x = np.array([1, 2, 3, 4])
y = np.array([0.9, 0.8, 0.95, 0.2])
arrindex = np.argsort(y)  # 升序

arrindex = np.argsort(y)  # 降序

x = x[arrindex]
y = y[arrindex]
```



## numpy切片 None,::

```
y_true = np.array([1,0,1])
y_true[:, None]  # 新增一个维度，新增列的维度
[[1],[0],[1]]
y_true[None, :]  # 新增一个维度，新增行的维度
[[1,0,1]]

一般配合用cast函数构建对角矩阵，例如：
y_true = K.cast(y_true[:, None] < y_true[None, :], K.floatx())

keras输出tensor用K.eval(tensor)
K.eval(y_true)
[[0., 0., 0.], 
 [1., 0., 1.], 
 [0., 0., 0.]]
```



# python

## 终端命令行使用变量

```
date = "20221122"
!hadoop fs -get /user/hadoop-hmart-mtai/wangchuan16/kg/script_recommendation/raw_data/chat/staff/staffs_$date

```



## @staticmethod 静态方法

就是可以不实例化类进行调用。

```
# https://www.runoob.com/python/python-func-staticmethod.html

class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
以上实例声明了静态方法 f，从而可以实现实例化使用 C().f()，当然也可以不实例化调用该方法 C.f()。
```



## random随机选取

```
#1.使用python random模块的choice方法随机选择某个元素
import random
foo = ['a', 'b', 'c', 'd', 'e']
from random import choice
print(choice(foo))
 
#2.使用python random模块的sample函数从列表中随机选择一组元素
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
#设置种子使得每次抽样结果相同
random.seed(10)
slice = random.sample(list, 5)  #从list中随机获取5个元素，作为一个片断返回  
print(slice)
print(list) #原有序列并没有改变。
```



## map 将list中的每个元素类型从字符变为int

```
labels = list(map(int, labels))

```



## 为什么Python 3.6以后字典有序并且效率更高？

```
https://www.cnblogs.com/xieqiankun/p/python_dict.html

```



## 快速求数据集的最长

```
import pandas as pd
tmp = pd.DataFrame({"text":texts, "label":labels})
tmp["length"] = tmp["text"].apply(lambda x:len(x))
tmp.describe()
```



## jupyter 忽略警告

```
import warnings
warnings.filterwarnings("ignore")
```



## eval 将str变为list

```
a = "[['12150', '2021-08-18'],['12115', '2021-10-18']]"
b = eval(a)
print(b[0], b[1], b[0][0])

['12150', '2021-08-18'] ['12115', '2021-10-18'] 12150
```



## any和all用法

```
if all(keyword not in i for keyword in ["反馈", "联系", "流转", "对接", "跟进", "回复"]):
	un_kefubanglianxi.append(i)
```



## 固定顺序shuffle打乱list np.random.shuffle

```
tmp = [1,2,3,4,5]
np.random.seed(42)
np.random.shuffle(tmp)
tmp


```



## python 找列表最大值

```
python 找列表中的最大值_在元组的python列表中查找最大值

l = [(10,"a"),(9,"b")]
t = max(l, key=lambda x: x[0])

l = ["absb", "sajjjsjsj"]
t = max(l, key=len)
```



## python datetime 时间加减法 比较大小

```
# https://www.cnblogs.com/qi-yuan-008/p/12418822.html

from datetime import datetime, date
# 不同天的时间差
time_1 = '2020-03-02 15:00:00'
time_2 = '2020-03-03 16:00:00'

time_1_struct = datetime.strptime(time_1, "%Y-%m-%d %H:%M:%S")
time_2_struct = datetime.strptime(time_2, "%Y-%m-%d %H:%M:%S")

# 来获取时间差中的秒数。注意，seconds获得的秒只是时间差中的小时、分钟和秒部分，没有包含天数差，total_seconds包含天数差
# 所以total_seconds两种情况都是可以用的
total_seconds = (time_2_struct - time_1_struct).total_seconds()
print('不同天的秒数为：')
print(int(total_seconds))

min_sub = total_seconds / 60
print('不同天的分钟数为：')
print(int(min_sub))
```



## python 输出日期

```python
str(time.strftime('%Y-%m-%d-%H:%M:%S',time.localtime(time.time())))

'2021-04-13-01:46:03'
```



## python 输出右对齐

```
https://blog.csdn.net/weixin_45953165/article/details/108937223

>>> s = "hello"
>>> print(f"{s:10s}")#左对齐
hello     
>>> print(f"{s:10s},world!")#左对齐
hello     ,world!
>>> print(f"{s}")#直接输出，默认左对齐
hello
>>> print(f"{s.rjust(10,'*')}")#右对齐
*****hello
>>> print(f"{s:*>10}")#右对齐
*****hello
>>> print(f"{s: >10}")#右对齐
     hello
>>> 

```



## python 输出精确两位小数

```
print("%.2f" % res, "Yes")  # 强制补全2位小数
```



## python fstring 快捷结构化输出

https://blog.csdn.net/sunxb10/article/details/81036693

### 精确到三位小数

```
print(f"召回：{recall:.3f}")
```

```
neg, pos = np.bincount(raw_df['label'])
total = neg + pos
print('Examples:\n    Total: {}\n    Positive: {} ({:.2f}% of total)\n'.format(
    total, pos, 100 * pos / total))

initial_bias = np.log([pos/neg])
print(f"initial_bias: \n    {initial_bias}")
```





## python读写文件

| 模式 | 可做操作 | 若文件不存在 | 是否覆盖   |
| ---- | -------- | ------------ | ---------- |
| r    | 只能读   | 报错         | -          |
| r+   | 可读可写 | 报错         | 是         |
| w    | 只能写   | 创建         | 是         |
| w+   | 可读可写 | 创建         | 是         |
| a    | 只能写   | 创建         | 否，追加写 |
| a+   | 可读可写 | 创建         | 否，追加写 |



## numpy hstack/concatenate/vstack (没有append)

```
# d = np.concatenate((data["dialogue"].values, data_test["dialogue"].values))
d = np.hstack((data["dialogue"].values, data_test["dialogue"].values))
len(d)
```



# JSON读写文件

```python
def jdump(filepath, dic):
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(dic, f)
        print(f"dump {filepath} 完成")
jdump("id2label.json", id2label)

def jload(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        load_dict = json.load(f)
        print(f"load {filepath} 完成")
        return load_dict
id2label = jload("id2label.json")
id2label = {int(k) : v for k, v in id2label.items()}  # json读入id2label 时id会变为str
label2id = jload("label2id.json")
```



# pickle读写文件

```
def save_pkl(obj, filepath):
    with open(filepath, 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def load_pkl(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)
```



# numpy保存字典

```
https://blog.csdn.net/weixin_35757704/article/details/124921501

my_dict = {"name": "小明", "age": 12}
output_filename = "save_dir/my_dict.npy"

# 保存
np.save(output_filename, my_dict)

# 加载
my_dict2 = np.load(output_filename, allow_pickle=True).item()
```



# python 内置函数open被重写 还原的方法 

```
from bert4keras.snippets import open  
del open
```



# SKlearn 计算余弦相似度

```
https://www.jianshu.com/p/65f683f49443
```



# BUGS 处理方法

## InvalidArgumentError: 2 root error(s) found.

pos bert任务重的错误 /home/drose/jupyter/006_WCLAC/BERT_POS/pos_bert

```python
BUG：  

InvalidArgumentError: 2 root error(s) found.
  (0) Invalid argument: Input to reshape is a tensor with 57 values, but the requested shape has 55
	 [[{{node loss/conditional_random_field_1_loss/Reshape}}]]
	 [[loss/mul/_6043]]
  (1) Invalid argument: Input to reshape is a tensor with 57 values, but the requested shape has 55
	 [[{{node loss/conditional_random_field_1_loss/Reshape}}]]
0 successful operations.
0 derived errors ignored.


解决方法：

1. 找到数据 删除数据。
2. https://blog.csdn.net/walker_Tjj/article/details/107195166
 最后在他人博客上找到了问题所在，显存分配问题，更改为动态分配内存就可以解决。

在训练的脚本开头添加以下代码即可进行内存的动态分配，重新运行即可。

import keras
import tensorflow as tf
 
config = tf.ConfigProto()
config.gpu_options.allow_growth = True      # TensorFlow按需分配显存
config.gpu_options.per_process_gpu_memory_fraction = 0.5  # 指定显存分配比例
keras.backend.tensorflow_backend.set_session(tf.Session(config=config))

```



# map用法

```
string_date='2016-8-1'
year,month,day=map(int,string_date.split('-'))
```



# （好）@classmethod 类方法 以及cls用法

```
# https://www.cnblogs.com/anzhangjun/p/9745881.html
这个网址说的非常好！
```



# GIT

## GITHUB TOKEN

```
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
```



## GIT免密拉取gitee的代码 修改后提交到gitee

```
参考：https://www.bilibili.com/video/BV1uv411Y7ci?t=332


(base) drose@ubuntu:~/jupyter$ ssh-keygen -t rsa

下面省略(base) drose@ubuntu:

cd
cd .ssh
cat id_rsa.pub # 查看公钥
# 复制该公钥 然后打开gitee 设置 里面有一个ssh公钥 复制就好了
cd git_test/ # 进入working dir
git clone git@gitee.com:buaachuanwang/machine-translation.git #clone gitee远端的代码到working dir
cd machine-translation
# 然后在本地修改了machine-translation 中readme的内容后 想要提交到gitee
git add -A
git commit -m "修改readme"
# 此时可能需要你设置邮箱和用户名
git config --global user.email "wangchuan@buaa.edu.cn"
git config --global user.name "高桥凉介"
# 设置完毕
git push origin master # push修改到gitee远端

```

## GIT将本地的代码第一次提交到gitee

```
参考：
# https://www.bilibili.com/read/cv8144676/
# https://www.jianshu.com/p/6054a7661cc2
# https://blog.csdn.net/darendu/article/details/90719446

cd 到working dir
git init
git add . # .表示将当前目录下的所有内容都添加到暂存区
git commit -m "测试把wd的东西上传到gitee" # 提交

# 然后在gitee创建一个仓库 与当前目录同名 比如当前目录叫git_push
# 然后创建号以后 复制http的链接
# 勾选 ”初始化仓库、设置模板（三个子选项都不要选，不要新建readme文件）、选择分纸模型”
git remote add origin https://gitee.com/buaachuanwang/git_push.git
git push -u origin master
(git push origin HEAD:master)


buaachuanwang
Aa

# 如果报错failed to push some refs to git因为本地没有LICENSE readme这种文件。可以通过如下命令进行代码合并【注：pull=fetch+merge] 
git pull --rebase origin master # 本地文件中会多了LICENSE
git push -u origin master

如果还是不行
于是我就用git push -f origin master强制push就成功了。（注意：大家千万不要随便用-f的操作，因为f意味着强制push，会覆盖掉远程的所有代码！）
```



## GIT 分支操作

```
git branch		//查看分支
git branch chuan		//创建分支
git checkout dev-tian		//切换分支
git push origin chuan  //push到某一个分支

```



## git pull拉取master代码合并到chuan分支

```
1.git checkout master     --------切换到master
2.git pull      -------拉取master代码
3.git checkout chuan     --------切换到本地分支
4.git merge master     --------合并代码到本地分支
```



## git分支与master合并一致

```
https://dandelioncloud.cn/article/details/1514488574396416002
其实代码同上
```



## git将本地代码上传到meituan个人仓库

```python
git config --global user.name "wangchuan16"
git config --global user.email "wangchuan16@meituan.com"

cd existing-project
git init
git add --all
git commit -m "Initial Commit"
git remote add origin ssh://git@git.sankuai.com/~wangchuan16/spelling_correction.git
git push origin HEAD:master
```



## git 删除一次commit中的某一个文件

```
https://blog.csdn.net/qq_34681580/article/details/105163691

git status / git log # 查看状态

b.txt被错误提交了，要把b.txt从这个commit中去掉
（1） 首先git rm --cached b.txt
（2）然后git commit --amend --allow-empty，commit的id和上次相同，–allow-empty意思是允许commit的comment为空。
```



## GIT ignore

```
https://blog.csdn.net/luhu124541/article/details/82049510

#过滤项目下的有所.c文件
*.c

#过滤整个项目文件
/*

#过滤目录/filename/
/filename/

#过滤/目录下的所有.cpp文件,无法过滤/filename/name.cpp
/*.cpp

#保留所有的.cpp文件
！*.cpp

#保留/filename/目录及其下所有文件
！/filename/

#保留/目录下所有.c和.o文件
！/*.[co]

```



# UniLM V2

```
https://zhuanlan.zhihu.com/p/113391609

部分自回归+自编码

部分自回归的意思是 通过添加span mask（连续的几个字同时mask），然后当遇到span mask需要与测试，同时预测这几个字。如：有x2,x4,x5被mask了，其中因为x4x5在句子中的顺序是连着的，而x4x5被同时mask，也就是span mask，那么就同时预测x4x5。当一句话全部被span mask 时，也就是自回归了。因此这种方式叫做 部分自回归。
```



# Precision和Recall

```
https://zhuanlan.zhihu.com/p/93586831

精确率和召回率有什么用？为什么需要它？通俗讲解(人话)

这里以两种需求为例

预测地震 - 不能接受漏报
人脸识别支付(银行人脸支付) - 不能接受误检


人脸识别支付：主要提升精确率，更倾向于不能出现错误的预测。

应用场景：你刷脸支付时就算几次没检测到你的脸，最多会让你愤怒，对银行损失不大，但是如果把你的脸检测成别人的脸，就会出现金融风险，让别人替你买单，对银行损失很大。所以宁愿让你付不了钱，也不会让别人帮你付钱。

预测地震：主要提升召回率，更倾向于宁愿多预测一些错的也不能漏检。

应用场景：地震预测时宁愿多预测一些错的，也不想漏掉一次地震，预测错误最多会让大家多跑几趟，造成少量损失。只要预测对一次，就会挽回百亿级别的损失，之前所有的损失都值了。



不同的应用场景，需要的评价标准不一样，所以才会有这些率。
```

一句话就是 召回率要求 *可以误查一百但不能漏查一个*，查准率要求查到的正确的要尽可能的正确。



# 自回归和自编码

参考本人硕士毕业论文，一句话说就是 GPT单向是自回归，BERT双向上下文是自编码。



# Latex

## 分段函数

```latex
# https://www.jianshu.com/p/b6a6083ed8fb

y= \begin{cases}
-x,\quad &x\leq 0 \\
x,\quad &x>0
\end{cases} 
```



# item快捷键设置

```
https://blog.csdn.net/kd_2015/article/details/113844127

行首：fn+←

行尾：fn+→

光标跳到上一个单词前：option+←

光标跳到下一个单词前：option+→
```



# Java

## 安装

```
https://blog.csdn.net/Riptide_Liu/article/details/108110701

下载intellij
下载jdk

其中环境变量在安装jdk的时候就应默认配置好了，只需要：
source ~/.bash_profile
（若没有默认配置好，则参考：https://segmentfault.com/a/1190000040495961）

然后就可以打开intellij进行java代码编写了
```





```
14.0.2
/Library/Java/JavaVirtualMachines/jdk-14.0.2.jdk/Contents/Home

export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-14.0.2.jdk/Contents/Home
export PATH=$JAVA_HOME/bin:$PATH

JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_261.jdk/Contents/Home
PATH=$JAVA_HOME/bin:$PATH:.
CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.
export JAVA_HOME
export PATH
export CLASSPATH

```

