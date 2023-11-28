#include "lists.h"

/**
 * insert_node - this function inserts a number in a sorted linked list
 * @head: the head of the linked list
 * @number: the number.
 * Return: return the address of the new node
 *	or NULL in case of failure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *previous = NULL;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;
	if (current == NULL)
		return (*head = new);

	while (current)
	{
		if (number < current->n)
		{
			if (current == *head)
			{
				*head = new;
				new->next = current;
				return (new);
			}
			new->next = current;
			previous->next = new;
			return (new);
		}
		if (current->next == NULL)
		{
			current->next = new;
			return (new);
		}
		previous = current;
		current = current->next;
	}

	return (NULL);
}
