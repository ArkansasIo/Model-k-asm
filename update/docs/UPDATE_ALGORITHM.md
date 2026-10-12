# Update Algorithms

Semantic versions are ordered lexicographically by major, minor, patch.

Integrity requires SHA256(before)=old_sha256 and SHA256(after)=new_sha256.

Transaction: CHECK -> VERIFY -> STAGE -> APPLY -> TEST -> COMMIT. Any failure enters ROLLBACK.

Dependency ordering uses topological sorting; a remaining nonzero indegree set indicates a cycle.
