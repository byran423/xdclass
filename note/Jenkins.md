### Jenkins 安装
* 前置条件：
JDK ，Tomcat


1. 安装Tomcat

		tomcat 官网去下载tar.gz ，使用非root用户登录后，tar -zxvf 包路径 -C 指定解压路径   
		useradd  tomcat --新增一个Tomcat用户
		passwd tomcat -- 给Tomcat用户设置密码
		chown -R 需要授权的用户:需要授权的组 文件夹路径  将整个目录和组的所属权转移
		./start.sh 就可使用
		
> 服务启动，网页却不能访问问题排查

```
1、ps aux | grep tomcat首先看服务有没有正常启动 
2、netstat -tlun服务正常启动后，查看8080端口是否开启 
3、vim /etc/sysconfig/iptables防火墙配置是否打开8080端口，如果没有增加一行然后重启
service iptables restart	
4、还不行的话，查看Tomcat路径/logs 下的日志 more catalina.out  端口是不是已经被占用
5、查看端口被什么程序占用 netstat -tlunp | grep 8080
6、修改端口 Tomcat/conf 目录下server.xml 文件 打开，/8080 找到响应的8080端口，修改端口号，重新启动Tomcat，再在防火墙中添加新修改的端口号


```
 Jenkins配置

* 下载地址： https://jenkins.io/download/​ 
* 进入ip/jenkins 进行Jenkins配置

	Jenkins插件离线
	由于插件https导致，进入插件代理地址  http://192.168.56.101:9999/jenkins/pluginManager/advanced​ 拉到最底下，将https--》改成http 提交后，重启Tomcat
	











		


