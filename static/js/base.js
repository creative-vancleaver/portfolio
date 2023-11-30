const $ = require('jquery')

function activeNavLink() {

    console.log('entering activeNavLink');

    let $buttons = document.querySelectorAll('.nav-link');
    console.log($buttons);
    console.log('HIII');

    // Object.keys($buttons).forEach(function (button){

    //     console.log($buttons[button]);
 
    // });

    $buttons.forEach((button) => {

        console.log(button);
        button.addEventListener('click', function() {

            // var $active = $('.active');
            var $button = $('.nav-link');

            if($button.hasClass('active')) {
                $button.removeClass('active');
            } else {
                $button.addClass('active');
            };
        });
    });

    // $('.nav-link').on('click', function() {

    //     console.log('HIIII');
    //     var $this = $(this);
    //     var $that = $('.active');

    //     console.log($(this));
    //     console.log($that);

    //     $that.removeClass("active");
    //     $this.addClass("active");



    // });
};

$(document).ready(function() {
    activeNavLink();
});

// module.export = activeNavLink;
module.exports = activeNavLink;