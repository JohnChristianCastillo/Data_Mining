cmake_minimum_required(VERSION 3.17)
project(df)

set(CMAKE_CXX_STANDARD 14)

add_executable(df testndi.cpp
        data.cpp
        data.cpp
        item.h
        ndi.cpp
        ndi.h
        qie.cpp)