import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

versicolor_petal_length = [4.7, 4.5, 4.9, 4. , 4.6, 4.5, 4.7, 3.3, 4.6, 3.9, 3.5, 4.2, 4. ,
       4.7, 3.6, 4.4, 4.5, 4.1, 4.5, 3.9, 4.8, 4. , 4.9, 4.7, 4.3, 4.4,
       4.8, 5. , 4.5, 3.5, 3.8, 3.7, 3.9, 5.1, 4.5, 4.5, 4.7, 4.4, 4.1,
       4. , 4.4, 4.6, 4. , 3.3, 4.2, 4.2, 4.2, 4.3, 3. , 4.1]
versicolor_petal_length = np.array(versicolor_petal_length)

differences  = versicolor_petal_length - versicolor_petal_length.mean()
diff_sq = differences**2
variance_explicit = np.mean(diff_sq)
variance_np = np.var(versicolor_petal_length)
print(variance_explicit,variance_np)

variance_sq = np.sqrt(variance_np)
std = np.std(versicolor_petal_length)
print(variance_sq, std)
