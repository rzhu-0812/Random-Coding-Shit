const wordleContainer = document.getElementById("wordle");

const rows = 6;
const columns = 5;

let currRow = 0;
let currCell = 0;
let wordList = [];
let targetWord = "";
let userGuess = "";

const grid = [];

wordleContainer.classList.add("grid", "grid-rows-6", "gap-2");

async function loadWords() {
    const response = await fetch("words.json");
    wordList = await response.json();
    targetWord = wordList[Math.floor(Math.random() * wordList.length)].toUpperCase();
}

function createGrid() {
    for (let i = 0; i < rows; i++) {
        const row = [];
        const rowDiv = document.createElement("div");
        rowDiv.classList.add("grid", "grid-cols-5", "gap-2");
        rowDiv.id = `row-${i}`;
        
        for (let j = 0; j < columns; j++) {
            const cell = document.createElement("div");
            cell.classList.add(
                "border", "border-gray-400", "w-16", "h-16",
                "flex", "items-center", "justify-center",
                "text-2xl", "font-bold", "bg-white",
                "transition-colors", "duration-300"
            );
            cell.id = `row-${i}-col-${j}`;
            rowDiv.appendChild(cell);
            row.push(cell);
        }
        
        grid.push(row);
        wordleContainer.appendChild(rowDiv);
    }
}

async function handleKeyPress(event) {
    const key = event.key.toUpperCase();
    
    if (/^[A-Z]$/.test(key) && currCell < columns) {
        grid[currRow][currCell].textContent = key;
        userGuess += key;
        currCell++;
    } else if (key === "BACKSPACE" && currCell > 0) {
        currCell--;
        grid[currRow][currCell].textContent = "";
        userGuess = userGuess.slice(0, -1);
    } else if (key === "ENTER" && currCell === columns) {
        if (currRow < rows) {
            document.removeEventListener("keydown", handleKeyPress);
            
            await checkWords();
            
            document.addEventListener("keydown", handleKeyPress);
            
            if (userGuess === targetWord) {
                setTimeout(() => alert("Congratulations! You won!"), 500);
                document.removeEventListener("keydown", handleKeyPress);
                return;
            }
            
            if (currRow === rows - 1) {
                setTimeout(() => alert(`Game Over! The word was ${targetWord}`), 500);
                document.removeEventListener("keydown", handleKeyPress);
                return;
            }
            
            currRow++;
            currCell = 0;
            userGuess = "";
        }
    }
}

function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function checkWords() {
    const currRowDiv = document.getElementById(`row-${currRow}`);
    const targetWordChars = targetWord.split("");
    const userGuessChars = userGuess.split("");
    const letterStates = new Array(5).fill('unused');
    const letterCounts = {};

    for (const char of targetWordChars) {
        letterCounts[char] = (letterCounts[char] || 0) + 1;
    }
    
    for (let i = 0; i < 5; i++) {
        if (targetWordChars[i] === userGuessChars[i]) {
            letterStates[i] = 'green';
            letterCounts[userGuessChars[i]]--;
        }
    }
    
    for (let i = 0; i < 5; i++) {
        const currColDiv = currRowDiv.querySelector(`#row-${currRow}-col-${i}`);
        
        currColDiv.classList.add("transform", "transition-transform", "duration-300");
        currColDiv.style.transform = "rotateX(90deg)";
        
        await delay(300);
        
        currColDiv.classList.remove("bg-white");
        
        if (letterStates[i] === 'green') {
            currColDiv.classList.add("bg-green-500", "text-white");
        } else if (letterCounts[userGuessChars[i]] > 0 && targetWordChars.includes(userGuessChars[i])) {
            currColDiv.classList.add("bg-yellow-300");
            letterCounts[userGuessChars[i]]--;
        } else {
            currColDiv.classList.add("bg-gray-400", "text-white");
        }
        
        currColDiv.style.transform = "rotateX(0deg)";
    }
    
    await delay(100 * 5);
}

loadWords();
createGrid();
document.addEventListener("keydown", handleKeyPress);