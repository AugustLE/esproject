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
        scrollTop: $('#'+checklist_id).offset().top - 50
    }, 1000);

}

function removeNodes() {

    while(body.hasChildNodes()) {

        body.removeChild(body.lastChild);
    }
}

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
        setTimeout(scrollDown, 500)
};

function setValueOnAnswer(object) {

    document.getElementById("answer-" + object.id).value=object.value;
    var optionDivIdParts = (object.id).split("-");
    var optionDivId = "options-" + optionDivIdParts[1] + "-" + optionDivIdParts[2];
    setColorOnButton(optionDivId, object.name);

}

function setColorOnButton(id, optionName) {

    var elements =  document.getElementById(id).childNodes;
    console.log(elements);
    for(var i = 0; i < elements.length; i++) {

        if(elements[i].nodeType !== Node.TEXT_NODE) {

            if(elements[i].name === optionName ) {

            elements[i].style.backgroundColor = "#87d4f1";
            console.log(elements[i].name);
            } else {

                elements[i].style.backgroundColor = "#FFFFFF";
            }
        }
    }


}








