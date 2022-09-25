# 1: WC/TA (Working Capital/Total Assets): Vốn lưu động/tổng tài sản
# 2: RE/TA (Retained Earnings/Total Assets):  Thu nhập dữ lại/tổng tài sản
# 3: EBIT/TA (Earnings Before Interest and Tax/Total Assets): Thu nhập trước lãi vay và thuế / Tổng tài sản
# 4: ME/TL (Market Value of Equity/ BV Debt (Book Value of Debt: Tổng giá trị )): Giá trị thị trường của Vốn chủ sở hữu / xxxx
# 5: S/TA (Sales/Total Assets): Doanh thu / Tổng tài sản
WC_TA   = float( input("Nhập vào giá trị của WC_TA: "))
RE_TA   = float( input("Nhập vào giá trị của RE_TA: "))
EBIT_TA = float( input("Nhập vào giá trị của EBIT_TA: "))
ME_TL   = float( input("Nhập vào giá trị của ME_TL:"))
S_TA    = float( input("Nhập vào giá trị của S_TA:"))

is_PhaSan = 0

if ME_TL < 0.23:
    if RE_TA < 0.12:
        if WC_TA < -0.28:
            if EBIT_TA < 0.14:
                is_PhaSan = 1
            else: #EBIT_TA >= 0.14:
                is_PhaSan = 0
        else: #WC_TA >= -0.28
            if RE_TA < -0.39:
                is_PhaSan = 0
            else: #RE_TA >= -0.39
                if RE_TA < -0.08:
                    is_PhaSan = 1
                else: #RE_TA >= -0.08
                    if WC_TA < 0.06:
                        if ME_TL < 0.14:
                            if WC_TA < -0.02:
                                is_PhaSan = 1
                            else: #WC_TA >= -0.02
                                if ME_TL < 0.07:
                                    if WC_TA < 0:
                                        is_PhaSan = 0
                                    else: #WC_TA >= 0
                                        is_PhaSan = 1
                                else: #ME_TL >= 0.07
                                    if WC_TA < 0.02:
                                        if WC_TA < -0.01:
                                            is_PhaSan = 0
                                        else: #WC_TA >= -0.01:
                                            is_PhaSan = 1

                                    else: #WC_TA >= 0.02
                                        is_PhaSan = 0
                        else: #ME_TL >= 0.14
                            if EBIT_TA < -0.01:
                                is_PhaSan = 1
                            else: #EBIT_TA >= -0.01
                                is_PhaSan = 0
                    else: #WC_TA >= 0.06
                        if RE_TA < -0.05:
                            is_PhaSan = 0
                        else: #RE_TA >= -0.05
                            if S_TA < 0.31:
                                if WC_TA < 0.34:
                                    is_PhaSan:0
                                else: #WC_TA >= 0.34
                                    is_PhaSan = 1
                            else: #S_TA >= 0.31
                                is_PhaSan = 1
    else: #RE_TA >= 0.12
        if S_TA < 0.64:
            if S_TA < 0.24:
                is_PhaSan = 0
            else: #S_TA >= 0.24
                is_PhaSan = 1
        else: #S_TA >= 0.64
            is_PhaSan = 0
else:

print("Result: " + is_PhaSan)
print("--DONE--")