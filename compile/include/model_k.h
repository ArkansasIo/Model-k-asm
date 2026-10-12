#ifndef MODEL_K_H
#define MODEL_K_H
#include <stdint.h>
#define MK20_MASK 0xFFFFFu
#define MK_RECORD_SIZE 20u
typedef struct {
    uint32_t id;
    uint8_t type, flags, version, status;
    uint32_t value20;
    uint8_t payload[8];
    uint8_t checksum;
} MKRecord;
uint32_t mk20_add(uint32_t a, uint32_t b);
uint8_t mk_record_checksum(const MKRecord *r);
int mk_record_valid(const MKRecord *r);
#endif
