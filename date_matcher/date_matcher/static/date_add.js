/**
 * Created by taisho6339 on 2014/07/25.
 */


var i = 0;

function setup_datepicker() {

    var last_content = $(".date").eq(i - 1);
    last_content.datepicker('option', "onSelect", function () {
    });

    var content = $(".date").eq(i);
    content.datepicker(
        {
            onSelect: function () {
                add_date_content();
            }
        }
    );
    content.datepicker('option', 'showOn', "button");
    content.datepicker('option', 'buttonImage', "http://jqueryui.com/resources/demos/datepicker/images/calendar.gif");
    content.datepicker('option', 'buttonImageOnly', "true");

}

function add_date_content() {
    i = i + 1;
    $("#date_add_area").append("<p><input class='date' tabindex='8' type='text'></p>");
    setup_datepicker();
}

function request_post() {
    var url = "addDate";

    var date_content = $("#date_add_area input");
    var date_json_array = [];
    date_content.each(function (i, child) {
        if (child.value != '')
            date_json_array.push({
                date: child.value
            })
    });

    var json = {
        user_name: $("#user_name").val(),
        choose_method: $("#add_form input[name='choose_method']").value,
        hash: $("#hash_id").val(),
        dates: date_json_array
    };
    $.post(url, json, function (result) {
    }, 'json');
    
    console.log(json);
}

$(function () {
    setup_datepicker();
});