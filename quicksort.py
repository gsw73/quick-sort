import sys
import re
import numpy as np

comparisons = 0
FIRST = 0
LAST = 1
MIDDLE = 2

def swap( arr, a, b ):
    keep = arr[ a ]
    arr[ a ] = arr[ b ]
    arr[ b ] = keep

    return

def find_pivot( el ):
    if len( el ) % 2 == 0:
        middle_index = int( len( el ) / 2 - 1 )

    else:
        middle_index = len( el ) // 2

    if el[ 0 ] < el[ middle_index ] < el[ -1 ] or el[ -1 ] < el[ middle_index ] < el[ 0 ]:
        pivot = middle_index

    elif el[ 0 ] < el[ -1 ] < el[ middle_index ] or el[ middle_index ] < el[ -1 ] < el[ 0 ]:
        pivot = -1

    else:
        pivot = 0

    return pivot

def quick_sort( el, pivot_meth = FIRST ):
    global comparisons

    # output of quicksort moves pivot point into location such that
    # [ L........; P; R........... ]
    # all elements in L are < P and all elements in R are > P

    # determine pivot point value to use
    if pivot_meth == FIRST:
        new_pivot_index = 0

    elif pivot_meth == LAST:
        new_pivot_index = -1

    elif pivot_meth == MIDDLE:
        new_pivot_index = find_pivot( el )

    # algo always uses el[ 0 ] as pivot; swap new pivot val to this loc
    pivot_point = 0
    swap( el, new_pivot_index, pivot_point )

    # i indicates the left-most element in the R array
    i = 1;

    # track number of comparisons
    comparisons += ( len( el ) - 1 )
    # print( 'total = {:d}, new = {:d}'.format( comparisons, len(el)-1 ) )

    for j in range( 1, len( el ) ):
        if el[ j ] < el[ pivot_point ]:
            swap( el, j, i )
            i += 1

    # upon completion, put pivot point in correct place
    swap( el, pivot_point, i - 1 )

    # recurse, if necessary
    leftLength = i - 1
    left = el[ 0:leftLength ]
    if leftLength > 0:
        quick_sort( left, pivot_meth )

    rightLength = len( el ) - i
    right = el[ i:len( el ) ]
    if rightLength > 0:
        quick_sort( right, pivot_meth )

    return

def main():
    global comparisons
    comparisons = 0
    genTestFile = False
    genFileName = ''
    elements = []
    pivot = FIRST

    # check for pivot point
    for switch in sys.argv:
        if re.match( '-last', switch ):
            pivot = LAST
            sys.argv.remove( switch )

        elif re.match( '-first', switch ):
            pivot = FIRST
            sys.argv.remove( switch )

        elif re.match( '-middle', switch ):
            pivot = MIDDLE
            sys.argv.remove( switch )

    if len( sys.argv ) > 1:
        if re.match( '-h', sys.argv[ 1 ] ):
            print( 'Usage -- with or without commas:' )
            print( 'my_prompt>  python3 quicksort.py 1 6 3 2 4 5' )
            print( 'my_prompt>  python3 quicksort.py 1, 6, 3, 2, 4, 5' )
            print( 'The next example writes the input values from the command line to a file, one per line.' )
            print( 'my_prompt>  python3 quicksort.py -g outputfile.txt 1, 6, 3, 2, 4, 5' )
            print( 'The next examples expects input values, one per line, in the associated file' )
            print( 'my_prompt>  python3 quicksort.py -f inputfile.txt' )
            return

        # generates output files for test
        if re.match( '-g', sys.argv[ 1 ] ):
            genTestFile = True
            genFileName = sys.argv[ 2 ]
            del sys.argv[ 1:3 ]

        # gets values from file
        if re.match( '-file', sys.argv[ 1 ] ):
            inputFileName = sys.argv[ 2 ]
            with open( inputFileName, 'rt' ) as fin:
                while True:
                    line = fin.readline()
                    if not line:
                        break
                    elements.append( int( line ) )
        else:
            # getting values from command line
            elements = [ int( re.sub( ',', '', x ) ) for x in sys.argv[ 1: ] ]

        if genTestFile:
            with open( genFileName, 'wt' ) as fout:
                for num in elements:
                    print( num, file = fout )

        print( 'original array:  {}'.format( elements ) )

        # call the sort function
        npArray = np.array( elements )
        quick_sort( npArray, pivot )

        print( 'sorted array:  {}'.format( npArray ) )
        print( 'number of comparisons:  {:,d}'.format( comparisons ) )

        return

    # if no command line arguments
    comparisons = 0
    elements = np.array( [ 87, 16, 2, 0, 12, 25, 26, 27, 63, 75, 28, 50, 2, 5, 41, 39 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 98, 97, 96, 90, 73, 72, 71, 70, 43, 42, 41, 40, 25, 24, 23, 22 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 5, 4, 3, 2, 1 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 6, 5, 4, 3, 2, 1 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 23, 27, 82, 69, 1, 4, 2, 100, 1023, 1000, 83, 41, 14, 19, 37, 18, 8 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 1, 2, 3, 4, 5, 6, 7, 8 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 6, 2, 3, 8, 4, 1, 7, 5 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )

    comparisons = 0
    elements = np.array( [ 3, 9, 8, 4, 6, 10, 2, 5, 7, 1 ] )
    quick_sort( elements )

    print( elements )
    print( 'number of comparisons:  {:d}'.format( comparisons ) )


if __name__ == '__main__':
    main()
