& make clean
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& make
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& make test
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
