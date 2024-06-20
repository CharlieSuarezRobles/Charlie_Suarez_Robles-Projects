vmalloc.c and vmfree.c are two C files that form part of one of my programming assignments, a library that manages memory. vmalloc.c has a function called vmalloc that
allocates a block of memory into a "heap" (not the actual heap of the process) that is created by using another function within the library. This block of memory occupies
a certain number of bytes which are determined by the size_t (an integer) that are provided to vmalloc as a parameter plus padding; vmfree.c has a function vmfree that frees a specific block
in memory. This block is specified by the void pointer provided to vmfree.
