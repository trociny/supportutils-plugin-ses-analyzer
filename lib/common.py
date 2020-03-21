import json
import os

SES_SUPPORTCONFIG_DIR = os.environ.get("SES_SUPPORTCONFIG_DIR")

def get_report():
    with open(SES_SUPPORTCONFIG_DIR + "/ceph/ceph-report", "r") as f:
        report_lines = f.readlines()
        if not report_lines:
                return None
        begin = 0
        end = len(report_lines)
        while begin < 10 and report_lines[begin] != "{\n":
                begin += 1
        while end > begin and report_lines[end - 1] != "}\n":
                end -= 1
        return json.loads("".join(report_lines[begin:end]))
