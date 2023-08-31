#include "lists.h"

/**
 * check_cycle - Checks for loop a listint_t list.
 * @list: Pointer to the first node in the list.
 *
 * Return: 0 if there is no cycle or
 *         1 if there is a cycle.
 */

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return (0);
	}

	slow = list;
	fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			return (1);
		}

	}
	return (0);
}
