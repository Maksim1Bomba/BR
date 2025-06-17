window.addEventListener('load', function(){
    document.getElementById('button').addEventListener('click', login);
});
function login() {
    fetch('/api/login', {
	method: 'POST',
	body: JSON.stringify({login: document.getElementById('login').value, 
			     password: document.getElementById('password').value})
    })
	.then(res => {
	    if(res.status === 404){
		return '404';
	    } 
	    return res.json();
	})
	.then((json) => {
	    if (!json.success){
		document.getElementById('error').style.display = 'block';
	    } else {
		document.getElementById('form').style.display = 'none';
		document.getElementById('cont').style.display = 'block';
	    }
	})
};


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
