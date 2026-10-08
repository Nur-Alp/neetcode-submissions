class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = {}
        for i, bill in enumerate(bills):
            if bill == 5:
                money[5] = 1 + money.get(5, 0)
            elif bill == 10:
                if money.get(5, 0) >= 1:
                    money[5] = money[5] -1
                    money[10] = 1 + money.get(10, 0)
                else: 
                    return False
            else:
                if money.get(5, 0) >= 3:
                    money[5] = money[5] - 3
                elif money.get(5, 0) >= 1 and money.get(10, 0) >= 1:
                    money[5] = money[5] - 1
                    money[10] = money[10] - 1
                else:
                    return False
        return True

            