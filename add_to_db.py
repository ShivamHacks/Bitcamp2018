import pandas as pd
import numpy as np
import json

df = pd.read_csv('table.csv')

# print(df.sort_values('Course').head(100))

courses = [x for x in list(df['Course'].unique()) if str(x) != 'nan']
semesters = [x for x in list(df['Semester'].unique()) if str(x) != 'nan']
print(semesters)
grade_columns = ["Total","A","A-","A+","B","B-","B+","C","C-","C+","D","D-","D+","Fs","Withdraw"]

data_dict = {}

# Initialize data dict with empty spots
for course in courses:
	if (course not in data_dict): data_dict[course] = {}
	for semester in semesters:
		data_dict[course][semester] = { 'Professors': [], 'Sections': [], 'Course_List': {} }

df = df[0:100]

# Go row by row in table to add to JSON
for index, row in df.iterrows():
	course = row['Course']
	semester = row['Semester']
	professor = row['Professor Name']
	section = row['Sect']
	if (str(course) != 'nan' and str(semester) != 'nan'):

		# Account for no professor/section
		if (str(professor) == 'nan'): professor = 'Unknown Professor'
		if (str(section) == 'nan'): professor = 'Unknown Section'

		# Aggregate data from different sections taught by the same professor
		# If professor not added to course in certain semester, add them and add grades
		if (professor not in data_dict[course][semester]['Professors']):
			data_dict[course][semester]['Professors'].append(professor)

			# Add this section data
			data_dict[course][semester]['Course_List'][professor] = row[grade_columns].to_dict()
		# Otherwise, add grades for same prof, diff section to the current totals
		else:
			a = data_dict[course][semester]['Course_List'][professor]
			b = row[grade_columns].to_dict()
			combined = dict(a.items() + b.items() + [(k, a[k] + b[k]) for k in set(b) & set(a)])
			data_dict[course][semester]['Course_List'][professor] = combined

		print('completed row: ' + str(index))

# Save data as JSON
json.dump(data_dict, open('table.json', 'w'), indent=4)
