#include "model_qk.h"

static void add_bytes(uint32_t *sum, const uint8_t *p, size_t n) {
    for (size_t i = 0; i < n; ++i) *sum += p[i];
}

uint64_t qk64_add(uint64_t a, uint64_t b) { return a + b; }
uint64_t qk64_sub(uint64_t a, uint64_t b) { return a - b; }

uint8_t qk_checksum64(const QKRecord *r) {
    uint32_t sum = 0;
    if (!r) return 0;
    add_bytes(&sum, (const uint8_t *)&r->record_id, sizeof(r->record_id));
    add_bytes(&sum, (const uint8_t *)&r->record_type, sizeof(r->record_type));
    add_bytes(&sum, (const uint8_t *)&r->flags, sizeof(r->flags));
    add_bytes(&sum, (const uint8_t *)&r->schema_version, sizeof(r->schema_version));
    add_bytes(&sum, (const uint8_t *)&r->status, sizeof(r->status));
    add_bytes(&sum, (const uint8_t *)&r->logical_value, sizeof(r->logical_value));
    add_bytes(&sum, (const uint8_t *)&r->payload_length, sizeof(r->payload_length));
    add_bytes(&sum, r->payload, sizeof(r->payload));
    add_bytes(&sum, (const uint8_t *)&r->reserved, sizeof(r->reserved));
    return (uint8_t)sum;
}

int qk_record_valid(const QKRecord *r) {
    return r && r->payload_length <= sizeof(r->payload) &&
           r->reserved == 0 && qk_checksum64(r) == r->checksum;
}
