#include "binary_trees.h"

size_t max(size_t a, size_t b)
{
	return (a > b ? a : b);
}

size_t _binary_tree_height(const binary_tree_t *tree)
{
	if (!tree)
		return (0);

	return (1 + max(
		_binary_tree_height(tree->left), 
		_binary_tree_height(tree->right)));
}

size_t binary_tree_height(const binary_tree_t *tree)
{
	if (!tree)
		return (0);

	return (_binary_tree_height(tree) - 1);
}
