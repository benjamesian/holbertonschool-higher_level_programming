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

int _binary_tree_is_perfect(const binary_tree_t *tree, size_t height)
{
	if (!tree)
		return (height == 0);
	else if (height == 1)
		return (!tree->left && !tree->right);
	else if (!tree->left || !tree->right)
		return (0);
	return (_binary_tree_is_perfect(tree->left, height - 1)
		&& _binary_tree_is_perfect(tree->right, height - 1));
}

int binary_tree_is_perfect(const binary_tree_t *tree)
{
	size_t height;

	if (!tree)
		return (0);
	height = _binary_tree_height(tree);

	return (_binary_tree_is_perfect(tree, height));
}
