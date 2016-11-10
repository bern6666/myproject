/* no jquery needed! without jquery:
*  an html input field calls this function on the event onkeyup
* if the input field contains only an empty string, it results in two messages
* one at the #msg-tag the other at the ouptut-tag.
* If the input-val is a reasonable string (we could demand for at least two letters)
* the ajax process starts: a new object of type XMLHttpRequest is created
* which calls via GET the url like so: /myschool/search-ajax/?term=val
* The django mechanism processes this url in a view and calls a html-snippet
* which is delivered at the #output-tag. Before it is delivered you can inspect
* it with the help of alert or better console.log  in the browser's console (key F12)
*/
function mySearch(val){
    if (val == ""){
        document.getElementById("msg").innerHTML="No input ..not searching";
        document.getElementById("output").innerHTML="No results";
        return;
    }
    document.getElementById("msg").innerHTML="Your input was " + val;
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange=function(){
       if (this.readyState==4 && this.status==200){
            // alert(this.responseText);
            // console.log(this.responseText);
            document.getElementById("output").innerHTML=this.responseText;
            }
        }
    xhttp.open("GET","/myschool/search-ajax/?term="+val,true);
    xhttp.send();
}
