function performSearch() {
    const searchQuery = document.querySelector('.search').value;
    
    if (searchQuery) {
        window.location.href = `https://www.google.com/search?q=${encodeURIComponent(searchQuery)}&sourceid=chrome&ie=UTF-8`;
    } else {
        alert("Please enter a search term.");
    }

    document.querySelector('.search').value = '';
}

document.querySelector('.search-button').addEventListener('click', function() {
    performSearch();
});

document.querySelector('.search').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        performSearch();
    }
});

document.querySelector('.lucky').addEventListener('mouseover', function() {
    const button = this;
    const choices = [
        "I'm Feeling Curious",
        "I'm Feeling Adventurous",
        "I'm Feeling Playful",
        "I'm Feeling Artistic",
        "I'm Feeling Hungry",
        "I'm Feeling Generous",
        "I'm Feeling Doodly",
        "I'm Feeling Stellar",
        "I'm Feeling Trendy"
    ];

    function shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }

        return array;
    }

    button.classList.add('active');

    let index = 0;
    const shuffleChoices = shuffleArray(choices);
    const animationTime = 500;
    const intervalTime = animationTime / shuffleChoices.length; 

    function updateText() {
        button.textContent = shuffleChoices[index];
        index = (index + 1) % shuffleChoices.length;
    }

    const interval = setInterval(updateText, intervalTime);
    button.intervalId = interval;

    setTimeout(() => {
        clearInterval(interval);
        button.classList.remove('active');
    }, animationTime);
});

document.querySelector('.lucky').addEventListener('mouseout', function() {
    const button = this;
    clearInterval(button.intervalId);
    button.textContent = "I'm Feeling Lucky";
});
