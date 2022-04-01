class User():
  first_name = ""
  last_name = ""
  email_address = ""
  phone_number = ""
  allergies = ""
  food_diet = ""

  def get_full_name(self):
    return "{} {}".format(self.first_name, self.last_name)


class fullMenu():
  mealItems = []
  date = ""


class Meals():
  name = ""
  serving_size = ""
  full_description = ""
  ingredients = ""


class Price():
  amount = ""
  quantity = ""
  totalPrice = ""


class Order(Meals, Price):
  orderId = ""
  short_description = ""
  isPacked = False
  additional_needs = ""


user = User()  # instantiate the user class
user.first_name = "Agatha"
user.last_name = "Ambrose"
user.phone_number = "+233256611702"
user.email_address = "agathambrose@gmail.com"
user.allergies = "fish, olives"

