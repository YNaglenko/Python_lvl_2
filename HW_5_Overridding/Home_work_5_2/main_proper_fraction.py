from HW_5_Overridding.Home_work_5_2.ProperFraction import ProperFraction

if __name__ == "__main__":
    pf_1 = ProperFraction(1, 3)
    pf_2 = ProperFraction(1, 3)
    print("pf_1 =", pf_1, "pf_2 =", pf_2, "\n", "pf_1 + pf_2")
    pf_1 + pf_2
    print(pf_1)

    pf_3 = ProperFraction(3, 5)
    pf_4 = ProperFraction(2, 10)
    print("pf_3 =", pf_3, "pf_4 =", pf_4, "\n", "pf_3 - pf_4")
    pf_3 - pf_4
    print(pf_3)

    pf_5 = ProperFraction(1, 2)
    pf_6 = ProperFraction(1, 4)
    print("pf_5 =", pf_5, "pf_6 =", pf_6, "\n", "pf_5 * pf_6")
    pf_5 * pf_6
    print(pf_5)

    pf_7 = ProperFraction(1, 2)
    pf_8 = ProperFraction(1, 4)
    print("pf_7 =", pf_7, "pf_8 =", pf_8, "\n", "pf_7 / pf_8")
    pf_7 / pf_8
    print(pf_7)

    pf_9 = ProperFraction(1, 2)
    pf_10 = ProperFraction(1, 4)
    print("pf_9 =", pf_9, "pf_10 =", pf_10, "\n", "pf_9 > pf_10")
    print(pf_9 > pf_10)

    pf_11 = ProperFraction(1, 3)
    pf_12 = ProperFraction(1, 3)
    print("pf_11 =", pf_11, "pf_12 =", pf_12, "\n", "pf_11 = pf_11")
    print(pf_11 == pf_12)
