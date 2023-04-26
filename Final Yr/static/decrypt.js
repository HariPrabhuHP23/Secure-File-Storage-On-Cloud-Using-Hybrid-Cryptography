debugger;

$.ajax({
    type: "GET",
    url: "/decrypt_json",
    dataType: "json",
    success: function(data) {
        var options=data;
       var select = $('#dropdown');
        for(var i=0;i<options.length;i++)
         {
         select.append($('<option></option>').attr('value',options[i]).text(options[i]));
     }
    }
});

///checking image format
function checkimg()
{
debugger;
var image=document.getElementById('img-upload');
var filename=image.value;
var extensions=['.jpg','jpeg','.png','.bmp', '.webp','.svg','.ico','.tiff','.tif']
var flag=true;
for(let i=0;i<extensions.length;i++)
{
 if(filename.endsWith(extensions[i]))
 {
 flag=true;
 break
 }
 else
 {
 flag=false;
 }
}
if(flag===false)
{
alert("Only image file is allowed to Upload");
image.value='';
}
}
