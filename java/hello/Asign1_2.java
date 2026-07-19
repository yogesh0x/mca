public class Asign1_2 {
    public static void main(String[] args) {
       
        int winningScore = 50;

        int player1Score = 0;
        int player2Score = 0;
 
        int currentPlayer = 1;
               
        while (player1Score < iwinnngScore && player2Score < winningScore) {
            
            int roll = (int) (Math.random() * 6) + 1;

            
            if (currentPlayer == 1) {
                player1Score += roll;
            } else {
                player2Score += roll;
            }

            
            System.out.println("Player " + currentPlayer + " rolled a " + roll + ". Their score is now " + (currentPlayer == 1 ? player1Score : player2Score));

          
            currentPlayer = (currentPlayer == 1) ? 2 : 1;
        }

        
        if (player1Score >= winningScore) {
            System.out.println("Player 1 wins with a score of " + player1Score);
        } else {
            System.out.println("Player 2 wins with a score of " + player2Score);
        }
    }
}