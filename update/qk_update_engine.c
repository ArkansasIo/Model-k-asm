/* Model QK update transaction engine.
 * Program ID: QK-UPD-0001
 * File ID: QK-UPD-0001-FILE-0001
 * Version: QK.2.0.0
 */
#include <stdio.h>
#include <string.h>

typedef enum { QK_CHECK, QK_VERIFY, QK_STAGE, QK_APPLY, QK_TEST, QK_COMMIT, QK_ROLLBACK } QKUpdateState;

const char *qk_update_state_name(QKUpdateState s){
    static const char *names[]={"CHECK","VERIFY","STAGE","APPLY","TEST","COMMIT","ROLLBACK"};
    return (s>=QK_CHECK&&s<=QK_ROLLBACK)?names[s]:"UNKNOWN";
}
int qk_update_transaction(int verify_ok,int test_ok){
    if(!verify_ok){puts("ROLLBACK: verification failed");return 0;}
    puts("CHECK -> VERIFY -> STAGE -> APPLY -> TEST");
    if(!test_ok){puts("ROLLBACK: tests failed");return 0;}
    puts("COMMIT");return 1;
}
