/* global document,window,localStorage */

/* Code for image changer */

var dogImage = document.querySelector('img');

dogImage.onclick = function () {
    'use strict';
    var  myImages = dogImage.getAttribute('src');
    if (myImages === 'images/dog.jpg') {
        dogImage.setAttribute('src', 'images/puppy.jpg');
    } else {
        dogImage.setAttribute('src', 'images/dog.jpg');
    }
};

// Personalized welcome messege code

var nameButton = document.querySelector('button');
var myHeading = document.querySelector('h1');

function setUserName() {
    'use strict';
    var myName = window.prompt('Please enter your name.');
    localStorage.setItem('name', myName);
    myHeading.textContent = 'Have  a nice day, ' + myName;
}
if (!localStorage.getItem('name')) {
    setUserName();
} else {
    var storedName = localStorage.getItem('name');
    myHeading.textContent = 'Have a nice day, ' + storedName;
}
nameButton.onclick = function () {
    'use strict';
    setUserName();
};