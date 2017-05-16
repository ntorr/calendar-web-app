

$(document).ready(function(){
   // initial check to see if user is logged in or not
   updateAuthStatus();

   // setup logged out view
   $("#logged-out-view #login-form").submit(function(e){
      e.preventDefault();
      var form = $(this);
      var loginData = extractFormInput(form);

      login(loginData)
         .done(function(response){
            showLoggedIn(response.data.first_name)
            form.trigger('reset');
         }).fail(function(response){
            alert('Incorrect username or password');
         });
   });

   // setup logged in view
   $('#logged-in-view button').click(function(){
      logout()
         .done(function(response){
            showLoggedOut()
         }).fail(function(response){
            showLoggedIn();
         });
   });

   // setup signup view
   $('#signup-view #signup-form').submit(function(e) {
      e.preventDefault();
      var form = $(this);
      var signupData = extractFormInput(form);

      signup(signupData)
         .done(function(response){
            alert('You just created a new user');
            form.trigger('reset');
            updateAuthStatus();
         }).fail(function(response){
            alert('Something went wrong');
         });

   });
});

// helpers
function updateAuthStatus() {
   verifyAuth()
      .done(function(response){
         showLoggedIn(response.data.first_name)
      }).fail(function(response){
         showLoggedOut()
      });
}
function extractFormInput(form) {
   var inputs = form.serializeArray();
   var data = {};
   $.each(inputs, function(index, input) {
      data[input.name] = input.value;
   });
   return data;
}

function showLoggedIn(username) {
   // show logged in view and show user's first name
   $("#logged-in-view span").text(username);
   $("#logged-out-view").addClass('hidden');
   $("#logged-in-view").removeClass('hidden');
}

function showLoggedOut() {
   // show logged out view
   $("#logged-out-view").removeClass('hidden');
   $("#logged-in-view").addClass('hidden');
}