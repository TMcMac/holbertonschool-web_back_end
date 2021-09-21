// Create a function getStudentsByLocation that returns an array of objects who are located in city.
/* eslint-disable */
const getStudentsByLocation = (students, city) => students.filter((student) => student.location === city);

export default getStudentsByLocation;
