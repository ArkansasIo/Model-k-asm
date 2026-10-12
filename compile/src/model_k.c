#include "model_k.h"
uint32_t mk20_add(uint32_t a, uint32_t b) { return (a + b) & MK20_MASK; }
uint8_t mk_record_checksum(const MKRecord *r) {
    uint32_t sum = 0;
    sum += (r->id >> 0) & 0xff; sum += (r->id >> 8) & 0xff;
    sum += (r->id >> 16) & 0xff; sum += (r->id >> 24) & 0xff;
    sum += r->type + r->flags + r->version + r->status;
    sum += (r->value20 >> 0) & 0xff;
    sum += (r->value20 >> 8) & 0xff;
    sum += (r->value20 >> 16) & 0x0f;
    for (int i = 0; i < 8; ++i) sum += r->payload[i];
    return (uint8_t)sum;
}
int mk_record_valid(const MKRecord *r) {
    return r && r->id > 0 && r->value20 <= MK20_MASK &&
           mk_record_checksum(r) == r->checksum;
}
