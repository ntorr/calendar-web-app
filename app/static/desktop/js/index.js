$(document).ready(function(){
    updateAuthStatus();

   // setup logged out view
   $("#logged-out-view #login-form").submit(function(e){
      e.preventDefault();
      var form = $(this);
      var loginData = extractFormInput(form);
      login(loginData)
        .done(function(response){
            showLoggedIn(response);
        }).fail(function(response){
            alert(response.data);
            showLoggedOut();
        });
   });

   // setup signup view
   $("#signup-view #signup-form").submit(function(e){
      e.preventDefault();
      var form = $(this);
      var signupData = extractFormInput(form);

      signup(signupData)
         .done(function(response){
            alert("You just created a new user");
            login(response);
         }).fail(function(response){
            alert("Something went wrong");
         });
    });

   $("#user-home button").click(function(){
      logout()
      .done(function(response){
        showLoggedOut();
      }).fail(function(response){
        alert("Something went wrong");
      });
   });

});

function updateAuthStatus() {
   verifyAuth()
      .done(function(response){
         showLoggedIn(response);
      }).fail(function(response){
         showLoggedOut();
      });
}

function showLoggedIn(user) {
   // show logged in view and show username
   // $("#logged-in-view span").text(username);
   $("#logged-out-view").addClass("hidden");
   $("#signup-view").addClass("hidden");
   $("#user-home").removeClass("hidden");
   $("#create-event-view").removeClass("hidden");
}

function showLoggedOut() {
   // show logged out view
   $("#logged-out-view").removeClass("hidden");
   $("#signup-view").removeClass("hidden");
   $("#user-home").addClass("hidden");
   $("#create-event-view").addClass("hidden");
}