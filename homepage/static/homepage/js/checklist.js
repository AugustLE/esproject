var body = null;
var nodes = [];
var menu_ids = [];
var node_ids = [];

function clickItem(id) {

    removeNodes();
    body.appendChild(nodes[id]);
    //nodes[id].scrollTop = nodes[id].scrollHeight;
    var menu_items = document.getElementsByClassName("checklists_menu_item");
    for(i = 0; i < menu_items.length; i++) {

        menu_items[i].style.backgroundColor = "white";
        //menu_items[i].style.margin = "0.5%";

    }
    document.getElementById(menu_ids[id]).style.backgroundColor = "#5690aa";

    $('body,html').animate({
        scrollTop: $('#'+node_ids[id]).offset().top - 50
    }, 1000);

}

function removeNodes() {

    while(body.hasChildNodes()) {

        body.removeChild(body.lastChild);
    }
}

function initView() {

    body = document.getElementById("checlists_content_container");

    var menu_items = document.getElementsByClassName("checklists_menu_item");
    var content_items = document.getElementsByClassName("checklist");

    for(i = 0; i < menu_items.length; i++) {

        menu_ids.push(menu_items[i].id);
        node_ids.push(content_items[i].id);
        nodes.push(content_items[i]);
    }

    //clickItem(0);
    removeNodes();
}

window.onload = function() {

    initView();
};

function setValueOnAnswer(object) {

    document.getElementById("answer-" + object.id).value=object.value;
    console.log(document.getElementById("answer-" + object.id).value);
}

