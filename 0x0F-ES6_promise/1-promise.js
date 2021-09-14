//Return a promise from a fake api call
function getFullResponseFromAPI(success) {
    return new Promise((resolve, reject) => {
	if (success) {
	   resolve({
               status: 200,
               body: 'Success',
	   });
	} else {
	    eject(new Error("Not the API you're looking for"));
	}
    });	
}
export default getFullResponseFromAPI;
