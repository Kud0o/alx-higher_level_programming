#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head to sigle linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *current = *head, *new_current = *head;
	unsigned int count = 0, cycle = 0, i = 0, len = 0;

	if (head == NULL)
		return (0);
	if (*head == NULL)
		return (1);
	while (current)
	{
		count++;
		current = current->next;
	}
	current = *head;
	cycle = count * 2;
	len = cycle - 2;

	for (i = 0; i < cycle; i = i + 2)
	{
		if (current[i].n != new_current[len].n)
			return (0);
		len = len - 2;
	}
	return (1);
}
