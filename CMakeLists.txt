cmake_minimum_required(VERSION 3.20)
# delegating constructors are permitted only in C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

project(learn-lldb)
add_subdirectory(src)
