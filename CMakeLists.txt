cmake_minimum_required(VERSION 3.14)
project(WEB_BIRTHDAY_16)
add_executable(${WEB_BIRTHDAY_16} main.cpp)
message("${WEB_BIRTHDAY_16 }")

//macro(prinrt_var Var)
function(print_var VaR)
    foreach(Var ${ARGN})
       message("${VaR}" = "${${VaR}}")
    endforeach()
    set("${VaR}" "Hello, CMake!" PARENT_SCOPE)
endfunction()


print_var(WEB_BIRTHDAY_16)