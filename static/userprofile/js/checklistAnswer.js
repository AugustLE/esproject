var body = null;
var nodes = [];
var node_ids = [];
var page_id = "";

function clickItem(menuItem) {

    removeNodes();

    var item_id_raw = (menuItem.id).split("-")[1];
    var checklist_id = "answer-" + item_id_raw;
    var checklist_index = node_ids.indexOf(checklist_id);

    console.log(checklist_index);
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

function initView() {

    page_id = document.getElementById("page_id").value;
    body = document.getElementById("answers_content_container");

    var menu_items = document.getElementsByClassName("checklists_menu_item");
    var content_items = document.getElementsByClassName("answer_body");

    for(i = 0; i < menu_items.length; i++) {

        node_ids.push(content_items[i].id);
        nodes.push(content_items[i]);
    }

    //clickItem(0);
    if(page_id === "answers")
        removeNodes();
}

function answerClick(answer) {

    console.log("Test");
    console.log(answer.querySelector(".answer_solution").value);

    $('.modal-header #header').html(answer.querySelector(".answer_question").innerHTML);
    $('.modal-body #your_answer').html(answer.querySelector(".answer_answer").innerHTML);
    $('.modal-body #our_tips').html(answer.querySelector(".answer_solution").value);
    $('#answer_modal').modal('show');

}

window.onload = function() {

    initView();
    if(page_id === "index")
        setTimeout(scrollDown, 250)
};