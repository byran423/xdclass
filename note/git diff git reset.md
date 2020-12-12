##git diff

git diff --cached  
`查看工作区和缓存区别`

git diff  head 	
`查看当前工作区和当前分支的区别`

git diff 分支名 	
`查看当前分支和指定分支的差异`

git diff 分支名1 分支名2 
`查看两个指定分支(已提交的)的差异`

git diff commitId1 commitId2 

* 用来查看两个提交之前的区别

git diff --stat 

* 用于罗列有变更的文件

* git reset head 文件名  `移除不必要的添加到暂存区的文件`
*  git reset 	head^    `去掉上一次的提交`
*   git reset --soft heah^ `修改上次提交的信息即把commit -m "修改这里的内容"`

> git reset --soft 只是将head引用指向指定的提交，工作区和暂存区里的文件不会改变
>  git reset --mixed (默认选项) 将head指向指定的提交，暂存区中的内容随之改变，工作区的内容不会改变
>  git reset --hard 将head 指向指定的提交，暂存区和工作区的内容都会改变



















