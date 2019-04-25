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
	console.log(dataURL);

	var canvas2 = document.getElementById('draw');
	var dataURL2 = canvas2.toDataURL();
	console.log(dataURL2);
}




/*
var fullQuality = canvas1.toDataURL('image/jpeg', 1.0);

var mediumQuality = canvas1.toDataURL('image/jpeg', 0.5);
var lowQuality = canvas1.toDataURL('image/jpeg', 0.1);
*/
