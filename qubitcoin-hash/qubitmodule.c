#include <Python.h>

#include "qubit.h"

static PyObject *qubit_getpowhash(PyObject *self, PyObject *args)
{
    char *output;
    PyObject *value;
#if PY_MAJOR_VERSION >= 3
    PyBytesObject *input;
#else
    PyStringObject *input;
#endif
    if (!PyArg_ParseTuple(args, "S", &input))
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

#if PY_MAJOR_VERSION >= 3
    qubit_hash((char *)PyBytes_AsString((PyObject*) input), output);
#else
    qubit_hash((char *)PyString_AsString((PyObject*) input), output);
#endif
    Py_DECREF(input);
#if PY_MAJOR_VERSION >= 3
    value = Py_BuildValue("y#", output, 32);
#else
    value = Py_BuildValue("s#", output, 32);
#endif
    PyMem_Free(output);
    return value;
}

static PyMethodDef QubitMethods[] = {
    { "getPoWHash", qubit_getpowhash, METH_VARARGS, "Returns the proof of work hash using qubit hash" },
    { NULL, NULL, 0, NULL }
};

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef QubitModule = {
    PyModuleDef_HEAD_INIT,
    "qubit_hash",
    "...",
    -1,
    QubitMethods
};

PyMODINIT_FUNC PyInit_qubit_hash(void) {
    return PyModule_Create(&QubitModule);
}

#else

PyMODINIT_FUNC initqubit_hash(void) {
    (void) Py_InitModule("qubit_hash", QubitMethods);
}
#endif
