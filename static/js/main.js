$(document).ready(function (){
    if($(window).height() <400){$(".show_bg").height(400)}
    else {$(".show_bg").height("100%")}

    if($(window).height() >400){
        $(".scaleable").css("transform","scale(" + $(window).height()/window.screen.height +")")
    }else{
        $(".scaleable").css("transform","scale(" + 400/window.screen.height +")")
    }
    $("#index_1 li:first-child").addClass("li_onselect").removeClass("breakingnews");
    $(".article > iframe").attr("src", "./article/"+$("#index_1 li:first-child").attr("name"));
    indexmask(".index_li")
});
$(window).resize(function () {
    if($(window).height() <400){$(".show_bg").height(400)}
    else {$(".show_bg").height("100%")};
    if($(window).height() >400){
        $(".scaleable").css("transform","scale(" + $(window).height()/window.screen.height +")")
    }else{
        $(".scaleable").css("transform","scale(" + 400/window.screen.height +")")
    }
});

$(".index_li").scroll(()=>indexmask(".index_li"));

let indexmask = (selector)=>{
    if($(selector).scrollTop() ==0){
        $(selector).css("-webkit-mask-image", "linear-gradient(to bottom,black 90%,transparent)");
        $(selector).css("mask-image", "linear-gradient(to bottom,black 90%,transparent)");
    }
    else if($(selector).innerHeight() + $(selector).scrollTop() +1>= $(selector)[0].scrollHeight){
        $(selector).css("-webkit-mask-image", "linear-gradient(to bottom,transparent, black 10%)");
        $(selector).css("mask-image", "linear-gradient(to bottom,transparent, black 10%)");
    }
    else{
        $(selector).css("-webkit-mask-image", "linear-gradient(to bottom,transparent, black 10%,black 90%,transparent)");
        $(selector).css("mask-image", "linear-gradient(to bottom,transparent, black 10%,black 90%,transparent)");
    }
}

let name_mapper = {
    "tag_1":"index_1",
    "tag_2":"index_2"
}

$(".index_li li").click(function (e) {
    e.preventDefault();
    $(".li_onselect").removeClass("li_onselect");
    $(this).addClass("li_onselect");
    $(this).removeClass("breakingnews");
    $(".article > iframe").attr("src", "./article/"+$(this).attr("name"));
});

$(".top_tag").click(function (e) {
    e.preventDefault();
    if ($(this).hasClass("tag_onselect")) {
        return
    }
    $("#" + name_mapper[$(".tag_onselect").attr("name")]).css("display","none");
    $(".tag_onselect").removeClass("tag_onselect").addClass("tag_offselect");
    $(this).removeClass("tag_offselect").addClass("tag_onselect");
    $(".li_onselect").removeClass("li_onselect");
    $("#" + name_mapper[$(".tag_onselect").attr("name")] + " li:first-child").addClass("li_onselect").removeClass("breakingnews");
    $(".article > iframe").attr("src", "./article/"+$(".li_onselect").attr("name"));
    $("#" + name_mapper[$(this).attr("name")]).css("display","block");
    indexmask(".index_li")
});


