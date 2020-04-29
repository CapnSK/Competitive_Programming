import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    static String decode(String str) 
    { 
        Stack<Integer> istack = new Stack<>(); 
        Stack<Character> sstack = new Stack<>(); 
        String t = "", res = "";
        for (int i = 0; i < str.length(); i++) 
        { 
            int count = 0;
            if (Character.isDigit(str.charAt(i))) 
            { 
                while (Character.isDigit(str.charAt(i))) 
                { 
                    count = count * 10 + str.charAt(i) - '0'; 
                    i++; 
                } 
       
                i--; 
                istack.push(count); 
            }
            else if (str.charAt(i) == ']') 
            { 
                t = ""; 
                count = 0;
                if (!istack.isEmpty()) 
                { 
                    count = istack.peek(); 
                    istack.pop(); 
                }
                while (!sstack.isEmpty() && sstack.peek()!='[' ) 
                { 
                    t = sstack.peek() + t; 
                    sstack.pop(); 
                }
                if (!sstack.empty() && sstack.peek() == '[') 
                    sstack.pop();
                for (int j = 0; j < count; j++) 
                    res = res + t; 
                for (int j = 0; j < res.length(); j++) 
                    sstack.push(res.charAt(j)); 
       
                res = ""; 
            }
            else if (str.charAt(i) == '[') 
            {
                if (Character.isDigit(str.charAt(i-1))) 
                    sstack.push(str.charAt(i));
                else
                { 
                    sstack.push(str.charAt(i)); 
                    istack.push(1); 
                } 
            }
            else
                sstack.push(str.charAt(i)); 
        }
        while (!sstack.isEmpty()) 
        { 
            res = sstack.peek() + res; 
            sstack.pop(); 
        } 
       
        return res; 
    }

    public static void main(String args[] ) throws Exception {
        Scanner sc=new Scanner(System.in);
        String str=sc.next();
        System.out.println(decode(str));
    }
}