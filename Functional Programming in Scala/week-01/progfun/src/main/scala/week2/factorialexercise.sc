object factorialexercise {
  def factorial(n: Int): Int = {
    def loop(acc: Int, n: Int): Int =
      if (n==0) acc
      else loop(acc*n, n-1)
    loop(1, n)
  }


//makes sense.
  // the above approach eliminates the carrying of n by
  // getting the reduction of the factorial done in the loop fxn
  // thus allowing tail recursion b/c only calling itself.

}


