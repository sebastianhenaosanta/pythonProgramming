total = 0

prices = {"banana": 4,
          "apple": 2,
          "orange": 1.5,
          "pear": 3
          }

stock = {"banana": 6,
          "apple": 0,
          "orange": 32,
          "pear": 15
        }

groceries = ["banana", "orange", "apple"]


def compute_bill(food):
    total = 0
    for i in food:
        if stock[i] > 0:
            total += prices[i]
            stock[i] -= 1
    return total



for i in prices:
    print(i)
    print("price: "+str(prices[i]))
    print("stock: "+str(stock[i]))
    total += prices[i]*stock[i] 

print(total)

