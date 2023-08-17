#include <pybind11/pybind11.h>
#include <pybind11/embed.h>
#include <vector>
#include <iostream>
namespace py = pybind11;

class Test
{
public:
    int add(int a, int b)
    {
        return a + b;
    }
};

PYBIND11_MODULE(my_module, m)
{
    py::class_<Test>(m, "Test")
        .def(py::init<>())
        .def("add", &Test::add);
}


