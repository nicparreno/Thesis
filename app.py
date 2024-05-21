from flask import Flask, request, jsonify

app = Flask(__name__)

# Constants and assumptions
FTE_HOURS_PER_YEAR = 1920
LEAVE_HOURS_PER_YEAR = 120
ROOM_ABSENCE_HOURS_PER_YEAR = 96
SECTIONS = 45
SUBJECTS_PER_SECTION = 8
DURATION_PER_SUBJECT_HOURS = 12

# Calculate total effective hours per year
effective_hours_per_year = FTE_HOURS_PER_YEAR - LEAVE_HOURS_PER_YEAR - ROOM_ABSENCE_HOURS_PER_YEAR

# Convert effective teaching hours per year to minutes per month
effective_minutes_per_month = (effective_hours_per_year * 60) / 12

# Workload assumptions
teaching_load_per_professor = 50  # Example: Each professor can handle 50 students
admin_workload_per_student = 5   # Example: Administrative workload per student, in minutes per month

# Constants from your data
total_minutes_sheet1 = 8520     # Total minutes per month from sheet 1
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

# Flask route for prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    current_students = data.get('current_students')
    
    # Validate input
    if not isinstance(current_students, int):
        return jsonify({"error": "Invalid input, please provide an integer for current_students"}), 400

    # Predict professors needed
    professors_needed = predict_professors_needed(current_students, SECTIONS)
    result = round(professors_needed, 2)
    
    # Return the result as JSON
    return jsonify({"professors_needed": result})

# Main function to run the Flask app
if __name__ == "__main__":
    app.run(debug=True)