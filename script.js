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
console.log(getComputerChoice());

function getHumanhoice(){
    let humanChoice= prompt("rock,paper or scissor");
    return choice.toLowerCase();
}
console.log(getHumanhoice());