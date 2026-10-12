# Model K Update Mathematics

Checksum: C = (sum b_i) mod 256.

CRC abstraction: R(x) = M(x)x^k mod P(x).

SHA-256 maps arbitrary byte sequences to a 256-bit digest.

Patch size: S_patch = sum(size(new_i)) + metadata + rollback_data.

Dependency sorting is O(V+E); hash processing is O(n) in input bytes; patch application is O(sum(file_size_i)).

System invariant: installed_version equals manifest.target_version after commit, or manifest.source_version after rollback.
