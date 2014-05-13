/*
 *
 * @author: Aaditya Talwai
 * Check for duplicates in an array of length N, containing only integers 0...N-1
 *
 */

import java.util.Arrays;

public class arrayDuplicates {
    
    /* Method: hasDuplicates(int[] array)
     * @param: 'array' - array of length N, containing only integers 0...N-1
     * return 'true' if input array contains duplicate elements( e.g. 2 in {0,1,2,3,2} ), false otherwise
     *
     * Basic idea is, for each i: visit array[ abs(i) ] and negate its value.
     * If we visit an index and find its value to be already negative, it means that we have previously visited that index.
     * Hence we have found a duplicate.
     * Since negating '0' gives the same value, we keep a boolean hasZero to track '0' specifically
    */

    public static boolean hasDuplicates(int[] array) {
        if (array.length < 2) {
            return false;
        }

        int abs; //to hold absoluteValue(i)

        boolean hasZero = false; //checks for zeroes in array

        for (int i = 0; i < array.length; i++) {
            abs = Math.abs(array[i]);
            if ( array[abs] > 0 ) {
                array[abs] = -( array[abs] ); //negate it so we can detect a duplicate
            } 
            else if (array[abs] == 0) { 
                if (hasZero) return true; else hasZero = true;
            }
            else { //array[abs] is negative meaning that element at array[i] is a duplicate
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        int[] array1 = {1,2,3,0,4,6,7,8,9,11,10,8}; //8 duplicated
        int[] array2 = {1,2,3,0,4,5,6,7,8,9,10,11}; // no duplicates
        int[] array3 = {2,1,2,3,4};
    
        System.out.println("Does array " + Arrays.toString(array1) + " contain duplicates?: " +
                                (hasDuplicates(array1) ? "yes" : "no") ); // should print 'yes'
        System.out.println("Does array " + Arrays.toString(array2) + " contain duplicates?: " + 
                                (hasDuplicates(array2) ? "yes" : "no") ); // should print 'no'
        System.out.println("Does array " + Arrays.toString(array3) + " contain duplicates?: " +
                                (hasDuplicates(array3) ? "yes" : "no") ); // should print 'yes'
   
    }
}
