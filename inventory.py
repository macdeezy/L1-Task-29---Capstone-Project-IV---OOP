# We create a class called Shoe.

class Shoe:

    # We create a constructor method with parameters, self, country, code, product, cost, quantity.

    def __init__(self, country, code, product, cost, quantity):

        # We create our Attributes within our class Shoe.
        # Were we set self to country,code,product,cost,quantity.

        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    # Create a method called get_cost.
    # Return self.cost.

    def get_cost(self):
        return self.cost
    
    # Create a method called file_updated with parameter self.
    # Then return with .format the self.country,code,product,cost,quantity.

    def file_updated(self):
        return f'''{self.country},{self.code},{self.product},{self.cost},{self.quantity}'''

    # Create a methos called get_quantity with parameter self.
    # Then return self.quantity.

    def get_quantity(self):
        return self.quantity
    
    # We then create a toString method.
    # Then return in our parameters country,code,product,cost,quantity.

    def __str__(self):
        return (f'''\nCountry:{self.country}
Shoe Code: {self.code}
Shoe Name: {self.product}
Shoe Cost: {self.cost}
Quantity: {self.quantity}\n''')

# We create an open list with the variable shoe_list
# This is where all the list will be appended.

shoe_list = []

# We create a function called read_shoes_data.
# We then also open our textfile called inventory.txt and read from it.
# We name the it as shoe_list_inventory.
# Then we create a variavble shoe_list_inside_file.
# We will use the .readlines to read through everyline in the textfile.

def read_shoes_data():

    try:

        with open('inventory.txt', 'r') as shoe_list_inventory:
            shoe_list_inside_file = shoe_list_inventory.readlines()
        

        # Then we create a for loop. 
        # We then say for line in the range 1 meaning our seconf line in the textfile.
        # Then we calculate using len passing parameter (shoe_inside_file).
        
        for line in range(1, len(shoe_list_inside_file)):
                
                # Then we say country, code, product, cost, quantity.
                # Then assign it to shoe_list_insidefile[line].
                # We then strip it to remove any new lines.
                # Then split it at the commas after its converted into a list.

                country, code, product, cost, quantity = shoe_list_inside_file[line].strip('\n').split(',')

                # We create an object named shoes. 
                # We call the shoe class.
                # And pass in country,code,product,cost as a float and quantity as an integer
                # Then we append shoes to our global list shoe_list.

                shoes = Shoe(country,code,product,float(cost),int(quantity))
                shoe_list.append(shoes)
    
    except FileNotFoundError:
        print('inventory file not found. Please check file name correctly')
      

read_shoes_data()
   
# We create a method called capture_shoes
# We pass in parameters(shoe_country,shoe_code,shoe_name,shoe_cost,shoe_quantity)
# We then create an object named shoes_captured.
# We the append to our shoe_list.

def capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity):
    shoes_captured = Shoe(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity)
    shoe_list.append(shoes_captured)
   


# We create a new method.
# This is will update the quantity once.

def update():

    # Create a variable called obj_data.
    # This will take my intake my shoe objects.

    obj_data = f'Country,Code,Product,Cost,Quantity'

    # Create a for loop for the to iterate over the shoe list.
    
    for shoe in shoe_list:
        obj_data += '\n' + shoe.file_updated()

    # We then open our file and write to it.

    with open('inventory.txt', 'w') as shoe_list_inventory:
        shoe_list_inventory.write(obj_data)  

# We create a function called view_all
# This function will print all details of the shoes.
# We call the print function.
# To print all my shoe_list using the __str__ method.

def view_all():
    print(*shoe_list)

# We create a method called re_stock.

def re_stock():

    # We create a variable called qty(quantity) initialse it to shoe_list index 0.
    # We then create a counter called shoe_index intialise it to 0.

    qty = shoe_list[0].quantity
    shoe_index = 0

    # Then we make a for loop and use enumerate to iterate our shoe list.
    # enumerate will allow us to iterate (shoe_list) and keep track of the index and element.
    # We then create an if stamtement where s.get_quantity which is our method.
    # Then we set variable qty to our method.

    for i, s in enumerate(shoe_list):
        if s.get_quantity() < qty:
          qty = s.quantity
          shoe_index = i

    # Then we return the shoe_index.

    return shoe_index
  

    
# We create a method called search_shoe.
# Pass the parameter s_code, which is our variable below.

def search_shoe(s_code):
   
   # We then create a for loop for our shoe_code in the shoe_list.
   # Create an if statement were our shoe_code call the .code.
   # if its eqauls to the parameter from the users input.
   # Then return the shoe_code.
   # if not found then return that the shoe code is not found.

    for shoe_code in shoe_list:
        if shoe_code.code == s_code:
            return shoe_code 
    
    return f'The shoe code {s_code} is not found\n'
    

# We create a method called value_per_item.

def value_per_item():

    # We create a for loop to iterate through the shoe_list.
    # We then create our calculation.
    # Where the cost and quantity are assigned to value.
    # thne we print out our shoes and the value.

    for s in shoe_list:
        value = s.cost * s.quantity
        print(f'{s}Value: {value}\n')


# We then create a method called highest_qty().
# Create a counter called shoe_index initialse it to 0.
# Create a varible called max_quatity. 
# Which will then take the shoe_list and the counter and call method.get_quantity.

def highest_qty():
    shoe_index = 0
    max_quantity = shoe_list[shoe_index].get_quantity()

    # Then we make a for loop and use enumerate to iterate our shoe list.
    # enumerate will allow us to iterate (shoe_list) and keep track of the index and element.
    # We then create an if stamtement where shoe.get_quantity which is our method.

    for s, shoe in enumerate(shoe_list):
        if shoe.get_quantity() > max_quantity:
            max_quantity = shoe.get_quantity()
            shoe_index = s

    # We print the sale and the shoe_list[shoe_index].

    print(f'Sale Sale Sale, This shoe is on sale {shoe_list[shoe_index]}\n')


# This is were we create our logic.

user_choice = ''' '''

# We create a while loop.

while user_choice != 'end stock taking':
    user_choice = input('''\nPlease view below and select
    capture = Capture data about a shoe
    view = This will view all the shoes
    restock = Find shoe that needs to be restocked
    find shoe - This will search for a shoe
    value = Calculate the total value
    sale = Shoe on sale \n''').lower()

    # When users enters 'capture'
    # The varaibles shoe_country,shoe_code,shoe_name,shoe_cost,shoe_quantity.
    # Variables will be invoked. 
    # Then we call our capture_shoes method.

    if user_choice == 'capture':

        shoe_country = input('Please enter the country of the shoes ')
        shoe_code = input('Please enter the shoe code ')
        shoe_name = input('Please enter product name ')
        shoe_cost = float(input('Please enter the cost of the shoe ')) 
        shoe_quantity = int(input('Please enter the quantity of the shoes '))
        capture_shoes(shoe_country, shoe_code, shoe_name, shoe_cost, shoe_quantity )

    # When a user enters 'view'.
    # We call upon the zoom method.

    elif user_choice == 'view':
        view_all()

    # When user enters restock.
    # We create an index for the shoes.
    # Assign it to the function re_stock().

    elif user_choice == 'restock':
        shoe_index = re_stock()

    # We then print the shoe with the lowest quantity.
    # Create a new variable to if user would like to restock.

        print(f' This is the shoe with the lowest quantity from all your stocking {shoe_list[shoe_index]} ')
        restock_choice = input('''Please see the quantity above and advise if you will be restocking
Please choose:
Yes - for the restock
No -  for not restocking \n''')
        

    # We create an if statement if user selects yes or no
    # if 'yes' we take object,quantity an request user to input new quantity.

        if restock_choice == 'yes':
            shoe_list[shoe_index].quantity = int(input('Please enter new quantity number: \n'))
    
    # if 'no' we will print that quantity will remain the same.
        if restock_choice == 'no':
            print('Quantity will remain the same\n')

        # We then call our methods update() and re_stock().

        update()
        re_stock()
       
        
    # if the 'find shoe' is entered.
    # We create a variable called s_code which is our parameter.
    # Then we print(the shearch_shoe method and pass (s_code)).

    elif user_choice == 'find shoe':
        s_code = input('Please enter the shoe code you looking for: ')
        
        print(f'{search_shoe(s_code)}')
        
    # if the user enters 'value'
    # We call the value function. 

    elif user_choice == 'value':
        value_per_item()
    
    # We the user enters 'sale'.
    # Then we call the highest_qty() function.

    elif user_choice == 'sale':
        highest_qty()

    # if user enters 'end stock taking'
    # then we exist the programme.

    elif user_choice == 'end stock taking':
        print('Thank you')
    
    # if user enters any incorrect string.
    # The else statement will be executed.

    else:
        print('Please select correctly what you would like to do.')
