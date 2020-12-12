### git remote 管理远程仓库
	git remote add origin git远程地址
	origin 名称可更改

	git push -u origin master 推送到远程仓库

* 删除远程仓库文件夹
	 	
		git rm --cached xd_api_test //cached 不会删除本地文件
		git commit -m "remove"
		git push -u origin master
		
*  git仓库包含子仓库时
		
		需要删除子仓库的.git 文件后再重新add
		
* git fetch 拉取远程仓库的变更到本地仓库
* git merge origin/master 讲远程的变更合并到本地仓库的master分支
 
上面两个命令= git pull  --不建议使用，建议手动merge

* git 文件状态
![git文件状态](https://github.com/byran423/xdclass/blob/master/img/git%E6%96%87%E4%BB%B6%E7%8A%B6%E6%80%81.png)


* git status 用于查看Git的状态


		git rm --cached  <文件名>  删除本地仓库中的文件
		如果不加--cached 会删除工作区里的文件  并提交到暂存区
		







	