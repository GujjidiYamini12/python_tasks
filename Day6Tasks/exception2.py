"""Q2: Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).
Example Output:
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
Calculation error: division by zero"""
dic={'Pen':10,'Notebook':50,'Pencil':5}
cart=[]
category={"Stationary"}
product_details=[]
for i in dic.keys():
    product_details.append((i,"Stationary"))
#print(product_details)
def displayProducts():
    print("Available Products:")
    for i,j in dic.items():
        print(f"{i}: {j}")
def addToCart(): #cart contains items,quantity
    try:
        productName=input("enter product name: ")
        if productName not in dic:
            raise NameError
        quantity=int(input("enter quantity: "))
        cart.append((productName,quantity))
        print(cart)
        print("Item added to cart successfully.")
    except NameError:
        print("Product not found in store.") 
    except ValueError:
        print("Invalid quantity! Please enter a number.") 
    except TypeError:
        print("Cart data type error.")   
def tot_price(list_cart,index):
    if index==len(list_cart):
        return 0
    product_name,quantity=list_cart[index]
    return dic[product_name]*quantity+tot_price(list_cart,index+1)
def view_tot_bill():
    try:
        print("Items in Cart")
        for product_name,quantity in cart:
            print(f"{product_name} x {quantity}")
        total=tot_price(cart,0)
        #avg=total/len(cart)
        print(len(cart))
        #print("Total Bill: ",total)
    except ZeroDivisionError:
        print("Calculation error: division by zero")
'''displayProducts()
addToCart()'''
view_tot_bill()
"""while True:
    x=int(input("Enter choice: "))
    if x==1:
        print("1. Display Products\n2. Add Item to Cart\n3. View Total Bill\n4. Exit\n")
        displayProducts()
        break
    elif x==2:
        print("1. Display Products\n2. Add Item to Cart\n3. View Total Bill\n4. Exit\n")
        addToCart()
        break
    elif x==3:
        print("1. Display Products\n2. Add Item to Cart\n3. View Total Bill\n4. Exit\n")
        view_tot_bill()
        break
    elif x==4:
        print("1. Display Products\n2. Add Item to Cart\n3. View Total Bill\n4. Exit\n")
        break
    else:
        print("Invalid choice")
        break"""