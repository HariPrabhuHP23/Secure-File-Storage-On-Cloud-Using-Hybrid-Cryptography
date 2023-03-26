var x=document.getElementById("login");
var y=document.getElementById("signin");
        var z=document.getElementById("btn");
        function signin(){
            x.style.left='-400px';
            y.style.left='50px';
            z.style.left='110px';
        }
        function login(){
            x.style.left='50px';
            y.style.left='450px';
            z.style.left='0px';

        }
       document.getElementById("login-btn").addEventListener("click", function(event) {
        event.preventDefault(); // prevent the form from submitting
     window.location.href = "choice.html";
       } )