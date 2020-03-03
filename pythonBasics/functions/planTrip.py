def hotel_cost(nights):
  return nights*140

def plane_ride_cost(city):
  if city == "Charlotte":
    return 183
  elif city == "Tampa":
    return 220
  elif city == "Pittsburgh":
    return 222
  elif city == "Los Angeles":
    return 475
  
def rental_car_cost(days):
  costPerDay = 40
  total = 40*days
  if days >= 7:
    total = costPerDay*days - 50
  elif days >= 3:
    total = costPerDay*days - 20
  return total

def trip_cost(city, days, spending_money):
  return rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money  

print(trip_cost("Los Angeles",5,600))
