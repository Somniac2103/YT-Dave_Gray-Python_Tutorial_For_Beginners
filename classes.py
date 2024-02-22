class Vechile:
  def __init__(self, make, model):
    self.make = make
    self.model = model

  def moves(self):
    print('Moves along...')

  def get_make_model(self):
    print(f"I'm a {self.make} {self.model}.")

my_car = Vechile('Tesla', 'Model 3')

print(my_car.make)
my_car.moves()
my_car.get_make_model()

your_car = Vechile('Cadillac', 'Escalade')
your_car.moves()
your_car.get_make_model()

class Airplane(Vechile):
  def __init__(self, make, model, faa_id):
    super().__init__(make,model)
    self.faaid = faa_id

  def moves(self):
    print('Flies along..')

class Truck(Vechile):
  def moves(self):
    print('Rumbles along..')

class GolfCart(Vechile):
  pass

cessna = Airplane('Cessna', 'Skyhawk', 'n-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

for v in (my_car, your_car, cessna, mack, golfwagon):
  v.get_make_model()
  v.moves()
  

