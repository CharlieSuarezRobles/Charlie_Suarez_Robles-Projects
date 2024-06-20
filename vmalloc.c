#include "vm.h"
#include "vmlib.h"

void *vmalloc(size_t size)
{
    
    if (size <= 0) {
        return NULL;
    }
    size += 8;
    if (size % 16 != 0) {
        size = ((size / 16) + 1) * 16;
    }

    struct block_header *freeHeaderToChoose;
    int wasAFreeHeaderFound = 0;
    struct block_header *current = heapstart;
    struct block_header *newHeader;
    struct block_footer *footer;

    while (current->size_status != 1) {
        if ((current->size_status & VM_BUSY) == 0) {
            if ((current->size_status >= size) && (wasAFreeHeaderFound == 0)) {
                freeHeaderToChoose = current;
                footer =
                    (struct block_footer *)(current + (current->size_status /
                                                       sizeof(*current)) -
                                            1);
                wasAFreeHeaderFound = 1;
            } else if ((current->size_status >= size) &&
                       (current->size_status <
                        freeHeaderToChoose->size_status)) {
                freeHeaderToChoose = current;
                footer =
                    (struct block_footer *)(current + (current->size_status /
                                                       sizeof(*current)) -
                                            1);
            }
        }
        current += (current->size_status) / sizeof(*current);
    }
    if (wasAFreeHeaderFound == 1) {

        if ((freeHeaderToChoose->size_status & VM_BLKSZMASK) > size) {
            newHeader = freeHeaderToChoose + size / sizeof(*newHeader);
            newHeader->size_status =
                (freeHeaderToChoose->size_status & VM_BLKSZMASK) - size + 2;
            footer->size =
                (freeHeaderToChoose->size_status & VM_BLKSZMASK) - size + 2;

            freeHeaderToChoose->size_status =
                (freeHeaderToChoose->size_status & VM_PREVBUSY) + size +
                VM_BUSY;
            void *ptr = freeHeaderToChoose + 1;
            return ptr;
        } else {
            freeHeaderToChoose->size_status =
                freeHeaderToChoose->size_status + VM_BUSY;
            footer->size = 0;
            void *ptr = freeHeaderToChoose + 1;
            return ptr;
        }
    }

    return NULL;
}
