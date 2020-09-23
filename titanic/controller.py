import sys
sys.path.insert(0, '/Users/bumsu/SbaProject')
from titanic.entity import Entity
from titanic.service import Service

"""
PassengerId  고객ID,
Survived 생존여부,  --> 머신러닝 모델이 맞춰야 할 답 
Pclass 승선권 1 = 1등석, 2 = 2등석, 3 = 3등석,
Name,
Sex,
Age,
SibSp 동반한 형제, 자매, 배우자,
Parch 동반한 부모, 자식,
Ticket 티켓번호,
Fare 요금,
Cabin 객실번호,
Embarked 승선한 항구명 C = 쉐브루, Q = 퀸즈타운, S = 사우스햄튼
"""

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def modeling(self, train, test):
        service = self.service
        this = self.preprocessing(train, test)
        
        this.label = service.create_label(this)
        this.train = service.create_train(this)

        return this

    def preprocessing(self, train, test):
        service = self.service
        this = self.entity

        this.train = service.new_model(train) # payload
        this.test = service.new_model(test) # payload
        this.id = this.test['PassengerId'] # machine 이에게는 이것이 question 이 됩니다. 

        print(f'드롭 전 변수 : \n{this.train.columns}')
        print('-'*50)
        this = service.drop_feature(this, 'Cabin')
        this = service.drop_feature(this, 'Ticket')
        print(f'드롭 후 변수 : \n{this.train.columns}')
        print('-'*50)
        this = service.title_nominal(this)  # name 변수에서 title 을 추출 했으니 name은 필요 없어 졌고, str이니 후에 Ml-lib가 이를 인식하는 과정에서 에러를 발생 시킨다
        this = service.drop_feature(this, 'Name')
        this = service.drop_feature(this, 'PassengerId')

        this = service.age_ordinal(this)

        this = service.sex_nominal(this)

        this = service.embarked_nominal(this)
        
        this = service.fareBand_nominal(this)
        this = service.drop_feature(this, 'Fare')
        print(f'train 정제결과:\n{this.train.head()}')
        print('-'*50)
        print(f'test 정제결과:\n{this.test.head()}')
        print('-'*50)
        print(f'train na 체크:\n{this.train.isnull().sum()}')
        print('-'*50)
        print(f'test na 체크:\n{this.test.isnull().sum()}')
        return this
        

    def learning(self, train, test):
        service = self.service
        this = self.modeling(train, test)


        print('-'*50 + 'Learning 결과' + '-'*50)
        print(f'결정트리 검증결과 : {service.accuracy_by_dtree(this)}')
        print(f'랜덤포리 검증결과 : {service.accuracy_by_rforest(this)}')
        print(f'나이브베이즈 검증결과 : {service.accuracy_by_nb(this)}')
        print(f'KNN 검증결과 : {service.accuracy_by_knn(this)}')
        print(f'SVM 검증결과 : {service.accuracy_by_svm(this)}')

    def submit(self): # machine 이 된다. 이 단계는 캐글에게 내 머신이를 보내서 평가받게 하는 것 입니다. 마치 수능장에 자식보낸 부모님 마음 ...
        pass


if __name__ == '__main__':
    ctrl = Controller()
    ctrl.learning('train.csv','test.csv')