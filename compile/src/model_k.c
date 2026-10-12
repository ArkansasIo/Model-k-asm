#include "model_k.h"
uint32_t mk20_add(uint32_t a,uint32_t b){return (a+b)&MK20_MASK;}
uint8_t mk_record_checksum(const MKRecord *r){uint32_t s=0;s+=(r->id>>0)&255;s+=(r->id>>8)&255;s+=(r->id>>16)&255;s+=(r->id>>24)&255;s+=r->type+r->flags+r->version+r->status;s+=(r->value20>>0)&255;s+=(r->value20>>8)&255;s+=(r->value20>>16)&15;for(int i=0;i<8;i++)s+=r->payload[i];return (uint8_t)s;}
int mk_record_valid(const MKRecord *r){return r&&r->id>0&&r->value20<=MK20_MASK&&mk_record_checksum(r)==r->checksum;}
