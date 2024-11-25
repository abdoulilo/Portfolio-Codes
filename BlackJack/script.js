// Blackjack Game
const playerScoreElement = document.getElementById("player-score");
const dealerScoreElement = document.getElementById("dealer-score");
const playerCardsElement = document.getElementById("player-cards");
const dealerCardsElement = document.getElementById("dealer-cards");
const messageElement = document.getElementById("message");

const hitButton = document.getElementById("hit");
const standButton = document.getElementById("stand");
const restartButton = document.getElementById("restart");

let playerCards = [];
let dealerCards = [];
let playerScore = 0;
let dealerScore = 0;
let gameOver = false;

// Utility functions
const getRandomCard = () => Math.floor(Math.random() * 11) + 1;

const updateScores = () => {
    playerScore = playerCards.reduce((sum, card) => sum + card, 0);
    dealerScore = dealerCards.reduce((sum, card) => sum + card, 0);
    playerScoreElement.textContent = playerScore;
    dealerScoreElement.textContent = dealerScore;
};

const renderCards = () => {
    playerCardsElement.innerHTML = playerCards.map(card => `<div class="card">${card}</div>`).join("");
    dealerCardsElement.innerHTML = dealerCards.map(card => `<div class="card">${card}</div>`).join("");
};

const checkGameOver = () => {
    if (playerScore > 21) {
        messageElement.textContent = "You busted! Dealer wins.";
        gameOver = true;
    } else if (dealerScore > 21) {
        messageElement.textContent = "Dealer busted! You win!";
        gameOver = true;
    }
};

// Player actions
const playerHit = () => {
    if (!gameOver) {
        playerCards.push(getRandomCard());
        updateScores();
        renderCards();
        checkGameOver();
    }
};

const dealerTurn = () => {
    while (dealerScore < 17 && !gameOver) {
        dealerCards.push(getRandomCard());
        updateScores();
        renderCards();
    }
    if (!gameOver) {
        if (dealerScore > playerScore) {
            messageElement.textContent = "Dealer wins!";
        } else if (dealerScore < playerScore) {
            messageElement.textContent = "You win!";
        } else {
            messageElement.textContent = "It's a tie!";
        }
        gameOver = true;
    }
};

const playerStand = () => {
    if (!gameOver) {
        dealerTurn();
    }
};

const restartGame = () => {
    playerCards = [getRandomCard(), getRandomCard()];
    dealerCards = [getRandomCard()];
    gameOver = false;
    messageElement.textContent = "";
    updateScores();
    renderCards();
};

// Event listeners
hitButton.addEventListener("click", playerHit);
standButton.addEventListener("click", playerStand);
restartButton.addEventListener("click", restartGame);

// Initialize the game
restartGame();
