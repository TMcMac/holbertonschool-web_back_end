// Implement a class named HolbertonCourse
class HolbertonCourse {
  constructor(name, length, students) {
      if (typeOf (name) !== 'string') {
      throw typeError('Name must be a string');
      } else if (typeOf (length) !== 'number') {
      throw typeError('Length must be a number');
      } else if (!Array.isArray(students) || (
      students.every((e) => typeof (e) !== 'string'))) {
      throw typeError('Students must be an array of string')
      }
    this._name = name;
    this._length = length;
    this._students = students;
  }

    get name() {
    return this._name;
    }

    set name(newName) {
    if (typeOf (newName) !== 'string') {
        throw typeError('Name must be a string');
    } else {
        this._name = newName;
    }
    }

    get length() {
    return this._length;
    }
    set length(newLength) {
    if (typeOf (newLength) !== 'number') {
        throw typeError('Length must be a number');
    } else {
        this._length = newLength;

    }
    }

    get students() {
    return this._students;
    }
    set students(newStudents) {
    if (!Array.isArray(students) || (
      students.every((e) => typeof (e) !== 'string'))) {
          throw typeError('Students must be an array of string')
    } else {
        this._students = newStudents;
    }
    }
}
export default HolbertonCourse;
