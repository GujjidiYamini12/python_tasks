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
def displayAdd():
    try:
        dict={pro_name:price}
    except: 
