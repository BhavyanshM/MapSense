cmake_minimum_required(VERSION 3.4)
project(factor_graph_node)

add_compile_options(-std=c++17)

set(CMAKE_MODULE_PATH "${PROJECT_SOURCE_DIR}/modules/" ${CMAKE_MODULE_PATH})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Wextra")

find_package(GTSAM REQUIRED)
find_package(Eigen3 3.3 REQUIRED NO_MODULE)

include_directories(${EIGEN3_INCLUDE_DIR})
include_directories(${GTSAM_INCLUDE_DIR})

set(FG_SOURCES
    src/FactorGraphHandler.cpp
    include/ApplicationState.h
    include/FactorGraphHandler.h
    src/SLAM.cpp include/SLAM.h
)


add_executable(FactorGraphNodeHeadless ${FG_SOURCES}  src/FactorGraphNodeHeadless.cpp include/FactorGraphNodeHeadless.h)
target_link_libraries(FactorGraphNodeHeadless
    gtsam
    eigen

)
target_include_directories(FactorGraphNodeHeadless PUBLIC
    include
)