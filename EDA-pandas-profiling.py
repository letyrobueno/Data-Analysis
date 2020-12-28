import pandas as pd
import pandas_profiling

df = pd.read_csv('dataset.csv', dtype='unicode')

profile = df.profile_report(title='Pandas Profiling Report')
profile.to_file(output_file="dataset_pandas_profiling.html")