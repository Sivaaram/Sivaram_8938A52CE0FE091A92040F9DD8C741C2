class Student:
	def __init__(self, name, roll_number, cgpa):
		self.name = name
		self.roll_number = roll_number
		self.cgpa = cgpa
def sort_students(student_list):
	#sort the list of students in descending order of CGPA
	sorted_students = sorted(student_list,
				key=lambda student: student.cgpa,
				reverse=True)
	return sorted_students  #return the list after sorted
	
	

# Example usage:
students = [
	Student("Adhi","A123", 8.8),
	Student("Hari","A124", 8.9),
	Student("Gopal", "A126", 7.8),
	Student("Sivaram", "A127", 9.5),
]
sorted_students = sort_students(students)
# Using for loop simultaneously sort the student list & Print the sorted list  of students
for student in sorted_students:
	print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
	
	
