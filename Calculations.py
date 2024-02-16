
#Question 1
# Function to calculate entropy
def entropy(target):
    elements, counts = np.unique(target, return_counts=True)
    entropy = np.sum([(-counts[i]/np.sum(counts)) * np.log2(counts[i]/np.sum(counts)) for i in range(len(elements))])
    return entropy

# Function to calculate information gain
def info_gain(data, split_attribute_name, target_name):
    # Total entropy
    total_entropy = entropy(data[:, -1])
    # Values and counts for the split attribute
    vals, counts = np.unique(data[:, split_attribute_name], return_counts=True)
    # Weighted entropy
    Weighted_Entropy = np.sum([(counts[i]/np.sum(counts)) * entropy(data[data[:, split_attribute_name] == vals[i], -1]) for i in range(len(vals))])
    # Information gain
    Information_Gain = total_entropy - Weighted_Entropy
    return Information_Gain

#Question 3
def calculate_gini_index(classes):
    _, counts = np.unique(classes, return_counts=True)
    probabilities = counts / counts.sum()
    gini = 1 - sum(probabilities**2)
    return gini

# Function to calculate Gini index for an attribute with multiple categories
def calculate_gini_for_attribute(data, column_index):
    unique_values = np.unique(data[:, column_index])
    gini_for_attribute = 0
    for value in unique_values:
        subset = data[data[:, column_index] == value]
        gini_for_attribute += (len(subset) / len(data)) * calculate_gini_index(subset[:, -1])
    return gini_for_attribute

#Question 4
