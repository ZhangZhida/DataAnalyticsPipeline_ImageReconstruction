/* 
let canvases = document.getElementsByTagName('upload_pic'),
	canvasOutput = document.createElement('upload_pic'),
	ctxOutput = canvasOutput.getContext('2d');

for (let i = canvases.length - 1; i >= 0; i--) {
    let image = new Image();
    image.src = canvases[i].toDataURL();
    ctxOutput.drawImage(image, 0, 0);
}

let srcOutput = canvasOutput.toDataURL();

let doc = {
    layers: []
};


canvases.forEach(function (canvas) {
    doc.layers.push({
        image: canvas.toDataURL()
    });
});

console.log(image);

download.href = "data:application/octet-stream;base64," + btoa(JSON.stringify(doc));
*/
function geturl() {
	var canvas1 = document.getElementById('upload_pic');
	var dataURL = canvas1.toDataURL();
	// console.log(dataURL);

	var canvas2 = document.getElementById('draw');
	var dataURL2 = canvas2.toDataURL();
	// console.log(dataURL2);
	return [dataURL, dataURL2]
}

function send_post_to_server() {
	var urls = geturl()
	var dataURL = urls[0]
	var dataURL2 = urls[1]
	console.log('dataUrl', dataURL);
	console.log('dataUrl2', dataURL2);

	const xhttp = new XMLHttpRequest();
	
	const url = "http://localhost:7777/upload";
	xhttp.open("POST", url);
	// http.setRequestHeader("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
	// xhttp.setRequestHeader("Access-Control-Allow-Headers", '*');
	// xhttp.setRequestHeader('Access-Control-Allow-Origin', '*');
	// xhttp.setRequestHeader('Content-type', 'text/html')
	// xhttp.setRequestHeader('Access-Control-Allow-Methods', "POST, GET, OPTIONS")

	data = {
		"original": dataURL,
		"mask": dataURL2
	}

	data_json = JSON.stringify(data)
	console.log('data = ', data_json)

	xhttp.send(data_json);

	

	xhttp.onreadystatechange = (e) => {
		console.log(xhttp.responseText)
	}
}







/*
var fullQuality = canvas1.toDataURL('image/jpeg', 1.0);

var mediumQuality = canvas1.toDataURL('image/jpeg', 0.5);
var lowQuality = canvas1.toDataURL('image/jpeg', 0.1);
*/
