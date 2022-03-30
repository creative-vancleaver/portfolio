function addAboutForm() {

    console.log('entering ADDABOUTFORM');
    
    $('#addAbout').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {

            $this.removeClass("clicked_once");
            $('#aboutForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#aboutForm').slideDown();
        };
    });
};

function addEduForm() {

    console.log('HELLO from edu');

    $('#addEdu').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {

            $this.removeClass("clicked_once");
            $('#eduForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#eduForm').slideDown();
        };
    });
};

function addSkillForm() {

    $('#addSkill').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {

            $this.removeClass("clicked_once");
            $('#skillForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#skillForm').slideDown();
        };
    });
};

function addProgProjForm() {

    $('#addProgProj').on('click', function () {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {

            $this.removeClass("clicked_once");
            $('#progProjForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#progProjForm').slideDown();
        };
    });
};

function addWorkForm() {

    $('#addWork').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {
            
            $this.removeClass("clicked_once");
            $('#workForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#workForm').slideDown();
        };
    });
};

$(document).ready(function() {

    $('#aboutForm').hide();
    $('#eduForm').hide();
    $('#skillForm').hide();
    $('#progProjForm').hide();
    $('#workForm').hide();

    addAboutForm();
    addEduForm();
    addSkillForm();
    addProgProjForm();
    addWorkForm();

});