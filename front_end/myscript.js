var imageLoader = document.getElementById('imageLoader');
imageLoader.addEventListener('change', handleImage, false);
var canvas_upload = document.getElementById('upload_pic');
var ctx_upload = canvas_upload.getContext('2d');


function handleImage(e){
    var reader = new FileReader();
    reader.onload = function(event){
        var img = new Image();
        img.onload = function(){
            canvas_upload.width = img.width;
            canvas_upload.height = img.height;
            //canvas_upload.width = 500;
            //canvas_upload.height = 500;
            ctx_upload.drawImage(img,0,0);
        }
        img.src = event.target.result;
    }
    reader.readAsDataURL(e.target.files[0]);  
    var dataURL = canvas1.toDataURL();
    return dataURL   
}

//