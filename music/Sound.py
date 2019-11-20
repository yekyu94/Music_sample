import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import scipy.io.wavfile as sci_wav  # Open wav files
import os  # Manipulate files
import matplotlib.pyplot as plt
import scipy.io.wavfile as wavf
import warnings  # Warning removal
warnings.filterwarnings('ignore')

data = sci_wav.read('./s2.wav')[1]
print(sci_wav.read('./s2.wav')[0])

data1 = []
data2 = []
for i in data:
    data1.append(i[0])
    data2.append(i[1])

fig, axs = plt.subplots(1, 2, figsize=(16,6))
axs[0].plot(data1)
axs[1].plot(data2)
plt.show()

samples = np.array(data1)
fs = 9000
out_f = 'out.wav'

wavf.write(out_f, fs, samples)
wavf.write('out2.wav', fs, np.array(data2))
wavf.write('org.wav', fs, np.array(data))