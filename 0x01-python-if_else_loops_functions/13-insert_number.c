#include "lists.h"
include ‘<stdlib.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to pointer to the head of the list
 * @number: number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current_node, *prev_node;

    /* Create a new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);
    new_node->n = number;
    new_node->next = NULL;

    /* If list is empty or number is less than head node */
    if (*head == NULL || (*head)->n > number)
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Traverse the list and find the correct position for the new node */
    prev_node = NULL;
    current_node = *head;
    while (current_node != NULL && current_node->n < number)
    {
        prev_node = current_node;
        current_node = current_node->next;
    }

    /* Insert the new node into the correct position */
    new_node->next = current_node;
    prev_node->next = new_node;

    return (new_node);
}
