var body = null;
var nodes = [];
var node_ids = [];
var page_id = "";

function clickItem(menuItem) {

    removeNodes();

    var item_id_raw = (menuItem.id).split("-")[1];

    var checklist_id = "checklist-" + item_id_raw;
    var checklist_index = node_ids.indexOf(checklist_id);

    console.log(item_id_raw);
    body.appendChild(nodes[checklist_index]);

    //nodes[id].scrollTop = nodes[id].scrollHeight;
    var menu_items = document.getElementsByClassName("checklists_menu_item");
    for(i = 0; i < menu_items.length; i++) {

        menu_items[i].style.backgroundColor = "white";
        //menu_items[i].style.margin = "0.5%";

    }
    document.getElementById(menuItem.id).style.backgroundColor = "#87d4f1";

    $('body,html').animate({
        scrollTop: $('#'+checklist_id).offset().top - 75
    }, 1000);

}

function removeNodes() {

    while(body.hasChildNodes()) {

        body.removeChild(body.lastChild);
    }
}

$(document).ready(function() {
  $(window).keydown(function(event){
    if(event.keyCode === 13) {
      event.preventDefault();
      return false;
    }
  });
});

function initView() {

    page_id = document.getElementById("page_id").value;
    body = document.getElementById("checlists_content_container");

    var menu_items = document.getElementsByClassName("checklists_menu_item");
    var content_items = document.getElementsByClassName("checklist");

    for(i = 0; i < menu_items.length; i++) {

        node_ids.push(content_items[i].id);
        nodes.push(content_items[i]);
    }

    //clickItem(0);
    if(page_id === "checklists")
        removeNodes();
}

window.onload = function() {

    initView();
    if(page_id === "index")
        setTimeout(scrollDown, 250)
};


function setValueOnAnswer(object) {

    console.log(object.className);
    if(object.className === "option_button") {

        document.getElementById("answer-" + object.id).value=object.value;
        var optionDivIdParts = (object.id).split("-");
        var optionDivId = "options-" + optionDivIdParts[1] + "-" + optionDivIdParts[2];
        setColorOnButton(optionDivId, object.name);
        scrollToNext(object);
    } else if(object.className === "input_elem") {

        $("#" + object.id).keyup(function(event){
            if(event.keyCode === 13){

                scrollToNext(object);

            }
        });
    }
}

function scrollToNext(object) {

    var checklist_id = object.id.split("-")[1];
    var question_id = "question-" + object.id.split("-")[1] + "-" + object.id.split("-")[2];

    var checklist = document.getElementById("checklist-" + checklist_id);
    var questions = checklist.getElementsByClassName("question");

    for(var i = 0; i < questions.length; i++) {

        if(questions[i].id === question_id) {

            if(i + 1 < questions.length) {

                document.getElementById(questions[i + 1].id).focus();
                $('body,html').animate({
                    scrollTop: $('#'+questions[i + 1].id).offset().top - 50
                }, 500);
                break;

            }
        }
    }

}

function setColorOnButton(id, optionName) {

    var elements = document.getElementById(id).childNodes;
    for(var i = 0; i < elements.length; i++) {

        if(elements[i].nodeType !== Node.TEXT_NODE) {

            if(elements[i].name === optionName ) {

            elements[i].style.backgroundColor = "#87d4f1";
            } else {

                elements[i].style.backgroundColor = "#FFFFFF";
            }
        }
    }

}


function checkForm(object) {

    var checklist_id = object.id.split("-")[1];
    var checklist = document.getElementById("checklist-" + checklist_id);

    //return !!checkAnswers(checklist);

    if(checkAnswers(checklist)) {

        return true;
    }

    //$('#not_filled_modal').modal('toggle');
    $('#not_filled_modal').modal('show');
    return false;
}

function valueIsEmpty(classname, question) {

    var checkValue = question.querySelector(classname).value;
    return checkValue === "" || checkValue.trim() === "";

}

function checkAnswers(checklist) {

    var questions = checklist.getElementsByClassName("question");
    var is_filled = true;
    for(var i = 0; i < questions.length; i++) {

        var is_options = questions[i].querySelector(".isOptions").value;
        console.log(is_options);
        if(is_options === "True") {

            if(valueIsEmpty(".answerOption", questions[i])) {
                is_filled = false;
                break;
            }

        } else {

            if(valueIsEmpty(".input_elem", questions[i])) {
                console.log(questions[i]);
                is_filled = false;
                break;
            }
        }
    }
    return is_filled;
}








