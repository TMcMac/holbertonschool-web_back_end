// Knowing that the functions in utils.js return promises, use the prototype below to collectively resolve all promises and log body firstName lastName to the console.
import { createUser, uploadPhoto } from './utils';

export default function handleProfileSignup() {
  return Promise.all([
    uploadPhoto(),
    createUser(),
  ]).then((values) => {
    console.log(values[0].body, values[1].firstName, values[1].lastName);
  }).catch(() => console.log('Signup system offline'));
}
