### 최초 커밋

git init
git add .
git commit -m "설명"
git push (origin master)
git remote add origin <원격 서버 주소>
git push -u origin master

-m의 m은 message

commit 상황 -> git status, git log



### 유저 정보 변경

git config --global user.name egyeasy

git config --global user.email dz1120@gmail.com

git config --get user.name : 어떤 user name을 쓰고 있는지 볼 수 있다

git config --get user.email