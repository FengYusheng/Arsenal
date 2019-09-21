cmake_minimum_required(VERSION 2.8)

project(cli)

AUX_SOURCE_DIRECTORY(c DIR_SRC)

add_executable(cli ${DIR_SRC})
