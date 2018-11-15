int jumpFloorII(int number) {
    if(number < 1) return 0;
    else return pow(2, number-1);
}
