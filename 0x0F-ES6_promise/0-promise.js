// Return a Promise
function getResponseFromAPI() {
  return new Promise((resolve) => {
    resolve('I did promise');
  });
}
export default getResponseFromAPI;
