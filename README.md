# **Student Management System**

A simple **Student Management System** developed using **Python** and **Object-Oriented Programming (OOP)**.

This is a **menu-driven console application** that allows users to **add, display, search, update, and delete student records**. It also calculates **total marks, average marks, grades, and the number of passed subjects**.

## **Features**

- **Add** multiple student records
- **Display** all student records
- **Search** for a student using register number
- **Update** student name and marks
- **Delete** student records
- **Calculate total marks**
- **Calculate average marks**
- **Count passed subjects**
- **Determine overall student result**
- **Assign grades based on average marks**
- **Validate marks between 0 and 100**
- **Prevent duplicate register numbers**
- **Handle invalid numeric input using exception handling**

## **Grading System**

| **Average Mark** | **Grade** |
|------------------|-----------|
| **90 - 100** | **A** |
| **80 - 89** | **B** |
| **70 - 79** | **C** |
| **60 - 69** | **D** |
| **50 - 59** | **E** |
| **40 - 49** | **F** |
| **Below 40** | **G** |

**Passing Criteria:** A student is considered to have **passed a subject** if the mark is **40 or above**.

**Overall Result:** A student is considered to have **passed the examination only if all subjects are passed**.

## **Concepts Used**

- **Python**
- **Object-Oriented Programming (OOP)**
- **Classes and Objects**
- **Constructors**
- **Instance Variables**
- **Instance Methods**
- **Lists**
- **Loops**
- **Conditional Statements**
- **Functions**
- **Exception Handling**
- **Input Validation**
- **CRUD Operations**

## **Student Information**

Each student record contains:

- **Name**
- **Register Number**
- **Department**
- **Marks**

The program automatically calculates:

- **Total Marks**
- **Average Marks**
- **Number of Passed Subjects**
- **Grade**
- **Overall Result**

## **Application Menu**

1. **Add Student**
2. **Display Students**
3. **Search Student**
4. **Update Student**
5. **Delete Student**
6. **Exit**

## **How to Run**

### **Prerequisites**

Make sure **Python 3** is installed on your computer.

### **Steps**

1. **Clone or download** this repository.
2. Open the project folder in a terminal.
3. Run the Python file:

**python student_management.py**

4. Follow the instructions displayed in the terminal.

## **Data Storage**

Currently, student records are stored in a **Python list while the program is running**.

**Note:** Student data will be **lost when the program is closed**, as permanent storage has not yet been implemented.

## **Future Improvements**

- Add **permanent data storage using files**
- Add **SQLite/MySQL database support**
- Add **student ranking and sorting**
- Add **department-wise filtering**
- Add **subject names**
- Generate **student performance reports**
- Add a **Graphical User Interface (GUI)**
- Improve **input validation and error handling**

## **Author**

**MOHAMED IRFAN J**

This project was developed as part of my **learning journey in Python and Object-Oriented Programming**.

Through this project, I strengthened my understanding of **classes, objects, methods, lists, functions, input validation, exception handling, and CRUD operations**.