# 문제 해결 기록
처음부터 접근하려는 안좋은 습관이 있다, 항상 문제는 역으로 접근해보자

## venv
간단한 데이터 호출도 30분 걸려도 안되길래 찾아보니 파이썬 버전 3.8이 너무 낮단다  
conda update하면(conda update -n base conda, conda update --all) 파이썬 업그레이드 안해주길래  
어쩔 수 없이 venv 생성(conda search python, conda create -n py3130 python=3.13.0, conda update --all)  


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
    안되면 echo "# temp-repository" >> README.md  
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
4. 깃헙에 push는 visual studio상 못하는가?
푸쉬 버튼 눌러서 가능
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
3. if __name__="__main__": 어떻게 쓰는 건가  
모듈내 클래스나 함수 밖에 있어야 파일 실행시 true가 되는 구문  
99. 기타  
\로 다음줄에 넘겨서 입력 가능  

## crawling
0. 질문  
1.   
99. 기타  