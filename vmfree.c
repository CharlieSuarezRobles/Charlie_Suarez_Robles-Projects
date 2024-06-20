#include "vm.h"
#include "vmlib.h"

/**
 * The vmfree() function frees the memory space pointed to by ptr,
 * which must have been returned by a previous call to vmmalloc().
 * Otherwise, or if free(ptr) has already been called before,
 * undefined behavior occurs.
 * If ptr is NULL, no operation is performed.
 */
void vmfree(void *ptr)
{
    if (ptr == NULL) {
        return;
    }

    struct block_header *headerToFree =
        (struct block_header *)((char *)ptr - 1 * sizeof(struct block_header));
    struct block_header *previousHeaderToRemove;
    struct block_header *nextHeaderToRemove;
    struct block_footer *previousFooter;
    struct block_footer *footerToFree; // technically footerToCreate instead of
                                       // footerToFree because free blocks need
                                       // footers
    struct block_footer *nextFooter;
    int coalescingPrevBlock = 0;
    int coalescingNextBlock = 0;

    if ((headerToFree->size_status & VM_BUSY) == 0) {
        return;
    } else {
        nextHeaderToRemove =
            headerToFree + ((headerToFree->size_status & VM_BLKSZMASK) /
                            sizeof(*headerToFree));

        if (((headerToFree->size_status & VM_PREVBUSY) >> 1) == 0) {

            previousFooter = (struct block_footer *)(headerToFree - 1);
            previousHeaderToRemove =
                (struct block_header *)(previousFooter -
                                        (((previousFooter->size &
                                           VM_BLKSZMASK) /
                                          sizeof(struct block_footer)) -
                                         1));
            coalescingPrevBlock = 1;
        }
        if ((nextHeaderToRemove->size_status != 1 &&
             nextHeaderToRemove->size_status & VM_BUSY) == 0) {
            nextFooter =
                (struct block_footer *)(nextHeaderToRemove +
                                        (((nextHeaderToRemove->size_status &
                                           VM_BLKSZMASK) /
                                          sizeof(struct block_header)) -
                                         1));
            coalescingNextBlock = 1;
        }
    }

    if (coalescingPrevBlock == 1 && coalescingNextBlock == 1) {
        previousHeaderToRemove->size_status =
            previousHeaderToRemove->size_status +
            (headerToFree->size_status & VM_BLKSZMASK) +
            (nextHeaderToRemove->size_status & VM_BLKSZMASK);

        nextFooter->size = previousHeaderToRemove->size_status +
                           (headerToFree->size_status & VM_BLKSZMASK) +
                           (nextHeaderToRemove->size_status & VM_BLKSZMASK);

        previousFooter->size = 0;
        headerToFree->size_status = 0;
        nextHeaderToRemove->size_status = 0;

    } else if (coalescingPrevBlock == 1 && coalescingNextBlock != 1) {
        previousHeaderToRemove->size_status =
            previousHeaderToRemove->size_status +
            (headerToFree->size_status & VM_BLKSZMASK);

        footerToFree = (struct block_footer *)(nextHeaderToRemove - 1);
        footerToFree->size = previousHeaderToRemove->size_status;

        previousFooter->size = 0;
        headerToFree->size_status = 0;
    } else if (coalescingPrevBlock != 1 && coalescingNextBlock == 1) {
        headerToFree->size_status =
            (headerToFree->size_status & ~VM_BUSY) +
            (nextHeaderToRemove->size_status & VM_BLKSZMASK);
        nextFooter->size = headerToFree->size_status;

        nextHeaderToRemove->size_status = 0;
    } else {
        headerToFree->size_status = (headerToFree->size_status & ~VM_BUSY);
        footerToFree = (struct block_footer *)(nextHeaderToRemove - 1);
        footerToFree->size = headerToFree->size_status;
        if (nextHeaderToRemove->size_status != 1) {
            nextHeaderToRemove->size_status =
                (nextHeaderToRemove->size_status -
                 VM_PREVBUSY); // saying that the next header block will know
                               // that the last block was freed.
        }
    }

}
