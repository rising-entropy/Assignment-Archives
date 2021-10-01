# Largest profit-weight ratio strategy

class ItemValue:

	def __init__(self, wt, val, ind):
		self.wt = wt
		self.val = val
		self.ind = ind
		self.cost = val // wt

	def __lt__(self, other):
		return self.val/self.wt < other.val/other.wt

class FractionalKnapsack:

	@staticmethod
	def getMaxValue(wt, val, cap):
		iVal = []
		for i in range(len(wt)):
			iVal.append(ItemValue(wt[i], val[i], i))

		# sorting items by value
		iVal.sort(reverse=True)

		totalValue = 0
		for i in iVal:
			curWt = int(i.wt)
			curVal = int(i.val)
			if cap - curWt >= 0:
				cap -= curWt
				totalValue += curVal
			else:
				fraction = cap / curWt
				totalValue += curVal * fraction
				cap = int(cap - (curWt * fraction))
				break
		return totalValue


w = [18,15,10]
p = [25,24,15]
M = 20

maxValue = FractionalKnapsack.getMaxValue(w, p, M)
print("Maximum value in Knapsack (Largest profit-weight ratio strategy) =", maxValue)