int jumpFloor(int number) {
    if(number < 1) return 0;
    if(number == 1) return 1;
    if(number == 2) return 2;
    int FibN;
    int FibMinusOne = 2;
    int FibMinusTwo = 1;
    for(int i = 3; i<=number; i++){
      FibN = FibMinusOne + FibMinusTwo;
      FibMinusTwo = FibMinusOne;
      FibMinusOne = FibN;
    }

    return FibN;
  }
