# Largest Profit Strategy

class ItemValue:

	def __init__(self, wt, val, ind):
		self.wt = wt
		self.val = val
		self.ind = ind
		self.cost = val // wt

	def __lt__(self, other):
		return self.cost < other.cost

class FractionalKnapsack:

	@staticmethod
	def getMaxValue(wt, val, capacity):
		iVal = []
		for i in range(len(wt)):
			iVal.append(ItemValue(wt[i], val[i], i))

		# sorting items by value
		iVal.sort(reverse=True)

		totalValue = 0
		for i in iVal:
			curWt = int(i.wt)
			curVal = int(i.val)
			if capacity - curWt >= 0:
				capacity -= curWt
				totalValue += curVal
			else:
				fraction = capacity / curWt
				totalValue += curVal * fraction
				capacity = int(capacity - (curWt * fraction))
				break
		return totalValue


w = [18,15,10]
p = [25,24,15]
M = 20

maxValue = FractionalKnapsack.getMaxValue(w, p, M)
print("Maximum value in Knapsack (Largest Profit Strategy) =", maxValue)