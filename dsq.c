#include <stdio.h>
#include <math.h>

int main(){
	
	printf("DOUBLE SQUARES CHALLENGE, HIYOOOOO\n\n");

	int x[] = {12,4,6,25,'\0'};
	// int x[] = {12,4,6,25,78,3,2,5,7,545678,76567,89,8,'\0'};

	//Double Squares problem
		//suppose we have a list of integers, x (from a file, hardcoded, whatever...)
			//(EASY MODE) the list is only 10 numbers long
		//the integers are UNSIGNED ranging [0, (2^32)-1]
		//for each number, we want to see if it is a double square AND 
			//how many variations of the double square there are
		//defn: a double square is a number that can be shown as the sum of 2 squares
			//e.g. x = a^2 + b^2, where a and b are commutative but only counted once
		//Examples:
			// 25 = 5^2 + 0^2 and 25 = 4^2 + 3^2
				// this answer results in 1
			// 0 = 0^2 + 0^2
				// also 1
			// 2 = 1^2 + 1^2
				//again, 1
			// 3 as input yields ZERO, since you can't do decimals
			//4 = 2^2 + 2^2.... WRONG< zero
			// 5 = 2^2 + 1^2
			// 6 = NOPE, 0

		//JM's strategy,
			//loop over the list of integers, for each one x[i]
				//if 0||1, return 1
				//if x[i] is 2 x a double-square (redundant?)
				//loop from 0 to ceil( sqrt(x[i]) )
					
		//GO!
			
		//...a brief C refresher on pointers
			//each var in c has the VALUE, the address of the value, and the POINTER to the value
			// printf("%d\n", x[i]);//should give 12, the value
			// printf("%p\n", &x[i]);//should give the address of the 12 value, the dereference
			// printf("%d\n", *x);//should give the pointer to the address of the value

		int *i = x, n = 0, numDS = 0;
		float sr, flr;
		// printf("*i -> %d", *i);
		// printf("*i -> %d\n\n", *(i+1));

		while(*i != '\0'){
			printf("Position %d: %d at address %p\n", n, *i, &(*i));

			//is it 1 or 0?
			if(*i == 1 || *i == 0){
				printf("ONLY ONE ANSWER HERE");
			}else{

				//get sqrt and it's floor value
				sr = sqrt(*i);
				flr = floorf(sr);
				printf("\tsqrt(%d) = %f, whose floor = %f\n", *i, sr, flr);

				//if exact, +1 DS
					// printf("is %f exact? %x", sr, (flr != 0) && (flr - sr == 0) );
					if( (flr - sr) == 0 ){
						printf("\tFOUND\t-\t %d = %d^2 + 0^2\n", *i, (int)flr);
						numDS++;
						flr--;//to check for other cases in our loop below!
					}

				//loop from 1 to floor(sqrt), looking for possible combinations that work with differences
				int diff;
				for(int j=flr; j>=flr/2;j--){
					diff = *i - (j*j);
					if(sqrt(diff) - floor(sqrt(diff)) == 0){
						printf("\tFOUND ??? %d^2 + %d^2 == %d\n",j, (int)(floorf(sqrt(diff))), *i);
						if(false){
							//TODO: if number not found in a list of all DS combination terms
							//	e.g. in 25, you can have 0, 5, 3, 4 to represent 0^2 + 5^2, 3^2 + 4^2, ...
							//traversing lists/arrays in C... hrmmm...
							//if it's ok, increment the counter!!!
							numDS++;
						}
						
					}

					//some workthru
						/*
						suppose num == 81
						floor(sqrt(num)) == 9
						9- sqrt(num) == 0
							exact case caught!
						let's look at other possible cases here
							num - 8^2 = 81 - 64 = 17
							diff <- 17
							if sqrt(diff) is not exact, MOVE ON!!!
							we move on
							num - 7^2 = 81 - 49 = 32
							move on...
							...reach zero. only one combo here...

						*/


				}
			}

			if(numDS > 0){
				printf("\n\tDouble Squares FOUND\t%d", numDS);
			}

			printf("\n--------------------------");

			i++;
			n++;
			numDS = 0;
			printf("\n");
		}

		// for(int i = 0; i<length; i++){
		// 	printf("Position %d: %d\n", i, x[i]);
		// }

}