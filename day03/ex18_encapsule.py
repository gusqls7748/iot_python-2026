## ex18_encapsule.py 캡슐화

class Account:
    def __init__(self, money):
        self.__balance = money # 정상

    def deposit(self, money):
        # self.__balance 라고 써야 합니다. (self. 이 빠짐)
        self.__balance += money 

    def get_balance(self):
        # 여기서도 self.__balance 라고 써야 합니다.
        return self.__balance
    

if __name__=='__main__':
    myacc = Account(1000000)
    print(f'계좌금액은 {myacc.get_balance():,}원')
    #print(f'계좌금액 : {myacc__balance}달러')

    myacc.deposit(100_000) # 정수를 사용시 _로 1000단위 구분가능
    print(f'계좌금액은 {myacc.get_balance():,}원')

    myacc.balance = -1000000000 # 맴버변수에 직접접근가능
    print(f'계좌금액은 {myacc.get_balance():,}원')
