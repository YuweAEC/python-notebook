import pandas as pd 

students = {
    'name': ['Alice', 'Bob', 'Carol', 'Dan', 'Eli', 'Fran', '\0'],
    'age': [24, 42, 18, 32, 44, 18, '\0'],
    'favorite_color': ['Blue', 'Green', 'Indigo', 'Red', 'Yellow', 'Blue', '\0'],
    'grade': [88, 76, 92, 79, 95, 80, '\0']
}   

frame = pd.DataFrame(students)

print("DataFrame:")
print(frame)

newData = pd.read_csv('students.csv')
print(newData)


