function getComputerChoice()
{
    let computerChoice= Math.floor(Math.random()*3)
    if(computerChoice===0)
    {
        return "rock";
    }
    else if(computerChoice===1)
    {
        return "paper";
    }
    else
    {
        return "scissors";
    }
}

function getHumanhoice(){
    let humanChoice= prompt("rock,paper or scissor");
    return humanChoice.toLowerCase();
}

let humanScore = 0;
let computerScore = 0;

function playRound(humanChoice, computerChoice) {
  humanChoice = humanChoice.toLowerCase();

  if (humanChoice === computerChoice) {
    console.log(`It's a tie! You both chose ${humanChoice}`);
  } else if (
    (humanChoice === "rock" && computerChoice === "scissors") ||
    (humanChoice === "paper" && computerChoice === "rock") ||
    (humanChoice === "scissors" && computerChoice === "paper")
  ) {
    console.log(`You win this round! ${humanChoice} beats ${computerChoice}`);
    humanScore++;
  } else {
    console.log(`You lose this round! ${computerChoice} beats ${humanChoice}`);
    computerScore++;
  }
  console.log(`Current Score -> You: ${humanScore}, Computer: ${computerScore}`);
}

function playGame() {
    humanScore = 0;
    computerScore = 0;
  
    for (let i = 0; i < 5; i++) {
      const humanSelection = getHumanhoice();
      const computerSelection = getComputerChoice();
      playRound(humanSelection, computerSelection);
    }
  
    if (humanScore > computerScore) {
      console.log(" Congratulations, you win the game!");
    } else if (computerScore > humanScore) {
      console.log(" Sorry, the computer wins this time.");
    } else {
      console.log(" It's a tie game! Well played.");
    }
  }
  
  // Start the game
  playGame();