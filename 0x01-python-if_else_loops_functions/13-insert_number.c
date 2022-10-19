#include "lists.h"

/**
 * insert_node - inserts node at given position
 * @head: head pointer
 * @number: new node data
 * Return: new node pointer
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *ptr_node = *head;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = number;

	if (*head == NULL || ptr_node->n >= number)
	{
		new_node->next = ptr_node;
		*head = new_node;
		return (*head);
	}
	while (ptr_node && ptr_node->next && ptr_node->next->n < number)
		ptr_node = ptr_node->next;
	new_node->next = ptr_node->next;
	ptr_node = new_node;
	return (ptr_node);
}
