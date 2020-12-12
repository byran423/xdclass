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

		新建文件，文件的状态是未跟踪
		使用add将新建的文件添加到暂存区,文件状态是暂存
		使用commit命令将暂存区的文件提交到本地仓库，文件状态是未修改
		如果对未修改文件状态进行更改，文件状态是已修改
		对未修改文件进行rm操作，文件状态变为未跟踪
	
	
		
		
		


* git status 用于查看Git的状态

**checkout谨慎操作**


		git rm --cached  <文件名>  删除本地仓库中的文件
		如果不加--cached 会删除工作区里的文件  并提交到暂存区
		git checkout 
		直接加文件名，从暂存区将文件恢复到工作区，如果工作区已有该文件，则会覆盖
		加分支名+ <文件名>则表示从分支名所在的本地仓库中拉取该文件，并覆盖工作区文件
	
		
		
#### Git图形化界面 sourcetree



				

		

		







	