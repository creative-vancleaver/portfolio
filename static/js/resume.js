
class Resume {
    constructor(name) {
        this.name = name;
    }

// ABOUT ME

    static addBio(about) {
        var text = about.text;
        // console.log('add bio text ', text);
        var image = about.image;
        var header = about.header;
        console.log('add bio header ', header);

        var bioImage = $('#bioImage');
        var bioHeader = $('#bioHeader');
        var bioText = $('#bioText');

        if (image != null) {

            var new_image = `<img src="${ image }" class="self round float-start w-50 col-sm-8 me-3" alt="photo of Jacob">`;

            $('#bioImage').empty();
            $('#bioImage').append(new_image);

        } else {
            bioImage.empty();
        }

        if (text != '') {

            $('#bioText').html(text);

        } else {
            bioText.html('');
        }

        if (header != '') {
            $('#bioHeader').html(header);
        } else {
            bioHeader.html('');
        }
    }

    static updateBioEvent() {
        const form = document.getElementById('updateBioForm');
        form.addEventListener('submit', Resume.updateBio);
    }

    static updateBio(event) {

        event.preventDefault();

        const about_id = '1';
        const formData = new FormData($('#updateBioForm')[0]);
        formData.append('about_id', about_id);

        $.ajax({
            type: 'POST',
            url: '/resume/update_about/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Resume.addBio(response['updated_about'])
                console.log(response['updated_about'])
            }
        })

    }

// POPULATE UPDATE FORMS  

    static populateEduForm(formData) {
        console.log('populating form');
        $('#updateSupplementalEducationForm #id_name').val(formData.name);
        $('#updateSupplementalEducationForm, #id_type').val(formData.type);
        $('#updateSupplementalEducationForm').attr('data-pk', formData.pk);
    }

    static populateProjForm(formData) {
        console.log('populating project form', formData);
        $('#updateProgrammingProjectForm #id_name').val(formData.name);
        $('#updateProgrammingProjectForm #id_description').val(formData.description);
        $('#updateProgrammingProjectForm').attr('data-pk', formData.pk);
    }

    static populateEmploymentForm(formData) {
        console.log('populating employment form');
        $('#updateEmploymentForm #id_name').val(formData.name);
        $('#updateEmploymentForm #id_job_title').val(formData.job_title );
        $('#updateEmploymentForm').attr('data-pk', formData.pk)
    }

    static populateTechSkillsForm(formData) {
        console.log('popuate TechSkillForm');
        $('#updateTechSkillsForm #id_type').val(formData.type);

        console.log(formData.programs);
        // UNCHECK ALL BOXES INITIALLY
        $('#updateTechSkills input[name="programs"]').prop('checked', false);
        var programs = formData.programs;
        for (let i = 0; i < programs.length; i++) {
            var programId = programs[i].id;
            console.log(programId);
            $(`#updateTechSkillsForm input[name="programs"][value="${ programId }"]`).prop('checked', true);
        }
        $('#updateTechSkillsForm').attr('data-pk', formData.pk);
        // $('#updateTechSkillsForm #')
    }

    static populateForm(model, id) {

        $.ajax({
            url: '/resume/populate_form/',
            data: { 'model_name': model, 'obj_id': id },
            dataType: 'json',
            success: function(response) {
                console.log('response ', response, response.form_data);

                if (model === 'SupplementalEducation') {
                    Resume.populateEduForm(response.form_data);
                    // Resume.updateEducationEvent(id);
                    // Resume.addUpdateEvent(model, id, 'submit');
                } else if (model === 'ProgrammingProject') {
                    Resume.populateProjForm(response.form_data);
                    // Resume.addUpdateProjEvent(model, id, 'submit');
                } else if (model === 'Employment') {
                    console.log('Employment')
                    Resume.populateEmploymentForm(response.form_data)
                } else if (model === 'TechSkills') {
                    console.log('TechSkills');
                    Resume.populateTechSkillsForm(response.form_data);
                    // Resume.showAddProgramForm();
                } else {
                    console.log('No model matching');
                }
                Resume.addUpdateEvent(model, id, 'submit');

            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    static populateFormEvent() {

        // const eduElements = document.querySelectorAll('.updateEdu');
        const formElements = document.querySelectorAll('.updateButton');

        formElements.forEach(form => {
            form.addEventListener('click', function() {
                var model = form.getAttribute('data-model');
                var id = form.getAttribute('data-id');
                Resume.populateForm(model, id);
                // Resume.updateEducationEvent(id);
            })
        })


        // edu.addEventListener('click', function() {
        //     Resume.populateForm(model, id);
        // });
    }

    static handleUpdateEvent(submitEvent, id, model) {

        if (submitEvent && submitEvent.preventDefault) {

            submitEvent.preventDefault();

            if (model === 'SupplementalEducation') {
                Resume.updateEducation(submitEvent, id, model);
            } else if (model === 'ProgrammingProject') {
                console.log('handleUpdateEvent === programmingproject');
                Resume.updateProgrammingProject(submitEvent, id, model);
            } else if (model === 'Employment') {
                console.log('handleUpdateEvent === employment');
                Resume.updateEmployment(submitEvent, id, model);
            } else if (model === 'TechSkills') {
                console.log('handleupdateevent == tech skills');
                Resume.updateTechSkill(submitEvent, id, model);
                // Resume.showAddProgramForm();
            }


        }
    }

    static addUpdateEvent(model, id, eventType) {
        console.log('adding event ', model);
        const form = document.querySelector(`#update${ model }Form[data-pk="${ id }"]`);
        console.log('addupdatevent form ', form);
        if (form) {

            form.addEventListener(eventType, function(submitEvent) {
                Resume.handleUpdateEvent(submitEvent, id, model);
            });

            // const listenerFunction = function(submitEvent) {
            //     Resume.updateEducation(submitEvent, id);
            // };

            // form.addEventListener(eventType, listenerFunction);
            // form.setAttribute('data-update-event-listener', listenerFunction);

            // form.addEventListener(eventType, function(submitEvent){
            //     Resume.updateEducation(submitEvent, id)
            // });
        }
    }

    static removeUpdateEvent(model, id, eventType) {
        console.log('removing event');
        const form = document.querySelector(`#update${ model }Form[data-pk="${ id }"]`);
        if (form) {

            form.removeEventListener(eventType, function(submitEvent){
                Resume.handleUpdateEvent(submitEvent, id, model);
            });

            // const listenerFunction = form.getAttribute('data-update-event-listener');

            // if (listenerFunction) {
            //     form.removeEventListener(eventType, listenerFunction);
            // }

            // form.removeEventListener(eventType);
        }
    }

// SUPPLEMENTAL EDUCATION

    static addEducationDisplay(education) {

        const $suppEduDiv = $('#suppEduDiv');

        var name = education.name;
        var type = education.type;
        var year = education.year;

        var newEduRow = `<div class="row row-cols-1 row-cols-md-2">`;
        newEduRow += `<div class="col">`;

        // newEduRow += `{% if request.user.is_superuser %}`;
        newEduRow += `<i class="fa-solid fa-arrows-rotate ms-3 me-3 resume-add"></i>`;
        // newEduRow += `{% endif %}`;

        newEduRow += `${ name }</div><div class="col"><p>`;
        newEduRow += `${ type }</p></div></div>`;

        $suppEduDiv.prepend(newEduRow);

    }

    static addEducationEvent() {
        const form = document.getElementById('addSupplementalEducationForm');
        form.addEventListener('submit', Resume.addEducation);
    }

    static addEducation(event) {

        event.preventDefault();

        const formData = new FormData($('#addSupplementalEducationForm')[0]);

        $.ajax({
            type: "POST",
            url: '/resume/add_edu/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Resume.addEducationDisplay(response['new_education']);
                $('#addSupplementalEducationForm')[0].reset();
            },
            error: function(error) {
                console.log(error);
            }
        })
    }

    static updateEducationDisplay(education) {

        var name = education.name;
        var type = education.type;
        var year = education.year;
        var pk = education.pk;

        var eduName = $('#eduName[data-id="' + pk + '"]');
        var eduType = $('#eduType[data-id="' + pk + '"]');

        eduName.html(name);
        eduType.html(type);

        // $('#eduName').html(name);
        // $('#eduType').html(type);

    }

    static updateEducation(event, pk, model) {
        event.preventDefault();

        console.log('UPDATEEDUCATION ', pk);

        const form = document.querySelector(`#updateSupplementalEducationForm[data-pk="${ pk }"]`);
        console.log('form ', form);
        if (form != null) {
            const formData = new FormData(form);
            console.log('formData = ', formData);
            formData.append('pk', pk);

            $.ajax({
                type: 'POST',
                url: '/resume/update_edu/',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    console.log(response);
                    Resume.updateEducationDisplay(response['updated_education']);
                    Resume.removeUpdateEvent(model, pk, 'submit')
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    }


    // static addUpdateProjEvent(model, id, eventType) {
    //     console.log('adding proj event');
    //     const form = document.querySelector(`#${ model }Form[data-pk="${ id }]`);
    //     if (form) {
    //         form.addEventListener(eventType, function(submitEvent) {
    //             console.log('project evvent listener ', model, id, form);
    //             // Resume.handleUpdateProjEvent(submitEvent, id);
    //         })
    //     }
    // }

    // static updateEducationEvent(id) {

    //     // document.addEventListener('DOMContentLoaded', function() {
            
    //     // })
    //     // const forms = document.querySelectorAll('.updateSupportEduForm');
    //     const form = document.querySelector(`#updateSupplementalEducationForm[data-pk="${ id }"]`);
    //     console.log(form);
    //     form.addEventListener('submit', function(submitEvent) {
    //         Resume.updateEducation(submitEvent, id);
    //     });

    //     // forms.forEach( form => {
    //     //     const eduPk = form.getAttribute('data-pk');
    //     //     console.log('pk ', eduPk);

    //     //     form.addEventListener('submit', function(submitEvent) {
    //     //         Resume.updateEducation(submitEvent, eduPk);
    //     //     })
    //     // })

    //     // var edPk = document.getElementById('')
    //     // // const form = document.getElementById('updateSupplementalEducationForm');
    //     // const form = document.querySelector('#updateSupplementalEducationForm[d')
    //     // const eduPk = form.getAttribute('data-pk');
    //     // console.log(eduPk);
    //     // form.addEventListener('submit', function(submitEvent) {
    //     //     Resume.updateEducation(submitEvent, eduPk)
    //     // });
    // }


// PROGRAMMING PROJECTS

    static addProgProjDisplay(prog_proj) {

        const $progProjDiv = $('#progProjDiv');

        var name = prog_proj.name;
        var description = prog_proj.description;

        var newProgProjRow = `<div class="row row-cols-1 row-cols-sm-2">`;
        newProgProjRow += `<div class="col">`;
        // newProgProjRow += `<i id="updateProj" class="updateProj updateButton fa-solid fa-arrows-rotate ms-3 me-3 resume-add" data-id="{{ proj.pk }}" data-model="ProgrammingProject" data-bs-toggle="modal" data-bs-target="#updateProgrammingProjectModal"></i>`;
        newProgProjRow += `<i class="fa-solid fa-arrows-rotate ms-3 me-3 resume-add"></i>`;
        newProgProjRow += `<span id="projName">${ name }</span></div><div class="col mb-3"><p>`;
        newProgProjRow += `${ description }</p></div></div>`;

        $progProjDiv.prepend(newProgProjRow);

    }

    static updateProgProjectDisplay(prog_proj) {

        var name = prog_proj.name;
        var description = prog_proj.description;
        var pk = prog_proj.pk;

        var projName = $('#projName[data-id="' + pk + '"]');
        var projDesc = $('#projDescription[data-id="' + pk + '"]');

        projName.html(name);
        projDesc.html(description);

    }

    static addProgProjEvent() {
        const form = document.getElementById('addProgrammingProjectForm');
        form.addEventListener('submit', Resume.addProgrammingProject);
    }

    static addProgrammingProject(event) {

        event.preventDefault();

        const formData = new FormData($('#addProgrammingProjectForm')[0]);

        $.ajax({
            type: 'POST',
            url: '/resume/add_programming_project/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Resume.addProgProjDisplay(response['new_prog_proj']);
                $('#addProgrammingProjectForm')[0].reset();
            },
            error: function(error) {
                console.log(error);
            }
        });
    }
    
    static updateProgrammingProject(event, pk, model) {
        event.preventDefault();
        console.log('updateProgrammingProject ', event, pk, model);

        const form = document.querySelector(`#updateProgrammingProjectForm[data-pk="${ pk }"]`);
        console.log(form);
        if (form != null) {
            const formData = new FormData(form);
            formData.append('pk', pk);

            $.ajax({
                type: 'POST',
                url: '/resume/update_prog_proj/',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    Resume.updateProgProjectDisplay(response['updated_prog_proj']);
                    Resume.removeUpdateEvent(model, pk, 'submit');
                },
                error: function(error) {
                    console.log(error);
                }
            });
        }
    }

// EMPLOYMENT

    static addEmploymentDisplay(employment) {

        const $employmentDiv = $('#employmentDiv');

        var name = employment.name;
        var job_title = employment.job_title;
        var start_date = employment.start_date;
        var end_date = employment.end_date;

        var newEmployDiv = `<div class="row row-cols-1 row-cols-sm-2">`;
        newEmployDiv += `<div class="col">`;
        newEmployDiv += `<i class="fa-solid fa-arrows-rotate ms-3 me-3 resume-add"></i>`;
        newEmployDiv += `<span id="employmentName">${ name }</span></div><div class="col"><p>`;
        newEmployDiv += `${ job_title }</p></div></div>`;

        $employmentDiv.prepend(newEmployDiv);

    }

    static updateEmploymentDisplay(employment) {

        var name = employment.name;
        var job_title = employment.job_title;
        // var start_date = employment.start_date
        // var end_date = employment.end_date;
        var pk = employment.pk;
        console.log(name, job_title, pk);

        var employName = $('#employmentName[data-id="' + pk + '"]');
        var employTitle = $('#employmentTitle[data-id="' + pk + '"]');

        employName.html(name);
        employTitle.html(job_title);

    }

    static addEmploymentEvent() {
        const form = document.getElementById('addEmploymentForm');
        form.addEventListener('submit', Resume.addEmployment);
    }

    static addEmployment(event) {
        event.preventDefault();

        const formData = new FormData($('#addEmploymentForm')[0]);
        console.log(formData);

        $.ajax({
            type: 'POST',
            url: '/resume/add_employment/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                Resume.addEmploymentDisplay(response['new_employment']);
                $('#addEmploymentForm').reset();
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    static updateEmployment(event, pk, model) {
        event.preventDefault();
        
        const form = document.querySelector(`#updateEmploymentForm[data-pk="${ pk }"]`);

        if (form != null) {
            const formData = new FormData(form);
            formData.append('pk', pk);

            $.ajax({
                type: 'POST',
                url: '/resume/update_employment/',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    Resume.updateEmploymentDisplay(response['updated_employment']);
                    Resume.removeUpdateEvent(model, pk, 'submit');
                },
                error: function(error) {
                    console.log(error);
                }
            })
        }
    }

// TECHNICAL SKILLS
    
    static addTechSkillDisplay(tech_skill) {

        const $techSkillsDiv = $('#techSkillsDiv');

        var type = tech_skill.type;
        var programs = tech_skill.programs;
        console.log(programs);

        var newTechSkillDiv = `<div class="row row-cols-1 row-cols-sm-2">`;
        newTechSkillDiv += `<div class="col">`;
        newTechSkillDiv += `<i class="fa-solid fa-arrows-rotate ms-3 me-3 resume-add"></i>`;
        newTechSkillDiv += `<span>${ type }</span></div>`;

        // WILL LIKELY NEED TO ADD SOME LOOP THROUGH PROGRAMS HERE

        newTechSkillDiv += `<div class="col">`;

        for (let i = 0; i < programs.length; i++) {
            newTechSkillDiv += `<p>${ programs[i].name }</p>`;
        }
        newTechSkillDiv += `</div></div>`;

        $techSkillsDiv.prepend(newTechSkillDiv);

    }

    static updateTechSkillDisplay(tech_skill) {

        var type = tech_skill.type;
        var programs = tech_skill.programs;
        var pk = tech_skill.pk;

        var $techType = $(`#techSkillType[data-id="${ pk }"]`);

        $techType.html(type);

        var $programsList = $('#techProgramsList');
        $programsList.empty();

        if (programs.length > 0) {
            for (let i = 0; i < programs.length; i++) {
                // var program = programs[i];
                // var $techSkillProg = $(`#techSkillProg[data-prog-id="${ program.pk }"]`);
                // $techSkillProg.html(program.name);
                $programsList.append(
                    `<p>${ programs[i].name }</p>`
                );
            }
        }

    }

    static addTechSkillEvent() {
        const form = document.getElementById('addTechSkillsForm');
        form.addEventListener('submit', Resume.addTechSkill);
    }

    static addTechSkill(event) {

        event.preventDefault();

        const formData = new FormData($('#addTechSkillsForm')[0]);

        $.ajax({
            type: 'POST',
            url: '/resume/add_tech_skill/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                Resume.addTechSkillDisplay(response['new_tech_skill']);
                $('#addTechSkillsForm')[0].reset();
            },
            error: function(error) {
                console.log(error);
            }
        });
    }

    static updateTechSkill(event, pk, model) {

        event.preventDefault();

        const form = document.querySelector(`#updateTechSkillsForm[data-pk="${ pk }"]`);
        console.log(form);
        if (form != null) {
            const formData = new FormData(form);
            formData.append('pk', pk);

            $.ajax({
                type: 'POST',
                url: '/resume/update_tech_skill/',
                data: formData,
                processData: false,
                contentType: false,
                success: function(response) {
                    Resume.updateTechSkillDisplay(response['updated_tech_skill']);
                    Resume.removeUpdateEvent(model, pk, 'submit');
                },
                error: function(error) {
                    console.log(error)
                }
            })
        }
    }

// PROGRAMS

    static showAddProgramForm() {
        console.log('show program form');
        $('#addProgramButton').on('click', function() {
            if ($('#addProgramButton').hasClass('open')) {
                $('#programFormContainer').slideUp();
                $('#addProgramButton').removeClass('open');
            } else {
                $('#addProgramButton').addClass('open');
                $('#programFormContainer').slideDown()
            }

        $('.hideProgramForm').on('click', function() {
            $('#programFormContainer').slideUp();
            $('#addProgramButton').removeClass('open');
        });

        });
    }

    static addProgramDisplay(program) {

        console.log('add program display');
        var $skillCheckboxList = $('#skillCheckboxList');

        var name = program.name;
        var id = program.id;

        var newProgramBox = `<label class="col-4"><label>`;
        newProgramBox += `<input type="checkbox" name="programs" value="${ id }">`;
        newProgramBox += `${ name }</label></label>`;

        $skillCheckboxList.append(newProgramBox);
    }

    static addProgramEvent() {
        // $('#programFormContainer').on('submit')
        const form = document.getElementById('addProgramForm');
        form.addEventListener('submit', Resume.addProgram);

    }

    static addProgram(event) {
        // const form  = document.getElement
        event.preventDefault();
        // BECAUSE THE FORM IS NOT RENDERING IN A <FORM> TAG - I MUST MANUALLY DECLARE FORM DATA
        // var formData = {
        //     csrfmiddlewaretoken: $('#programFormContainer input[name="csrfmiddlewaretoken"]').val(),
        //     name: $('#programFormContainer input[name="name"]').val()
        // };
        const formData = new FormData($('#addProgramForm')[0]);

        $.ajax({
            type: 'POST',
            url: '/portfolio/add_program/',
            data: formData,
            processData: false,
            contentType: false,
            success: function(response) {
                console.log(response);
                Resume.addProgramDisplay(response['new_program']);
                $('#addProgramForm')[0].reset();
            },
            error: function(error) {
                console.log(error);
            }
        })


    }








}


// function addAboutForm() {

//     console.log('entering ADDABOUTFORM');
    
//     $('#addAbout').on('click', function() {
//         var $this = $(this);

//         if($this.hasClass("clicked_once")) {

//             $this.removeClass("clicked_once");
//             $('#aboutForm').slideUp();

//         } else {

//             $this.addClass("clicked_once");
//             $('#aboutForm').slideDown();
//         };
//     });
// };

// function addEduForm() {

//     console.log('HELLO from edu');

//     $('#addEdu').on('click', function() {
//         var $this = $(this);

//         if($this.hasClass("clicked_once")) {

//             $this.removeClass("clicked_once");
//             $('#eduForm').slideUp();

//         } else {

//             $this.addClass("clicked_once");
//             $('#eduForm').slideDown();
//         };
//     });
// };

// function addSkillForm() {

//     $('#addSkill').on('click', function() {
//         var $this = $(this);

//         if($this.hasClass("clicked_once")) {

//             $this.removeClass("clicked_once");
//             $('#skillForm').slideUp();

//         } else {

//             $this.addClass("clicked_once");
//             $('#skillForm').slideDown();
//         };
//     });
// };

// function addProgProjForm() {

//     $('#addProgProj').on('click', function () {
//         var $this = $(this);

//         if($this.hasClass("clicked_once")) {

//             $this.removeClass("clicked_once");
//             $('#progProjForm').slideUp();

//         } else {

//             $this.addClass("clicked_once");
//             $('#progProjForm').slideDown();
//         };
//     });
// };

// function addWorkForm() {

//     $('#addWork').on('click', function() {
//         var $this = $(this);

//         if($this.hasClass("clicked_once")) {
            
//             $this.removeClass("clicked_once");
//             $('#workForm').slideUp();

//         } else {

//             $this.addClass("clicked_once");
//             $('#workForm').slideDown();
//         };
//     });
// };

// $(document).ready(function() {

//     $('#aboutForm').hide();
//     $('#eduForm').hide();
//     $('#skillForm').hide();
//     $('#progProjForm').hide();
//     $('#workForm').hide();

//     addAboutForm();
//     addEduForm();
//     addSkillForm();
//     addProgProjForm();
//     addWorkForm();

// });