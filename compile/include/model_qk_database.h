#ifndef MODEL_QK_DATABASE_H
#define MODEL_QK_DATABASE_H
#include <stdint.h>
#include <stddef.h>
#include "model_qk.h"

#define QK_MAGIC 0x32544B41u /* "AKT2" little-endian */
#define QK_HEADER_SIZE 32u

typedef struct {
    uint32_t magic;
    uint16_t version;
    uint16_t header_size;
    uint16_t record_size;
    uint16_t flags;
    uint32_t record_count;
    uint64_t master_seed;
    uint32_t schema_id;
    uint8_t checksum;
    uint8_t reserved[3];
} QKTableHeader;

uint8_t qk_table_checksum(const QKTableHeader *h);
int qk_table_header_valid(const QKTableHeader *h);
size_t qk_record_encode(const QKRecord *r, uint8_t out[64]);
int qk_record_decode(QKRecord *r, const uint8_t in[64]);

#endif
