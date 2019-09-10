#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *p;

	if (!head)
		return (NULL);

	p = *head;

	new = malloc(sizeof(*new));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (!p)
		*head = new;
	else if (p->n >= number)
	{
		*head = new;
		new->next = p;
	}
	else
	{
		while (p && p->next)
		{
			if (p->n < number && p->next->n >= number)
			{
				new->next = p->next;
				p->next = new;
				break;
			}
			p = p->next;
		}
		if (!p->next)
			p->next = new;
	}

	return (new);
}
