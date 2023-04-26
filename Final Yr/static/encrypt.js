
////Displaying Users Mail////

$.ajax({url:"/upload1",
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

/*
///Getting selected options
function selectedopt() {
  var image=document.getElementById('img-upload')
  var file=document.getElementById('file-upload')
  var fname=file.files[0];
  var imgname=image.files[0];
  var key=document.getElementById('key').value
  var selectElement = document.getElementById("dropdown");
  var selectedOptions = selectElement.selectedOptions;
  var selectedValues = [];
  for (let i = 0; i < selectedOptions.length; i++) {
    selectedValues.push(selectedOptions[i].value);
  }
  console.log(imgname['name'])
  console.log(fname['name'])
  var info={'image':imgname['name'],'options':selectedValues,'file':fname['name'],'key':key}

  debugger;
  $.ajax({
      type: "POST",
     url: "/upload1",
     data: JSON.stringify(info),
     dataType:'json',
     contentType:'application/json; charset=utf-8',

});

}
*/

///////////
function selectedopt() {
debugger;
var selectElement = document.getElementById("dropdown");
  var selectedOptions = selectElement.selectedOptions;
  var selectedValues = [];
  for (let i = 0; i < selectedOptions.length; i++) {
    selectedValues.push(selectedOptions[i].value);
  }


$.ajax({
  url: '/upload1',
  type: 'POST',
  data: {file: selectedValues}/*JSON.stringify(selectedValues),
  dataType:'json',

  contentType: 'application/json; charset=utf-8',*/


});
}



