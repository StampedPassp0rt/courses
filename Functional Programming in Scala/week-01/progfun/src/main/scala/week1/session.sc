object session {
  1+2
  def abs(x: Double) = if (x<0) -x else x

  def sqrt(x: Double) = {
    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess
      else sqrtIter(improve(guess))

    //Should return a Boolean if guess squared is close enough to x
    def isGoodEnough(guess: Double): Boolean =
      abs(guess * guess - x)/x < 0.001


    //Improve. Should do mean of guess and x/guess.
    def improve(guess: Double): Double =
      (guess + x/guess)/2

    //Hard coded initial guess
    sqrtIter(1.0)

    //Because x not defined in the block, it stays same
    //and hence we don't have to pass it to aux fxns as
    //already available to them
  }

sqrt(2)
  sqrt(1)
  sqrt(4)
  sqrt(9)
  sqrt(1E60)
  sqrt(1E-6)


  sqrt(2)
  sqrt(4)
  sqrt(1e60)
  sqrt(1e40)
  sqrt(1e-6)


}






