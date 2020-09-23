import sys
sys.path.insert(0, '/Users/bumsu/SbaProject')
from titanic.entity import Entity
import pandas as pd
import numpy as np

# sklearn algorithm : classification, regression, clustring, reduction
from sklearn.tree import DecisionTreeClassifier       # dtree
from sklearn.ensemble import RandomForestClassifier   # rforest
from sklearn.naive_bayes import GaussianNB           # nb
from sklearn.neighbors import KNeighborsClassifier    # knn
from sklearn.svm import SVC                          # svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold            # k값은 count의 의미로 이해 
from sklearn.model_selection import cross_val_score
# dtree, rforest, nb, knn, svm, 


"""
#answer# PassengerId  고객ID,
#answer# Survived 생존여부,  --> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
#dummy# Ticket 티켓번호,
Fare 요금,
#dummy# Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Service:
    def __init__(self):
        self.entity = Entity()  
        pass

    
    def new_model(self, payload) -> object:
        this = self.entity
        this.fname = payload
        return pd.read_csv(this.context + this.fname) # p.139  df = tensor

    @staticmethod
    def create_train(this) -> object:
        return this.train.drop('Survived', axis=1) # train 은 답이 제거된 데이터셋이다. 

    @staticmethod
    def create_label(this) -> object:
        return this.train['Survived'] # label 은 곧 답이 된다.

    @staticmethod
    def drop_feature(this, feature) -> object:
        this.train = this.train.drop([feature], axis = 1)
        this.test = this.test.drop([feature], axis = 1) # p.149 에 보면 훈련, 테스트 세트로 나눈다
        return this

    @staticmethod
    def pclass_ordinal(this) -> object:
        return this

    @staticmethod
    def title_nominal(this) -> object:  # name에서 중간의 mr, ms 등만 따옴
        combine = [this.train, this.test]
        for dataset in combine:
            dataset['Title'] = dataset.Name.str.extract('([A-Za-z]+)\.', expand=False)  # Mr. 부분 추출 / 영어만 혀용 A-Za-z / 한글 추가 A-Za-zㄱ-힣 / 숫자 추가 A-Za-zㄱ-힣0-9 띄워 쓰기 없음 / \.은 .을 호출자로 사용 안하 고 문자로 인식 Mr.의 .
        for dataset in combine:
            dataset['Title'] = dataset['Title'].replace(['Capt', 'Col', 'Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona', 'Mme'], 'Rare')
            dataset['Title'] = dataset['Title'].replace(['Countess', 'Lady', 'Sir'], 'Royal')
            dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
            dataset['Title'] = dataset['Title'].replace('Mlle', 'Mr')
        title_mapping = {'Mr':1, 'Miss':2, 'Mrs':3, 'Master':4, 'Royal':5, 'Rare':6}
        for dataset in combine:
            dataset['Title'] = dataset['Title'].map(title_mapping)
            dataset['Title'] = dataset['Title'].fillna(0)
        this.train = this.train
        this.test = this.test
        return this

    @staticmethod
    def sex_nominal(this) -> object:
        # male = 0, female = 1
        combine = [this.train, this.test]   # train과 test가 묶입니다.
        sex_mapping = {'male':0, 'female':1}
        for dataset in combine:
            dataset['Sex'] = dataset['Sex'].map(sex_mapping)
        
        this.train = this.train # overriding 분리
        this.test = this.test
        return this

    @staticmethod
    def age_ordinal(this) -> object:
        train = this.train
        test = this.test
        train['Age'] = train['Age'].fillna(-0.5)
        test['Age'] = test['Age'].fillna(-0.5)

        # null age를 평균 or 다수결로 넣기에는 근거가 없다 
        # 특히 age는 생존률 판단에서 가중치(weight)가 높으므로 디테일한 접근이 필요
        # 나이를 모르는 승객은 모르는 상태로 처리해야 값의 왜곡을 줄일수 있어서
        # -0.5 라는 중간값으로 처리
        bins = [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]   # np.inf = 없는 값
        # []에 있으니 이것은 변수명 이겠군요.. 라고 판단하면 잘 이해함
        labels = ['Unknown', 'Baby', 'Child', 'Teenager','Student','Young Adult', 'Adult', 'Senior']
        # [] 은 변수명으로 선언됨
        train['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        test['AgeGroup'] = pd.cut(train['Age'], bins, labels=labels)
        age_title_mapping = {
            0: 'Unknown',
            1: 'Baby',
            2: 'Child',
            3: 'Teenager',
            4: 'Student',
            5: 'Young Adult',
            6: 'Adult',
            7: 'Senior'
        } # 이렇게 []에서 {}으로 처리하면 labels를 값으로 처리
        for x in range(len(train['AgeGroup'])):
            if train['AgeGroup'][x] == 'Unknown':
                train['AgeGroup'][x] = age_title_mapping[train['Title'][x]]
        for x in range(len(test['AgeGroup'])):
            if test['AgeGroup'][x] == 'Unknown':
                test['AgeGroup'][x] = age_title_mapping[test['Title'][x]]
        
        age_mapping = {
            'Unknown': 0,
            'Baby': 1,
            'Child': 2,
            'Teenager': 3,
            'Student': 4,
            'Young Adult': 5,
            'Adult': 6,
            'Senior': 7
        }
        train['AgeGroup'] = train['AgeGroup'].map(age_mapping)
        test['AgeGroup'] = test['AgeGroup'].map(age_mapping)
        this.train = train
        this.test = test
        return this

    # 가중치가 적으므로 pass 나중에 내가 혼자 할때는 넣어 보기!
    # @staticmethod
    # def sipsp_numeric(this) -> object:
    #     return this

    # @staticmethod
    # def parch_numeric(this) -> object:
    #     return this        
                
    @staticmethod
    def fare_ordinal(this) -> object:
        this.train['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        this.test['FareBand'] = pd.qcut(this['Fare'], 4, labels={1, 2, 3, 4})
        return this  

    @staticmethod
    def fareBand_nominal(this) -> object:  # 요금이 다양하니 클러스트링을 하기 위한 준비
        this.train = this.train.fillna({'FareBand' : 1})
        this.test = this.train.fillna({'FareBand' : 1})
        return this

    @staticmethod
    def embarked_nominal(this) -> object:
        this.train = this.train.fillna({'Embarked':'S'})    # s가 가장 많기에 null(누락데이터)를 대체
        this.test = this.test.fillna({'Embarked':'S'})
        # 많은 머신러닝 라이브러리는 클래스 레이블이 *!정수!* 로 인코딩 되었다고 기대함
        # 교과서 p146 문자 blue = 0, green = 1, red = 2 로 치환 -> mapping 한다고 함
        this.train['Embarked'] = this.train['Embarked'].map({'S' : 1, 'C' : 2, 'Q' : 3})    # 치환 된다고 해서 ordinal로 해석 하진 않는다.
        this.test['Embarked'] = this.test['Embarked'].map({'S' : 1, 'C' : 2, 'Q' : 3})    # 치환 된다고 해서 ordinal로 해석 하진 않는다.
        return this 


    # Learning Algrothm 중에서 dtree, rforest, nb, knn, svm 이것을 대표로 사용

    @staticmethod
    def create_k_fold():
        return KFold(n_splits=10, shuffle=True, random_state=0)

    def accuracy_by_dtree(self, this):
        drtee = DecisionTreeClassifier()
        score = cross_val_score(drtee, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
        
    def accuracy_by_rforest(self, this):
        rforest = RandomForestClassifier()
        score = cross_val_score(rforest, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
        
    def accuracy_by_nb(self, this):
        nb = GaussianNB()
        score = cross_val_score(nb, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
        
    def accuracy_by_knn(self, this):
        knn = KNeighborsClassifier()
        score = cross_val_score(knn, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)
        
    def accuracy_by_svm(self, this):
        svm = SVC()
        score = cross_val_score(svm, this.train, this.label, cv=Service.create_k_fold(), n_jobs=1, scoring='accuracy')
        return round(np.mean(score) * 100, 2)

