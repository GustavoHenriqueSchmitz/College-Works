#include <stdio.h>
#include <stdlib.h>

typedef struct Card {
    int number;
    char priority;
    struct Card *next;
} Card;

static Card *firstCardInQueue = NULL;
static int nextCommonNumber = 1;
static int nextPriorityNumber = 301;

void insertWithoutPriority(Card *newCard) {
    Card *current = firstCardInQueue;

    while (current->next != NULL) {
        current = current->next;
    }

    current->next = newCard;
}

void insertWithPriority(Card *newCard) {
    Card *previous = NULL;
    Card *current = firstCardInQueue;

    while (current != NULL && current->priority == 'P') {
        previous = current;
        current = current->next;
    }

    if (previous == NULL) {
        newCard->next = firstCardInQueue;
        firstCardInQueue = newCard;
    } else {
        newCard->next = current;
        previous->next = newCard;
    }
}

void insert(void) {
    Card *newCard;
    char priority;
    int flushedChar;

    printf("\nDigite a prioridade do cliente (P - prioritario / C - comum): ");
    if (scanf(" %c", &priority) != 1) {
        printf("Entrada encerrada.\n");
        return;
    }

    while ((flushedChar = getchar()) != '\n' && flushedChar != EOF);

    if (priority == 'p') priority = 'P';
    if (priority == 'c') priority = 'C';

    if (priority != 'P' && priority != 'C') {
        printf("Prioridade invalida! Use apenas P ou C.\n");
        return;
    }

    newCard = (Card *) malloc(sizeof(Card));
    if (newCard == NULL) {
        printf("Erro: memoria insuficiente.\n");
        return;
    }

    newCard->priority = priority;
    newCard->next = NULL;

    if (priority == 'C') {
        newCard->number = nextCommonNumber;
        nextCommonNumber++;
    } else {
        newCard->number = nextPriorityNumber;
        nextPriorityNumber++;
    }

    if (firstCardInQueue == NULL) {
        firstCardInQueue = newCard;
    } else if (newCard->priority == 'C') {
        insertWithoutPriority(newCard);
    } else {
        insertWithPriority(newCard);
    }

    printf("Cliente adicionado a fila com o cartao %c%d.\n",
           newCard->priority, newCard->number);
}

void printClientQueue(void) {
    Card *current = firstCardInQueue;
    int position = 1;

    printf("\n----- FILA DE CLIENTES -----\n");

    if (current == NULL) {
        printf("A fila esta vazia.\n");
        return;
    }

    while (current != NULL) {
        printf("%do lugar -> Cartao: %c%d\n",
               position, current->priority, current->number);
        current = current->next;
        position++;
    }
    printf("----------------------------\n");
}

void serveClient(void) {
    Card *served;

    if (firstCardInQueue == NULL) {
        printf("\nNao ha clientes na fila para serem atendidos.\n");
        return;
    }

    served = firstCardInQueue;
    firstCardInQueue = firstCardInQueue->next;

    printf("\nCliente do cartao %c%d, dirija-se ao caixa para atendimento!\n",
           served->priority, served->number);

    free(served);
}

void freeQueue(void) {
    Card *current = firstCardInQueue;
    Card *next;

    while (current != NULL) {
        next = current->next;
        free(current);
        current = next;
    }
    firstCardInQueue = NULL;
}

int main(void) {
    int option;
    int flushedChar;

    do {
        printf("\n===== BANCO - SISTEMA DE SENHAS =====\n");
        printf("1 - Adicionar cliente a fila\n");
        printf("2 - Mostrar clientes na fila\n");
        printf("3 - Chamar cliente\n");
        printf("4 - Sair\n");
        printf("Escolha uma opcao: ");

        if (scanf("%d", &option) != 1) {
            while ((flushedChar = getchar()) != '\n' && flushedChar != EOF);

            if (flushedChar == EOF) {
                option = 4;
            } else {
                option = 0;
            }
        }

        switch (option) {
            case 1:
                insert();
                break;
            case 2:
                printClientQueue();
                break;
            case 3:
                serveClient();
                break;
            case 4:
                printf("\nSistema encerrado. Ate logo!\n");
                break;
            default:
                printf("\nOpcao invalida! Escolha uma opcao entre 1 e 4.\n");
                break;
        }
    } while (option != 4);

    freeQueue();
    return 0;
}
