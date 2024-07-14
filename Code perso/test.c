#include <stdio.h>
#include <math.h>

double racine(double n, unsigned short max_iter){

    /*
    This function returns the estimated square root of a number n by approximating it
    max_iter is the maximum number of iterations the main approximation loop will do (1000 is fine)
    Caution : This function only works on numbers greater or equal to 1
    Caution2 : Maximum for max_iter is 65535
    */

    if(n<1){return -1;} // Not supported yet

    double u=1;

    while(u*u < n){                 // Loop while u is smaller than n
        u = u*2;                    // Double it each time (and give it to the next person)
    }

    if(u*u == n){return u;}         // If u² = n then return u because it's it's square root

    double s=u/8;                   // Set the step to an eight of u
                                    // (4 also works but 8 is what works best)

    u = u - u/4;                    // Set u to the middlepoint between the first time u²>n 
                                    // and the last time u²<n

    for (short iter = 0; iter < max_iter; iter++)  // loop while reducing the step to be closer and closer
                                                    // to the number
    {
        if      (u*u>n){u = u-s;}   // If u² > n then reduce it
        else{if (u*u<n){u = u+s;}}  // If u² > n then make it bigger

        s = s/2;                    // Reduce the step for next iteration

        if(u*u == n){return u;}     // If u² = n then return u
    }
    return u;
}

int main(){
    return 0;
}