class Pizza:
  def __init__(self, toppings):
    self.toppings = toppings

  @staticmethod
  def validate_topping(topping):
    if topping == "pineapple":
      raise ValueError("No pineapples!")
    else:
      return True

ingredients = ["cheese", "onions", "spam", "apple"]
if all(Pizza.validate_topping(i) for i in ingredients):
  pizza = Pizza(ingredients)
for top in pizza.toppings:
    print(top)