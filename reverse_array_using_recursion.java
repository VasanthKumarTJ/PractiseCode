import java.util.Arrays;

class Main {
    static void myMethod(int[] arr, int i, int n){
        if(i>=arr.length/2){
            return;
        }
        arr[i]=arr[i] + arr[n-i-1] - (arr[n-i-1] = arr[i]);
        myMethod(arr, i+1, n);
    }
    
    public static void main(String[] args) {
       int[] arr = {1, 2, 3, 4, 5};
       myMethod(arr, 0, 5);
       System.out.println(Arrays.toString(arr));
    }
}