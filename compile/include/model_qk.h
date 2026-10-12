#ifndef MODEL_QK_H
#define MODEL_QK_H
#include <stdint.h>

#define QK64_MASK UINT64_MAX
#define QK_RECORD_SIZE 64u
#define QK_LEGACY_RECORD_SIZE 20u

typedef struct {
    uint32_t record_id;
    uint16_t record_type;
    uint16_t flags;
    uint16_t schema_version;
    uint16_t status;
    uint64_t logical_value;
    uint32_t payload_length;
    uint8_t payload[35];
    uint32_t reserved;
    uint8_t checksum;
} QKRecord;

uint64_t qk64_add(uint64_t a, uint64_t b);
uint64_t qk64_sub(uint64_t a, uint64_t b);
uint8_t qk_checksum64(const QKRecord *r);
int qk_record_valid(const QKRecord *r);

#endif
