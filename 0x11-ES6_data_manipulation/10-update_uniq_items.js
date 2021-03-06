// returns an updated map for all items with initial quantity at 1
const updateUniqueItems = (map) => {
  if (!(map instanceof Map)) throw Error('Cannot process');
  map.forEach((value, key) => {
    if (value === 1) {
      map.set(key, 100);
    }
  });

  return map;
};

export default updateUniqueItems;
