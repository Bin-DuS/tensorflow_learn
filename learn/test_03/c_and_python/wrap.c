#include <Python.h>
#include <stdlib.h>
#include "colin.h"
PyObject* wrap_func2(PyObject* self, PyObject* args)
{
        int n, result;
        /* 从参数列表中导出一个整形，用"i" */
        if (!PyArg_ParseTuple(args, "i", &n))
                return NULL;

        /* 用C语言的库实现来计算 */
        result = func2(n);
        /* 计算结果必须要导成python识别的类型 */
        return Py_BuildValue("i", result);
}

PyObject* wrap_func3(PyObject* self, PyObject* args)
{
        int n, result;
        int i, j;
        int size, size2;
        PyObject *p,*q;
        y_t *y;

        y = malloc(sizeof(y_t));
        /* 先数数有多少个参数，也就是列表的个数 */
        size = PyTuple_Size(args);
        /* 把数组的个数先分配了 */
        y->len = size;
        y->ax = malloc(sizeof(x_t)*size);
        /* 遍历python里各个列表(参数) */
        for(i=0;i<size;i++) {
                /* 先获得第i个参数，是一个列表 */
                p = PyTuple_GetItem(args, i);
                /* 获得列表的长度 */
                size2 = PyList_Size(p);
                /* 为数组分配好空间 */
                y->ax[i].len = size2;
                y->ax[i].a = malloc(sizeof(int)*size2);
                /* 遍历列表，依次把列表里的数转到数组里 */
                for(j=0;j<size2;j++) {
                        q = PyList_GetItem(p, j);
                        PyArg_Parse(q,"i",&y->ax[i].a[j]);
                }
        }

        /* 用C语言的库实现来计算 */
        result = func3(y);
        free_y_t(y);
        free(y);
        /* 结果转成python识别格式 */
        return Py_BuildValue("i", result);
}

/* 这是接口列表，加载时是只加载此列表的地址，所以这个数据结构不能放栈（局部变量）内，会被清掉 */
static PyMethodDef colinMethods[] =
{
        {"func2", wrap_func2, METH_VARARGS, "Just a test"},
        {"func3", wrap_func3, METH_VARARGS, "Just a test"},
        {NULL, NULL, METH_NOARGS, NULL}
};

/* python加载的时候的接口 */
/* 注意，既然库名叫colin,此函数必须交initcolin */
void initcolin()
{
        PyObject *m;
        m = Py_InitModule("colin", colinMethods);
}