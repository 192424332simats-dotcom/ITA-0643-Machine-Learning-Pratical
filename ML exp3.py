import pandas as pd
import numpy as np
from math import log2

# Create dataset
data = pd.DataFrame({
    'Outlook': ['Sunny','Sunny','Overcast','Rain','Rain','Rain','Overcast',
                'Sunny','Sunny','Rain','Sunny','Overcast','Overcast','Rain'],
    'Temperature': ['Hot','Hot','Hot','Mild','Cool','Cool','Cool',
                    'Mild','Cool','Mild','Mild','Mild','Hot','Mild'],
    'Humidity': ['High','High','High','High','Normal','Normal','Normal',
                 'High','Normal','Normal','Normal','High','Normal','High'],
    'Wind': ['Weak','Strong','Weak','Weak','Weak','Strong','Strong',
             'Weak','Weak','Weak','Strong','Strong','Weak','Strong'],
    'PlayTennis': ['No','No','Yes','Yes','Yes','No','Yes',
                   'No','Yes','Yes','Yes','Yes','Yes','No']
})

# Entropy function
def entropy(target):
    values, counts = np.unique(target, return_counts=True)
    ent = 0
    for i in range(len(values)):
        p = counts[i] / sum(counts)
        ent -= p * log2(p)
    return ent

# Information Gain
def info_gain(data, attribute, target):
    total_entropy = entropy(data[target])
    values, counts = np.unique(data[attribute], return_counts=True)
    
    weighted_entropy = 0
    for i in range(len(values)):
        subset = data[data[attribute] == values[i]]
        weighted_entropy += (counts[i]/sum(counts)) * entropy(subset[target])
    
    return total_entropy - weighted_entropy

# ID3 Algorithm
def id3(data, original_data, features, target):
    
    if len(np.unique(data[target])) <= 1:
        return np.unique(data[target])[0]
    
    if len(features) == 0:
        return np.unique(original_data[target])[np.argmax(
            np.unique(original_data[target], return_counts=True)[1])]
    
    gains = [info_gain(data, feature, target) for feature in features]
    best_feature = features[np.argmax(gains)]
    
    tree = {best_feature: {}}
    features = [f for f in features if f != best_feature]
    
    for value in np.unique(data[best_feature]):
        subset = data[data[best_feature] == value]
        subtree = id3(subset, original_data, features, target)
        tree[best_feature][value] = subtree
    
    return tree

# Build tree
features = list(data.columns[:-1])
decision_tree = id3(data, data, features, 'PlayTennis')

print("Decision Tree:")
print(decision_tree)
