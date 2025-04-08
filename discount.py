def calculate_discount(price, discount_percent):
	if discount_percent >= 20:
         	final_price = price * (1-discount_percent/100)
         	return final_price
	else:
		final_price = price
		return final_price
print(calculate_discount(price=int(input("price: ")), discount_percent=int(input("discount: "))))