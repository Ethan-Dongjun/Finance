# 문제 해결 기록

## git
1. 세팅
    1) 계정 등록
    git config  - global user.name "아이디"
    git config  - global user.email "이메일주소"
    2) 로컬 디렉토리에서 .git 생성
    cd "경로"
    git init
    3) git add readme.md
    git commit -m "커밋메시지"
    추가안하면 branch 생성이 안됨
    4) 로컬 디렉토리 경로에서 git remote add origin "주소"
    origin은 url의 별칭
    5) git branch main
    원격 repo에 main브랜치에 변경 푸쉬
    git push origin main

