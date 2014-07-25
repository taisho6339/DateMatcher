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

function add_error_message(msg) {
    $("#err_msg").text(msg);
}

function request_post() {
    var url = "addDateAction";

    var date_content = $("#date_add_area input");
    var date_json_array = [];
    date_content.each(function (i, child) {
        if (child.value != '') {
            date_json_array.push({
                date: child.value
            })
        }
    });

    var json = {
        user_name: $("#user_name").val(),
        choose_method: $("#add_form input[name='choose_method']:checked").val(),
        hash: $("#hash_id").val(),
        dates: date_json_array
    };

    $.ajax(
        {
            async: false,
            type: 'POST',
            url: url,
            data: JSON.stringify(json),
            contentType: "application/json; charset=utf-8",
            success: function (data, status) {
                console.log(data);
                if (data["status"] == 200)
                    window.location.href = data["redirect_url"];
                else
                    add_error_message(data["err_message"]);
            }
        }
    );
}

$(function () {
    setup_datepicker();
});