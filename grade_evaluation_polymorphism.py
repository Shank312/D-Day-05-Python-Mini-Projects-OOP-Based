
# Base class representing a generic grading system
class GradeSystem:
    # This method is intended to be overridden by subclasses
    def evaluate(self):
        pass

# Subclass for evaluating grades based on percentage scores
class PercentageSystem(GradeSystem):
    def __init__(self, score):
        self.score = score

    def evaluate(self):
        return "Pass" if self.score >= 40 else "Fail" 
    
# Subclass for evaluating grades based on GPA
class GPASystem(GradeSystem):
    def __init__(self, gpa):
        self.gpa = gpa

    def evaluate(self):
        return "Pass" if self.gpa >= 2.0 else "Fail"
    
# Subclass for evaluating grades based on letter grades
class LetterGradeSystem(GradeSystem):
    def __init__(self, grade):
        self.grade = grade 

    def evaluate(self):
        return "Pass" if self.grade in ['A', 'B', 'C'] else "Fail"
    

# ---Testing and Output---


# Create instances with example inputs
percentage_student = PercentageSystem(75)
gpa_student = GPASystem(1.8)
letter_grade_student = LetterGradeSystem('B')


# Print results using polymorphic behavior
print("Percentage System Evaluation(75): ", percentage_student.evaluate())
print("GPA System Evaluation(1.8): ", gpa_student.evaluate())
print("Letter Grade System Evaluation(B): ", letter_grade_student.evaluate())