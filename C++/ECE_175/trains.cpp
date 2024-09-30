#include<stdio.h>
#include<string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

typedef struct {
     int protect; 
     int value;
     char action[15];
} card;

void createFileDeck(card gameDeck[]);
void createRandomDeck(card gameDeck[]);
void shuffleDeck(card gameDeck[]);
void fillDeck(card gameDeck[]);
void printDeck(card hand[], int size);
void dealHands(card gameDeck[], card player1[], card player2[]);
void sortHand(card hand[], int size); 
void initalizeBoard(card board[]);
int boardIsEmpty(card board[]); 
void printTurn(int user, card player[], card board[]);
void drawCard(card gameDeck[], card player[], card gameBoard[], int *deckUsed);
void use_ability(card gameDeck[], card player[], card otherPlayer[], card gameBoard[], int deckUsed);
void swapCards(card player[], int value1, int value2);
void swapCardsIndex(card player[], int index1, int index2);
void swapAdjacent(card player[]);
void swapSkip1Card(card player[]);
void shift2Left(card player[]);
void shift2Right(card player[]);
void protect(card player[]);
void removePos(card player1[], card otherPlayer[], card board[], card gameDeck[], int *deckUsed, int pos);
int checkWin(card player[]);

int main(){
    int deckUsed = 0;
    card gameDeck[84];
    card gameBoard[8];
    card player1[7];
    card player2[7];

    printf("------------------------------------------------\n");
    printf("Welcome to trains!! Choose who is person 1 and 2\n");
    printf("------------------------------------------------\n");

    initalizeBoard(gameBoard);
    fillDeck(gameDeck);
    dealHands(gameDeck, player1, player2); 
    deckUsed += 14; 

    int coinflip = (rand() % 2) + 1;

    printf("Flipping coin...");
    sleep(1); 

    if (coinflip == 1){
        printf("\nPerson1 is player 1!\n\n");
    }
    else{
        printf("\nPerson2 is player 1!\n\n");
    }

    while (deckUsed <= 84){
        printf("\nPlayer 1's turn!\n");
        printTurn(1, player1, gameBoard);

        if(boardIsEmpty(gameBoard) == 1){
            printf("Board is empty! ");
            drawCard(gameDeck, player1, gameBoard, &deckUsed);
        }
        else{
            char choice;
            printf("Would you like to draw or use board (D/B)?");
            scanf(" %c", &choice);

            if (choice == 'D'){
                drawCard(gameDeck, player1, gameBoard, &deckUsed);
            }
            else if(choice == 'B'){
                use_ability(gameDeck, player1, player2, gameBoard, deckUsed);
            }
        }

        if(checkWin(player1) == 1){
            printf("\nPlayer 1 Wins!");
            return 0;
        }

        printf("\nPlayer 2's turn!\n");
        printTurn(2, player2, gameBoard);

        if(boardIsEmpty(gameBoard) == 1){
            printf("Board is empty! ");
            drawCard(gameDeck, player2, gameBoard, &deckUsed);
        }
        else{
            char choice;
            printf("Would you like to draw or use board (D/B)? ");
            scanf(" %c", &choice);

            if (choice == 'D'){
                drawCard(gameDeck, player2, gameBoard, &deckUsed);
            }
            else if(choice == 'B'){
                use_ability(gameDeck, player1, player2, gameBoard, deckUsed);
            }
        }
        if(checkWin(player2) == 1){
            printf("\nPlayer 2 Wins!");
            return 0;
        }
    }

    int player1Streak = 0;
    int player2Streak = 0; 
    int i = 0;
    while(player1[i+1].value > player1[i].value){
        player1Streak++;
    }
    i = 0;
    while(player2[i+1].value > player2[i].value){
        player1Streak++;
    }

    if (player1Streak > player2Streak){
        printf("\nCard out! Player 1 Wins!");
    }
    if (player1Streak < player2Streak){
        printf("\nCard out! Player 2 Wins!");
    }
    if (player1Streak == player2Streak){
        printf("\nCard out! It's a tie!");
    }

    return 0;
}

void createFileDeck(card gamedeck[]){
    char answer; 
    char filename[100];
    int value;
    char action[15];
    int index = 0;

    printf("Enter file name: ");
    scanf("%s", filename);
    FILE *inFile = fopen(filename, "r");

    while (fscanf(inFile, "%d %15s", &value, action) != EOF) {
        card currCard;
        currCard.value = value;
        strcpy(currCard.action, action);
        gamedeck[index] = currCard;
        index++;
    } 
}

void createRandomDeck(card gamedeck[]){
    int value;
    char action[15];
    int index = 0; 
    FILE *inFile = fopen("sampledeck.txt", "r");

    while (fscanf(inFile, "%d %15s", &value, action) != EOF) {
        card currCard;
        currCard.value = value;
        strcpy(currCard.action, action);
        gamedeck[index] = currCard;
        index++;
    }

    shuffleDeck(gamedeck);
}

void shuffleDeck(card deck[]) {
    int i, j;
    card temp;

    for (i = 83; i > 0; i--) {
        j = rand() % (i + 1); 
        // Generates random index between 0-1

        temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
        // Swaps elements
    }
}

void fillDeck(card gameDeck[]) {
    char answer;
    printf("Load a deck? (Y/N) ");
    scanf(" %c", &answer);
    srand(time(NULL));

    if (answer == 'Y'){
        createFileDeck(gameDeck);
    }
    else{
        createRandomDeck(gameDeck);
        printf("Shuffling cards...\n");
        sleep(1);
    }
}

void dealHands(card gameDeck[], card player1[], card player2[]) {
    int i;

    // Deals cards to player1
    for (int i = 0; i < 7; i++) {
        player1[i] = gameDeck[i];
    }
    // Deals cards to player2
    for (i = 0; i < 7; i++) {
        player2[i] = gameDeck[i + 7];
    }

    sortHand(player1, 7);
    sortHand(player2, 7);
}

void printDeck(card hand[], int size) {
    for (int i = 0; i < size; i++) {
        if(hand[i].value == -1){
            NULL;
        }
        else if(hand[i].protect == 1){
            printf("|%d,%s(P)|", hand[i].value, hand[i].action);
        }
        else{
            printf("|%d,%s|", hand[i].value, hand[i].action);
        }
    }
}

void sortHand(card hand[], int size) {
    // Bubble sort to sort the hand array by card value in descending order
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (hand[j].value < hand[j + 1].value) {
                // Swap cards
                card temp = hand[j];
                hand[j] = hand[j + 1];
                hand[j + 1] = temp;
            }
        }
    }
}

void initalizeBoard(card board[]){
    for(int i=0; i < 8; i ++){
        board[i].value = -1 ;
    }
}

int boardIsEmpty(card board[]){
    for(int i=0; i < 8; i++){
        if (board[i].value != -1){
            return 0;
        }
    }
    return 1; 

}

void printTurn(int user, card player[], card board[]){
    printf("--------------------------------------------------[Player %d's Hand]----------------------------------------------------\n", user);
    printf("|LOCOMOTIVE|");
    printDeck(player, 7);
    printf("\n-----------------------------------------------------------------------------------------------------------------------\n\n");

    printf("-------------------------------------------------------[Board]---------------------------------------------------------\n");
    printDeck(board, 8);
    printf("\n-----------------------------------------------------------------------------------------------------------------------\n\n");
}

void drawCard(card gameDeck[], card player[], card board[], int *deckUsed){
    int choice; 
    printf("You draw: |%d, %s|\n", gameDeck[*deckUsed].value, gameDeck[*deckUsed].action);
    printf("Which card would you like to replace (Enter value)? ");
    scanf("%d", &choice); 

    for(int i=0; i < 7; i++){
        if (player[i].value == choice) {
            // Copies discarded to first empty spot on board
            for(int j=0; j < 8; j++){
                if (board[j].value == -1){
                    board[j].value = player[i].value;
                    strcpy(board[j].action, player[i].action);
                    break;
                }
            }

            // Copies drawn card to hand
            player[i].value = gameDeck[*deckUsed].value;
            strcpy(player[i].action, gameDeck[*deckUsed].action); 
        }

    }

    (*deckUsed)++;
    // Checks board for matching pairs of abilities
    for(int i=0; i < 6; i++){
        if (strcmp(board[i].action,board[i+1].action) == 0){
            board[i].value = -1; 
            board[i+1].value = -1;
        }
    }
}

void use_ability(card gameDeck[], card player[], card otherPlayer[], card gameBoard[], int deckUsed){
    int choice; 
    printf("Which card on the board would you like to use (Enter value)? ");
    scanf("%d", &choice); 

    for(int i=0; i < 8; i++){
        if (gameBoard[i].value == choice){
            if (strcmp(gameBoard[i].action, "swapAdjacent") == 0){
                swapAdjacent(player);
            }
            if (strcmp(gameBoard[i].action, "swapSkip1Card") == 0){
                swapSkip1Card(player);
            }
            if (strcmp(gameBoard[i].action, "shift2Left") == 0){
                shift2Left(player);
            }
            if (strcmp(gameBoard[i].action, "shift2Right") == 0){
                shift2Right(player);
            }
            if (strcmp(gameBoard[i].action, "protect") == 0){
                protect(player);
            }
            if (strcmp(gameBoard[i].action, "removeLeft") == 0){
                removePos(player, otherPlayer, gameBoard, gameDeck, &deckUsed, 0);
            }
            if (strcmp(gameBoard[i].action, "removeRight") == 0){
                removePos(player, otherPlayer, gameBoard, gameDeck, &deckUsed, 6);
            }
            if (strcmp(gameBoard[i].action, "removeMiddle") == 0){
                removePos(player, otherPlayer, gameBoard, gameDeck, &deckUsed, 3);
            }
            gameBoard[i].value = -1;
        }
    }
}

void swapAdjacent(card player[]) {
    int choice1Val, choice2Val;

    printf("Which two adjacent cards in your hand would you like to swap (Enter values): ");
    scanf("%d %d", &choice1Val, &choice2Val);
    swapCards(player, choice1Val, choice2Val);
}

void swapSkip1Card(card player[]) {
    int choice1Val, choice2Val;

    printf("Which two cards with exactly one card between them would you like to swap (Enter values): ");
    scanf("%d %d", &choice1Val, &choice2Val);
    swapCards(player, choice1Val, choice2Val);
}

void swapCards(card player[], int value1, int value2) {
    int index1;
    int index2;
    for(int i=0; i < 7; i++){
        if (player[i].value == value1){
            index1 = i;
        }
        else if(player[i].value == value2){
            index2 = i;
        }
    }
    card temp = player[index1];
    player[index1] = player[index2];
    player[index2] = temp;

    if (player[index1].protect == 1){
        player[index1].protect = 0;
    }
    if (player[index2].protect == 1){
        player[index2].protect = 0;
    }  
}

void swapCardsIndex(card player[], int index1, int index2){
    card temp = player[index1];
    player[index1] = player[index2];
    player[index2] = temp;

    if (player[index1].protect == 1){
        player[index1].protect = 0;
    }
    if (player[index2].protect == 1){
        player[index2].protect = 0;
    }  
}

void shift2Left(card player[]){
    int choice;
    int choiceIndex;
    printf("Which card would you like to shift itself and the following 2 cards to the left (Enter value)? ");
    scanf("%d", &choice);
    for(int i=0; i < 7; i++){
        if (player[i].value == choice){
            choiceIndex = i;
        }
    }
    if (choiceIndex <= 4){
        swapCardsIndex(player, choiceIndex, choiceIndex+1);
        swapCardsIndex(player, choiceIndex+1, choiceIndex+2);
    }
    else{
        printf("Invalid use\n");
    }
}

void shift2Right(card player[]){
    int choice;
    int choiceIndex;
    printf("Which card would you like to shift itself and the previous 2 cards to the right (Enter value)? ");
    scanf("%d", &choice);
    for(int i=0; i < 7; i++){
        if (player[i].value == choice){
            choiceIndex = i;
        }
    }
    if (choiceIndex >= 2){
        swapCardsIndex(player, choiceIndex, choiceIndex-1);
        swapCardsIndex(player, choiceIndex-1, choiceIndex-2);
    }
    else{
        printf("Invalid use\n");
    }
}

void protect(card player[]){
    char choice; 
    printf("Which card would you like to protect (L/M/R)? ");
    scanf(" %c", &choice); 

    if (choice == 'L'){
        player[0].protect = 1; 
    }
    if (choice == 'M'){
        player[3].protect = 1; 
    }
    if (choice == 'R'){
        player[6].protect = 1; 
    }
}

void removePos(card player1[], card otherPlayer[], card board[], card gameDeck[], int *deckUsed, int pos){
    if (otherPlayer[pos].protect != 1){
        // Adds otherPlayer left card to board
        for(int i=0; i < 8; i++){
            if (board[i].value == -1){
                board[i].value = otherPlayer[pos].value;
                strcpy(board[i].action, otherPlayer[pos].action);
                break;
            }
        }
        
        // Replaces otherPlayer 1 left card with top of deck
        otherPlayer[pos].value = gameDeck[*deckUsed].value;
        strcpy(otherPlayer[pos].action, gameDeck[*deckUsed].action);
        (*deckUsed)++;
    }

    // If not protected
    if (player1[pos].protect != 1){
        // Adds player1 left card to board
        for(int i=0; i < 8; i++){
            if (board[i].value == -1){
                board[i].value = player1[pos].value;
                strcpy(board[i].action, player1[pos].action);
                break;
            }
        }
        
        // Replaces player 1 left card with top of deck
        player1[pos].value = gameDeck[*deckUsed].value;
        strcpy(player1[pos].action, gameDeck[*deckUsed].action);
        (*deckUsed)++;
    }

    // Checks board for matching pairs of abilities
    for(int i=0; i < 6; i++){
        if (strcmp(board[i].action,board[i+1].action) == 0){
            board[i].value = -1; 
            board[i+1].value = -1;
        }
    }
}

int checkWin(card player[]){
    for(int i=0; i < 6; i++){
        if (player[i+1].value < player[i].value){
            return 0;
        }   
    }
    return 1;
}