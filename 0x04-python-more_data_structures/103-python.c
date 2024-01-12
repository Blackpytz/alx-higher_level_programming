#include <Python.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject (Python bytes object)
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	str = PyBytes_AsString(p);

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n
