
$ mkdir learngit     #创建learngit目录命令
$ cd learngit         #更改目录命令 
$ pwd                #用于显示当前目录
/Users/michael/learngit


$ git init         #命令把这个目录变成Git可以管理的仓库（初始化仓库）
$ git add readme.txt   #添加resdme.txt文件到仓库
$ git commit -m "wrote a readme file"   #把文件提交到仓库，wrote a readme file是对文件的说明
$ git add file2.txt file3.txt    #添加多个文件

$ git status        #掌握仓库当前的状态
$ git log          #可查看历史记录
$ git log --pretty=oneline    #详细信息，HEAD表示当前版本，HEAD^表示上一个版本，HEAD^^上上个版本，HEAD~100第100个版本
$ git reflog        #查找所记录的每一条命令

$ git checkout -- readme.txt   #可以丢弃工作区的修改
$ git reset HEAD readme.txt     #表示可以把暂存区的修改撤销掉（unstage），重新放回工作区