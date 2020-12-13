### gitignore 

`*.log` 忽略项目中以.log结尾的文件

`123?.log` 忽略项目中所有以123加任意字符的文件

`/error.log` 忽略项目中根目录下的error.log 文件

`src/main/test/*` 忽略src/main/test/目录下的所有文件

`**/java/` 匹配所有Java目录下的所有文件

对于已经提交到远程或本地仓库里的文件，.gitignore 配置之后不会生效，我们必须先删除暂存区里的 git rm -rf --cached + 文件夹 ,之后再加上.gitignore 文件，最后再把变更提交到远程上



