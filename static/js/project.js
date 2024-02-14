class Project {
    constructor(name) {
        this.name = name;
    }

    static clearForm() {
        $('.clear-form').on('click', function() {
            $('form').trigger('reset');
        });
    }

    static getProjectID() {
        const project_id = window.location.pathname.split('/')[4];
        return project_id;
    }

    static newProjectThumb(id, title, name, about, image) {
       var thumb = `<div class="col-md-4"><div class="card mb-4 border-0">`;
        thumb += `<img src=${ image } alt="${ name }" class="card-img-top proj-card-img">`;
        thumb += `<div class="card-body"><h5 class="card-title">`;
        thumb += `<a href="/portfolio/project/${ name }/${ id }/" class="card-link">`;
        thumb += `${ title.slice(0, 50) }</a></h5>`;
        thumb += `<p class="card-text">${ about.slice(0, 75) }</p></div></div></div>`;
        console.log('thumb = ', thumb);
        return thumb;
    }

    static prependNewProject(project) {
        console.log('prepend project');
        var id = project.id;
        var title = project.title;
        var name = project.name;
        var about = project.about;
        var image = project.image;

        $('#project_list_div').prepend(Project.newProjectThumb(id, title, name, about, image));
    }

    static addProjectEventListener() {
        const form = document.getElementById('addProjectForm');
        form.addEventListener('submit', Project.addProject);
        // $('#addProjectForm').on('hide.bs.modal', function() {
        //     $(this).trigger('reset');
        // })
        // document.getElementById('addProjectModal').modal('hide');
        // document.getElementById('addProjectForm').addEventListener('submit', Project.addProject);
        // console.log(url)
    }

    static addProject(event) {
        event.preventDefault();
        console.log('project.js');

        const formData = new FormData($('#addProjectForm')[0]);
        // NOTE: FormData EXPECTS DOM ELEMENT - NOT JQUERY OBJECT. [0] RETRIEVES FIRST DOM ELEMENT IN JQUERY OBJECT ARRAY
        // const url = '/portfolio/add_project/';

        $.ajax({
            type: 'POST',
            url: '/portfolio/add_project/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('response', response['new_project']);
                Project.prependNewProject(response['new_project']);
                // $('#addProjectForm').trigger('reset');
                // $('#addProjectModal').on('hidden.bs.modal', function() {
                //     $(this).find('form').trigger('reset');
                // });
                $('#addProjectForm').trigger('reset');
            },
            error: function(error) {
                console.log(error);
            }
        });

        // $.post(url, formData, function(response) {
        //     if (response['success'] == true) {
        //         console.log(response)
        //     }
        // })
    }

    static addBrief(project) {
        console.log('addBrief ', project);
        var year = project.year;
        console.log(year);
        var programs = project.programs;
        var sub_title = project.sub_title;
        var brief = project.brief;

        if (!$('#briefDiv').hasClass('mb-5')) {
            $('#breifDiv').addClass('mb-5')
        }
    
        if (year !== '') {
            $('#project_year').html(year);
        }

        var $programsList = $('.program-list');
        $programsList.empty();
        if (programs.length !== 0) {
            for ( var i = 0; i < programs.length; i++ ) {
                $(`.program-list`).append(
                    `<li id="program_${ programs[i].pk }">${ programs[i].name }</li>`
                );
            }
        }

        if (sub_title.length !== 0){
            $('#project_sub_title').html(sub_title);
        }

        if (brief !== '') {
            $('#project_brief').html(brief);
        }

    }

    static updateProjectBriefEventListener() {
        const form = document.getElementById('updateProjectBriefForm');
        console.log(form);
        form.addEventListener('submit', Project.updateProjectBrief);
        
    }

    static updateProjectBrief(event) {
        event.preventDefault();
        console.log('updateProjectBrief');

        const project_id = window.location.pathname.split('/')[4];
        console.log('project_id ', project_id);

        const formData = new FormData($('#updateProjectBriefForm')[0]);
        formData.append('project_id', project_id);
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_brief/',
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                console.log('response ', response['updated_project']);

                Project.addBrief(response['updated_project']);
                // $('#updateProjectBriefForm').trigger('reset');

            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageI(image) {

        var $imageDiv = $('#imageI');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageI = `<img src="${ image }" alt="Screenshot of project" />`;
        $('#imageI').append(imageI);

    }

    static ImageIEvent() {

        const form = document.getElementById('updateProjectImgIForm');
        form.addEventListener('submit', Project.projectImageI);

    }

    static projectImageI(event) {

        event.preventDefault();
        console.log('projectImageI');

        const project_id = window.location.pathname.split('/')[4];
        console.log('project_id ', project_id);

        const formData = new FormData($('#updateProjectImgIForm')[0]);
        formData.append('project_id', project_id);
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageI/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('response ', response['updated_project']);
                // var project = response['updated_project'];
                // console.log(project, project.image);
                Project.addImageI(response['updated_project'].fullpage_imgI);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addProcessI(project) {

        const $bannerTextIandProcessI = $('#bannerTextIandProcessI');

        if ($bannerTextIandProcessI.length > 0) {
            $bannerTextIandProcessI.removeClass('mb-5');
            $bannerTextIandProcessI.empty();
        }

        var banner_textI = project.banner_textI;
        var processI = project.processI;

        if (banner_textI != '' && processI != '') {

            var processIDiv = `<div class="row align-items-center"><div class="col-md-5">`;
            processIDiv += `<h2 id="bannerTextI" class="text-center">${ banner_textI }</h2></div>`;
            processIDiv += `<div class="col-md-7 pe-0 me-0"><p id="processI" class="">`;
            processIDiv += `${ processI }</p></div></div>`;

            $bannerTextIandProcessI.addClass('mb-5');
            $bannerTextIandProcessI.append(processIDiv);

        } else if (banner_textI != '' && processI == '') {

            var bannerTextDiv = `<div class="row justify-content-center">`;
            bannerTextDiv += `<div id="bannerTextICol12" class="col-md-12">`;
            bannerTextDiv += `<h2 id="bannerTextI" class="text-center">${ banner_textI }</h2></div></div>`;

            $bannerTextIandProcessI.addClass('mb-5');
            $bannerTextIandProcessI.append(bannerTextDiv)

        } else if  (banner_textI == '' && processI != '') {

            var processIDiv = `<div class="row justify-content-center">`;
            processIDiv += `<div id="processICol12" class="col-md-12">`;
            processIDiv += `<p id="processI" class="">${ processI }`;
            processIDiv += `</p></div></div>`;
            
            $bannerTextIandProcessI.addClass('mb-5');
            $bannerTextIandProcessI.append(processIDiv);

        }

        // $('#banner_textI').html(banner_textI);
        // $('#processI').html(processI);

    }

    static processIEvent() {

        const form = document.getElementById('updateProjectProcessIForm');
        form.addEventListener('submit', Project.projectProcessI);

    }

    static projectProcessI(event) {

        event.preventDefault();
        console.log('projectProcessI');

        const project_id = window.location.pathname.split('/')[4];

        const formData = new FormData($('#updateProjectProcessIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processI/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('response ', response['updated_project']);
                Project.addProcessI(response['updated_project']);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageII(image) {

        var $imageDiv = $('#imageII');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageII = `<img src="${ image }" alt="project screenshopt" />`;
        $('#imageII').append(imageII);

    }

    static imageIIEvent() {

        const form = document.getElementById('updateProjectImgIIForm');
        form.addEventListener('submit', Project.projectImageII);

    }

    static projectImageII(event) {

        event.preventDefault();
        console.log('Image II');

        const project_id = window.location.pathname.split('/')[4];

        const formData = new FormData($('#updateProjectImgIIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageII/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('response ', response['updated_project']);
                Project.addImageII(response['updated_project'].fullpage_imgII);
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    static addProcessII(processII) {

        $('#processII').html(processII);

    }

    static processIIEvent() {

        const form = document.getElementById('updateProjectProcessIIForm');
        form.addEventListener('submit', Project.processII);

    }

    static processII(event) {
        
        event.preventDefault();

        var project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectProcessIIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processII/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log('response ', response['updated_project']);
                Project.addProcessII(response['updated_project'].processII);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageIII(image) {

        var $imageDiv = $('#imageIII');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageIII = `<img src="${ image }" alt="project screenshot" />`;
        $imageDiv.append(imageIII);

    }

    static imageIIIEvent() {

        const form = document.getElementById('updateProjectImgIIIForm');
        form.addEventListener('submit', Project.imageIII);

    }

    static imageIII(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectImgIIIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageIII/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addImageIII(response['updated_project'].fullpage_imgIII);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageIV(image) {

        var $imageDiv = $('#imageIV');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty()
        }

        var imageIV = `<img src="${ image }" atl="project screenshot" />`;
        $imageDiv.append(imageIV);
    }

    static imageIVEvent() {

        const form = document.getElementById('updateProjectImgIVForm');
        form.addEventListener('submit', Project.imageIV);
    }

    static imageIV(event) {

        event.preventDefault()

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectImgIVForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageIV/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addImageIV(response['updated_project'].fullpage_imgIV);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addProcessIII(project) {

        var $processIIIandprocessIV = $('#processIIIandprocessIV');
        
        if ($processIIIandprocessIV.length > 0) {
            $processIIIandprocessIV.empty();
        }

        if (project.processIII != '' && project.processIV != '') {
            // var $processIV = $('#processIV');
            // $processIV.html(project.processIV);
            var processIIIandIVCols = `<div class="col-md-6">`;
            processIIIandIVCols += `<p id="processIII" class="">${ project.processIII }`;
            processIIIandIVCols += `</p></div>`;
            processIIIandIVCols += `<div class="col-md-6">`;
            processIIIandIVCols += `<p id="processIV" class="">${ project.processIV }`;
            processIIIandIVCols += `</p></div>`;

            $processIIIandprocessIV.append(processIIIandIVCols);

        } else if ( project.processIII != '' && project.processIV == '' ) {

            // var $processIII = $('#processIII');

            var processIIICol = `<div id="processIIICol12" class="col-md-12">`;
            processIIICol += `<p id="processIII" class="">${ project.processIII}`;
            processIIICol += `</p></div>`;

            // $processIII.html(project.processIII);
            $processIIIandprocessIV.append(processIIICol);

        } else if ( project.processIV != '' && project.processIII == '' ) {

            var $processIIICol12 = $('#processIIICol12');
            $processIIICol12.removeClass('col-md-12').addClass('col-md-6');

            var processIVCol = `<div class="col-md-12">`;
            processIVCol += `<p id="processIV" class="">${ project.processIV }`;
            processIVCol += `</p></div>`;

            $processIIIandprocessIV.append(processIVCol);

        }

    }

    static processIIIEvent() {

        const form = document.getElementById('updateProjectProcessIIIForm');
        form.addEventListener('submit', Project.processIII);

    }

    static processIII(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectProcessIIIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processIII/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addProcessIII(response['updated_project']);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageV(image) {

        var $imageDiv = $('#imageV');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageV = `<img src="${ image }" alt="project screenshot" />`;
        $imageDiv.append(imageV);
    }

    static imageVEvent() {
        
        const form = document.getElementById('updateProjectImgVForm');
        form.addEventListener('submit', Project.imageV);
    }

    static imageV(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectImgVForm')[0]);
        formData.append('project_id', project_id );

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageV/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addImageV(response['updated_project'].fullpage_imgV);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addProcessIV(processV) {

        $('#processV').html(processV);

    }

    static processIVEvent() {

        const form = document.getElementById('updateProjectProcessIVForm');
        form.addEventListener('submit', Project.processIV);

    }

    static processIV(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectProcessIVForm')[0]);
        formData.append('project_id', project_id);
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processIV/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                Project.addProcessIV(response['updated_project'].processV);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageVI(image) {
        
        var $imageDiv = $('#imageVI');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageVI = `<img src="${ image }" alt="project screenshot" />`;
        $imageDiv.append(imageVI);
    }

    static imageVIEvent() {

        const form = document.getElementById('updateProjectImgVIForm');
        form.addEventListener('submit', Project.imageVI);

    }

    static imageVI(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectImgVIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageVI/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addImageVI(response['updated_project'].fullpage_imgVI);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addProcessV(project) {

        var $processVIandporcessVII = $('#processVIandprocessVII');

        if ($processVIandporcessVII.length >0) {
            $processVIandporcessVII.empty();
        }

        if (project.processVI != '' && project.processVII != '') {
            var processVIandVIICols = `<div class="col-md-6">`;
            processVIandVIICols += `<p id="processVI" class="">${ project.processVI }`;
            processVIandVIICols += `</p></div>`;
            processVIandVIICols += `<div class="col-md-6">`;
            processVIandVIICols += `<p id="processVII" class="">${ project.processVII }`;
            processVIandVIICols += `</p></div>`;

            $processVIandporcessVII.append(processVIandVIICols);

        } else if (project.processVI != '' && project.processVII == '') {
            var processVICol = `<div id="processVICol12" class="col-md-12">`;
            processVICol += `<p id="processVI" class="">${ project.processVI }`;
            processVICol += `</p></div>`;

            $processVIandporcessVII.append(processVICol);

        } else if (project.processVII != '' && project.processVI == '') {
            var processVIICol = `<div id="processVIICol12" class="col-md-12">`;
            processVIICol += `<p id="processVII" class="">${ project.processVII }`;
            processVIICol += `</p></div>`;

            $processVIandporcessVII.append(processVIICol);
        }
    }

    static processVEvent() {
        const form = document.getElementById('updateProjectProcessVForm');
        form.addEventListener('submit', Project.processV);
    }

    static processV(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectProcessVForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processV/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addProcessV(response['updated_project']);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addImageVII(image) {

        var $imageDiv = $('#imageVII');

        if ($imageDiv.children().length > 0) {
            $imageDiv.empty();
        }

        var imageVII = `<img src="${ image }" alt="project screenshopt" />`;
        $imageDiv.append(imageVII);

    }

    static imageVIIEvent() {

        const form = document.getElementById('updateProjectImgVIIForm');
        form.addEventListener('submit', Project.imageVII);

    }

    static imageVII(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectImgVIIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_imageVII/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addImageVII(response['updated_project'].fullpage_imgVII);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static addProcessVI(project) {

        var $processVIIIandprocessIX = $('#processVIIIandprocessIX');

        if ($processVIIIandprocessIX.length > 0) {
            $processVIIIandprocessIX.empty();
        }

        if (project.processVIII != '' && project.processIX != '') {

            var processVIIIandIX = `<div class="col-md-6">`;
            processVIIIandIX += `<p id="processVIII" class="">${ project.processVIII }`;
            processVIIIandIX += `</p></div>`;
            processVIIIandIX += `<div class="col-md-6">`;
            processVIIIandIX += `<p id="processIX" class="">${ project.processIX }`;
            processVIIIandIX += `</p></div>`;

            $processVIIIandprocessIX.append(processVIIIandIX);

        } else if (project.processVIII != '' && project.processIX == '') {

            var processVIII = `<div id="processVIIICol12" class="col-md-12">`;
            processVIII += `<p id="processVIII" class="">${ project.processVIII }`;
            processVIII += `</p></div>`;

            $processVIIIandprocessIX.append(processVIII);

        } else if (project.processVIII == '' && project.processIX != '') {

            var processIX = `<div id="processIXCol12" class="col-md-12">`;
            processIX += `<p id="processIX" class="">${ project.processIX }`;
            processIX += `</p></div>`;

            $processVIIIandprocessIX.append(processIX);

        }

    }

    static processVIEvent() {

        const form = document.getElementById('updateProjectProcessVIForm');
        form.addEventListener('submit', Project.processVI);

    }

    static processVI(event) {

        event.preventDefault();

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectProcessVIForm')[0]);
        formData.append('project_id', project_id);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_processVI/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Project.addProcessVI(response['updated_project']);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static responsiveIWithIIIImages(imageI, imageII, imageIII) {

        var responsiveDivWithIII = `<div class="row d-flex container-fluid justify-content-center g-0">`;
        responsiveDivWithIII += `<div class="col-sm-5">`;
        responsiveDivWithIII += `<div id="responsiveI" class="col-img mb-4 d-flex justify-content-center">`;
        responsiveDivWithIII += `<img src="${ imageI }" alt="responsive screenshot"></div>`;

        responsiveDivWithIII += `<div class="row"><div class="col-sm-12">`;
        responsiveDivWithIII += `<div id="responsiveII" class="col-img d-flex justify-content-center">`;
        responsiveDivWithIII += `<img src="${ imageII }" alt="responsive screenshot"></div>`;
        responsiveDivWithIII += `</div></div></div>`;
        responsiveDivWithIII += `<div class="col-sm-5 ms-0 ps-0">`;
        responsiveDivWithIII += `<div class="ps-4 mb-4"><h1 id="bannerTextII" class="col-text">`;

        responsiveDivWithIII += `</h1></div>`;
        responsiveDivWithIII += `<div id="responsiveIII" class="col-img d-flex justify-content-center align-items-center">`;
        responsiveDivWithIII += `<img src="${ imageIII }" alt="responsive screenshot"></div></div></div>`;

        return responsiveDivWithIII;

    }

    static responsiveIWithIIImages(imageI, imageII) {
        
        var responsiveDivWithII = `<div class="row d-flex container-fluid justify-content-center g-0">`;
        responsiveDivWithII += `<div class="col-sm-5">`;
        // responsiveDivWithII += `<div id="">`;
        responsiveDivWithII += `<div class="ps-4 mb-4">`;
        responsiveDivWithII += `<h1 id="bannerTextII" class="col-text"></h1></div>`;
        // responsiveDivWithII += `</div>`;
        responsiveDivWithII += `<div id="responsiveI" class="col-img mb-4 d-flex justify-content-center">`;
        responsiveDivWithII += `<img src="${ imageI }" alt="responsive screenshot"></div></div>`;
        responsiveDivWithII += `<div class="col-sm-5">`;
        responsiveDivWithII += `<div id="responsiveII" class="col-img d-flex justify-content-center">`;
        responsiveDivWithII += `<img src="${ imageII }" alt="responsive screenshot"></div></div></div>`;

        return responsiveDivWithII;

    }

    static responsiveIWithIImage(imageI) {

        var responsiveDivWithI = `<div class="row justify-content-center mb-4">`;
        responsiveDivWithI += `<h2 id="bannerTextII" class="text-center"></h2></div>`;
        responsiveDivWithI += `<div class="row justify-content-center"><div class="col-md-5">`;
        responsiveDivWithI += `<div id="responsiveI" class="col-img mb-4 d-flex justify-content-center">`;
        responsiveDivWithI += `<img src="${ imageI }" alt="responsive screenshot"></div></div></div>`;

        return responsiveDivWithI;
    }

    static addResponsiveI(project) {

        var imageI = project.responsive_imgI;
        var imageII = project.responsive_imgII;
        var imageIII = project.responsive_imgIII;

        var $responsiveDivI = $('#responsiveDivI');
        $responsiveDivI.empty();
        console.log('empty div');

        if (imageI != null && imageII != null && imageIII != null) {
            console.log('3 images');
            var divWith3Images = Project.responsiveIWithIIIImages(imageI, imageII, imageIII);

            $responsiveDivI.append(divWith3Images)

            if (project.banner_textII != '') {
                $('#bannerTextII').html(project.banner_textII);
            }  

        } else if (imageI != null && imageII != null && imageIII == null) {
            console.log('2 images');
            var divWith2Image = Project.responsiveIWithIIImages(imageI, imageII);

            $responsiveDivI.append(divWith2Image);

            if (project.banner_textII != '') {
                $('#bannerTextII').html(project.banner_textII)
            }
            
        } else if (imageI != null && imageII == null && imageIII == null) {
            console.log('1 image');
            var divWith1Image = Project.responsiveIWithIImage(imageI);

            $responsiveDivI.append(divWith1Image);

            if (project.banner_textII != '') {
                $('#bannerTextII').html(project.banner_textII);
            }

        }


        // $responsiveDivI.css('display', 'block');
        // $responsiveDivI.append(responsiveDiv);

    }

    static responsiveIEvent() {

        const form = document.getElementById('updateProjectResponsiveIForm');
        form .addEventListener('submit', Project.responsiveI);

    }

    static responsiveI(event) {

        event.preventDefault()

        const project_id = Project.getProjectID();
        const formData = new FormData($('#updateProjectResponsiveIForm')[0]);
        formData.append('project_id', project_id);
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/portfolio/update_responsiveI/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                Project.addResponsiveI(response['updated_project']);
            },
            error: function(error) {
                console.log(error);
            }
        })
    }


}
