# Develop a Python program for a small shop to process customer purchases. Store product names and prices in a dictionary, items added to the cart in a list, product categories in a set, 
# and product details using tuples. Create functions to display products, add items to the cart, and calculate the total bill. Use a recursive function to compute the total price of all items in the cart. 
# Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError (calculation errors), TypeError (wrong data types in the cart), and NameError (when a product 
# name entered by the user does not exist). 
'''Example Output: 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 1 
Available Products: 
Pen : 10 
Notebook : 50 
Pencil : 5 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 2 
Enter product name: Pen 
Enter quantity: 3 
Item added to cart successfully. 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 2 
Enter product name: Notebook 
Enter quantity: 2 
Item added to cart successfully. 
1. Display Products 
2. Add Item to Cart 
3. View Total Bill 
4. Exit 
Enter choice: 3 
Items in Cart: 
Pen x 3 
Notebook x 2 
Total Bill: 130 
Example Exception Outputs 
ValueError 
Enter quantity: abc 
Invalid quantity! Please enter a number. 
NameError 
Enter product name: Eraser 
Product not found in store. 
TypeError 
Cart data type error. 
ZeroDivisionError 
Calculation error: division by zero.'''

product = {"Pen":10,"Notebook":50,"Pencil":5}  #products storing in dictionary
product_category = {"Stationery","Education","Office"} #product_category storing in set
product_details = (("Pen",10),("Notebook",50),("Pencil",5)) #product_details using tuples
cart = [] # empty list creating to store cart
def display_products():
    print('\n Available products:-')

    for name,price in product_details:
        print(name,':',price)


def add_cart():
    try:
        name= input('Enetr product name:-').title()

        if name not in products:
            raise NameError
        quantity = int(input('Enter quantity:-'))

        if quantity <=0:
            raise ValueError
        price = products[name]
        
        cart.append((name,quatity,price))
        print('Ietm added to cart sucessfully.')

    except ValueError:
        print('Invalid quantity!please enter a number/')
    except NameError:
        print('product not found in store.')

def calculate_total(index = 0):

    if index == len(cart):
        return 0
    item = cart[index]
    name,quantity,price = item
    return(quantity*price)+calculate_total(index+1)

def view_bill():
    try:
        print('\n Items in cart:-')

        for item in cart:

            if not isinstance(item,tuple):
                raise TypeError
            name,quantity,price = item

            print(name,'x',qunatity)

        total = calculate_total()
        print('Total Bill:-',total)

        average = total/len(cart)
        print('Average item cost:-',average)

    except TypeError:
        print('cart data type error.')
    except ZeroDivisionError:
        print('calculation error')

while True:

    print('\n1.Display Products')
    print('2.Add item to cart')
    print('3.View total bill')
    print('4.Exit')

    try:
        choice = int(input('Enter choice:'))
        if choice ==1:
            display_products()
        elif choice ==2:
            add_cart()
        elif choice ==3:
            view_bill()
        elif choice ==4:
            print('Thank you for shopping')
            break
        else:
            print('Invalid choice,please try again')

    except ValueError:
        print('please enter a valid menu number')
            

