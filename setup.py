from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

# Tên module Python sẽ được tạo ra
module_name = "my_module"

# Tên tệp mã nguồn C++
source_file = "main.cpp"

# Tạo extension
ext_modules = [
    Pybind11Extension(
        module_name,
        [source_file],
        cxx_std=11,
    ),
]

# Setup thông tin cho setuptools
setup(
    name=module_name,
    version="0.1",
    author="Your Name",
    description="A Python C++ extension example",
    ext_modules=ext_modules,
)