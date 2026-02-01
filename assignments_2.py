#########################################################
##              Assignments 2 : Python - Control Flow(Conditionals & Loops )
################################################################################################################

########################################################
##      Task - 1 : Discount Rules (if / elif / else )
########################################################

### user input using input() 
#Order_amount = input("Enter your order amount : ")

# ## Discount rules
# if Order_amount.isdigit():

#     Order_amount = int(Order_amount)

#     if Order_amount >= 2000:
#         discount = Order_amount * 0.15
#         amount = Order_amount - discount
#         print(f"your order amount after 15% discount is  : {amount}")
#     elif 1500 <= Order_amount < 2000:
#         discount =  Order_amount * 0.10
#         amount = Order_amount - discount
#         print(f"your order amount after 10% discount is  : {amount}")
#     elif 1000 <= Order_amount < 1500:
#             discount =  Order_amount * 0.07
#             amount = Order_amount - discount
#             print(f"your order amount after 7% discount is  : {amount}")
#     else:
#         print(f"your order amount is : {Order_amount}")

# else :
#     print("Error : Please enter a valid amount")


#######################################################
##      Task - 2 : Process Multiple Orders (for loop )
########################################################

orders = [1200, 2500, 800, 1750, 3000]
total_revenue = 0
discount_orders = 0

for order in orders:
    
    if order >= 2000:
        discount_percent = 15
    elif 1500 <= order < 2000:
        discount_percent = 10
    elif 1000 <= order < 1500:
        discount_percent = 7
    else:
        discount_percent = 0

    discount_amoount = order * discount_percent/100
    final_amount = order - discount_amoount

    if discount_percent>0:
        discount_orders+=1

    total_revenue += final_amount

    print(f"{order:12} :-->  {discount_percent:10}%  :--> {final_amount}")

print(f"Total Revenue after discounts: {total_revenue}")
print(f"Number of orders with discount: {discount_orders}")

