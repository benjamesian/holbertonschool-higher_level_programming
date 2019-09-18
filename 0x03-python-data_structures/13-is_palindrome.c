#include "lists.h"
#include <stdlib.h>

int is_palindrome(listint_t **head)
{
	size_t len, i;
	listint_t *p1, *p2;

	if (!head || !*head)
		return (1);

	for (len = 0, p1 = *head; p1; p1 = p1->next, len++)
		;
	if (len < 2)
		return (1);

	len = len / 2;
	while (len--)
		p2 = p2->next;
	for(i = len; len--; i++)
		if (arr[len] != arr[i])
		{
			free(arr);
			return (0);
		}

	free(arr);
	return (1);
}
