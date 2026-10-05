cost_price = 100
selling_price = 120

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit =", profit)

elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss =", loss)

else:
    print("No profit, no loss")
