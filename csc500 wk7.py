# Carmen V. Elston
# CSC 500 Week 7 Critical Thinking
# Dictionaries of Courses Info

# Dictionary of course number to room number
course_rooms = {"CSC101": "3004", "CSC102": "4501", "CSC103": "6755",
    "NET110": "1244", "COM241": "1411"}

# Dictionary: course number to instructor name
course_instructors = {"CSC101": "Haynes", "CSC102": "Alvarado", "CSC103": "Rich",
    "NET110": "Burke", "COM241": "Lee"}

# Dictionary: course number to meeting time
course_times = {"CSC101": "8:00 a.m.", "CSC102": "9:00 a.m.", "CSC103": "10:00 a.m.",
    "NET110": "11:00 a.m.", "COM241": "1:00 p.m."}

# User inputs a course number
course = input("Enter a course number: ").strip().upper()

# Check if the course exists
if course in course_rooms:
    print(f"Room Number: {course_rooms[course]}")
    print(f"Instructor: {course_instructors[course]}")
    print(f"Meeting Time: {course_times[course]}")
else:
    print("Course information not found.")

