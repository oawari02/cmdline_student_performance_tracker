# Command-Line Student Performance Tracker

A command-line Python application for managing and tracking student academic records, scores, averages, and grades with JSON data persistence.

## Features

- **Add Student**: Register new students with an ID, Name, and subject scores (Math, Science, English).
- **Search Student**: Query a student by ID to view total score, average, and calculated letter grade (A, B, C, F).
- **Update Student**: Update subject scores for an existing student.
- **Delete Student**: Remove a student record.
- **View All**: Display all student records currently in memory.
- **Data Persistence**: Automatically loads and saves student data to a local `students.json` file.

## Requirements

- Python 3.7+

## Usage

Run the script from your terminal:

```bash
python cmdline_student_performance_tracker.py
```

### Menu Options

```text
1. Add student
2. Search student
3. Update student
4. Delete student
5. View students
6. Exit
```
