# 문제 해결 기록
처음부터 접근하려는 안좋은 습관이 있다, 항상 문제는 역으로 접근해보자

## git
0. 질문
반드시 커밋은 cmd켜서 git push origin main해야하는가?
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
2. git push origin main 했더니 failed to push some refs to ~  
원격 repo에 로컬에 없는 파일이 있다 (협력할 때 빈번)  
결국 먼저 pull해서 해당 파일 받아오고 push 해야함  
3. README.md 글씨가 엔터 없이 출력  
각 줄마다 반드시 띄어쓰기 2번씩  
99. 기타 내용  

## python  
0. 질문  
1. class  
    모듈 불러오는 것만으로 부족, 특정 class까지 호출해야함  
    ex) import pandas 해도 read_csv는 해당 모듈 최상위  
    import datetime  
    from datetime import datetime 모듈안의 클래스 이름까지 써줘야함 
2. ValueError: The truth value of a Series is ambiguous  
    문제는 항상 데이터 타입이 맞지 않기 때문  
    df.squeeze로 해결, dataframe하면 series가, series하면 스칼라값이 됨 (아예 row데이터 등을 삭제)  
99. 기타  
\로 다음줄에 넘겨서 입력 가능  

## 크롤링
0. 질문  
1.   
99. 기타  