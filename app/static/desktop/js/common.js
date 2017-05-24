// Setup csrf token for all ajax calls
var token = $('meta[name=csrf-token]').attr('content');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
         xhr.setRequestHeader("X-CSRFToken", token);
      }
    }
});

// alert helpers
function errorMessage(response) {
    // var msg = response.responseJSON.errors.message;
    var type = response.responseJSON.errors.type;
    return type.toString() + "!"; //\n" + msg.toString();
}

function welcomeMessage(response) {
    var first_name = response.data.first_name.toString();
    return "Welcome, " + first_name + "!";
}

// auth helpers
function verifyAuth(callback) {
   var url = '/api/auth/verify_auth';
   return $.get(url);
}

function login(loginData){
   var url = '/api/auth/login';
   return $.post(url, loginData);
}

function logout(){
    var url = '/api/auth/logout';
    return $.post(url)
}

function signup(signupData) {
   var url = '/api/auth/signup';
   return $.post(url, signupData);
}

// event helpers
function createUserEvent(eventData) {
    var url = '/api/event/create';
    return $.post(url, eventData);
}

// form helpers
function extractFormInput(form) {
   var inputs = form.serializeArray();
   var data = {};
   $.each(inputs, function(index, input) {
      data[input.name] = input.value;
   });
   return data;
}