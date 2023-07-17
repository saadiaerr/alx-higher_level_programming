#include <Python.h>

/**
 * print_python_list_info - Prints basic info.
 * @p: PyObject
 */
void print_python_list_info(PyObject *p)
{
	int size, alloc, y;
	PyObject *obj;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloc);

	for (y = 0; y < size; y++)
	{
		printf("Element %d: ", y);

		obj = PyList_GetItem(p, y);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
