// Zmienna do przechowywania wiadomości
const chatContainer = document.querySelector('.chat-container');
const messageInput = document.getElementById('messageInput');
const sendMessageBtn = document.getElementById('sendMessageBtn');

// Funkcja do dodania wiadomości do okna czatu
function addMessage(content, type) {
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message', type);

    const messageText = document.createElement('div');
    messageText.classList.add('text');
    messageText.textContent = content;

    const messageTime = document.createElement('span');
    messageTime.classList.add('time');
    const currentTime = new Date();
    messageTime.textContent = `${currentTime.getHours()}:${currentTime.getMinutes()}`;

    messageContainer.appendChild(messageText);
    messageContainer.appendChild(messageTime);
    chatContainer.appendChild(messageContainer);

    // Przewiń czat na dół po dodaniu nowej wiadomości
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Obsługa kliknięcia przycisku wysyłania wiadomości
sendMessageBtn.addEventListener('click', () => {
    const messageContent = messageInput.value.trim();
    if (messageContent !== "") {
        addMessage(messageContent, 'sent');
        messageInput.value = ''; // Wyczyść pole tekstowe
    }
});

// Obsługa Entera (wysyłanie wiadomości po naciśnięciu Enter)
messageInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        const messageContent = messageInput.value.trim();
        if (messageContent !== "") {
            addMessage(messageContent, 'sent');
            messageInput.value = ''; // Wyczyść pole tekstowe
        }
    }
});

// Przykładowe wiadomości (do testowania)
setTimeout(() => {
    addMessage("Cześć! Jak się masz?", 'received');
}, 1000);

setTimeout(() => {
    addMessage("Wszystko w porządku, dziękuję!", 'received');
}, 3000);