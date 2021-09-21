// returns a boolean if all the elements in the array exist within the set.
const hasValuesFromArray = (set, array) => {
  let result = true;
  for (const element of array) {
    if (!set.has(element)) {
      result = false;
      break;
    }
  }

  return result;
};

export default hasValuesFromArray;
