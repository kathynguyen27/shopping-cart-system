#Kathy Nguyen
#PM
#Shopping Cart System
# I was absent on the 14th what this was assigned :(


products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]
#products and their prices must be listed with the same index
shopping_cart = []
user_choice = 0
#so it forces u into menu

#option 1 item display
def display_items(products):
        for i in range(len(products)):
            print("----------------")
            print(f"{i + 1}. {products[i]}   ${prices[i]}")
        #formatting so its #. PRODUCT $price

#option 2 add products
def add_product(products):
    product_num = 0
    print("What item would you like to add to cart?")
    print("1. Chips")
    print("2. Soda")
    print("3. Candy")
    print("4. Cookies")
    print("5. Water")
    print("6. Sandwich") 
    product_num = int(input("Enter product number: "))
    #check the condiitons first before adding it into cart with while loop
    while product_num > 6 or product_num < 1:
        print("Invalid number! Please try again")
        product_num = int(input("Enter product number: "))
        #must loop until it actually add a product

    shopping_cart.append(products[product_num-1])
    #because index for a list starts at 0, the number the user adds will be off, hence why we add 1

    print(f"{products[product_num - 1]} was added to the cart")
    

#option 3 remove products from cart
def remove_cart(products):
    print("------------------")
    print("CURRENT SHOPPING CART")
    print("------------------")
    # len() == 0 to check if it has 0 elements because this list has strings (can't = 0)
    if len(shopping_cart) == 0:
        print("Shopping cart empty, add something first!")
        return
    #sends the user back to the main menu because they cant do anything from here
    for i in range(len(shopping_cart)):
        print(f"{i+ 1}. {shopping_cart[i]}")
        #i + 1 because the the index starts at 0, so user input is off
    remove_product = int(input("Enter product you want to remove: "))
    removed = shopping_cart.pop(remove_product - 1)
        #so the index is correct when you remove from the list (ex. if user enters 2, in the list itll be the 3rd element, but we want the acutal 2nd element (-1))
    print(removed, "was removed from shopping cart!")


def check_cart(products):
     #display the current cart
    print("------------------")
    print("CURRENT SHOPPING CART")
    print("------------------")
    for i in range(len(shopping_cart)):
        print(f"{i+ 1}. {shopping_cart[i]}  ${prices[i]}")
        print(" ")
    #indented out of for loop so it doesnt repeat
    print("Total items: ", len(shopping_cart))


#total fucntionn
def total_price(products):
    total = 0
    print("-------------------")
    print("CURRENT TOTAL")
    print("-------------------")
    for i in range(len(shopping_cart)):
            product_index = products.index(shopping_cart[i])
            #this links products' index to the shopping cart list because its all strings we need their index
            total += prices[product_index]
            #here we're grabbing the prices based of product index
            #closed bracks because we're taking from the list like [i]
            #totalling all the prices
            print(f"{i+ 1}. {shopping_cart[i]}  ${prices[product_index]}")
            # printing #. item  $price
            #displaying current cart
    print(f"Total Cart Cost: $ {total:.2f}")
    #we need to return the total so it can be used later in checkout
    return total

    
total = 0
final_total = 0     
#set to 0 so it can be added into later
while user_choice != 6:
    #menu
    print("-------------------------------")
    print("SMART SHOPPING CART")
    print("-------------------------------")
    print(" ")
    print("1. View Available Products")
    print("2. Add Product to Cart")
    print("3. Remove Product from Cart")
    print("4. View Current Shopping Cart")
    print("5. View Current Total")
    print("-------------------------------")
    print("6. Checkout!")
    user_choice = int(input("Enter your choice based off the numbers: "))
    #menu above always prints then asks where user wants to go
    #each choice below goes to designated function
    if user_choice == 1:
        display_items(products)
    elif user_choice == 2:
        add_product(products)
    elif user_choice == 3:
        remove_cart(products)
    elif user_choice == 4:
        check_cart(products)
    elif user_choice == 5:
        total = total_price(products)
    while user_choice < 1 or user_choice > 6:
        print("INVALID NUMBER, PLEASE TRY AGAIN")
        user_choice = int(input("Enter your choice based off the numbers: "))

#this imports the current month/day/year
import datetime
current_date = datetime.datetime.now().strftime("%m/%d/%Y")

def checkout(total, final_total, shopping_cart):
    print("==============================")
    print("CHECKOUT")
    print("==============================")
    print("")
    print(current_date)
    print("------------------------------")
    total = total_price(products)
    final_total = 0

    #must check if theres even anything before we start
    #returns the user back to the main menu
    if len(shopping_cart) == 0:
        print("NOTHING IN CART TO CHECKOUT! Please add something to checkout")
        return
    #NO discount 
    if total < 10: 
        final_total = total
        print("Subtotal: $", total)
        print("Discount: N/A")
        print("Final Total: $",final_total)
    #5% discount
    elif 10 <= total < 20:
        final_total = total - total*0.05
        print("Subtotal: $", total)
        print("Discount: 5%")
        print("Final Total: $",final_total)
    #10% discount
    elif 20 <= total < 40:
        final_total = total - total*0.1
        print("Subtotal: $", total)
        print("Discount: 10%")
        print("Final Total: $",final_total)
    #15% discount
    elif total >= 40:
        final_total = total - total*0.15
        print("Subtotal: $", total)
        print("Discount: 15%")
        print("Final Total: $",final_total)
#function callback
checkout(total, final_total, shopping_cart)
print("")
print("==============================")
print("Thank you for shopping :D")
