class worker():
    def __init__(self, type, salary, tools, do):
        self.type = type
        self.salary = salary
        self.tools = tools
        self.do = do
class chef(worker):
    def cuisine():
        return ("I can cook in a lot of cuisines like chinese, indian, italian, french and japanese")
class waiter(worker):
    def service():
        return ("I always give the customers a fresh plate and water when they come")
class janitor(worker):
    def clean():
        print("I always keep the restaunt clean and I properly clean the tables")
rohan = chef('chef', 50000, 'kitchen equipment', 'cookes food')
print("Rohan")
print("job", rohan.type)
print("salary", rohan.salary)
print("tools", rohan.tools)
print("what he does :",rohan.do)
print(chef.cuisine())
ram = waiter('waiter', 30000, 'note pad', 'takes orders and serves food')
print("\nRam")
print("job", ram.type)
print("salary", ram.salary)
print("tools", ram.tools)
print("what he does",ram.do)
print(waiter.service())
sham = janitor('janitor', 30000, 'broom', 'cleans tables and floor')
print("\nSham")
print("job", sham.type)
print("salary", sham.salary)
print("tools", sham.tools)
print("what he does", sham.do)
print(janitor.clean())