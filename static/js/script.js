document.addEventListener('DOMContentLoaded', function() {
    const userTypes = ['Student', 'Faculty', 'Parent'];

    function setupProfilePicPreview(userType) {
        const input = document.getElementById(`profilePicInput${userType}`);
        const preview = document.getElementById(`imagePreview${userType}`);

        if (input && preview) {
            input.addEventListener('change', function(e) {
                const file = e.target.files[0];
                
                if (file) {
                    const reader = new FileReader();
                    reader.onload = function(e) {
                        preview.src = e.target.result;
                        preview.style.display = 'block';
                    }
                    reader.readAsDataURL(file);
                }
            });
        }
    }

    userTypes.forEach(userType => setupProfilePicPreview(userType));
});

function scrollToBottom() {
    const chatContainer = document.querySelector('.chat-container');
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Call this function after the page loads
document.addEventListener('DOMContentLoaded', scrollToBottom);