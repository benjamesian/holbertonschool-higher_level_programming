#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p = *head;

	if (!head)
		return (NULL);

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!p)
		*head = new;
	else
		while (p)
		{
			if (p->n < number && (!p->next || p->next->n >= number))
			{
				new->next = p->next;
				p->next = new;
			}
			p = p->next;
		}

	return (new);
}
