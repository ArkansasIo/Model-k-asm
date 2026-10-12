#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "model_k.h"
static void usage(const char*p){puts("Model K native reference build");printf("Usage: %s status | add20 A B | checksum ID TYPE FLAGS VER STATUS VALUE20 | version\n",p);}
int main(int argc,char**argv){if(argc<2){usage(argv[0]);return 1;}if(!strcmp(argv[1],"version")){puts("Model K 1.1.0 compiled reference");return 0;}if(!strcmp(argv[1],"status")){puts("MODEL K");puts("CPU: 8-bit reference");puts("LOGICAL VALUE: 20-bit");puts("RECORD: 20-byte");puts("MEMORY: magnetic-core model");puts("QUANTUM: QISA interface");return 0;}if(!strcmp(argv[1],"add20")&&argc==4){uint32_t a=strtoul(argv[2],0,0),b=strtoul(argv[3],0,0);if(a>MK20_MASK||b>MK20_MASK)return 2;printf("0x%05X\n",mk20_add(a,b));return 0;}if(!strcmp(argv[1],"checksum")&&argc==7){MKRecord r={0};r.id=strtoul(argv[2],0,0);r.type=strtoul(argv[3],0,0);r.flags=strtoul(argv[4],0,0);r.version=strtoul(argv[5],0,0);r.status=0;r.value20=strtoul(argv[6],0,0);printf("checksum=0x%02X\n",mk_record_checksum(&r));return 0;}usage(argv[0]);return 1;}
