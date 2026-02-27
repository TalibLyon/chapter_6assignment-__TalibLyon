"""
COMP 163 - Introduction to Programming
Assignment: Chapter 7 - Course Schedule Formatter
Name: [Talib Lyon]
GitHub Username: [TalibLyon]
Date: [Submission Date]
Description: [This program takes in cluttered as well as messy data, and uses string methods to clean and organize it into a formatted course schedule. It also checks for tme conflicts between classes.]
AI Usage: [Describe any AI assistance OR write "None"]
"""

# ============================================================
# Step 1: Input Parsing & Course Code Formatting
# ============================================================

courses = []

while True:
    line = input()

    if line == "DONE":
        break

    parts = line.split("|")

    code = parts[0].strip()
    title = parts[1].strip()
    days = parts[2].strip()
    time = parts[3].strip()
    room = parts[4].strip()

    code = code.upper()

    courses.append([code, title, days, time, room])
    
# ============================================================
# Step 2: Title and Room Formatting
# ============================================================

for course in courses:
    course[1] = course[1].title()

    course[4] = course [4].upper().strip()

# ============================================================
# Step 3: Day Code Expansion
# ============================================================

day_map = {
    "M": "Monday",
    "T": "Tuesday",
    "W": "Wednesday",
    "R": "Thursday",
    "F": "Friday"
}

for course in courses:
    expanded_days = []

    for letter in courses[2]:
        if letter in day_map:
            expanded_days.append(day_map[letter])

    course[2] = ", ". join(expanded_days)        

# ============================================================
# Step 4: Time Standardization
# ============================================================


# ============================================================
# Step 5: Conflict Detection
# ============================================================


# ============================================================
# Step 6: Full Output & Formatted Printing
# ============================================================
