// Import the ClassRoom class from 0-classroom.js and implement a function named initializeRooms
import ClassRoom from './0-classroom';

const initializeRooms = () => {
  const array = [new ClassRoom(19), new ClassRoom(20), new ClassRoom(34)];
  return array;
};
export default initializeRooms;
