
////Displaying Users////

$.ajax({url:"/encrypt_users",
       type:"GET",
       dataType:"json",
       success:function(data)
       {
       var options=data['user'];
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


///Getting selected options
function selectedopt() {
  var selectElement = document.getElementById("dropdown");
  var selectedOptions = selectElement.selectedOptions;
  var selectedValues = [];
  for (let i = 0; i < selectedOptions.length; i++) {
    selectedValues.push(selectedOptions[i].value);
  }
  debugger;
  $.ajax({
      type: "POST",
     url: "/upload1",
     data: { file: selectedValues},
     })
}

