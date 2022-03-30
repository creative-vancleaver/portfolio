function addProjectForm() {

    console.log('Thisis the ProjectForm JS');

    // may seem obvious - but this vv should be the BUTTON clicked to show form further down..
    $('#addProject').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {
            $this.removeClass("clicked_once");
            // also just now realizing this is NOT the form itself, but a div on the page containing the form...
            $('#projectForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#projectForm').slideDown();
        };
    });
};

function addDesignForm() {

    console.log('this is deisgg form JS');

    $('#addDesign').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {
            $this.removeClass("clicked_once");
            $('#designForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#designForm').slideDown();
        };
    });
};

function addDevForm() {

    $('#addDev').on('click', function() {
        var $this = $(this);

        if($this.hasClass("clicked_once")) {
            $this.removeClass("clicked_once");
            $('#devForm').slideUp();

        } else {

            $this.addClass("clicked_once");
            $('#devForm').slideDown();
        };
    });
};

$(document).ready(function() {

    $('#projectForm').hide();
    $('#designForm').hide();
    $('#devForm').hide();

    addProjectForm();
    addDesignForm();
    addDevForm();

});