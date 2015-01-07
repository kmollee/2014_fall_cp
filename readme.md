# Hello ! this is CP 2014 TA repo

# bug or question

please report the problem at issue

注意!請勿留下個人敏感資訊在其中, issues 中的內容是公開的, 請各位同學自行注意

# deadline datetime

11:59 P.M.(GMT+8) January 12, 2015

# git - version control tool

[git cheat sheet](http://www.git-tower.com/blog/assets/2013-05-22-git-cheat-sheet/cheat-sheet-large01.png)

`git init` inital repo

`git log` check out all git log

`git log --stat` (more detail)

`git log --graph`

`git log --graph --oneline master branch-name`

`git log -n 1` only show log 1 line

`git status` check between staing area and working directory

`git commit` git commit the staging area file

`git add` git add working directory file to staging area

`git checkout <hash>` checkout to that commit hash status, whole directory file will back to that moment

notice in this status, should not direct add new commit, instead shoud add new branch to commit change, otherwise, checkout master branch will lost what you just commit, the commit is unreachable, so add branch will avoid this problem

`git diff` check working directory and staging area

`git diff --staged` check staging area and repo

`git diff commit1 commit2` check two commmit different

`git reset --hard` reset back to the version

`git branch` show all branch, also show out what branch you stay

`git branch new-branch-name` create new branch

`git branch -d branch-name` delete branch

`git checkout branch-name` switch branch to branch-name

`git merge branch1 branch2` merge branch1 and branch2

may have some conflict, if automatic merge fail,git don't know, and would not guess which one should adapt

it will let user to decide what to do, need to fix and commit to conclude the merge

`git show <hash>` show commit and it's parent diff

`git remote` show all remote name

`git remote -v` show all remote name and url(more detail like fetch and push)

`git remote add remote-name remote-url` add new remote

`git push remote-name branch-name` push to remote with branch

`git pull remote-name remote-branch-name` pull remote data to local

`git fetch branch-name`

`git pull master` = `git fech master` + `git merge master origin/master`

---

# python escape sequnce

| Escape Sequence | Meaning Notes                                               |
|-----------------|-------------------------------------------------------------|
| \newline        | Ignored                                                     |
| \\              | Backslash (\)                                               |
| \'              | Single quote (')                                            |
| \"              | Double quote (")                                            |
| \a              | ASCII Bell (BEL)                                            |
| \b              | ASCII Backspace (BS)                                        |
| \f              | ASCII Formfeed (FF)                                         |
| \n              | ASCII Linefeed (LF)                                         |
| \N{name}        | Character named name in the Unicode database (Unicode only) |
| \r              | ASCII Carriage Return (CR)                                  |
| \t              | ASCII Horizontal Tab (TAB)                                  |
| \uxxxx          | Character with 16-bit hex value xxxx (Unicode only)         |
| \Uxxxxxxxx      | Character with 32-bit hex value xxxxxxxx (Unicode only)     |
| \v              | ASCII Vertical Tab (VT)                                     |
| \ooo            | Character with octal value ooo                              |
| \xhh            | Character with hex value hh                                 |

# Making python files executable in Ubuntu

```sh
chmod +x file.py
./file.py
```

# windows python portable(dll) contain

```sh
    msvcp100.dll
    msvcr100.dll
    python33.dll
```
