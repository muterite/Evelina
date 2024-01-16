for i in range(0, 41, 1) :  # ņem skaitļus 0-40, katrs nākamais ir par 1 lielāks
    if i % 2 == 0 :      # ja skaitlis dalās ar 2 bez atlikuma, tad pārbauda vai tas arī dalās ar 4, ja nē, tad raksta tikai skaitli
        if i % 4 == 0 :  # ja skaitlis dalās ar 4, tad var rakstīt, ka dalās gan ar 2, gan ar 4, ja nē, tad raksta ka dalās tikai ar 2
            print(i, "- Dalos gan ar 2, gan ar 4")
        else :
            print(i, "- Dalos ar 2")
    else :
        print(i)
