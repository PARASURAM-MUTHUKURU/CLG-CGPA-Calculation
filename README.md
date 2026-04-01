# SGPA & CGPA Calculator

A Python-based GUI application for calculating **SGPA (Semester Grade Point Average)** and **CGPA (Cumulative Grade Point Average)** using the official college grading system.

## Features

✅ **Add Subjects Dynamically** - Input subject name, internal marks (IM), external marks (EM), and credits  
✅ **Official Grading System** - Grade points (0.0 to 10.0) with letter grades (F, P, C, B, B+, A, A+, O)  
✅ **SGPA Calculation** - Automatically calculate semester GPA for current subjects  
✅ **CGPA Calculation** - Track multiple semesters and compute cumulative GPA  
✅ **Class Distinctions** - Determine class based on CGPA (First Class with Distinction, First Class, etc.)  
✅ **Equivalent Percentage** - Convert CGPA to equivalent percentage  
✅ **Sample Data** - Load pre-populated sample data for testing  
✅ **User-Friendly Interface** - Built with Tkinter for easy navigation  

## Grading System

| Total Marks | Grade Point | Letter Grade |
|-------------|-------------|--------------|
| 91 - 100   | 10.0        | O            |
| 81 - 90    | 9.0         | A+           |
| 71 - 80    | 8.0         | A            |
| 61 - 70    | 7.0         | B+           |
| 51 - 60    | 6.0         | B            |
| 41 - 50    | 5.0         | C            |
| 40         | 4.0         | P (Pass)     |
| < 40       | 0.0         | F (Fail)     |

## Class Classification

- **First Class with Distinction**: CGPA ≥ 7.5
- **First Class**: CGPA ≥ 6.5
- **Second Class**: CGPA ≥ 5.5
- **Pass Class**: CGPA ≥ 4.0
- **Fail**: CGPA < 4.0

## Installation

### Requirements
- Python 3.x
- tkinter (comes built-in with Python)

### Setup
```bash
# Clone the repository
git clone https://github.com/PARASURAM-MUTHUKURU/CLG-CGPA-Calculation.git
cd CLG-CGPA-Calculation

# Run the application
python Main-P.py
```

## Usage

### 1. **Add Subjects**
   - Enter subject name, internal marks, external marks, and credits
   - Click "Add Subject" to add to the current semester
   - Repeat for all subjects

### 2. **View Subject Details**
   - The table displays:
     - Subject number, name, IM, EM
     - Total marks, letter grade, grade point
     - Credits and credit × grade point

### 3. **Calculate SGPA**
   - Click "Calculate SGPA" to compute the semester GPA
   - Result displays in the "Current SGPA" field

### 4. **Add Semester to CGPA**
   - Click "Add Semester to CGPA" after calculating SGPA
   - The semester is added to the cumulative list
   - Current semester is cleared for the next semester

### 5. **Calculate Final CGPA**
   - After adding multiple semesters, click "Calculate Final CGPA"
   - View CGPA, class, and equivalent percentage

### 6. **Load Sample Data** (Optional)
   - Click "Load Melam Akash Sample" to load pre-populated subjects for testing

## Example Calculation

**Sample Subject:**
- Subject: DATA SCIENCE
- Internal Marks (IM): 36
- External Marks (EM): 27
- Total: 63
- Grade: B+ (7.0 points)
- Credits: 3.0
- Credit × Points: 3.0 × 7.0 = 21.0

**SGPA Formula:**
```
SGPA = Σ(Credits × Grade Points) / Σ(Credits)
```

**CGPA Formula:**
```
CGPA = Σ(Credits × SGPA for each semester) / Σ(All Credits)
```

## Project Structure

```
CLG-CGPA-Calculation/
├── Main-P.py       # Main application file
├── README.md       # Documentation
└── .gitignore      # Git ignore file
```

## Author

**PARASURAM MUTHUKURU**

## License

This project is open source and available for educational purposes.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Application won't start | Ensure Python 3.x and tkinter are installed |
| Calculation errors | Check that all marks are within valid range (0-100) |
| Credits showing as 0 | Enter decimal values like 1.5, 3.0, not just integers |

## Future Enhancements

- 📊 Export results to PDF/Excel
- 💾 Save and load semester data
- 📈 Graphical CGPA trend visualization
- 🌙 Dark mode support
- 📱 Mobile app version
