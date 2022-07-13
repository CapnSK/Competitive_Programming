debug = False
for _ in range(int(input())):
	Inventory = {}
	Cart = {}
	Cost = {}
	while True:
		Line = input().strip().split()
		if len(Line)==1 and Line[0]=='END':
			break
		Ans = -1
		if Line[1] == "SM":
			command = Line[2]
			if command == "ADD":
				item,qty = Line[3::]
				qty = int(qty)
				if item not in Inventory:
					if qty>0:
						Inventory[item] = qty 
						Ans = qty
			elif command == "REMOVE":
				item = Line[3]
				if item in Inventory:
					if Inventory[item]>0:
						Ans = 1
						del Inventory[item]

			elif command == "GET_QTY":
				item = Line[3]
				if item in Inventory:
					if Inventory[item]>0:
						Ans = Inventory[item]
				Ans = max(Ans,0)

			elif command == "INCR":
				item,qty = Line[3::]
				qty = int(qty)
				if item in Inventory and qty>0:
					if Inventory[item]>0:
						Ans = qty
						Inventory[item] += qty

			elif command == "DCR":
				item,qty = Line[3::]
				qty = int(qty)
				if item in Inventory:
					if qty>0:
						Ans = min(qty,Inventory[item])
						Inventory[item]-=qty
						if Inventory[item] <= 0:
							del Inventory[item]

			elif command == "SET_COST":
				item,cost = Line[3::]
				cost = float(cost)
				if cost>0:
					Cost[item] = cost
					Ans = round(cost,1)

		elif Line[1] == "S":
			command = Line[2]
			if command == "ADD":
				item,qty = Line[3::]
				qty = int(qty)
				if item not in Cart:
					if qty>0:
						if item in Inventory and Inventory[item]>=qty:
							Cart[item] = qty 
							Ans = qty
							Inventory[item] -= qty
							if Inventory[item] == 0:
								del Inventory[item]
			elif command == "REMOVE":
				item = Line[3]
				if item in Cart:
					if Cart[item]>0:
						Ans = 1
						if item not in Inventory:
							Inventory[item] = Cart[item]
						else:
							Inventory[item] += Cart[item]
						del Cart[item]

			elif command == "INCR":
				item,qty = Line[3::]
				qty = int(qty)
				if item in Cart:
					if Cart[item]>0:
						if item in Inventory and Inventory[item]>=qty and qty>0:
							Ans = qty
							Cart[item] += qty
							Inventory[item] -= qty
							if Inventory[item] == 0:
								del Inventory[item]

			elif command == "DCR":
				item,qty = Line[3::]
				qty = int(qty)
				if item  in Cart:
					if qty>0:
						Ans = min(qty,Cart[item])
						Cart[item]-=qty
						if item not in Inventory:
							Inventory[item] = Ans
						else:
							Inventory[item] += Ans
						if Cart[item] <= 0:
							del Cart[item]

			elif command == "GET_ORDER_AMOUNT":
				for item,qty in Cart.items():
					if item in Cost:
						if Ans == -1:
							Ans = 0
						Ans += qty*Cost[item]
					else:
						Ans = -1
						break
				if Ans != -1:
					temp = str(Ans).split('.')[1]
					if len(temp)<2:
						Ans = str(Ans)
						while len(temp)<2:
							Ans += '0'
							temp += '0'
					else:
						Ans = round(Ans,2)
		print(Ans)
		if debug:
			print("Inventory",Inventory)
			print("Cart",Cart)
			print("Cost",Cost)