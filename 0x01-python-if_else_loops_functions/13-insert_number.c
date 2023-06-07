#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/** 
 * insert_node: a function in C that inserts a number into a
 * sorted singly linked list.
 * @head: head of list
 * @number: int
*/

listint_t *insert_node(listint_t **head, int number)
{
  listint_t *new_node;
  listint_t *current;
  
  current = *head;

  new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
      return (NULL);

  new_node->n = number;
  new_node->next = NULL;

  if (*head == NULL)
        *head = new_node;
  else if (number < (*head)->n)
  {
    new_node->next = *head;
    *head = new_node;
  }
  else
  {
    while (current->next != NULL && current->next->n < number)
      current = current->next;
    new_node->next = current->next;
    current->next = new_node;
  }
  return (new_node);
}
