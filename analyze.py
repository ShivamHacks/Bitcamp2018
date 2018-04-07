import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('table.csv')

# Read data for one course for all semesters

course = 'CMSC132'
semesters = list(df['Semester'].unique()) # todo: fix order

for semester in semesters:
	query = 'Semester == "%s" & Course == "%s"' % (semester, course)
	df_query = df.query(query)
	grade_data = df_query.groupby(['Semester'])[['Total','A','A-','A+','B','B-','B+','C','C-','C+','D','D-','D+','Fs','Withdraw']].sum()
	#print(grade_data.values[0])

	#plt.scatter(grade_data.columns, grade_data.values[0])
	#df_aggs = df_query.drop(['Semester','Course','Sect','Professor Name'], axis=1).agg(['sum'])
	
	"""
	labels = ['Total','A','A-','A+','B','B-','B+','C','C-','C+','D','D-','D+','Fs','Withdraw']
	index = np.arange(len(labels))
	plt.bar(index, grade_data.values[0])
	plt.xticks(index, labels, fontsize=5, rotation=30)
	plt.show()
	"""


"""

# print(df.query('A > B')) # print where more A's than B's
df_spring2016_csmc132 = df.query('Semester == "Spring2016" & Course == "CMSC132"')
print(df_spring2016_csmc132.drop(['Semester','Course','Sect','Professor Name'], axis=1).agg(['sum']))
"""

"""
plt.hist(df['Semester'], bins=df['Semester'].unique())
plt.plot()

"""