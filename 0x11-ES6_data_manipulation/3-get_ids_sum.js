// Get the sum of all IDs from students array of student objs
import getListStudentIds from './1-get_list_student_ids';

const getStudentIdsSum = (students) => {
  const reducer = (previousValue, currentValue) => previousValue + currentValue;
  const studentIds = getListStudentIds(students);
  return studentIds.reduce(reducer);
};

export default getStudentIdsSum;
