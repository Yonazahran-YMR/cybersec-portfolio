import requests
import pytest
from seed import seed
from run_scan import run_all

@pytest.fixture(scope="module")
def findings():
    requests.post("http://localhost:4566/moto-api/reset")
    seed()
    return run_all()

def test_total_count(findings):
    assert len(findings) == 5

def test_bad_sg_is_critical(findings):
    by_resource = {f["resource"]: f for f in findings}
    assert by_resource["bad-sg"]["severity"] == "CRITICAL"

def test_worst_sg_is_critical_with_no_ports(findings):
    by_resource = {f["resource"]: f for f in findings}
    assert by_resource["worst-sg"]["severity"] == "CRITICAL"
    assert by_resource["worst-sg"]["from_port"] is None

def test_web_sg_is_low(findings):
    by_resource = {f["resource"]: f for f in findings}
    assert by_resource["web-sg"]["severity"] == "LOW"

def test_good_resources_not_flagged(findings):
    flagged = {f["resource"] for f in findings}
    assert "good-sg" not in flagged

def test_bad_bucket_has_two_findings(findings):
    bucket = [f for f in findings if f["resource"] == "bad-public-bucket"]
    assert len(bucket) == 2
    assert {f["check_id"] for f in bucket} == {"S3_PUBLIC_ACL", "S3_NO_PUBLIC_ACCESS_BLOCK"}

