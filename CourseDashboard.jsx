import React, { useState } from "react";

function CourseDashboard() {

  // Map<id, student>
  const [students, setStudents] = useState(new Map());

  const [name, setName] = useState("");
  const [gpa, setGpa] = useState("");
  const [courses, setCourses] = useState("");
  const [filterCourse, setFilterCourse] = useState("");

  // Add new student
  const addStudent = () => {
    const id = Date.now();

    const newStudent = {
      id,
      name,
      gpa: parseFloat(gpa),
      enrolledCourses: new Set(courses.split(",").map(c => c.trim()))
    };

    const newMap = new Map(students);
    newMap.set(id, newStudent);

    setStudents(newMap);

    setName("");
    setGpa("");
    setCourses("");
  };

  // Remove student by ID
  const removeStudent = (id) => {
    const newMap = new Map(students);
    newMap.delete(id);
    setStudents(newMap);
  };

  // Convert Map -> Array
  const studentArray = [...students.values()];

  // Sort by GPA descending
  const sortedStudents = [...studentArray].sort((a, b) => b.gpa - a.gpa);

  // Filter by course
  const filteredStudents = filterCourse
    ? sortedStudents.filter(student =>
        student.enrolledCourses.has(filterCourse)
      )
    : sortedStudents;

  // Get all unique courses
  const uniqueCourses = studentArray.reduce((acc, student) => {
    student.enrolledCourses.forEach(course => acc.add(course));
    return acc;
  }, new Set());

  return (
    <div style={{padding:"20px"}}>

      <h2>Course Enrollment Dashboard</h2>

      <h3>Add Student</h3>

      <input
        placeholder="Name"
        value={name}
        onChange={(e)=>setName(e.target.value)}
      />

      <input
        placeholder="GPA"
        value={gpa}
        onChange={(e)=>setGpa(e.target.value)}
      />

      <input
        placeholder="Courses (comma separated)"
        value={courses}
        onChange={(e)=>setCourses(e.target.value)}
      />

      <button onClick={addStudent}>Add</button>


      <h3>Filter by Course</h3>

      <input
        placeholder="Course name"
        value={filterCourse}
        onChange={(e)=>setFilterCourse(e.target.value)}
      />


      <h3>Students (Sorted by GPA)</h3>

      {filteredStudents.map(student => (
        <div key={student.id} style={{border:"1px solid gray", margin:"10px", padding:"10px"}}>

          <p><b>ID:</b> {student.id}</p>
          <p><b>Name:</b> {student.name}</p>
          <p><b>GPA:</b> {student.gpa}</p>

          <p><b>Courses:</b>
            {[...student.enrolledCourses].join(", ")}
          </p>

          <button onClick={()=>removeStudent(student.id)}>
            Remove
          </button>

        </div>
      ))}


      <h3>All Unique Courses</h3>

      <ul>
        {[...uniqueCourses].map(course => (
          <li key={course}>{course}</li>
        ))}
      </ul>

    </div>
  );
}

export default CourseDashboard;