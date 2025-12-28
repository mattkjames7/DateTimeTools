#include <Python.h>

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "_wheelstub",
    NULL,
    -1,
    NULL,
};

PyMODINIT_FUNC PyInit__wheelstub(void) {
    return PyModule_Create(&moduledef);
}

