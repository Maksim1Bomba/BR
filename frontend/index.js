window.addEventListener('load', init);
function init(){ 
    fetch('/api/hello', {
	method: 'POST',
	body: JSON.stringify({})
    })
	.then(res => {
	    if(res.status === 404){
		throw '404';
	    }
	    return res.json();
	})
 	.then(json => {
	    if (json.success) {

	    } else {
		document.getElementById('greet').style.display = 'none';
	    }
	})
 	.catch(error => renderError(error));
 }

function renderError(error){
    if (error == 404){
	render404();
    } else {
	document.body.innerHTML = `<h1 style="color: red">${error}</h1>`;
    }
}

function render404(){
    document.body.innerHTML = `<h1 style="color: blue">404</h1>`;
}
