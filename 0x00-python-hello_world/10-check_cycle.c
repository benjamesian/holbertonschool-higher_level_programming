#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *t = list, *h = list;

	while (h && h->next)
	{
		h = h->next->next;
		t = t->next;
		if (h == t)
			return (1);
	}

	return (0);
}
