#include <stdio.h>
#include <Python.h>

void print_python_list(PyObject *p) {
    PyListObject *list = (PyListObject *)p;
    PyVarObject *var_obj = (PyVarObject *)p;
    Py_ssize_t size = var_obj->ob_size;
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", var_obj->ob_alloc);

    for (i = 0; i < size; ++i) {
        PyObject *element = list->ob_item[i];
        const char *type = element->ob_type->tp_name;

        printf("Element %ld: %s\n", i, type);

        if (strcmp(type, "bytes") == 0) {
            printf("[.] bytes object info\n");
            printf("  size: %ld\n", PyBytes_GET_SIZE(element));
            printf("  trying string: %s\n", PyBytes_AsString(element));
            printf("  first 10 bytes: ");
            for (int j = 0; j < 10 && j < PyBytes_GET_SIZE(element); ++j) {
                printf("%02x ", (unsigned char)PyBytes_AsString(element)[j]);
            }
            printf("\n");
        }
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n");
        fprintf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", PyBytes_GET_SIZE(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));
    printf("  first 10 bytes: ");
    for (int j = 0; j < 10 && j < PyBytes_GET_SIZE(p); ++j) {
        printf("%02x ", (unsigned char)PyBytes_AsString(p)[j]);
    }
    printf("\n");
}

