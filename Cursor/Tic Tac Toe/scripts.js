let board = Array(9).fill(null); // Represents the 3x3 board
let currentPlayer = 'X'; // Start with player 'X'
let gameActive = true; // To track if the game is still ongoing
document.querySelectorAll('.square').forEach((square, index) => {
    square.addEventListener('click', () => {
        if (gameActive && !board[index]) {
            board[index] = currentPlayer;
            square.textContent = currentPlayer;
            square.setAttribute('data-player', currentPlayer);
            if (checkWinner()) {
                showModal(currentPlayer + ' Wins!', false);
                gameActive = false;
            } else if (board.every(cell => cell)) {
                showModal("It's a Draw!", true);
                gameActive = false;
            } else {
                currentPlayer = currentPlayer === 'X' ? 'O' : 'X';
            }
        }
    });
});

function checkWinner() {
    const winningCombinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // Columns
        [0, 4, 8], [2, 4, 6]            // Diagonals
    ];

    for (let combination of winningCombinations) {
        const [a, b, c] = combination;
        if (board[a] && board[a] === board[b] && board[a] === board[c]) {
            // Add winner class to winning squares
            const squares = document.querySelectorAll('.square');
            squares[a].classList.add('winner');
            squares[b].classList.add('winner');
            squares[c].classList.add('winner');
            return true;
        }
    }
    return false;
}

function resetGame() {
    board.fill(null);
    currentPlayer = 'X';
    gameActive = true;
    document.querySelectorAll('.square').forEach(square => {
        square.textContent = '';
        square.removeAttribute('data-player');
        square.classList.remove('winner'); // Remove winner class
    });
    closeModal();
}

document.getElementById('resetButton').addEventListener('click', resetGame);

function showModal(message, isDraw) {
    const modal = document.getElementById('winnerModal');
    const winnerMessage = document.getElementById('winnerMessage');
    winnerMessage.textContent = message;

    if (isDraw) {
        modal.classList.add('draw');
    } else {
        modal.classList.remove('draw');
    }

    modal.style.display = 'block';
}

function closeModal() {
    const modal = document.getElementById('winnerModal');
    modal.style.display = 'none';
    modal.classList.remove('draw');
}

document.querySelector('.close-button').addEventListener('click', closeModal);

window.addEventListener('click', (event) => {
    const modal = document.getElementById('winnerModal');
    if (event.target === modal) {
        closeModal();
    }
});

