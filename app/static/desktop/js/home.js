// setup csrf token for all ajax calls
var csrftoken = $('meta[name=csrf-token]').attr('content');
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
         xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
});

$(document).ready(function(){

    $("#create-event-view #create-event-form").submit(function(e){
        verify_auth();
        var form = $(this);
        var eventData = extractFormInput(form);
        create_event(eventData)
         .done(function(response){
            form.trigger('reset');
         }).fail(function(response){
            alert('Could not create event');
         });
    });
});

function create_event(eventData){
   var url = '/api/events/create';
   return $.post(url, eventData);
}
