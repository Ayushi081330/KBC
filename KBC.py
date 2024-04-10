Prashans = [
        "Governor", 4
    ],
    [
        "National Education Day?", "11 November", "15 August", "1 April",
        "8 October", 1
    ],
    ["National river of India?", "Yamuna", "Ganga", "Brahmaputa", "Kaveri", 2],
    ["Who invented pen?", "Petrache Poenaru", "Mathew", "Charles", "James", 1],
    ["Who invented paper?", "Fa Xian", "Ding Du", "Jin Jin", "Cai Lun", 4],
    [
        "Winnner of ICC T20 World Cup 2007?", "India", "England", "Newzealand",
        "Australia", 1
    ],
    [
        "Who invented Zero?", "Devi Dutt", "Bhavya Bhaskar", "Aryabhatta",
        "Ramraja", 3
    ]
]

Padhav = [
    1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000,
    1250000, 2500000, 5000000, 70000000
]
Dhanrashiis = 0
for i in range(0, len(Prashans)):

  Prashan = Prashans[i]
  print(
      f"\n\n{Padhav[i]} kai liye pehla prashan aapki computer screen paar:\n",
      Prashan[0])
  print(f"a. {Prashan[1]}          b. {Prashan[2]} ")
  print(f"c. {Prashan[3]}          d. {Prashan[4]} ")
  Jawab = int(input("Answer(1,2,3,4) or quit with(0):\n"))
  if (Jawab == 0):
    Dhanrashiis = Padhav[i - 1]
    break
  if (Jawab == Prashan[-1]):
    print(f" Sahi jawab aap jeette hai paise {Padhav[i]}")
    if (i == 4):
      Dhanrashiis = 10000
    elif (i == 9):
      Dhanrashiis = 320000
    elif (i == 14):
      Dhanrashiis = 10000000
  else:
    print("Galat jawab")
    break

print(f"Aap ghar lai jate hai paise {Dhanrashiis}")
