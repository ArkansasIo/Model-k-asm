# Rollback Model

Before applying a patch, save the installed version, patch ID, paths, previous SHA-256 values, configuration snapshot, database schema version, binary-table format version, and quantum QISA version.

Rollback is applied in reverse operation order and succeeds only when restored hashes match the rollback manifest.
