#!/usr/bin/env python3

from myhdl import bin
from bits import nasm_test
import os.path

import pytest
import yaml

try:
    from telemetry import telemetryMark

    pytestmark = telemetryMark()
except ImportError as err:
    print("Telemetry não importado")


def source(name):
    dir = os.path.dirname(__file__)
    src_dir = os.path.join(dir, ".")
    return os.path.join(src_dir, name)


@pytest.mark.telemetry_files(source("exe1.nasm"))
def test_exe1():
    ram = {0: 0, 0: 1}
    tst = {10: 5}
    assert nasm_test("exe1.nasm", ram, tst)

@pytest.mark.telemetry_files(source("add.nasm"))
def test_add():
    ram = {0: 2, 1: 42}
    tst = {2: 44}
    assert nasm_test("add.nasm", ram, tst)

    ram = {0: 0, 1: 0}
    tst = {2: 0}
    assert nasm_test("add.nasm", ram, tst)

    ram = {0: 2, 1: 1}
    tst = {2: 3}
    assert nasm_test("add.nasm", ram, tst)


@pytest.mark.telemetry_files(source("mov.nasm"))
def test_mov():
    ram = {0: 33, 1: 44}
    tst = {0: 44, 1: 33, 3: 1}
    assert nasm_test("mov.nasm", ram, tst)


@pytest.mark.telemetry_files(source("sub.nasm"))
def test_sub():
    ram = {0: 2, 1: 4}
    tst = {2: 2}
    assert nasm_test("sub.nasm", ram, tst)
