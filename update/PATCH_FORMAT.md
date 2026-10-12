# MKPATCH v1

A patch contains PATCH.MANIFEST, PATCH data, CHECKSUMS, ROLLBACK metadata, and documentation.

Each file entry records path, operation (ADD/MODIFY/DELETE), old SHA-256, new SHA-256, and size.

MODIFY and DELETE operations require the installed old hash to match the manifest.
