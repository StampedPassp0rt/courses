package recfun

object Main {
  def main(args: Array[String]) {
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(pascal(col, row) + " ")
      println()
    }
  }

  /**
   * Exercise 1
   */
    def pascal(c: Int, r: Int): Int = {
      if (c>r) 0
      else {
        if (r==0 || c == r || c == 0) 1
        else {
          pascal(c, r-1) + pascal(c-1, r-1)
        }
      }
    }



  /**
   * Exercise 2
   */
    def balance(chars: List[Char]): Boolean = {

      //Function to subtract when end parenthesis is found, add when beginning one is found
      //Keeps track of number. If the first one is an end parenthesis, then the count will be -1.
      //And we'll want to have the function stop then.
      def balance_change(character: Char): Int =  {
        if (character == ')') -1
        else {
          if (character == '(') 1
          else 0
        }
      }

      //Need to slice using head, and compare to to prior head

      def parentheses_search(charlist: List[Char], notmatched: Int): Boolean = {
        //If the first parenthesis found is ")", then it will be unbalanced.
        if (notmatched < 0 ) false
        else {
          //Once fully sliced, ideally count is 0. If negative, then we know we had extra end parentheses.
          //If positive, we know we had extra starting parentheses.
          if (charlist.isEmpty) notmatched == 0
          else {
            parentheses_search(charlist.tail, notmatched + balance_change(charlist.head))
          }
        }
      }

      parentheses_search(chars, 0)



    }



  
  /**
   * Exercise 3
    * Write a recursive function that counts how many different ways you can make change for an amount,
    * given a list of coin denominations. For example, there are 3 ways to give change for 4 if you have coins with
    * denomination 1 and 2: 1+1+1+1, 1+1+2, 2+2.
    *
    * Once again, you can make use of functions isEmpty, head and tail on the list of integers coins.
    *
    * Hint: Think of the degenerate cases. How many ways can you give change for 0 CHF(swiss money)?
    * How many ways can you give change for >0 CHF, if you have no coins?
    *
    * (Should be zero for both)
    *
    *
   */


    def countChange(money: Int, coins: List[Int]): Int = {
      def makeChange(remainder: Int, coinlist: List[Int]): Int = {
        //Solves for degenerate cases - should not be able to give change for 0 CHF.
        if (coinlist.isEmpty || (remainder - coinlist.head) < 0) 0
        else {
          if (remainder - coinlist.head == 0) 1
          else {
            countChange(remainder - coinlist.head, coinlist) + countChange(remainder, coinlist.tail)
          }
        }
      }

      makeChange(money, coins.sorted)

    }

  }

