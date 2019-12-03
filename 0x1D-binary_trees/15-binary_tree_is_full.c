#include "binary_trees.h"

int node_full(const binary_tree_t *tree)
{
	return ((tree->left && tree->right) ||
		(!tree->left && !tree->right));
}
#include <stdio.h>
int _binary_tree_is_full(const binary_tree_t *tree)
{
	if (!tree)
		return (1);

	return (node_full(tree)
		&& _binary_tree_is_full(tree->left)
		&& _binary_tree_is_full(tree->right));
}

int binary_tree_is_full(const binary_tree_t *tree)
{
	if (!tree)
		return (0);

	return (_binary_tree_is_full(tree));	
}
