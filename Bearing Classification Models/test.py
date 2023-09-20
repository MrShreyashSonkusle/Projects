import pandas as pd
import scipy.io.loadmat
import os

for filename in os.listdir("C:/Users/HP/Downloads/CWRU_Bearing_Fault_Classification-main/CWRU_Bearing_Fault_Classification-main/0_load_48_KHz"):
#   mat = scipy.io.loadmat("/content/drive/MyDrive/0_load_48_KHz/"+filename)
#   mat = {k:v for k, v in mat.items() if k[0] != '_'}
#   data = pd.DataFrame({k: pd.Series(v[0]) for k, v in mat.items()}) # compatible for both python 2.x and python 3.x
#   print(data.head())

  mat_file = os.path.join('C:/Users/HP/Downloads/CWRU_Bearing_Fault_Classification-main/CWRU_Bearing_Fault_Classification-main/0_load_48_KHz',filename)
  data_dict = scipy.io.loadmat(mat_file)
  keys=list(data_dict.keys())
  A=data_dict[keys[-3]]
  B=data_dict[keys[-2]]
  C=data_dict[keys[-1]]
  # Convert the data to a pandas DataFrame
  df = pd.DataFrame(list(zip(A,B,C)),
               columns =[keys[-3],keys[-2],keys[-1]])

  print(df.shape)
  split_point=int(0.7*df.shape[0])
  print(split_point)
  df1 = df.iloc[:split_point, :]
  df2 = df.iloc[split_point:, :]

  df1.to_csv('C:/Users/HP/Downloads/CWRU_Bearing_Fault_Classification-main/CWRU_Bearing_Fault_Classification-main/0_load_48_KHz/SPLITTED_DATA/'+filename.split('.')[0]+'_train.csv')
  df2.to_csv('C:/Users/HP/Downloads/CWRU_Bearing_Fault_Classification-main/CWRU_Bearing_Fault_Classification-main/0_load_48_KHz/SPLITTED_DATA/'+filename.split('.')[0]+'_test.csv')
