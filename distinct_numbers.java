import java.lang.*;
import java.util.*;

class DistinctNumber{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N =  sc.nextInt();

        Set<Integer> numset = new HashSet<Integer>(N);
        for(int i=0; i<N; i++)
            numset.add(sc.nextInt());
        System.out.println(numset.size());

    }
}