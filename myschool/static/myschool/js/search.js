/* jquery needed!
 * ajax function which takes from a html-input field #input
 * a value on the event onkeyup
 * display this same value in the html-file at #msg
 * calls an url like so: myschool/?term=$input
 * GETs the result and display it in the html-file at #output
 */
$(function(){
    $('#input').keyup(function() {
        var $input =  $('#input').val()
        $.get({
            url:      '/myschool/search-ajax/',
            data:     {'term': $input},
            success:  searchSuccess,
            dataType: 'html'
        });
        if ($input == ''){ $input='all'};
        $("#msg").html("Searching for " + $input)
    });
});

function searchSuccess(data, textStatus, jqXHR){
    $('#output').html(data);
}
