"""
0. 기본 개념
"""

### 0-1. 변수

name = 'gyubeen'
print(name)
age = 28
print(age)

# line을 실행하면 print 없이도 값 출력 가능
age


### 0-2. 식별자

snake_case = 'snake_case'            # 변수, 함수명으로 활용
CamelCase = 'CamelCase'             # 클래스명으로 활용

# # 불가능한 식별자
# 1stcourse = 'python and datatypes'  # 숫자로 시작하는 경우.
# course name = 'basic python course' # 띄어쓰기가 포함된 경우.
# break = '10 minutes'                # keyword.

# keyword (식별자 사용 X) 확인
import keyword
keyword.kwlist  # 추가로 자료형을 나타내는 str, list 등도 지양.

### 0-3. 주석

# 한 줄 주석. line 선택 후 'cntl + /'로 단축키 사용 가능!

'''
여러 줄에 주석이 필요한 경우
'''
"""
이런 식으로
입력 할 수 있다.
"""

### 0.4 추가 내용
type(name)                          # type으로 자료형(datatype) 확인 가능
del(name)                           # del으로 변수, 함수 등 삭제 가능
del(age, snake_case, CamelCase)     # 여러 개 동시에도 삭제 가능

"""
1. 수치 자료형
"""

### 1-0. 종류

int_type = 1
float_type = 1.1
complex_type = 1+1j

### 1-1. int (integer. 정수)

num1 = 1
num2 = int(1)
num3 = int(1.5)     # 정수 부분만
num4 = int('1')     # 문자를 정수로 바꿀 수 있다.
num5 = int(-1.9)    # 음수도 정수 부분만

del (num1,num2,num3,num4,num5)


### 1-2. float (floating point. 실수, 부동소수점)
# python엔 double이 없다.

num1 = 1.1
num2 = float(1.1)
num3 = 1.               # 정수를 실수형으로 저장하고 싶다면 .을 붙인다.
num4 = float(1)         # 아니면 직접 선언
num5 = float('1.1')     # 문자를 바꿀 수 있다.
num6 = float(-1.5)      # 음수도 가능

del (num1,num2,num3,num4,num5,num6)

### 1-3. complex (complex. 복소수)
num1 = 1+1j
num2 = complex(1,1)     # 각각 정수부, 허수부
num3 = 1+0j             # 정수를 복소수로 저장하려면 0j를 추가한다.
num4 = complex(1)       # 아니면 직접 선언
num5 = complex('1+1j')  # 문자를 바꿀 수 있다.
num6 = complex(-1,-1)   # 음수도 가능

del (num1,num2,num3,num4,num5,num6)


### 1.4 수치 연산
3+2     # 덧셈 (3)
3-2     # 뺄셈(3)
3*2     # 곱셈 (2)
3/2     # 나눗셈 (2)
3//2    # 몫 (2)
3%2     # 나머지 (2)
3**2    # 제곱 (1)

# # 참고사항
# # 1. ^는 제곱이 아니라 이진 연산 XOR gate이니 주의!
# 3^2 # 11, 10 -> XOR -> 01 -> 1
# # 2. 다른 수치 자료형끼리 연산이 가능하다!
# 1 + 1.1
# 3 * (1+4j)
# # 3. 연산 우선순위를 바꾸기 위해서 ()사용 가능.
# (1+3)*2
# 3*1+4j
#
# # 되도록 깔끔하게 표현되는 선에서는 괄호를 사용하는 것을 추천.

"""
2. 불 자료형
"""

### 2-1. bool (boolean. 불리언, 논리연산자)
tf1 = True
tf2 = bool(False)
tf3 = bool(0)               # 0은 False를 의미
tf4 = bool(1)               # 1은 True를 의미
tf5 = bool(5)               # 0이 아닌 모든 값은 True
tf6 = bool('abc')           # 문자열도 True
tf7 = bool('0')             # 문자 0도 0이 아니므로 True
tf8 = bool([1,2,3,4])       # 딕셔너리 등 다른 모든 불, 군집 자료형, 기타 자료형 모두 True
tf9 = bool(0.0)             # 수치형 0은 int가 아니어도 False
tf10 = bool(complex(0,0))   # complex도 마찬가지
del (tf1,tf2,tf3,tf4,tf5,tf6,tf7,tf8,tf9,tf10)


"""
3. 군집 자료형
"""

### 3-0. 종류

str_type = 'string'
list_type = ['val1', 'val2', 'val3']
tuple_type = ('val1', 'val2', 'val3')
set_type = {'val1', 'val2', 'val3'}
dict_type = {'key1':'value', 'key2': 'value'}


### 3-1. str (string. 문자열) : 순서 O, 중복 O, 수정 X
# 선언
string1 = '내용'
string2 = str(1)        # 숫자를 문자로 저장 가능
string3 = str([1,2,3])  # 다른 data type도 문자로 저장 가능
string4 = ''            # 비어있는 string 선언
string5 = str()         # 이런 방식도 가능

# 활용 (순서)
sample_string = '012345'
sample_string[0]        # indexing.
sample_string[1:3]      # slicing. [a:b] -> a 이상 b 미만의 index만 출력
len(sample_string)      # 길이
sample_string.index('2')# index
sample_string.count('3')
sample_string.find('5')

'123'+'456'             # string 합치기
'123'* 3                # string 반복하기

# 심화
''.join(['1','2','3'])          # list 내의 string 합치기
' and '.join(['1','2','3'])     # list 내의 string 합치기 (기준값)
'1 2 3'.split()                 # string 분할
'1a2a3'.split('a')              # string 분할 (기준값)
sorted('159246')                # string sorting하여 list로 저장
val = input('값을 입력하시오. :')  # input값 입력받아서 저장하기


### 3-2. list (list, 리스트) : 순서 O, 중복 O, 수정 O
# 선언
l1 = [1,2,3]
l2 = list((1,2,3))              # tuple을 list로 저장
l3 = list('1234')               # string을 list로 저장
l4 = []                         # 비어있는 list 생성
l5 = list()                     # 이렇게도 가능
l6 = [1, True, 'a', [1], None]  # 모든 수치, 불, 군집, 기타 자료형 모두 가능

# 활용 (순서)
sample_list = [0,1,2,3,4,5]
sample_list[0]                  # indexing
sample_list[-1]                 # 마지막 index 값 추출
sample_list[1:4]                # 1 이상 4 미만인 index 값 추출
len(sample_list)                # list 길이
sample_list.index(0)            # 해당값의 index
sample_list.count(3)            # 개수 세기

[1,2,3] + [4,5,6]               # list 합치기
[1,2,3] * 2                     # list 반복

# 활용 (수정) 1추가 2삭제 3특정값 바꿔주기 4순서바꾸기
sample_list.append(6)           # 값 추가 (맨 뒤)
sample_list.insert(1,3)         # 값 추가 (특정 index)
sample_list.extend([1,2,3])     # 여러 값 추가
sample_list.remove(6)           # 값 제거
del sample_list[5]              # 값 제거
sample_list.clear()             # 모든 값 제거
sample_list[0] = 99             # 값 수정
sample_list.sort()              # 정렬 (오름차순 정렬)
sample_list.sort(reverse=True)  # 역방향 정렬 (내림차순 정렬)
sample_list.reverse()           # 순서 뒤집기 (리스트 뒤집기)

a = [1,7,2,3,55]
a.sort(reverse=True)
a

a.reverse()
a


### 3-3. tuple (tuple, 튜플) : 순서 O, 중복 O, 수정 X
# 선언
t1 = (1,2,3)
t2 = tuple([1,2,3])             # 리스트를 튜플로 저장
t3 = tuple('1234')              # string을 튜플로 저장
t4 = ()                         # 비어있는 튜플 생성
t5 = tuple()                    # 비어있는 튜플 생성
t6 = (1,)                       # 값이 하나인 튜플 (1)은 그냥 i으로 인식
t7 = (1,'1', [1], (1,), None)   # 모든 자료형 가능

# 활용 (순서)
sample_tuple = (1,2,3,4,5)
sample_tuple[0]                 # indexing
sample_tuple[-1]                # indexing, 마지막 값
sample_tuple[2:4]               # 2이상 4미만 index 값 추출
len(sample_tuple)               # 튜플 길이
sample_tuple.index(1)           # 특정 값 index 추출
sample_tuple.count(3)           # 특정 값 개수 세기

(1,2,3) + (4,5,6)               # 튜플 합치기
(1,2,3) * 2                     # 튜플 반복

### 3-4. set (set. 집합) : 순서 X, 중복 X, 수정 O
# 선언
s1 = {1,2,3}
s2 = set([1,2,3])               # list를 set으로 저장
s3 = set('123')                 # string을 set으로 저장
s4 = set()                      # 비어있는 집합 만들기
s5 = {1, '1', None}             # 모든 자료형 가능
s6 = {1, 2, 2, 3, 3, 3}         # 중복 불가능

# 연산
{1,2,3} | {3,4,5}               # 합집합
{1,2,3}.union({3,4,5})          # 합집합
{1,2,3} & {3,4,5}               # 교집합
{1,2,3}.intersection({3,4,5})   # 교집함
{1,2,3} - {3,4,5}               # 차집합
{1,2,3}.difference({3,4,5})     # 차집합

# 활용 (수정)
sample_set = {1,2,3}
sample_set.add(4)               # 값 추가
sample_set.update([4,5,6])      # 값 추가 (여러 개)
sample_set.remove(3)            # 값 제거

### 3-5. dict (dictionary. 딕셔너리,사전 =hash) : 순서 X (key-value), 중복 key X, value O, 수정 O
# 선언
d1 = {'1':1, '2':2,'3':3}
d2 = {}                                 # 비어있는 dict
d3 = dict()                             # 비어있는 dict
d4 = {1:1, '2':'2', (3,):(3,), None:None}  # key엔 수치형, string, tuple, None만 가능. value엔 모든 자료형 가능
d5 = {1:1,1:2,1:3}                      # key에 중복이 있을 경우 하나만 인식
d6 = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

{'key1':'value1', 'key1':'value2', 'key1':'value3'}
{'key1':'value1', 'key2':'value1', 'key3':'value1'}

# 활용 (key-value)
sample_dict = {'key1':1, '2':2, '3':3}
# sample_dict에는 key로 1, '2', '3'이 저장되어있고, value에 1,2,3이 저장되어있음

sample_dict['key1']                          # key로 색인. 여기서 1은 1번 index의 값이 아니라 key 1에 대한 값을 달라는 의미.
sample_dict['2']                        # key로 색인
sample_dict.keys()                      # 모든 key 값
sample_dict.values()                    # 모든 value 값
sample_dict.items()                     # 모든 (key-value) 쌍
len(sample_dict)                        # dict 길이

# 활용 (수정)
sample_dict['name'] = 'kyeongjun'       # 값 추가 ('name'이란 key가 없어서 추가됨)
sample_dict['key1'] = 2                      # 값 수정 (1이란 key가 있어서 수정됨)
del sample_dict['name']                 # 값 제거
sample_dict.clear()                     # 모든 값 제거


### 3-6. 기타
# 공통 기능
'a' in 'abc'                # string 안에 포함되었는지
'a' not in 'abc'            # string 안에 포함되지 않았는지
1 in [1,2,3]                # list도 가능
2 in (1,2,3)                # tuple도 가능
3 in {1,2,3}                # set도 가능
'1' in {'1':1}              # dict도 가능 (key 기준)
1 in {'1':1}                # dict의 value로는 불가능
1 in {'1':1}.values()       # dict의 value에 대한 포함 여부는 이렇게 확인

