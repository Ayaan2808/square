class car():
    print("WELCOME TO ASPIRATION CARS:\nWe have:\nBMW\nAudi\nJaguar")
    def __init__(self,model,price,color,seats):
        self.model = model
        self.price = price
        self.color = color
        self.seats = seats
class BMWs(car):
    def  ventilation():
        return ("Features : This car has a strong AC which you can adjust")
class Audis(car):
    def auto_drive():
        return ("Features : This car has has a auto drive feaature in which the car will auto drive to you location")
class Jaguars(car):
    def shocker():
        return ("Feature : This can has a very good shocker which doesn't let you feel the rough drive")
    def GPS():
        return ("it also has a GPS screen in the car.")

bmw = BMWs("3 Series M340i xDrive Sedan", 100000000, "gray",5)
print("\nDetails of BMW:")
print("Model :", bmw.model)
print("Price :", bmw.price)
print("color :", bmw.color)
print("Seats :", bmw.seats)
print(BMWs.ventilation())

Audi = Audis("R8 2022",30000000,'blue',5)
print("\nDetails of Audi")
print("Model :",Audi.model)
print("Price :", Audi.price)
print("Color :", Audi.color)
print("Seats :", Audi.seats)
print(Audis.auto_drive())

Jaguar = Jaguars("I-PACE", 20000000, "black", 5)
print("\nDetails for Jaguar")
print("Model :", Jaguar.model)
print("Price :", Jaguar.price)
print("Color :", Jaguar.color)
print("Seats :", Jaguar.seats)
print(Jaguars.shocker())
print(Jaguars.GPS())
class check():
    inp = input('\nwhat car would you like?')
    if inp == 'BMW':
        print("congratulations you just bought a BMW 3 Series M340i xDrive Sedan")
    elif inp == 'Jaguar':
        print("congratulations you just bought a jaguar I-PACE")
    elif inp == 'Audi':
        print("congratulations you just bought a audi R8")