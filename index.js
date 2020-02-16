
Survey
    .StylesManager
    .applyTheme("modern");

var json = {
    showQuestionNumbers: "off",
    pages: [
        {
            name: "Registration",
            title: "Registration",
            questions: [
                {
                    type: "text",
                    name: "fistName",
                    title: "What is your first name?",
                    isRequired: true
                }, {
                    type: "text",
                    name: "lastName",
                    title: "What is your last name?",
                    isRequired: true
                }, {
                    type: "text",
                    name: "personalEmail",
                    inputType: "email",
                    title: "What is your personal email address?",
                    isRequired: true,
                    validators: [
                        {
                            type: "email"
                        }
                    ]
                }, {
                    type: "text",
                    name: "school",
                    title: "Which school are you currently attending?",
                }, {
                    type: "multipletext",
                    name: "login",
                    title: "Login",
                    isRequired: true,
                    items: [
                        {
                            name: "username",
                            title: "Username: "
                        }, {
                            name: "password",
                            title: "Password: "
                        }
                    ]
                }, {
                    type: "file",
                    title: "Please upload your photo",
                    name: "image",
                    storeDataAsText: false,
                    showPreview: true,
                    imageWidth: 150,
                    maxSize: 102400
                }
            ]
        }, {
            name: "Courses",
            title: "Courses",
            questions: [
                {
                    type: "dropdown",
                    name: "car",
                    title: "What is your intended area of study?",
                    isRequired: true,
                    colCount: 0,
                    choices: [
                        "Agricultural Sciences",
                        "Anthropology",
                        "Architecture and Environmental Design",
                        "Art and Design",
                        "Biology",
                        "Business and Economics",
                        "Chemistry",
                        "Communications",
                        "Computer Science",
                        "Culture and Society",
                        "Engineering",
                        "Environmental Studies and Sciences",
                        "Health and Physical Education",
                        "History",
                        "Humanities",
                        "Languages and Literature",
                        "Mathematics",
                        "Media/Film and Television",
                        "Performing Arts",
                        "Philosophy",
                        "Physical Sciences",
                        "Physics", 
                        "Political Science",
                        "Phychology",
                        "Sociology and Social Sciences",
                        "Teacher Education",
                        "Undeclared"
                    ]
                }, {
                    type: "radiogroup",
                    name: "minUnit",
                    title: "Have you taken at least 60 semester (90 quarter) units of transferable credit?",
                    isRequired: true,
                    choices: [
                        "Yes", "No"
                    ]
                }, {
                    type: "radiogroup",
                    name: "note1",
                    visibleIf: "{minUnit}='No'",
                    title: "To transfer, you need to complete at least 60 semester (90 quarter) units of transferable credit",
                    isRequired: true,
                    choices: ["ok"]
                }, {
                    type: "radiogroup",
                    name: "maxUnit",
                    title: "Have you taken more than 70 semester (105 quarter) units of transferable credit?",
                    isRequired: true,
                    choices: [
                        "Yes", "No"
                    ],
                    colCount: 0
                }, {
                    type: "radiogroup",
                    name: "note2",
                    title: "You cannot transfer no more than 70 semester (105 quarter) units of transferable credit",
                    visibleIf: "{maxUnit}='Yes'",
                    isRequired: true,
                    choices: ["ok"]
                },{
                    type: "multipleText",
                    name: "passFail",
                    title: "How many of the completed units were pass/fail?",
                    colCount: 2,
                    items: [
                        {
                            name: "quarter",
                            title: "Semester Units: "
                        },{
                            name: "semester",
                            title: "Semester Units: "
                        }
                    ]
                }, {
                    type: "radiogroup",
                    name: "q1",
                    title: "Have you completed at least two transferable courses in English composition?",
                    choices: [
                        "Yes", "No"
                    ]
                },{
                    type: "radiogroup",
                    name: "q2",
                    title: "Have you completed at least two transferable courses in English composition?",
                    choices: [
                        "Yes", "No"
                    ]
                },{
                    type: "radiogroup",
                    name: "q3",
                    title: "What transferable college courses have you taken from the following subject areas?",
                    choices: [
                        "arts and humanities (UC-H)", "social and behavioral sciences (UC-B)", "physical and biological sciences (UC-S)"
                    ]
                }
            ]
        }, {
            name: "Resident",
            title: "Resident",
            questions: [
                {
                    type: "radiogroup",
                    name: "q4",
                    title: "Are you a California resident?",
                    choices: [
                        "Yes", "No"
                    ]
                }, {
                    type: "radiogroup",
                    name: "q4a",
                    title: "Do you have 2.40 GPA or higher?",
                    visibleIf: "{q4}='Yes'",
                    choices: [
                        "Yes", "No"
                    ]
                }, {
                    type: "radiogroup",
                    name: "note1",
                    visibleIf: "{q4a}='No'",
                    title: "To transfer as a California resident, you need at least 2.40 GPA.",
                    isRequired: true,
                    choices: ["ok"]
                }, {
                    type: "radiogroup",
                    name: "q4b",
                    title: "Do you have 2.80 GPA or higher?",
                    visibleIf: "{q4}='No'",
                    choices: [
                        "Yes", "No"
                    ]
                }, {
                    type: "radiogroup",
                    name: "note1",
                    visibleIf: "{q4b}='No'",
                    title: "To transfer as a non-California resident, you need at least 2.80 GPA.",
                    isRequired: true,
                    choices: ["ok"]
                }, {
                    type: "radiogroup",
                    name: "q4b",
                    title: "Would you be open to relocating?",
                    choices: [
                        "Yes", "No"
                    ]
                }, {
                    type: "text",
                    name: "q4b",
                    title: "What is your zip code?",
                }
            ]
        }
    ]
};

window.survey = new Survey.Model(json);

survey
    .onComplete
    .add(function (result) {
        document
            .querySelector('#surveyResult')
            .textContent = "Result JSON:\n" + JSON.stringify(result.data, null, 3);
    });

$("#surveyElement").Survey({model: survey});

function animate(animitionType, duration) {
    if (!duration) 
        duration = 1000;
    var element = document.getElementById("surveyElement");
    $(element).velocity(animitionType, {duration: duration});
}

var doAnimantion = true;
survey
    .onCurrentPageChanging
    .add(function (sender, options) {
        if (!doAnimantion) 
            return;
        options.allowChanging = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.currentPage = options.newCurrentPage;
            doAnimantion = true;
        }, 500);
        animate("slideUp", 500);
    });
survey
    .onCurrentPageChanged
    .add(function (sender) {
        animate("slideDown", 500);
    });
survey
    .onCompleting
    .add(function (sender, options) {
        if (!doAnimantion) 
            return;
        options.allowComplete = false;
        setTimeout(function () {
            doAnimantion = false;
            sender.doComplete();
            doAnimantion = true;
        }, 500);
        animate("slideUp", 500);
        window.location.replace("landing.html");
    });
animate("slideDown", 1000);
survey.showProgressBar = 'bottom';