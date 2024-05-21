# Define constants (example values, adjust as per your institution's data)
FTE_HOURS_PER_YEAR = 1920  # Full-time equivalent teaching hours per year
LEAVE_HOURS_PER_YEAR = 120  # Hours for leave, workshops, etc.
ROOM_ABSENCE_HOURS_PER_YEAR = 96  # Hours for room absence, renovations, etc.
SECTIONS = 45  # Number of sections
SUBJECTS_PER_SECTION = 8  # Number of subjects per section
DURATION_PER_SUBJECT_HOURS = 12  # Duration of each subject in hours

# Calculate total effective hours per year
effective_hours_per_year = FTE_HOURS_PER_YEAR - LEAVE_HOURS_PER_YEAR - ROOM_ABSENCE_HOURS_PER_YEAR

# Convert effective teaching hours per year to minutes per month
effective_minutes_per_month = (effective_hours_per_year * 60) / 12

# Workload assumptions (example)
teaching_load_per_professor = 50  # Example: Each professor can handle 50 students
admin_workload_per_student = 5  # Example: Administrative workload per student, in minutes per month

# Constants from your data
total_minutes_sheet1 = 8520  # Total minutes per month from sheet 1
total_minutes_activities = 259200  # Total minutes per month for activities

# Calculate the ratio of total minutes for activities to total minutes from sheet 1
activity_ratio = total_minutes_activities / total_minutes_sheet1

# Function to predict professors needed based on current student numbers and sections
def predict_professors_needed(current_students, sections):
    # Calculate total workload generated by current students, sections, subjects, and duration
    total_workload_per_month = current_students * (teaching_load_per_professor + admin_workload_per_student) * sections

    # Calculate professors needed based on workload and effective teaching time, adjusted by activity ratio
    professors_needed = (total_workload_per_month / effective_minutes_per_month) * activity_ratio
    
    return professors_needed

def main():
    try:
        # Input for current number of students
        current_students = int(input("Enter the current number of students: "))
        
        # Predict professors needed
        professors_needed = predict_professors_needed(current_students, SECTIONS)
        
        # Print the results
        print("\nCapacity Prediction Based on Current Enrollment, Sections, Subjects, and Duration:")
        print("Current Students:", current_students)
        print("Sections:", SECTIONS)
        print("Subjects per Section:", SUBJECTS_PER_SECTION)
        print("Duration per Subject (hours):", DURATION_PER_SUBJECT_HOURS)
        print("Professors Needed (predicted):", round(professors_needed, 2))
    
    except ValueError:
        print("Error: Please enter a valid number for students.")

if __name__ == "__main__":
    main()