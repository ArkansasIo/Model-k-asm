"""Deterministic quantum job scheduler.

Program ID: QK-QSCH-0001
File ID: QK-QSCH-0001-FILE-0001
Version: QK.2.0.0
"""

from dataclasses import dataclass, field


@dataclass(order=True)
class QuantumJob:
    priority: int
    job_id: str = field(compare=False)
    operations: list[tuple] = field(compare=False, default_factory=list)
    shots: int = field(compare=False, default=1024)
    seed: int | None = field(compare=False, default=None)


class ModelQKScheduler:
    def __init__(self) -> None:
        self._queue: list[QuantumJob] = []

    def submit(self, job: QuantumJob) -> str:
        self._queue.append(job)
        self._queue.sort()
        return job.job_id

    def next_job(self) -> QuantumJob | None:
        return self._queue.pop(0) if self._queue else None

    def pending(self) -> int:
        return len(self._queue)
