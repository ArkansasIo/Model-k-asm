#include "model_qk_database.h"
#include <string.h>

static void put16(uint8_t *p, uint16_t v){p[0]=(uint8_t)v;p[1]=(uint8_t)(v>>8);}
static void put32(uint8_t *p, uint32_t v){for(int i=0;i<4;i++)p[i]=(uint8_t)(v>>(8*i));}
static void put64(uint8_t *p, uint64_t v){for(int i=0;i<8;i++)p[i]=(uint8_t)(v>>(8*i));}
static uint16_t get16(const uint8_t *p){return (uint16_t)p[0]|((uint16_t)p[1]<<8);}
static uint32_t get32(const uint8_t *p){uint32_t v=0;for(int i=0;i<4;i++)v|=(uint32_t)p[i]<<(8*i);return v;}
static uint64_t get64(const uint8_t *p){uint64_t v=0;for(int i=0;i<8;i++)v|=(uint64_t)p[i]<<(8*i);return v;}

uint8_t qk_table_checksum(const QKTableHeader *h){
    const uint8_t *p=(const uint8_t*)h; uint32_t s=0;
    for(size_t i=0;i<29;i++)s+=p[i];
    return (uint8_t)s;
}
int qk_table_header_valid(const QKTableHeader *h){
    return h && h->magic==QK_MAGIC && h->header_size==32 && h->record_size==64 &&
           h->checksum==qk_table_checksum(h);
}
size_t qk_record_encode(const QKRecord *r,uint8_t out[64]){
    if(!r||!out||r->payload_length>35)return 0;
    memset(out,0,64);
    put32(out+0,r->record_id); put16(out+4,r->record_type); put16(out+6,r->flags);
    put16(out+8,r->schema_version); put16(out+10,r->status); put64(out+12,r->logical_value);
    put32(out+20,r->payload_length); memcpy(out+24,r->payload,35); put32(out+59,r->reserved);
    uint32_t s=0;for(int i=0;i<63;i++)s+=out[i];out[63]=(uint8_t)s;return 64;
}
int qk_record_decode(QKRecord *r,const uint8_t in[64]){
    if(!r||!in)return 0;uint32_t s=0;for(int i=0;i<63;i++)s+=in[i];
    if((uint8_t)s!=in[63])return 0;
    r->record_id=get32(in);r->record_type=get16(in+4);r->flags=get16(in+6);r->schema_version=get16(in+8);
    r->status=get16(in+10);r->logical_value=get64(in+12);r->payload_length=get32(in+20);
    memcpy(r->payload,in+24,35);r->reserved=get32(in+59);
    return r->payload_length<=35 && r->reserved==0;
}
