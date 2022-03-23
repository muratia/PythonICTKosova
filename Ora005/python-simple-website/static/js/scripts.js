function checkPwds(){
var pwd= document.getElementById("pwd");
 var pwd1 = document.getElementById("pwd1");
 if(pwd == pwd1){
 return true;
  }else{
 return false;
 }

}




/* Set the width of the side navigation to 250px */
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

/* Set the width of the side navigation to 0 */
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}

function addPost(){
var content = CKEDITOR.getData();
console.log("content: "+content);
return;

  }

  $('.switch').click(()=>{
    $([".light [class*='-light']", ".dark [class*='-dark']"]).each((i,ele)=>{
        $(ele).toggleClass('bg-light bg-dark')
        $(ele).toggleClass('text-light text-dark')
        $(ele).toggleClass('navbar-light navbar-dark')
    })
    // toggle body class selector
    $('body').toggleClass('light dark')
})

function selectItem (){
 var value = jQuery('#PostsTitles').find(":selected").val();


jQuery.getJSON( "./posting/?id="+value, function( data ) {
    console.log(data)

  post = '<div class="card" style="width: 18rem;">'+
  '<img src="'+data.image+'" class="card-img-top" alt="...">'+
 ' <div class="card-body">'+
  '  <h5 class="card-title">'+data.title+'</h5>'+
  '  <p class="card-text">'+data.body+'.</p>'+
  '  <a href="#" class="btn btn-primary">Go somewhere</a>'+
  '</div>'+
'</div>';
  jQuery("#postDisplay").html(post);
  });


}

function addPost(){
jQuery("#editor").val ( editor.getData())
}