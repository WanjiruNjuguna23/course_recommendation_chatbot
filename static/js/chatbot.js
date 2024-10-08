// chatbot.js

// collecting user interests
document.addEventListener('DOMContentLoaded', function () {
    const chatBox = document.getElementById('chat-box');
    const userInput = document.getElementById('user-input');
    const submitButton = document.getElementById('submit-btn');

    const interests = ['Math', 'Science', 'Art', 'History'];  //User interests
    let currentQuestion = 0;
    let selectedInterests = [];

    // Function to display a question in the chatbot
    function askNextQuestion() {
        if (currentQuestion < interests.length) {
            chatBox.innerHTML += `<p>Do you like ${interests[currentQuestion]}? (yes/no)</p>`;
        } else {
            submitInterests();
        }
    }

    // Event listener for user input submission
    submitButton.addEventListner('click', function () {
        const userResponse= userInput.value.toLowerCase();
        if (userResponse === 'yes') {
            selectedInterests.push(interests[currentQuestion]);
        }
        currentQuestion++;
        userInput.value = '';  // Clear input field
        askNextQuestion();  // next question
    });

    // Function to submit selected interests
    function submitInterests() {
        chatBox.innerHTML += `<p>Recommended courses based on your interests: ${selectedInterests.join(', ')}</p>`;
    }

    askNextQuestion();  // Start chatbot interaction
});
