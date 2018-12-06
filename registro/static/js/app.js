

function field_focus(field, email)
  {
    if(field.value == email)
    {
      field.value = '';
    }
  }

  function field_blur(field, email)
  {
    if(field.value == '')
    {
      field.value = email;
    }
  }

//Fade in dashboard box
$(document).ready(function(){
    $('.box').hide().fadeIn(1000);
    });

//Stop click event
$('a').click(function(event){
    event.preventDefault(); 
  });
  
  newFunction();

function newFunction() {
  <script src="https://code.jquery.com/jquery-3.2.1.js"></script>
    ,
    <script type="text/javascript">
      $(".input").focus(function() {$(this).parent().addClass("focus")}
    })
    </script>;
}




