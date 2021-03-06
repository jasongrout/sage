"""
Verify that the ATLAS enums are in sync with the spkg-install enums

TESTS::

    sage: check_enums(sample_print_enums_output)
"""

# constants from src/ATLAS/CONFIG/include/atlconf.h
# Note: must be lists, not tuples, for Python-2.4 support

ATLAS_OSTYPE = (  # static char *osnam
    'UNKNOWN', 'Linux', 'SunOS', 'SunOS4', 'OSF1',
    'IRIX', 'AIX', 'Win9x', 'WinNT', 'Win64',
    'HPUX', 'FreeBSD', 'OSX')

ATLAS_MACHTYPE = (  # static char *machnam
    'UNKNOWN', 'POWER3', 'POWER4', 'POWER5', 'PPCG4', 'PPCG5',
    'POWER6', 'POWER7', 'IBMz9', 'IBMz10', 'IBMz196',
    'x86x87', 'x86SSE1', 'x86SSE2', 'x86SSE3',
    'P5', 'P5MMX', 'PPRO', 'PII', 'PIII', 'PM', 'CoreSolo',
    'CoreDuo', 'Core2Solo', 'Core2', 'Corei1', 'Corei2', 'Atom', 'P4', 'P4E',
    'Efficeon', 'K7', 'HAMMER', 'AMD64K10h', 'AMDDOZER', 'UNKNOWNx86',
    'IA64Itan', 'IA64Itan2',
    'USI', 'USII', 'USIII', 'USIV', 'UST2', 'UnknownUS',
    'MIPSR1xK', 'MIPSICE9', 'ARMv7')

ATLAS_ISAEXT = (  # static char *ISAXNAM
    'None', 'VSX', 'AltiVec', 'AVXMAC', 'AVXFMA4', 'AVX', 'SSE3', 'SSE2', 'SSE1',
    '3DNow', 'NEON' )



# for doctesting purposes
sample_print_enums_output = \
"""
Architectural enums (Config's enum MACHTYPE):
     0 = 'UNKNOWN'
     1 = 'POWER3'
     2 = 'POWER4'
     3 = 'POWER5'
     4 = 'PPCG4'
     5 = 'PPCG5'
     6 = 'POWER6'
     7 = 'POWER7'
     8 = 'IBMz9'
     9 = 'IBMz10'
    10 = 'IBMz196'
    11 = 'x86x87'
    12 = 'x86SSE1'
    13 = 'x86SSE2'
    14 = 'x86SSE3'
    15 = 'P5'
    16 = 'P5MMX'
    17 = 'PPRO'
    18 = 'PII'
    19 = 'PIII'
    20 = 'PM'
    21 = 'CoreSolo'
    22 = 'CoreDuo'
    23 = 'Core2Solo'
    24 = 'Core2'
    25 = 'Corei1'
    26 = 'Corei2'
    27 = 'Atom'
    28 = 'P4'
    29 = 'P4E'
    30 = 'Efficeon'
    31 = 'K7'
    32 = 'HAMMER'
    33 = 'AMD64K10h'
    34 = 'AMDDOZER'
    35 = 'UNKNOWNx86'
    36 = 'IA64Itan'
    37 = 'IA64Itan2'
    38 = 'USI'
    39 = 'USII'
    40 = 'USIII'
    41 = 'USIV'
    42 = 'UST2'
    43 = 'UnknownUS'
    44 = 'MIPSR1xK'
    45 = 'MIPSICE9'
    46 = 'ARMv7'

Operating System enums (Config's enum OSTYPE):
     0 = 'UNKNOWN'
     1 = 'Linux'
     2 = 'SunOS'
     3 = 'SunOS4'
     4 = 'OSF1'
     5 = 'IRIX'
     6 = 'AIX'
     7 = 'Win9x'
     8 = 'WinNT'
     9 = 'Win64'
    10 = 'HPUX'
    11 = 'FreeBSD'
    12 = 'OSX'

Compiler integer defines:
     0 = 'ICC'
     1 = 'SMC'
     2 = 'DMC'
     3 = 'SKC'
     4 = 'DKC'
     5 = 'XCC'
     6 = 'GCC'
     7 = 'F77'


ISA extensions are combined by adding their values together (bitvector):
         none: 1
          VSX: 2
      AltiVec: 4
       AVXMAC: 8
      AVXFMA4: 16
          AVX: 32
         SSE3: 64
         SSE2: 128
         SSE1: 256
        3DNow: 512
         NEON: 1024

"""


def check_enums(print_enums_output):
    """
    Verify that the output of ATLAS print_enums matches our enums

    INPUT:

    - ``print_enums_output`` -- string. The output of the ATLAS
      print_enums utility.
    """
    lines = print_enums_output.splitlines()
    found_MACHTYPE = found_OSTYPE = found_ISAEXT = False
    while len(lines) > 0:
        line = lines.pop(0)
        if line.startswith('Architectural enums'):
            check_enums_ATLAS_MACHTYPE(lines)
            found_MACHTYPE = True
        if line.startswith('Operating System enums'):
            check_enums_ATLAS_OSTYPE(lines)
            found_OSTYPE = True
        if line.startswith('ISA extensions'):
            check_enums_ATLAS_ISAEXT(lines)
            found_ISAEXT = True
    if not (found_MACHTYPE and found_OSTYPE and found_ISAEXT):
        raise RuntimeError('failed to parse the output of print_enums')


def check_enums_ATLAS_MACHTYPE(lines):
    for i, mach_type in enumerate(ATLAS_MACHTYPE):
        got = lines.pop(0).strip()
        expect = "{0} = '{1}'".format(i, mach_type)
        if got != expect:
            raise RuntimeError('ATLAS_MACHTYPE mismatch at position '+str(i)+
                               ': got >>'+got+'<<, expected >>'+expect+'<<')

def check_enums_ATLAS_OSTYPE(lines):
    for i, os_type in enumerate(ATLAS_OSTYPE):
        got = lines.pop(0).strip()
        expect = "{0} = '{1}'".format(i, os_type)
        if got != expect:
            raise RuntimeError('ATLAS_OSTYPE mismatch at position '+str(i)+
                               ': got >>'+got+'<<, expected >>'+expect+'<<')

def check_enums_ATLAS_ISAEXT(lines):
    for i, isaext in enumerate(ATLAS_ISAEXT):
        got = lines.pop(0).strip()
        if i == 0:
            expect = 'none: 1'
        else:
            expect = "{0}: {1}".format(isaext, 1 << i)
        if got != expect:
            raise RuntimeError('ATLAS_ISAEXT mismatch at position '+str(i)+
                               ': got >>'+got+'<<, expected >>'+expect+'<<')


def make_check_enums():
    """
    Build the print_enums utility and check its output against our
    enums

    You can only call this function when you are in the atlas build
    directory, and only after configuring atlas.
    """
    from subprocess import check_output
    output = check_output('make xprint_enums ; ./xprint_enums', shell=True)
    print output
    check_enums(output)

