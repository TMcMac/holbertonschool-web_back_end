// returns a string of all the set values that start with a specific string
const cleanSet = (set, startString) => {
  if (startString === '') return '';
  if (typeof startString !== 'string') return '';

  return [...set]
    .filter((s) => typeof s === 'string' && s.startsWith(startString))
    .map((value) => value.substring(startString.length))
    .join('-');
};

export default cleanSet;
