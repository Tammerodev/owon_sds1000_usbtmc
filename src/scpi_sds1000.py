# SCPI calls are seperated into groups:
# 1. Commmon comands CMN
# 2. Channel specific (CH1, CH2)
# 3. Measurement SIG_CH1, SIG_CH2

class SDS1000_SCPI_QUERY:
    CMN_ID = "*IDN?"

    # Channel 1
    CH1_PROBE = ":CH1:PROBe?"
    CH1_SCALE = ":CH1:SCALe?"
    CH1_OFFSET = ":CH1:OFFSet?"

    # Channel 2
    CH2_PROBE = ":CH2:PROBe?"
    CH2_SCALE = ":CH2:SCALe?"
    CH2_OFFSET = ":CH2:OFFSet?"

    # Channel 1
    SIG_CH1_PKPK = ":MEASU:CH1:PKPK?"
    SIG_CH1_AMP = ":MEASU:CH1:VAMP?"
    SIG_CH1_RMS = ":MEASU:CH1:CYCR?"
    SIG_CH1_PERIOD = ":MEASU:CH1:PER?"
    SIG_CH1_FREQ = ":MEASU:CH1:FREQ?"

    # Channel 2
    SIG_CH2_PKPK = ":MEASU:CH2:PKPK?"
    SIG_CH2_AMP = ":MEASU:CH2:VAMP?"
    SIG_CH2_RMS = ":MEASU:CH2:CYCR?"
    SIG_CH2_PERIOD = ":MEASU:CH2:PER?"
    SIG_CH2_FREQ = ":MEASU:CH2:FREQ?"




