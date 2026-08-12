def calculate_total(topping_count):
	"Return the final price for a pizza with topping_count toppings."
	base_price = 10.00
	topping_price = 1.50
	return base_price + topping_count * topping_price

def main():
	available = {"pepperoni", "mushrooms", "extra cheese"}
	topping_count = 0
	while True:
		choice = input("What topping would you like? ").strip().lower()
		if choice == "done":
			break
		if choice in available:
			topping_count += 1
		else:
			print("ts not on the menu boii")

	total = calculate_total(topping_count)

	code = input("Do you have a discount code? ").strip()
	if code == "PYTHON20":
		total = total * 0.8

	print(f"Your total is: ${total:.2f}")
if main() == "__main__":
	main()
