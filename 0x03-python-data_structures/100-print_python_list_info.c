#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - function that prints some basic
 *	info about Python lists
 * @p: pointer to PyObject
 */

void print_python_list_info(PyObject *p)
{
	int list_size = PyList_Size(p), i;
	PyObject *item;
	PyTypeObject *type;
	PyListObject *list = (PyListObject *)p;

	printf("[*] Size of the Python List = %d\n", list_size);
	printf("[*] Allocated = %lu\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		type = Py_TYPE(item);
		printf("Element %d: %s\n", i, type->tp_name);
	}
}
