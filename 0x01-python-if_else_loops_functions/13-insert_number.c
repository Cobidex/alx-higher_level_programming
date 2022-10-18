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
	int num = 0;

	new_node = malloc(sizeof(listint_t));

	new_node->n = number;

	while (num < 5)
	{
		num++;
		ptr_node = ptr_node->next;
	}
	new_node->next = ptr_node;
	ptr_node = new_node;

	return (ptr_node);
}
