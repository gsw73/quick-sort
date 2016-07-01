#include <cstdlib>
#include <cstdio>
#include <string>

static unsigned long comparisons = 0;

void swap( unsigned int *a, unsigned int *b ) {
    unsigned int keep;

    keep = *a;
    *a = *b;
    *b = keep;

    return;
}

unsigned int *quick_sort( unsigned int *el, unsigned int length ) {
    // output of quicksort moves pivot point into location such that
    // [ L........; P; R........... ]
    // all elements in L are < P and all elements in R are > P
    
    // select pivot point as first element
    unsigned int pivot_p = 0;

    // i indicates the left-most element in the R array
    unsigned int i = 1;

    // track number of comparisons
    comparisons += ( length - 1 );

    // pointer j walks entire array beginning with elementa after pivot point
    for ( unsigned int j = 1; j < length; j++ ) {
        if ( el[ j ] < el[ pivot_p ] ) {
            swap( &el[ i ], &el[ j ] );
            i++;
        }
    }

    // upon completion, put pivot point in correct place
    swap( &el[ pivot_p ], &el[ i - 1 ] );

    // recurse, if necessary
    unsigned int *left_p = el;
    unsigned int leftLength = i - 1;
    if ( leftLength > 0 )
        quick_sort( left_p, leftLength );

    unsigned int *right_p = &el[ i ];
    unsigned int rightLength = length - i;
    if ( rightLength > 0 )
        quick_sort( right_p, rightLength );

    return( el );
}

void arrayPrint( unsigned int* array_p, unsigned int len ) {
    for ( unsigned int i = 0; i < len; i++ ) {
        printf( "%d ", array_p[ i ] );
    }

    printf( "\n" );
    return;
}

int main( int argc, char *argv[] ) {
    comparisons = 0;
    unsigned int elements[] = { 87, 16, 2, 0, 12, 25, 26, 27, 63, 75, 28, 50, 2, 5, 41, 39 };
    unsigned int sz = sizeof( elements ) / sizeof( unsigned int );
    unsigned int *sorted_p = quick_sort( elements, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );
    
    comparisons = 0;
    unsigned int elementsB[] = { 98, 97, 96, 90, 73, 72, 71, 70, 43, 42, 41, 40, 25, 24, 23, 22 };
    sz = sizeof( elements ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsB, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );
    
    comparisons = 0;
    unsigned int elementsC[] = { 5, 4, 3, 2, 1 };
    sz = sizeof( elementsC ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsC, sz );
    
    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );

    comparisons = 0;
    unsigned int elementsE[] = { 6, 5, 4, 3, 2, 1 };
    sz = sizeof( elementsE ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsE, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );

    comparisons = 0;
    unsigned int elementsD[] = { 23, 27, 82, 69, 1, 4, 2, 100, 1023, 1000, 83, 41, 14, 19, 37, 18, 8 };
    sz = sizeof( elementsD ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsD, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );

    comparisons = 0;
    unsigned int elementsF[] = { 1, 2, 3, 4, 5, 6, 7, 8 };
    sz = sizeof( elementsF ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsF, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );

    comparisons = 0;
    unsigned int elementsG[] = { 6, 2, 3, 8, 4, 1, 7, 5 };
    sz = sizeof( elementsG ) / sizeof( unsigned int );
    sorted_p = quick_sort( elementsG, sz );

    arrayPrint( sorted_p, sz );
    printf( "Number of comparisons:  %ld\n", comparisons );
    
    return( 0 );
}
