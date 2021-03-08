import java.lang.*;
import java.util.*;

class OnesPositions {
    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[][] arr = new int[N][N];
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                arr[i][j] = sc.nextInt();
            }
        }

        int validones = 0;
        boolean rowpos = false, colpos =false;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                rowpos = false; colpos =false;
                if( i != N-1 ){
                    if(arr[i][j] == 1 && arr[i+1][j] == 1 )
                        rowpos = true;
                }else if(arr[i][j] == 1){
                    rowpos = true;
                }

                if( j != N-1){
                    if(arr[i][j] == 1 && arr[i][j+1] == 1)
                        colpos = true;
                }else if(arr[i][j] == 1){
                    colpos = true;
                }

                if( rowpos && colpos)
                    validones += 1;
            }
        }    

        System.out.println(validones);
    
    }
}