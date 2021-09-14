// That returns a resolved promise with object
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
