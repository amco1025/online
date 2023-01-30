class Pig:
    belly_price = 1000 # 클래스 변수
    def __init__(self, stock):
        self.stock = stock

    # 주문이 들어왔을 때의 가격 -> 메서드
    def order_price(self, amount):
        if self.stock >= amount:
            return self.belly_price * amount

        else:
            return "재고가 없어요."
            # return f"재고가 {self.stock}만큼 있습니다"
        

    def order(self, amount, money):
        
        price = self.order_price(amount)
        if price <= money:
            self.stock = self.stock - amount
            change = money - price
            return change
        else: 
            return '못삼'
        
a_pig = Pig(100)
b_pig = Pig(150)
# print(a_pig.belly_price)
# print(b_pig.belly_price)

b_pig.belly_price = 500
# print(a_pig.belly_price)
# print(b_pig.belly_price)

print(a_pig.stock)
print(a_pig.order(50, 10000000))
print(a_pig.stock)
print(b_pig.stock)