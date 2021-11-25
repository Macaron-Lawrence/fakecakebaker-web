

$(document).ready(function () {
    $(".bodyscale").css("transform","scale(" + $(window).height()/864 +")")
    $(".bodyscale").css("height",100/$(window).height()*864 +"vh")
    $("#scroll").height(100*$('.text_main').height()/$('.text_main')[0].scrollHeight + "%");
    $(".text_main p").each(function(){
        // str = $(this).html(space_replace($(this).text()));
        $(this).html($(this).html().replace(/“|”|《|》|（|）/gi, function(matched){
            return mapper[matched];
        }))
    });

}
);

let mapper = {
    "“":"<span>“</span>",
    "”":"<span>”</span>",
    "《":"<span>《</span>",
    "》":"<span>》</span>",
    "（":"<span>（</span>",
    "）":"<span>）</span>"
}

// let space_replace=(txt)=>{
//     t = txt.replace(/“|”|《|》|（|）/gi), function(matched){
//         return "1"
//     }
//     return t
// }

$(".text_main").scroll(function () {
    $("#scroll").css('top',100*$(".text_main").scrollTop()/$('.text_main')[0].scrollHeight + "%")
});

$(window).resize(function () {
    $(".bodyscale").css("transform","scale(" + $(window).height()/864 +")")
    $(".bodyscale").css("height",100/$(window).height()*864 +"vh")
    $("#scroll").height(100*$('.text_main').height()/$('.text_main')[0].scrollHeight + "%")
});

