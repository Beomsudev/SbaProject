class Contact(object):
    def __init__():
        def __init__(self, name, phone, email, addr):
            pass # 위 파라미터를 보고 나머지 완성

        def print_info(self):
            print(f'이름 : {name}, 전화번호 : {phone}, 이메일 : {email}, 주소 : {addr}')

        @staticmethod
        def set_contact():
            name = input('이름') # 나머지 완성
            contact = Contact()
            return Contact

        @staticmethod
        def get_contact(clist):
            for i in clist:
                i.print_info()

        @staticmethod
        def del_contact(clist, name):
            for i, t in enumerate(clist):
                if t.name == name:
                    def clist[i]

        @staticmethod
        def print_menu()
            print('1 연락처 입력')
            print('2 연락처 출력')
            print('3 연락처 삭제')
            print('4 종료')
            menu = input('메뉴 선택')
            return menu
        
        @staticmethod
        def run():
            clist = []
            while 1:
                menu = Contact.print_menu()
                if menu == '1':
                    t = Contact.print_menu()
                    clist.append(t)

                if menu == '2':
                    pass # 직접 완성

                if menu == '3':
                    pass # 직접 완성

                else menu == '4':
                    break

if __name__ == '__main__':
    Contact.run()
"""
python의 데코레이터는 함수형 2가지, class형 2가지 총 4가지 방식을 통해 작성할 수 있습니다.
1. 함수형 decorator(데코레이터에 인수 전달이 없는 경우 X)
1) main 함수 제작(Decorator함수에 끌려갈 함수)
2) Decorator 함수에 전달받을 함수 받기 & Decorator 함수 안에 main 함수를 매개변수로 갖는 함수 제작(wrapper라고 주로 부름)
3) wrapper에서 전달받은 main 함수를 호출 or return(사용자 마음대로)
4) Decorator함수(wrapper 함수와 같은 위치)에서 wrapper를 return
2. 함수형 decorator(데코레이터에 인수 전달이 있는 경우 O)
1) main 함수 제작(Decorator함수를 먼저 작성해도 상관 없음.)
2) Decorator 함수 제작 인수 전달이 있는 경우엔 main 함수가 아니라 decorator의 매개변수를 먼저 불러옴.(decortator의 변수 지정)
3) decorator 안에 진짜 데코레이터(1.의 구조와같음) 구현 real_deco에서 main함수를 매개변수로 전달받는다.
4) real_deco의 안에 wrapper 생성(wrapper에서 function(main)의 매개변수를 받음.
5) real_deco에서 wrapper를 반환하고 가장 바깥의 main_deco에서 real_deco를 리턴한다.
3. Class 형 decorator(데코레이터에 인수가 없는 경우 X)
1) __init__메서드에 main함수(호출할 함수) 저장, self.function = function
2) __call__(인스턴스를 함수 호출처럼 사용가능하게 만들어줌.)메서드에 호출할 함수의 매개변수를 넘긴다.
3) 메인함수에 매개변수를 넣어서 호출하는 형태로 return
4. Class 형 decorator(데코레이터에 인수가 있는 경우 O)
1) __init__메서드에 decorator의 인수 저장
2) __call__ 메서드에 호출할 함수를 전달한다.
3) 메인함수에 매개변수를 넣어서 호출하는 형태로 return
4) __call__메서드에 wrapper 함수 생성 후 wrapper에 매개변수 전달
5) wrapper 함수에서 전달받은 함수 return6) __call__ 메서드의 리턴을 return wrapper(매개변수)과 같은 형식으로 한다.
"""

