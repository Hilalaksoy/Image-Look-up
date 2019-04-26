var xhr = new XMLHttpRequest();
 xhr.onreadystatechange = function() {
   if (xhr.readyState==4 && xhr.status==200) {
       var blob = new Blob([xhr.response], {
           type: xhr.getResponseHeader("Content-Type")
       });
       var imgUrl = window.URL.createObjectURL(blob);
       document.getElementById("img").src = imgUrl;
     }
   }
 xhr.responseType = "arraybuffer";
 xhr.open("GET","Hacker.jpg",truexhr.send();

xhr.send();
