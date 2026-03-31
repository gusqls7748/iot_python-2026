# iot_python-2026
IoT 개발자 파이썬 리포지토리

## 1일차

### 사건 정리

사전 C/C++ 학습완료. 프로그래밍 문법 파악 중

**기본 문법 리스트**
- 변수, 데이터형
- 제어문
    - 조건문
    - 제아문
- 함수/메서드
- 배열 개념
- 포인터/참조 개념 - 포인터없음
- 구조체 - 구조체없음
- 객체지향 클래스 
- 파일 입출력
- 예외처리

다른 언어는 새로 다시 공부해야 한다보다 필요한 것만 보충 학습하겠다는 생각할 것

### 이론적 개념 정리

#### 파이썬에 신경 안써도 되는 것
- 학습 난이도를 낮추는 목록
    - 자료형 선언 안 함
    - 세미콜론 없음(옵션으로 사용 가능)
    - 중괄호 없음 - `들여쓰기를 신중히`
    - `int main()` 강제 아님 - 비슷한 기능은 있음
    - 메모리 할당/해제 거의 안 함
    - 헤더 파일 개녕 없음
    - 컴파일 과정 신경 거의 안 씀
    - 개발환경 설정 어렵지 않다.

- 문법 비교표

    |이론개념|C/C++|phthon|
    |----|----|----|
    |출력|printf(),cout|`print()`|
    |변수 선언|int a = 10; | `a= 10`|
    |조건문| if (a > b) {...} | `if a > b:`|
    |반복문| for (int i = 0; i < 10; i++) {} | `for i in range(10);`|
    |함수| int add(int a, int b) {} | `def add(a,b):` |
    |배열| int arr[5] | `list`|
    |문자/문자열| char, char[], char*, string | `str `|

- `장점`
    - 들여쓰기가 코드 블록, {} 불필요
    - 선언이 없음
    - 리스트가 배열보다 훨씬 편하고 간결
    - 문자열 처리 간단
    - 함수 만들기 간단

- 단점
    - 상대적으로 실행속도가 느림
    - 들여쓰기 문제 가능성(공백하나로도 문법오류)
    - 파일명 지정 시 클래스명과 동일하게 사용하면 문제발생
    - 디버그 콘솔이 여러개 실행 가능(하나만 실행되도록 정리)

    ![alt text](image-6.png)

    ![alt text](image-7.png)

#### 파이썬 설치

- https://python.org - 다운로드
    - 최신버전 설치 지양 3. 12 버전
    - Python install manager클릭 (x)~ 

    ![alt text](image.png)

    - 3.12 페이지 검색, Windows installer (64-bit) 클릭

- 설치
    - 아래와 같이 설치

    ![alt text](image-1.png)

    - 다음에서 Documentation만 체크해제
    - Advanced Options에서 Install Python 3.12 for all users 활성화
    - Install 시작
    - 설치 후

    ![alt text](image-2.png)

    - 윈도우 디렉토리 Path 길이 260자 제한되어 있음. Linux/MaxOS등과 호환시 문제 발생

    - 콘솔에서 확인 안되면 시스템 속성(sysdm.cpl) 에서 Path 확인할 것

    ![alt text](image-3.png)

### VS Code 확장
- 확장
    - Python으로 검색 후 설치

    ![alt text](image-4.png)

    - Jupyter 검색 후 설치

    ![alt text](image-5.png)

### 깃허브 확장
- 웹 코딩 환경
    - https://github.com -> com을 dev로 변경 실행 
    - Visual Stuido Code와 동일한 화면으로 변경
    - 주피터 노트북으로 데이터분석 등을 깃허브에서 바로 개발할 때 활용
    - Google Colab과 동일

    ![alt text](image-8.png)

#### 파이썬 기본 학습

 <!-- append = c.언어에서는 pop 밀어 -->

1. 기본 입출력 - [소스](./day01/ex01_basicoutput.py)
    - .py 파일 작성
    - Ctrl + F5 실행
    - 디버거 선택 > `Python Debugger` 선택

2. 리스트(배열 대체) - [소스](./day01/ex02\_array.py)
    - 어떤 데이터타입도 추가 가능
    - append ~ sort 까지 11개 함수만 학습

3. 제어문 - [소스](./day01/ex03_logic_control.py)
    - if, for, while
    - swich~case 문 없음

## 2일차 

### 파이썬 기본 학습

4. 변수, 자료형 - [소스](./day02/ex04_variable.py)
    - 선언이 없고 자료형을 지정안함
    - 자료형 자체를 사용안함, 형변환 필요
    - 기본자료형, int, float, str, bool, Type(Null과 거의 똑같은 기능)

5. 연산자- [소스](./day02/ex05_operator.py)
    - 사칙연산, 할당연산, 비교연산, 논리연산, 맴버십연산
    - 연산자 우선순위 : 거듭제곱 > 곱셈/나눗셈 > 뎃셈/뺄셈, ()로 연산자 우선순위 설정

6. 문자열 - [소스](./day02/ex06_string.py)
    - C방식 문자열 처리가능
    - 여러문자열 출력방식 존재, f-string 사용추천
    - 포맷팅 기법

7. 함수 - [소스](./day02/ex07_funtion.py)
    - 객체지향언어 함수 -> 메서드로(Method)로 호칭(C#, Java,...)
    - 파이썬은 함수(Funtion)으로 호칭
    - C와 유사하게 함수 사용 전에 선언
    - def로 선언 파라미터 괄호 뒤 : 사용

8. 파일 입출력 - [소스](./day02/ex08_fileio.py)
    - C/C++과 모드가 동일 r, w, a
    - with 구문으로 close() 생략가능
    - 쓰기 각 문장끝 '\n' 추가
    - 기본적으로 UTF-8
    - CSV, JSON 텍스트파일 등 읽기에 많이 사용


9. 여기까지 배우고 활용하는 분야도 존재
    - 데이터분석, 머신러닝/딥러닝,...

10. 연습
    - 구구단 - [소스](./day02/pr01_gugudan.py)
    - 자판기 - [소스](./day02/pr02_vending.py)

11. 외부 라이브러리 사용 - [소스](./day02/ex10_builtin_lib.py)
    - 파이썬 표준 라이브러리 - 파이썬에 포함된 기본 라이브러리
    - 외부 라이브러리 - pip로 설치하는 3rd-party에서 개발된 라이브러리
    - C/C++ `include` -> python `import`
    - import : 모듈과 클래스를 모두 기재
    - from ~ import ~ : 클래스명만 기재
    - 라이브러리(모듈).클래스. 함수() 형태로 존재

## 3일차

### 파이썬 기본 학습

11. 라이브러리 사용 계속 - [소스](./day03/ex11_out_package.py)
    - 타언어의 경우 웹 검색, 다운로드, 개발위치 설치나 복사
    - CPU 아키텍처에 따라 32bit(x86), 64bit 마다 설치방법 상이
    - 파이썬은 자신만의 패키지 관리자(Packge Manager :pip) 사용
    - 웹 검색(http://pypi.org) 후 pip 명령어로 각 파이썬 개발환경에 맞춰서 설치

    ```bash
    > python --version
     Python 3.12.10
    > pip --version
    pip 25.0.1 from C:\Program Files\Python312\Lib\site-packages\pip (python 3.12)
    > pip install requsts

    ...
    Successfully installed ... requests-2.33.0
    ```

    > pip list
    Package Version
    ------- -------
    numpy   2.4.4
    pip     25.0.1

    > pip

    - CSV 라이브러리 - - [소스](./day03/ex12_csv_package.py)

12. 기타 자료구조 - [소스](./day03/ex13_datastruct.py)
    - 리스트 외 튜플, 딕셔너리, 셋 등...
    - 각 자료구조 형태를 구분

13. main- [소스](./day03/ex14_main.py)
    - 파이썬은 main 함수가 필요없음
    - 여러 파일 중 시작저믕ㄹ 지칭할 떄는 사용
    - `__name__` 특수변수를 사용

14. 가상환경 (Virtual Enviroment)
    - 프로젝트 마다 파이썬 환경을 따로 사용하기 위해 만들어진 개념
    - 프로젝트 생성 시 독립된 파이썬, 라이브러리 세트 새로 생성
    - 실제환경 C:\Program Files\Python312 와 비교
    - 일반적으로 프로젝트 폴더에서 생성

    - 파워쉘 실행정책 변경 필요(관리자모드)
    
    ```bash
    >Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
![alt text](image-9.png)
    ```


    ```bash
    >python -m venv iot-venv(가상환경이름)
    ```

    - 가상환경 생성 후 가상환경 활성화해야 함

     ```bash
    > .\iot-venv\Scripts\Activate.ps1
    ```

    ![alt text](image-10.png)

    - 가상환경은 github에 올리지 말 것.. gitignore에 가상환경 폴더명 추가할 것


15. 객체지향 - [소스](./day03/ex15_oop.py) ~ - [소스](./day03/ex18_encapsule.py)
    - C++의 객체지향, 클래스와 동일
    - 접근제한자가 없음(public, privated, protected)
    - C++과 달리 new 안 씀, 변수등 선언 제약사항이 많이 없음
    - 클래스 내의 모든 함수의 파라미터는 `self`로 시작, C++의 this와 동일
    - 호출시에는 self를 사용 x
    - 파이썬의 철학 : `막지 말고, 알아서 지켜라`
    - public, private(__로 변수 선언),protected(변수선언), C++처럼 접근제한자를 많이 사용안함

16. 예외처리 - [소스](./day03/ex19_exception.py)
    - 비정상 종료를 막는 기능
    - try ~ exceot ~ finally로 구분지어서 사용 (else는 잘 사용안함)
    - except를 여러번 슬쑤 았낫, 'except Exception as e' 하나로 통일해도 무방
    - 예외처리가 발생하면 처리속도가 늦어짐, 비정상종료를 막기위한법

17. main

### 파일 입출력
- 인코딩
    - EUC-KR : 2바이트 한글 완성형 인코딩. CP949 동일한 의미
    - UTF-8 : 1바이트 영문(ASCII호환), 3바이트 한글, 4바이트 이모지 등 최대 4바이트 국제어표쥰
    - 대한민국 데이터 포털 제공하는 CSV는 EUC-KR 사용중. UTF-8 변환필요 

- CSV
    - 엑셀과 호환가능한 텍스트파일
    - 텍스트 양이 많으면 한번에 읽을 수 없음. 한줄씩 나눠서 읽어야함
    - 보통 CSV 라이브러리 사용

- JSON
    - Javascript Object Notation : 자바스크립트에서 데이터를 사용하기 위해 만든 표기방법
    - 딕셔너리를 텍스트화
    - 데이터를 네트워크로 전달할 때 가장 효율적인 파일형식
    - XML을 대체하는 기술
    - 저장된 json 파일을 사용 또는 OpenAPI 네트워크로 전달된 데이터를 사용

### 주피터 노트북
- 주피터 노트북
    - 파이썬을 좀 더 인터랙티브하게 사용하고자 하는 취지
    - Project Jupyter
    - 확장에서 Jupter 설치

- 사용법 - [노트북](./day03/ex20_jupyter_start.ipynb)
    - 명령 팔레트(Ctrl + Shit + P)

    ![alt text](image-11.png)

    - Untitled-1.ipynb 파일 생성, 파일 저장 우선
    - 커널 선택 클릭
    - 마크다운셀(일반적 설명글), 코드셀(소스코드 작성)로 구분

    ![alt text](image-12.png)

    - 최초 한번만 판업

- 주피터 노트북 단축키
    - a : [선택모드] 현재 셀 위에 코드셀 추가
    - b : [선택모드] 현재 셀 아래에 코드셀 추가된다.
    - enter : [선택모드] 현재 셀 편집모드로 진입(커서 깜빡임 확인)
    - Ctrl + enter : [편집모드] 마크다운셀은 빠져나오기, 코드셀을 실행
    - l : [선택모드]에서 라인번호 표시 토글
    - dd : [선택모드]에서 셀 삭제
    - alt + 위아래 방향기 : [선택모드] 셀 위치 변경
    - c : [선택모드]에서 셀 복사
    - v : [선택모드]에서 셀 붙여넣기

- 사용처
    - 웹상에서 동작하므로 많은 서비스를 지원, 로컬 컴퓨터보다 속도 느림
    - [Github Codespace](https://github.com/features/codespaces) - 기존 리포지토리와 연결 지원(무료일 경우 한달 140시간)
    - [Google Colab](https://colab.research.google.com/) - 구글에서 지원하는 노트북서비스, 90분 연결무료, 기능 제약적

### 데이터 분석 기초

- 분석용 기초 이론 - [노트북](./day03/ex21_dataprocess.ipynb)
    # - 리스트, 튜플, 딕셔너리
    - 리스트 컴프리헨션
    - 파일입출력
    - Numpy

## 4일차

### 데이터 분석 기초 - [노트북]()
    - Numpy
    - Pandas
    - Matplotlib
    - Seaborn
    - Folium
    - WordCloud
    - 기초통계
    - 데이터전처리

- 데이터분석 이유
    - 인사이트(Insight) : 특정한 맥락 속에서 특정 원인이나 효과를 이해하는 것
    - 방대한 데이터 속에서 패턴이나 인사이트(통찰)를 도출, `합리적인 의사결정`, `고객 행동 예측` , `운영 효율화`, `신규 비즈니스 기회 창출` 등을 하는 핵심 도구
        - 데이터 기반의 의사결정 기능
        - 고객 이해도 증가
        - 운영 효율성 및 비용 절감 
        - 트랜드 파악 및 경쟝력 강화
        - 미래 예측

