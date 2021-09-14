// A script that rejects promises
export default function uploadPhoto(filename) {
  return Promise.reject(
    Error(`${filename} cannot be processed`),
  );
}
