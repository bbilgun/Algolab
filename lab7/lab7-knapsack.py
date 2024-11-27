class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __lt__(self, other):
       
        return (self.value / self.weight) > (other.value / other.weight)

def fractional_knapsack(items, W):
    items.sort()

    max_value = 0.0 
    for item in items:
        if W == 0:  
            break

        if item.weight <= W:
            W -= item.weight
            max_value += item.value
        else:
            max_value += item.value * (W / item.weight)
            W = 0

    return max_value

values = [60, 100, 120] 
weights = [10, 20, 30]   
W = 50             

items = [Item(values[i], weights[i]) for i in range(len(values))]

max_value = fractional_knapsack(items, W)
print("Хамгийн их утга:", max_value)
