#include <iostream>
using std::cout;
using std::endl;
using std::ios;

#include <fstream>
using std::ifstream;
using std::ofstream;

int main( int argc, char *argv[] )
{
   // check number of command-line arguments
   if ( argc != 3 )
      cout << "Usage: copyFile infile_name outfile_name" << endl;
   else
   {
      ifstream inFile( argv[ 1 ], ios::in );
      if ( !inFile )
      {
         cout << argv[ 1 ] << " could not be opened" << endl;
         return -1;
      }

      ofstream outFile( argv[ 2 ], ios::out );
      if ( !outFile )
      {
         cout << argv[ 2 ] << " could not be opened" << endl;
         inFile.close();
         return -2;
      }

      char c = inFile.get();

      while ( inFile )
      {
         outFile.put( c );  
         c = inFile.get();
      }
   }
   return 0;
}