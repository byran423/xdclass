### Linux常用命令

cd 

* cd - 返回之前的文件夹
ls

* -lrt -l以列表形式 -r倒序 -t以时间顺序排序
* ls -l 首字母有d代表文件夹，没有d代表文件

man 

*  man 命令  查看命令帮助文档，结合翻译知道对应后缀意义

cat
 
 * 查看文档全部内容

touch
 
 * 创建一个新文件

wc -l
 
 * 统计文件行数

id

* 查看当前用户信息

df

* 查看磁盘空间信息

echo

* 标准输出命令

### shell 使用技巧

命令行模式

插入模式

底行模式

* shift+： 进入底行模式
* set nu 可以设置行号
* / 可以搜索内容

一个shell脚本,不一定有解释器

* 首行 #!/bin/zsh 标识解释器
* 注释，介绍shell脚本的作用和作者和日期
* rwx x-代表执行 r=4 w=2 x=1
* 所有者 所属者 其它用户

执行方法：

* sh test.sh
* ./test.sh 需要有执行权限
* source test.sh

### Shell 常见变量和常见符号

#### 常见变量

...

### grep、cut、AWK、sed命令

grep命令

```
grep -v 对内容进行取反提取
grep -i 忽略大小写
grep -n 显示行数
grep -w 精确匹配
grep '^abc' 行首为abc的行
grep -E 正则匹配 grep -E 'aaa|bbb|ccc' 匹配aaa 、bbb、ccc的行
```

cut命令

	对数据列进行提取

awk命令 ： 通常对数据进行列的提取

sed命令 ： 主要对数据进行操作（选组、新增、删除、替换）

	语法 ：sed  [选项] [动作] 文件名
	
* 常见的选项参数：
	
	-n  把匹配到的行打印到屏幕
	
	p 以行为单位进行搜寻，通常与-n一起使用
	
		eg: df -h | sed -n '2p'  输出第二行内容
	
	d 删除
	
		eg: df -h |sed '2d'  输出时删除第二行	，对原文件不改动
		
	a 在行的下面插入新的内容
	
	i 在行的上面插入新的内容
	
	c 替换
	
### 实战例子

巡检内存使用率

```
	#!/bin/zsh
	# 内存使用率
	mem_total = `free -m | sed -n '2p' | awk '{print $2}'`
	mem_used = `free -m | sed -n '2p' | awk '{print $3}'`
	mem_free= `free -m | sed -n '2p' | awk '{print $4}'`
	Percent_mem_used = `echo "scale=2; $mem_used / $mem_total * 100" | bc`
	Percent_mem_free = `echo "scale=2; $mem_free / $mem_total * 100" | bc`
	nowtime = `date+"%Y-%m-%d %H:%M:%S 星期%w"`
	echo -e
	echo -e "$nowtime\n内存的使用率是：$Percent_mem_used%"
	echo -e "内存还剩：$Percent_mem_free%未使用"
	# 检查负载是否有压力
	if [$mem_used -gt 1]
			then
			echo -e "\033[31m内容使用率超过负载能力，目前使用率达到：$Percent_mem_used\033[0m"
	else
			echo "目前内容负载正常"
	fi
	
	echo -e "\n"
```

高效登录远程机器

```
	#! /bin/zsh
	# 登录脚本
	LoginIp = `cat /home/shell/ip.txt | grep $1 | awk -F "|" '{print $2}'`
	ssh ${LoginIp}
```

