#include "lists.h"
/**
 * *insert_node - function in C that inserts a number into a sorted singly linked list.
 * @head: is
 * @number: is
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new , *aux1, *aux2;
	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	aux1 = *head;
	if (!aux1 || aux1->n >= number)
	{
		new->next = aux1, *head = new;
		return (new);
	}
	aux2 = aux1->next;
	while (aux1 && aux2 && (aux2->n < number))
		aux1 = aux1->next, aux2 = aux1->next;
	aux1->next = new, new->next = aux2;
	return (new);
}
