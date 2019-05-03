var imageLoader = document.getElementById('imageLoader');
imageLoader.addEventListener('change', handleImage, false);
var canvas_upload = document.getElementById('upload_pic');
var ctx_upload = canvas_upload.getContext('2d');
var maxlength = 0




function handleImage(e){ //e = event is a string, in this case = 'change'
    var reader = new FileReader();
    reader.onload = function(event){
        var img = new Image();
        img.onload = function(){
            canvas_upload.width = img.width;
            canvas_upload.height = img.height;
            

            //resize the upload picture to fit the canvas size
         
            maxlength = Math.max(img.width, img.height)
            var factor = Math.ceil(maxlength/800)

            new_width = img.width/factor
            new_height = img.height/factor

            canvas_upload.width = new_width
            canvas_upload.height = new_height

            ctx_upload.drawImage(img,x=0,y=0,width=new_width,height=new_height);
           
            // painting function 
            painting(img.width/factor, img.height/factor)

        }
        img.src = event.target.result;
    }

    reader.readAsDataURL(e.target.files[0]);  


    


}


function painting(target_width, target_height){
    var canvas = document.querySelector('#draw'); // define a canvas object(ctx)
    var ctx = canvas.getContext('2d');
    canvas.width = target_width
    canvas.height = target_height


    ctx.lineJoin = 'round';  //Sets or returns the type of corner created, when two lines meet
    ctx.lineCap = 'round'; //Sets or returns the style of the end caps for a line
    ctx.lineWidth = 20; //current line width
    ctx.strokeStyle = 'black'; //Sets or returns the color, gradient, or pattern used for strokes

    let isDrawing = false; // track our mouse movements, we need a boolean variable. 
    let lastX = 0;
    let lastY = 0;

    // pass through an event listener
    function draw(e) {
        // stop the function if they are not mouse down
        if(!isDrawing) return;
        //listen for mouse move event

        //console.log(e);

        ctx.beginPath(); //Begins a path, or resets the current path
        ctx.moveTo(lastX, lastY); //Moves the path to the specified point in the canvas, without creating a line
        ctx.lineTo(e.offsetX, e.offsetY); //Adds a new point and creates a line to that point from the last specified point in the canvas
        ctx.stroke(); //Actually draws the path you have defined
        [lastX, lastY] = [e.offsetX, e.offsetY]; // return the xy coordinate of the mouse pointer 
    }

    canvas.addEventListener('mousedown', (e) => { //occurs when press the mouse
    isDrawing = true;
    [lastX, lastY] = [e.offsetX, e.offsetY]; //returns the x-coordinate of the mouse pointer, relative to the target element.
    });
    // element.addEventListener(event, function, useCapture)
    canvas.addEventListener('mousemove', draw);   //occurs whenever the mouse is moving (no click)
                                                // as long as move the mouse, we will run draw function 


    canvas.addEventListener('mouseup', () => isDrawing = false); //occurs when release the mouse 
    canvas.addEventListener('mouseout', () => isDrawing = false); // (no click) occurs when the mouse pointer leaves the selected element.

}

// User drawing 


// print url 
function geturl() {

	var canvas1 = document.getElementById('upload_pic');
	var dataURL = canvas1.toDataURL();
    console.log(dataURL)
  

	var canvas2 = document.getElementById('draw');
    // canvas2.width = canvas1.width
    // canvas2.height = canvas1.height  
	var dataURL2 = canvas2.toDataURL();
	console.log(dataURL2);
    return [dataURL, dataURL2];

}

function send_post_to_server() {
    var urls = geturl()
    var dataURL = urls[0]
    var dataURL2 = urls[1]
    // console.log('dataUrl', dataURL);
    // console.log('dataUrl2', dataURL2);

    const xhttp = new XMLHttpRequest();
    
    const url = "http://52.37.174.117:7777/upload";
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



