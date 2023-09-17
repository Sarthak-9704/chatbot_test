function sendMessage() {
    var message = document.getElementById('user-input').value;
    // if (message.trim() === '') return;

    var messagesContainer = document.getElementById('chat-messages');
    var userMessageElement = document.createElement('div');
    userMessageElement.classList.add('message', 'user-message');
    userMessageElement.textContent = message;
    messagesContainer.appendChild(userMessageElement);

    // Clear input field after sending message
    document.getElementById('user-input').value = '';

    // Simulate bot response (replace this with actual backend integration)
    setTimeout(function() {
        var botMessageElement = document.createElement('div');
        botMessageElement.classList.add('message', 'bot-message');
        botMessageElement.textContent = 'Bot response goes here.';
        messagesContainer.appendChild(botMessageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight; // Scroll to the bottom
    }, 500);
}
