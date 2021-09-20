// Create a function getListStudentIds that returns an array of ids from a list of object.
const getListStudentIds = (anArray) => {
  if ( !Array.isArray(anArray) ) return [];

  return anArray.map((object) => object.id);  
};

export default getListStudentIds;
