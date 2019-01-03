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



### 커밋 제외 폴더

.gitignore 파일을 만든다 ->  파일 안에 .vscode/ 를 쓴다(vscode 폴더와 그 밑의 모든 것을 무시해줘)

google python git ignore 검색하면 -> 파이썬 개발할 때 관례상 무시하는 것들 정리되어 있음.
(https://github.com/github/gitignore/blob/master/Python.gitignore)



### 다른 컴퓨터에서 같은 레포지토리 공유

1. Clone
   git clone "복사주소" -> git remote add origin 할 필요 없음. 어디서 왔는지 알고 있다(git remote -v)
2. 수정할 거 수정
3. git add .
4. git commit -m "Edit browser.py" # commit message는 동사+목적어 형태로 쓰는 것이 관례
5. 각각의 컴퓨터에서 git log를 찍어보면 홈컴퓨터에는 commit이 두개, saffy에는 commit이 하나만 찍힌 걸 볼 수 있다.
6. 홈컴에서 git push origin master
7. 싸피컴에서 최신화하기
   git pull origin master
8. single source of origin



### 실수한다면? 컴플리트 or 브랜칭

!!! 항상 작업 시작 전엔 pull !!!



### Github 공동 프로젝트 - 대장 + 팀원

1. 대장 mkdir collabo해서 레포지토리 최초 푸쉬까지 한다.
2. clone 주소를 공유
3. advanced 계정이 아니라면 동시에 같은 파일을 수정하지 않는 것이 원칙!
4. 팀원은 git clone "복사주소" team_member -> team_member로 폴더가 만들어져서 클론된다.
5. 팀원이 수정해서 push하면 권한 없어서 안된다
6. 대장 레포지토리 settings -> collaborators 에서 추가한다 -> collabo/invitations 를 통해서 승인받을 수 있다.



### Issue

게시판처럼 문제가 있을 때 올릴 수 있다. 이슈를 열고 닫을 수 있음. 수정 사항 반영되면 이슈 닫으면 됨.



### origin master

origin - 가장 오리지날한 레포지토리



### Merge conflict

내 커밋 <-> 팀원의 푸시가 충돌할 때 코드가 두 종류로 보이게 되는데, 하나를 지우고 남은 하나를 저장 후 git add 및 커밋하면 됨 -> git log 보면 대장의 실수 커밋도 같이 log에 남아있다 -> push 하면 다같이 기록됨

vscode에서는 merge complete 상황에서 선택지를 고를 수 있게 해서 편의 제공

origin/master는 원격저장소의 상태 -> git push origin master 하면 원격저장소가 내가 커밋한 것을 따라서 최신화된다.

% commit은 로컬 상태라 지울 수 있지만, push는 하고 나면 지울 수가 없다.



# Branching

메인 라인은 master, 다른 라인은 slave. slave가 맘에 안들면 삭제, 괜찮으면 merge.

- 보기
  git branch : branch 구조 파악 가능
- 생성
  git branch "name" : name 명으로 branch 생성
- 이동(브랜치 간, 커밋 간)
  git checkout [브랜치 이름] : 해당 브랜치로 이동



### git flow

충돌을 방지하기 위해 만드는 흐름 구조(배달의 민족)
http://woowabros.github.io/experience/2017/10/30/baemin-mobile-git-branch-strategy.html



### 다른 branch

- checkout으로 help 브랜치에서 작업 후 commit -> 그 다음 master로 이동하게 되면 이전에 작업했던 내용은 존재하지 않음 -> 다시 help로 돌아오면 생겨있다.

- branch의 commit을 git merge를 통해 master에 병합
  1) git checkout master 병합할 메인 줄기로 이동
  2) git merge help 병합





