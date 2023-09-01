#include "lists.h"
#include <stddef.h>
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted listint_t  list.
 * @head: Pointer to the pointer to the first node of the list.
 * @number: Number to insert into the sorted list.
 *
 * Return: The address of the new node,
 *         or NULL if the function fails.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		return (NULL);
	}

	new->n = number;

	temp = *head;

	if (temp == NULL || temp->n >= number)
	{
		new->next = temp;
		*head = new;
		return (new);
	}

	while (temp && temp->next && temp->next->n < number)
	{
		temp = temp->next;
	}

	new->next = temp->next;
	temp->next = new;

	return (new);
}
